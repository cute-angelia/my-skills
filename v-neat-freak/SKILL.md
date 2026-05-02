---
name: v-neat-freak
description: >
  End-of-session knowledge cleanup with editor-level rigor. Use when the user asks
  to sync docs, tidy knowledge, update memory, do handoff cleanup, or when a dev
  milestone changed code/docs and the knowledge base may have drifted. Cross-agent:
  works for Hermes, Claude Code, Codex, OpenCode, and OpenClaw. Focus on reconciling
  durable memory, project instructions (CLAUDE.md / AGENTS.md / equivalents), README,
  and docs/ against the real codebase so future humans and agents inherit clean,
  current knowledge instead of stale notes.
---

# v-neat-freak

你不是记录员，你是知识库编辑。

记录员只会往后追加；编辑会盘点全局、发现漂移、合并重复、修正过期、删除废弃，并把不同受众该看的那一层知识同步好。这个 skill 的目标不是“留痕”，而是让项目知识体系始终干净、准确、可接手。

适用平台：
- Hermes
- Claude Code
- OpenAI Codex
- OpenCode
- OpenClaw
- 其他支持 `SKILL.md` 的 agent（按本文的“平台映射”做等价替换）

如果当前 agent 没有独立记忆系统，也照样可用：把重点放在项目根 markdown、README 和 docs/。

## 何时触发

出现以下任一类意图时触发：

1. 用户显式要求同步 / 收尾 / 整理
- “sync up”
- “tidy up docs”
- “update memory”
- “clean up docs”
- “/sync”
- “/neat”
- “同步一下”
- “整理文档”
- “整理一下”
- “更新记忆”
- “梳理一下”
- “收尾”
- “这个阶段做完了”
- “新人能直接上手”

2. 用户指出知识漂移
- 文档过期
- memory/记忆矛盾
- README 跟代码不一致
- 接手人看不懂怎么启动/接入/运维

3. 会话虽然没明确说“整理”，但已经发生明显里程碑
- 新增 API / 路由 / CLI 命令
- 新增或改名环境变量
- 引入新目录结构、工作流、状态文件
- 影响到上下游项目的对接方式
- 适合做 handoff、发版前清理、阶段性交接

触发原则：宁可略微早触发，也不要漏掉阶段收尾。

## 三层知识模型：先分受众，再决定改哪里

| 层级 | 受众 | 典型载体 | 职责 |
|---|---|---|---|
| Agent 记忆层 | 当前 agent 自己跨会话复用 | Hermes memory、Claude memory、其他平台记忆机制 | 用户偏好、非显而易见的稳定事实、跨会话提醒 |
| 项目指令层 | 下次进入该项目的 agent | `CLAUDE.md` / `AGENTS.md` / 平台等价文件 | 项目约定、红线、目录结构、命令入口、环境假设 |
| 公共文档层 | 人类同事、下游系统、未来接手者 | `README.md`、`docs/*.md`、handoff/runbook | 如何安装、接入、运维、理解系统 |

三层受众不同，不互相替代。

例子：
- “新增了 5 个 device flow 路由”
  - 不是只改 `CLAUDE.md` 就结束
  - 还要看 `README.md` / `docs/integration-guide.md` / `docs/architecture.md` 是否也该改
- “用户偏好中文、要求严筛盘前票”
  - 适合 Hermes memory 或等价记忆层
  - 不该塞进项目 README

## 平台映射

### Hermes
- 记忆层：优先用 `memory` 工具维护 durable facts
- 项目指令层：项目里的 `CLAUDE.md` / `AGENTS.md` / 等价 markdown
- 文档层：`README.md`、`docs/`、handoff 文档
- 检查/修改：优先用 `read_file`、`search_files`、`patch`、`write_file`
- 验证：必要时用 `terminal` 做 `git status`、测试、路径校验

### Claude Code
- 记忆层：`~/.claude/projects/<...>/memory/`
- 项目指令层：项目根 `CLAUDE.md`
- 文档层：`README.md`、`docs/`

### OpenAI Codex
- 记忆层：通常没有独立 memory 文件；跨会话项目知识主要落在 `AGENTS.md`
- 项目指令层：项目根 `AGENTS.md` / `AGENTS.override.md`
- 文档层：`README.md`、`docs/`

### OpenCode
- 可能同时扫描 `.opencode/`、`.claude/`、`.codex/`
- 依旧按“三层知识”做，不要因为目录多就把受众混在一起

### OpenClaw
- 没有强依赖独立 memory 文件时，优先同步项目根 markdown 与 docs
- 若平台支持 workspace/project/user 多层 skill 与配置，仍然遵守“读者分层”原则

## 执行流程

### 第一步：强制盘点，不能跳

先枚举，再判断。不要凭印象说“这项目应该只有 README 和 docs”。

对每个本次会话涉及的项目，至少做这些事：

1. 枚举项目根目录
2. 枚举 `docs/`（即使不存在，也要确认不存在）
3. 搜索散落在根目录或二级目录里的 markdown
4. 读取这些文件中与项目知识相关的候选项：
   - `README.md`
   - `CLAUDE.md`
   - `AGENTS.md`
   - `TEAM_GUIDE.md`
   - `docs/*.md`
   - 其他承担 handoff / runbook / architecture / integration 的 markdown
5. 检查平台级知识位置（按当前 agent 选）
   - Hermes：查看是否需要改 memory；必要时回顾已有 memory 注入内容
   - Claude Code / Codex / OpenCode / OpenClaw：读等价的项目指令与记忆文件
6. 回顾本次对话与本次代码变更

必须在脑中形成一张“文件清单”：
- 已评估
- 要改
- 明确不用改

漏掉一个关键文档，就是这个 skill 最常见的失败模式。

### 第二步：建立“变更影响矩阵”

不要只问“新增了什么事实”，而要问：
“这条事实会影响哪几层知识、哪几类读者？”

常见映射：
- 新增 API / 路由
  - 项目指令层路由说明
  - `docs/integration-guide.md`
  - `docs/architecture.md`
- 新增 / 改名环境变量
  - 项目指令层环境变量表
  - `docs/operator-runbook.md`
  - 接入文档（若下游也要配置）
- 新增数据库表 / 状态文件 / 目录结构
  - 项目指令层结构说明
  - `docs/architecture.md`
  - 必要时 README 启动步骤
- 新增大特性
  - integration-guide
  - architecture
  - runbook
  - handoff / changelog
- 跨项目改动
  - 上游项目文档和下游项目接入文档都要改

参考表见：
- `references/sync-matrix.md`

### 第三步：实际修改，不接受“口头计划”

必须真的改文件或记忆，不能停留在“建议这样改”。

推荐顺序：
1. 先改 docs / README（影响外部读者最大）
2. 再改项目指令层（CLAUDE.md / AGENTS.md / 等价文件）
3. 最后理 agent 记忆层

为什么这个顺序更稳：
- 就算中途被打断，最外层读者先看到的是最新文档
- memory 最灵活，应该最后收口，不应替代正式文档

编辑原则：
- 合并优于追加
- 删除优于保留
- 精确优于冗长
- 绝对时间优于相对时间
- 面向对应受众写作，不要跨层污染
- 只把 durable facts 写进记忆层，不把临时任务状态塞进去

### 第四步：按平台落地

#### 在 Hermes 里
- 读文件：`read_file` / `search_files`
- 改文件：`patch` / `write_file`
- 改记忆：`memory`
- 校验：`terminal` 看 `git status`、路径、测试或命令输出
- 如果工作量大，可用 `todo` 管理收尾 checklist

Hermes 专属硬规则：
- 用户偏好、稳定环境事实、长期约定 → `memory`
- 会话进度、一次性任务结果、临时 TODO → 不进 `memory`
- 如果你说“我会同步/检查/修改”，必须立刻真的调用工具

#### 在其他 agent 里
采用等价能力：
- Read / Search / Edit / Write / Memory API / shell
- 如果没有 memory，就把精力集中到项目指令层和公共文档层

### 第五步：自检清单

逐项过，不要偷懒：

- [ ] 第一步枚举到的每个关键文件都已经判断“已改”或“无需改”
- [ ] README 的安装 / 运行 / 接入步骤与代码一致
- [ ] 项目指令层提到的路径、命令、环境变量在仓库里真实存在
- [ ] 新增 API / 路由时，integration-guide 与 architecture 都同步了
- [ ] 新增环境变量时，runbook 与项目指令层都同步了
- [ ] 新增结构化状态文件 / 数据模型时，architecture 与项目指令层都同步了
- [ ] 跨项目影响已检查，不只改上游不改下游
- [ ] 没有残留“今天 / 最近 / yesterday / recently”这类相对时间
- [ ] 记忆层（若有）没有重复、矛盾、一次性临时信息

### 第六步：输出变更摘要

改完之后再总结，不要先总结后执行。

建议格式：

```text
同步完成

记忆变更
- 更新：...
- 新增：...
- 删除：...

文档变更
- <项目>/README.md — ...
- <项目>/CLAUDE.md — ...
- <项目>/docs/architecture.md — ...

未处理
- ...（只有确实需要用户拍板时才写）
```

只列有实际变更的项；没改的不写。

## 特殊情况

### 1. 对话没有新增事实
也要做审查。

如果发现文档本来就过期、矛盾、含糊、还在用相对时间，照样应该修。这个 skill 的价值不只在“新增”，也在“清污”。

### 2. 项目还没有 README / CLAUDE.md / AGENTS.md
判断项目成熟度：
- 已有可运行代码或可接手工作流：应补最小可用文档
- 还只是 vibe / 草稿阶段：可以暂缓，但要在摘要说明

### 3. 记忆冲突无法自动裁决
这是少数需要用户介入的情况。

例如：
- 两条长期偏好互相打架
- 两个项目事实无法从代码或对话验证

除此之外，优先自己拍板，不要把一般性的整理工作甩回给用户。

### 4. 跨项目会话
本次会话如果碰了多个仓库，就对每个仓库独立跑一次“盘点 → 影响矩阵 → 修改 → 自检”。

最容易漏改的是：
- 上游 API 变了，但下游接入文档没改
- 共享环境变量变了，但 consumer 项目 setup 文档没改
- CLI 行为变了，但 README 仍是旧命令

## 完成标准

只有同时满足以下条件，才算真的完成：

1. 代码事实、项目指令、公共文档、agent 记忆之间没有明显漂移
2. 受众分层清晰，没有把 memory、项目约定、外部文档混成一锅
3. 至少做过一次实际修改或一次明确的“全量核查后确认无需修改”
4. 给用户的摘要能说明改了什么、为什么改、还有什么未决项

## 反模式

不要这样做：
- 只改 `CLAUDE.md` / `AGENTS.md` 就说“同步完成”
- 只往后追加，不清理过期信息
- 把一次性任务状态写进长期 memory
- 把用户偏好塞进 README
- 把 README 当成给 agent 自己看的内部提示本
- 发现跨项目影响却只改当前仓库
- 只口头建议，不实际动手

## 参考资料

- `references/sync-matrix.md` — 变更类型到文档层的映射
- `references/agent-paths.md` — 各 agent 的记忆/配置/skill 路径速查
