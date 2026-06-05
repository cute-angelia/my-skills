# My Skills

个人 skills 仓库，当前主要给支持 `.agents/skills` 约定的 agent 使用。

当前本地源码目录：
`/Users/vanilla/git/github/cute-angelia/my-skills`

推荐安装方式：保留这个仓库作为唯一源目录，再把各个 skill 软链接到：
`~/.agents/skills/`

这样后续只需要修改仓库里的源文件，agent 侧会自动生效。

## 当前技能列表

- `v-AI-Short-Drama-Agent-Skill`
  - 短剧剧本创作万能工作流
  - 适合从灵感、故事大纲、分集设计到单集剧本初稿与精修的全流程推进

- `v-humanizer`
  - 中文去 AI 味 / 人味化编辑
  - 适合对文章、说明文、观点文做去模板化、去套话、去宣传腔处理

- `v-khazix-writer`
  - 长文内容生产与风格化写作
  - 适合做公众号/内容稿的结构整理、扩写与输出

- `v-neat-freak`
  - 知识库洁癖式收尾同步 skill
  - 适合在阶段开发完成后，系统整理 memory、CLAUDE/AGENTS、README、docs 与 handoff 文档，确保对人和对 agent 都不漂移

- `v-novel-anti-ai`
  - 小说反 AI 直接实改技能
  - 适合对章节正文、场景段落、人设表达做去 AI 味、去模板化、去解释腔实改；默认直接修改正文或给可替换成稿，只有用户明确要求只审查时才输出报告

- `v-novel-anti-ai-only-sentence`
  - 小说句式生活化提示 skill
  - 适合只做语言句式、口吻和表达自然度修正提示；不删场景描写，不删说明信息，不做强反 AI 实改，默认只提示可替换句

- `v-novel-对话感情增强`
  - 小说/短剧对话情绪增强 skill
  - 适合只针对已有正文里的对话做感情、人味、拉扯、嘴硬、停顿和接话感增强；保留剧情、人物关系、信息点和事件顺序，不做全文润色

- `v-novel-build`
  - novelOs 三项目分流选择技能
  - 适合在 open-novel-writing、novel-pro、webnovel-writer 之间快速选型并进入正确工作流

- `v-novel-chaiwen`
  - 长篇样文/小说章节结构化拆文 skill
  - 适合按章节连续拆解样本文，稳定输出每章功能、麻烦链、伏笔、地图与可迁移机制，并默认自动续拆不等待“继续”

- `v-novel-fanqie-bestseller-template`
  - 番茄爆款故事填写模板 skill
  - 适合从 0 填写爽文/连载故事底盘，先设计局势、利益、立场，再生成剧情、大纲或正文

- `v-novel-大纲排雷清单`
  - 初大纲番茄短爽文简版排雷 skill
  - 适合从 0 起短爽文/番茄爽文初始大纲，或检查、完善、排雷已有大纲，重点筛掉水剧情、假冲突、工具人、工业糖精和 AI 说明书味

- `v-novel-新小说开坑总控`
  - 新小说开坑总控 skill（精简白金版）
  - 适合先以“白金作家 + 番茄金番作家”双作家会审给 3-5 个原创话题；用户确认后再做开坑孵化、细纲、正文或落盘
  - 参考原文/样文时只借机制，不沿用原文姓名、书名、资产名、事件链和结局道具
  - 短篇爽文话题必须给出爽文类型、写作公式、代入身份爽、情感释放爽、三方利益、三方极致性格和主基调情绪，缺一项即不合格
  - 话题必须是可直接开场的具体点子，不能只是题材名、套路名或抽象情绪；短篇爽文必须先选身份打脸、偏心清算、冒名自爆、退让接盘、惨事清算等具体爽型，并套对应写作公式，不同爽型不能共用同一套打脸公式
  - 内容禁区：禁止用法律、证据、账单、论文、政府、商业项目、电竞、厨师、酒庄、奇怪商业当核心推进器

- `v-novel-细纲-修仙`
  - 修仙剧情 3-5 章小阶段推进 skill
  - 适合接住修仙/仙侠/玄幻仙门文的当前卡点，把设定、卷目标、人物利益和已有伏笔推进成可直接扩写正文的小闭环细纲

- `v-novel-reversal-foreshadowing`
  - 网文/短剧通用反转与伏笔找补 skill
  - 适合长篇网文、番茄连载、短篇和短剧的身份反转、动机反转、认知反转设计与审查，确保反转有伏笔、有动机、能往回找补

- `v-novel-round-table`
  - 网文拆文后圆桌会策划 skill
  - 适合让番茄爽文读者、毒舌读者、番茄金番小说家、起点白金作家等角色讨论拆文成果、避撞车并缝合生成新小说大纲

- `v-novel-write-shuangwen`
  - 番茄爽文正文直出 skill
  - 适合按“番茄连载口感”直接写爽文开篇、续写、改写、扩写与章节正文

- `v-novel-write-hero`
  - 网文英雄之旅嵌套齿轮写作 skill
  - 适合男频快节奏连载的章节设计、弧线规划、卷级衔接、升级螺旋、主线副本与多线收束结构治理

- `v-novel-write-xiuxian`
  - 通用修仙正文直出 skill
  - 适合写修仙、仙侠、玄幻仙门、反套路修仙、命数/因果/宗门斗争/天命抗争类章节；未指定时默认男频长篇用第三人称有限视角

- `v-novel-multi-role-review`
  - 多角色网文审查 skill
  - 适合用多个创作/读者/商业化视角联合审查章节、大纲或片段

- `v-novel-镜灵章节审查`
  - 镜灵章节审查与实改流水线 skill
  - 适合对章节正文做 v-novel-anti-ai、毒舌读者、番茄爽文金番作家、番茄组与圆桌会多轮审查实改，目标把实稿打到 9.7 分以上

- `小说情绪自检`
  - 小说/网文/短剧正文的读者情绪自检 skill
  - 适合检查章节、场景、片段或细纲是否真正让读者产生情绪变化，重点校验“读者情绪 ≠ 角色情绪”、处境代入、真实代价、情绪因果链、紧松节奏、外化动作与结尾未回答问题

- `v-stock-analysis`
  - A 股强势股资金分析技能
  - 适合涨停池、强势股、资金指标、单股技术面综合分析

- `v-wechat-article-formatter-skill`
  - 微信公众号 Markdown 格式化与发布 skill
  - 适合通过 bm.md 渲染和微信官方 API 发布文章

- `v-wechat-publish`
  - 微信公众号完整发布流程
  - 适合从正文优化、去 AI 痕迹、格式化到发布草稿与通知的流水线处理

## 目录结构

```text
my-skills/
├── v-AI-Short-Drama-Agent-Skill/
│   └── SKILL.md
├── v-humanizer/
│   ├── SKILL.md
│   └── readme.md
├── v-khazix-writer/
│   ├── SKILL.md
│   ├── readme.md
│   └── references/
├── v-neat-freak/
│   ├── SKILL.md
│   └── references/
├── v-novel-anti-ai/
│   └── SKILL.md
├── v-novel-anti-ai-only-sentence/
│   └── SKILL.md
├── v-novel-对话感情增强/
│   └── SKILL.md
├── v-novel-build/
│   └── SKILL.md
├── v-novel-chaiwen/
│   ├── SKILL.md
│   └── chaiwen/
├── v-novel-fanqie-bestseller-template/
│   └── SKILL.md
├── v-novel-大纲排雷清单/
│   └── SKILL.md
├── v-novel-新小说开坑总控/
│   ├── SKILL.md
│   └── readme.md
├── v-novel-细纲-修仙/
│   └── SKILL.md
├── v-novel-reversal-foreshadowing/
│   └── SKILL.md
├── v-novel-round-table/
│   └── SKILL.md
├── v-novel-write-shuangwen/
│   ├── SKILL.md
│   └── references/
├── v-novel-write-hero/
│   └── SKILL.md
├── v-novel-write-xiuxian/
│   └── SKILL.md
├── v-novel-multi-role-review/
│   └── SKILL.md
├── v-novel-镜灵章节审查/
│   └── SKILL.md
├── 小说情绪自检/
│   └── SKILL.md
├── v-stock-analysis/
│   └── SKILL.md
├── v-wechat-article-formatter-skill/
│   ├── SKILL.md
│   └── readme.md
├── v-wechat-publish/
│   └── SKILL.md
└── README.md
```

## 安装方式

### 方式 1：逐个软链接（推荐）

```bash
mkdir -p ~/.agents/skills
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-AI-Short-Drama-Agent-Skill ~/.agents/skills/v-AI-Short-Drama-Agent-Skill
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-humanizer ~/.agents/skills/v-humanizer
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-khazix-writer ~/.agents/skills/v-khazix-writer
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-neat-freak ~/.agents/skills/v-neat-freak
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-anti-ai ~/.agents/skills/v-novel-anti-ai
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-anti-ai-only-sentence ~/.agents/skills/v-novel-anti-ai-only-sentence
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-对话感情增强 ~/.agents/skills/v-novel-对话感情增强
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-build ~/.agents/skills/v-novel-build
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-chaiwen ~/.agents/skills/v-novel-chaiwen
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-fanqie-bestseller-template ~/.agents/skills/v-novel-fanqie-bestseller-template
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-大纲排雷清单 ~/.agents/skills/v-novel-大纲排雷清单
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-新小说开坑总控 ~/.agents/skills/v-novel-新小说开坑总控
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-细纲-修仙 ~/.agents/skills/v-novel-细纲-修仙
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-reversal-foreshadowing ~/.agents/skills/v-novel-reversal-foreshadowing
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-round-table ~/.agents/skills/v-novel-round-table
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-write-shuangwen ~/.agents/skills/v-novel-write-shuangwen
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-write-hero ~/.agents/skills/v-novel-write-hero
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-write-xiuxian ~/.agents/skills/v-novel-write-xiuxian
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-multi-role-review ~/.agents/skills/v-novel-multi-role-review
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-镜灵章节审查 ~/.agents/skills/v-novel-镜灵章节审查
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/小说情绪自检 ~/.agents/skills/小说情绪自检
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-stock-analysis ~/.agents/skills/v-stock-analysis
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-wechat-article-formatter-skill ~/.agents/skills/v-wechat-article-formatter-skill
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-wechat-publish ~/.agents/skills/v-wechat-publish
```

如果目标位置已有同名目录，先删除再重建：

```bash
rm -rf ~/.agents/skills/v-AI-Short-Drama-Agent-Skill
rm -rf ~/.agents/skills/v-humanizer
rm -rf ~/.agents/skills/v-khazix-writer
rm -rf ~/.agents/skills/v-neat-freak
rm -rf ~/.agents/skills/v-novel-anti-ai
rm -rf ~/.agents/skills/v-novel-anti-ai-only-sentence
rm -rf ~/.agents/skills/v-novel-对话感情增强
rm -rf ~/.agents/skills/v-novel-build
rm -rf ~/.agents/skills/v-novel-chaiwen
rm -rf ~/.agents/skills/v-novel-fanqie-bestseller-template
rm -rf ~/.agents/skills/v-novel-大纲排雷清单
rm -rf ~/.agents/skills/v-novel-新小说开坑总控
rm -rf ~/.agents/skills/v-novel-细纲-修仙
rm -rf ~/.agents/skills/v-novel-reversal-foreshadowing
rm -rf ~/.agents/skills/v-novel-round-table
rm -rf ~/.agents/skills/v-novel-write-shuangwen
rm -rf ~/.agents/skills/v-novel-write-hero
rm -rf ~/.agents/skills/v-novel-write-xiuxian
rm -rf ~/.agents/skills/v-novel-multi-role-review
rm -rf ~/.agents/skills/v-novel-镜灵章节审查
rm -rf ~/.agents/skills/小说情绪自检
rm -rf ~/.agents/skills/v-stock-analysis
rm -rf ~/.agents/skills/v-wechat-article-formatter-skill
rm -rf ~/.agents/skills/v-wechat-publish
```

### 方式 2：复制目录

如果某个 agent 不认软链接，可以直接复制：

```bash
mkdir -p ~/.agents/skills
cp -R /Users/vanilla/git/github/cute-angelia/my-skills/v-neat-freak ~/.agents/skills/
```

但复制方式后续需要手动同步更新，不如软链接方便。

## 已完成的本地链接

当前已经建立好的软链接：

- `~/.agents/skills/v-AI-Short-Drama-Agent-Skill`
- `~/.agents/skills/v-neat-freak`
- `~/.agents/skills/v-novel-anti-ai`
- `~/.agents/skills/v-novel-对话感情增强`
- `~/.agents/skills/v-novel-build`
- `~/.agents/skills/v-novel-chaiwen`
- `~/.agents/skills/v-novel-fanqie-bestseller-template`
- `~/.agents/skills/v-novel-大纲排雷清单`
- `~/.agents/skills/v-novel-新小说开坑总控`
- `~/.agents/skills/v-novel-细纲-修仙`
- `~/.agents/skills/v-novel-reversal-foreshadowing`
- `~/.agents/skills/v-novel-round-table`
- `~/.agents/skills/v-novel-write-shuangwen`
- `~/.agents/skills/v-novel-write-hero`
- `~/.agents/skills/v-novel-write-xiuxian`
- `~/.agents/skills/v-novel-multi-role-review`
- `~/.agents/skills/v-novel-镜灵章节审查`
- `~/.agents/skills/小说情绪自检`
- `~/.agents/skills/v-stock-analysis`
- `~/.agents/skills/v-wechat-publish`
- `~/.claude/skills/v-neat-freak`
- `~/.codex/skills/v-neat-freak`
- `~/.hermes/skills/software-development/v-neat-freak`
- `~/.hermes/skills/creative/v-novel-大纲排雷清单`
- `~/.hermes/skills/creative/v-novel-对话感情增强`

它们都指向本仓库对应目录。

## 维护建议

1. 每个 skill 独立一个目录
2. 主说明文件统一使用 `SKILL.md`
3. 如需补充脚本或参考材料，优先使用：
   - `scripts/`
   - `references/`
   - `assets/`
4. 修改时只改本仓库源码，不直接改 `~/.agents/skills` 里的软链接目标路径外壳
5. 如果 skill 面向多个 agent，优先把“原则”和“平台映射”写清楚，不把某一家平台的命令硬编码成唯一做法

## 兼容性说明

`~/.agents/skills` 不是所有 agent 的通用标准，但很多兼容 open-agent / pi-agent / QClaw 风格技能发现机制的 agent 会扫描这个目录。

如果某个 agent 不识别这里，可再按该 agent 的约定补一份：
- `~/.hermes/skills/`
- `~/.claude/skills/`
- `~/.codex/skills/`
- 项目内 `.agents/skills/`

## 后续可扩展

后面如果继续新增 skill，建议统一按下面流程：

1. 在 `my-skills/` 下新建目录
2. 写好 `SKILL.md`
3. 软链接到 `~/.agents/skills/`
4. 验证 agent 是否能发现并读取
