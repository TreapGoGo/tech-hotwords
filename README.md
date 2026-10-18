# tech-hotwords

给科技口语听写使用的简短词包，覆盖 AI 模型与产品、开发工具、硬件和创投话题。优先收母词、常说的专名和有实际使用依据的中文称呼，不把产品目录搬进词库。

最近核实：**2026-10-18 UTC**。当前共 **161 个概念、211 个写法**。英文名和中文别称属于同一个概念；客户端兼容格式把这些写法分别放在一行。

| 词包 | 范围 | 写法数 |
| --- | --- | ---: |
| `ai.txt` | 模型、产品、科技人物 | 52 |
| `dev.txt` | 开发工具、协议、技能生态 | 46 |
| `hardware.txt` | 芯片家族、算力、机器人品牌 | 31 |
| `topics.txt` | AI 概念、创业与投资话题 | 82 |

包含 harness、human-in-the-loop、AGI、JEPA、OpenClaw、Hermes Agent、skill、Codex、Anthropic、Sam Altman、Claude Opus、Claude Mythos、GPT-6 Astra 等讨论中的名称。模型名以核实当日的官方页面为依据；收录不表示模型对所有用户开放。

## 使用

下载 [最新 Release](https://github.com/TreapGoGo/tech-hotwords/releases/latest) 的 `.txt` 文件，每行一个写法，UTF-8，`#` 开头为说明。`index.json` 提供包名、词数和核实日期。

Loqua 用户在热词设置中同步词包，按需要勾选四个包。概念和创投用语放在新增的 `topics.txt`，已有配置需要勾选该包才能使用。词包是识别提示，不是自动翻译或强制替换规则。

## 收录原则

- 母词优先。MCP 保留 MCP、MCP Server、MCP Client、MCP Apps；不枚举各语言 SDK，也不机械组合术语。
- 型号克制。保留常用品牌、架构和产品家族，去掉大量完整 SKU、日期后缀和规格名；常被讨论的当前模型系列可保留。
- 中英写法有据可查。只有在中文社区、媒体或官方页面实际看到的称呼才作为别称；不为每个英文品牌生造中文音译。一个概念最多四个写法。
- 关注当前讨论，也保留仍常用的基础词。没有首次发布年份门槛；公众科技人物可以收录，不收私人资料。
- 榜单用于发现候选。一次上榜、一个新 checkpoint 或一篇报道不足以证明值得常驻，不追求凑数量。

本轮缩减硬件枚举和 MCP 组合，补入此前缺失的概念、人物和中英别称。总行数不能直接用来衡量概念是否冗余；分组见 `lexicon.tsv`。

## 数据与维护

`lexicon.tsv` 是唯一词源：`pack` 为词包，`canonical` 为母词，`aliases` 为 `|` 分隔的别称，`sources` 为 `sources.json` 中的来源 ID。`sources.json` 记录链接、来源类型、语言和实际观察到的用法；[SOURCES.md](SOURCES.md) 说明发现渠道与核实边界。

修改 TSV 和来源后运行：

```sh
python build.py
python build.py --check
python validate.py
```

生成的 `.txt` 和 `index.json` 也需提交。校验覆盖来源引用、中文来源、跨包重复、Unicode 规范化、客户端长度限制、每包最多 150 个写法及四包合计最多 600 个写法。校验能检查结构，不能替代对来源内容和使用频率的人工判断。

欢迎提交附有真实用法链接的 issue 或 PR。main 推送通过校验后自动创建 Release，附带四个词包、索引以及可审计的词源和来源文件。当前更新由人工调研辅助 AI 整理，不承诺自动实时追踪全网。

## 许可

本仓库整理的词表和贡献采用 **CC0 1.0**，见 [LICENSE](LICENSE)。来源网页、文章和第三方仓库保留各自许可；列出链接不表示其内容属于 CC0。

