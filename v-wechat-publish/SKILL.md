---
name: v-wechat-publish
description: 微信公众号完整发布流程。引导用户提供标题、封面和正文，对正文进行内容补充优化 → humanizer-zh 去AI痕迹 → wechat-article-formatter 格式化发布 → 飞书自定义机器人 Webhook 通知完成。触发场景：用户说「发布公众号」「微信公众号发布」「发布到微信」「发布文章到公众号」。
---

# 微信公众号完整发布流程

## 技能概述

本 skill 串联以下技能，形成一键发布流水线：

1. **内容补充** — 对用户提供的初稿进行内容丰富和优化
2. **humanizer-zh** — 去除 AI 写作痕迹，使文字更自然
3. **wechat-article-formatter** — bm.md 渲染 + 微信官方 API 发布
4. **飞书自定义机器人** — 发布完成后 Webhook 通知

## 执行流程

```
Step 0  → 收集素材（标题 + 封面 + 正文）
Step 1  → 内容补充优化
Step 2  → humanizer-zh 去AI痕迹
Step 3  → wechat-article-formatter 发布
Step 4  → 飞书自定义机器人通知
```

---

## Step 0：收集素材

向用户请求以下信息（可一次性提供，也可分步）：

| 字段   | 说明                    | 必填             |
| ------ | ----------------------- | ---------------- |
| 标题   | 文章标题                | ✅               |
| 封面图 | 本地图片路径或 URL      | ✅（发布时需要） |
| 正文   | 初稿文本，支持 Markdown | ✅               |

**提示语示例**：

> 好的！开始微信公众号发布流程 📤
> 请提供以下信息：
>
> 1. **标题**：文章标题是什么？
> 2. **封面图**：封面图片路径（本地文件或 URL）
> 3. **正文**：文章内容（支持 Markdown）

收到所有素材后，进入 Step 1。

---

## Step 1：内容补充优化

**读取并应用** `humanizer-zh` skill（/Users/vanilla/.agents/skills/humanizer-zh/SKILL.md）。

对用户的初稿进行以下补充和优化：

- 补充具体细节、数据、案例（避免空洞表达）
- 优化段落结构，增强可读性
- 调整语气，使文章更有温度和个性
- 保留原文的核心信息和风格倾向
- 检查并修复 humanizer-zh 文档中列出的 24 种 AI 写作模式

**输出格式**：优化后的完整 Markdown 文章（不含标题，标题在 Step 0 已收集）。

---

## Step 2：humanizer-zh 去 AI 痕迹

**再次读取** `humanizer-zh` skill，并对其"处理流程"部分严格执行：

1. 逐段扫描 Step 1 输出中的 AI 模式（24 种模式见 skill 文档）
2. 重写所有问题片段
3. 确保大声朗读时自然流畅
4. 变化句子长短，保持节奏感
5. 使用具体细节替代模糊表述
6. 适当注入个性和真实感受

**质量评估**：按 skill 中的"质量评分"维度（直接性/节奏/信任度/真实性/精炼度）自评，确保达到 40+/50。

---

## Step 3：wechat-article-formatter 发布

**读取并执行** `wechat-article-formatter` skill（/Users/vanilla/.qclaw/skills/wechat-article-formatter/SKILL.md）。

关键步骤：

1. **准备 Markdown 文件**：将 Step 2 最终文本写入临时 Markdown 文件（如 `/tmp/wechat-final.md`）

2. **获取 Access Token**：通过 `WECHAT_APP_ID` + `WECHAT_APP_SECRET` 获取

3. **上传封面图**：`material/add_material` → 获取 `thumb_media_id`

4. **bm.md 渲染**：使用 curl POST 到 `https://bm.md/api/markdown/render`，使用 `green-simple` 风格 + 自定义 CSS（bm.md API 返回 key 为 `result` 而非 `html`）

5. **发布草稿**：`POST draft/add`，包含：

   - `title`、`author`、`thumb_media_id`、`content`（HTML）
   - `need_open_comment: 1`（开启评论）
   - `only_fans_can_comment: 0`（所有人可评）
   - `original_article_type: 1`（声明原创）
   - `digest`（摘要，≤60 字）

6. **保存发布结果**：`media_id`、`title`、`digest` 供 Step 4 使用

> 💡 如封面图缺失，在此步骤中断并请求用户提供。

---

## Step 4：飞书自定义机器人通知

使用飞书**自定义机器人 Webhook**，直接 POST 到飞书，不需要 lark-cli。

### 凭证

Webhook URL 存放在 `~/.env`：

```
FEISHU_WEBHOOK=https://open.feishu.cn/open-apis/bot/v2/hook/{your-webhook-token}
```

### 通知内容（富文本格式）

```python
payload = {
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": "✅ 微信公众号发布成功",
                "content": [
                    [{"tag": "text", "text": f"📌 标题：{title}"}],
                    [{"tag": "text", "text": f"📅 时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}"}],
                    [{"tag": "text", "text": f"💬 摘要：{digest}"}],
                    [{"tag": "text", "text": f"📁 media_id：{media_id}"}],
                    [{"tag": "text", "text": "🔗 预览：https://mp.weixin.qq.com → 内容管理 → 草稿箱"}],
                    [{"tag": "at", "user_id": "all"}]
                ]
            }
        }
    }
}
```

### 发送方式

使用 curl 发送 POST 请求：

```bash
curl -s -X POST "$FEISHU_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c 'import json,sys; print(json.dumps(json.load(sys.stdin)))')"
```

> 注意：飞书 Webhook 通知失败不影响草稿发布，仅告知用户可手动查看。

---

## 错误处理

| 场景                     | 处理方式                                    |
| ------------------------ | ------------------------------------------- |
| 封面图缺失               | Step 3 中断，请求用户提供                   |
| WeChat API 凭证缺失      | 引导用户提供 AppID/AppSecret，写入 `~/.env` |
| humanizer-zh 自评 <40 分 | 重新修订 Step 2 输出                        |
| 飞书通知发送失败         | 告知用户草稿已保存，可手动查看              |

---

## 凭证存放

| 凭证                     | 路径                                              |
| ------------------------ | ------------------------------------------------- |
| WeChat AppID / AppSecret | `~/.env`（`WECHAT_APP_ID` / `WECHAT_APP_SECRET`） |
| 飞书 Webhook URL         | `~/.env`（`FEISHU_WEBHOOK`）                      |
