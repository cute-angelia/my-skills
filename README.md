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
  - 小说反 AI 审查技能
  - 适合对章节正文、场景段落、人设表达做去 AI 味、去模板化、去解释腔审查；默认先给审查报告，由用户决定是否实改

- `v-novel-build`
  - novelOs 三项目分流选择技能
  - 适合在 open-novel-writing、novel-pro、webnovel-writer 之间快速选型并进入正确工作流

- `v-novel-multi-role-review`
  - 多角色网文审查 skill
  - 适合用多个创作/读者/商业化视角联合审查章节、大纲或片段

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
├── v-novel-build/
│   └── SKILL.md
├── v-novel-multi-role-review/
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
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-build ~/.agents/skills/v-novel-build
ln -s /Users/vanilla/git/github/cute-angelia/my-skills/v-novel-multi-role-review ~/.agents/skills/v-novel-multi-role-review
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
rm -rf ~/.agents/skills/v-novel-build
rm -rf ~/.agents/skills/v-novel-multi-role-review
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
- `~/.agents/skills/v-novel-build`
- `~/.agents/skills/v-novel-multi-role-review`
- `~/.agents/skills/v-stock-analysis`
- `~/.agents/skills/v-wechat-publish`
- `~/.claude/skills/v-neat-freak`
- `~/.codex/skills/v-neat-freak`
- `~/.hermes/skills/software-development/v-neat-freak`

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
