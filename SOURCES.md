# 来源与核实说明

本轮核实日期：**2026-10-18 UTC**。链接和实际观察记录在 [`sources.json`](sources.json)，每个母词通过 [`lexicon.tsv`](lexicon.tsv) 引用来源。来源记录用于追溯名称和写法，不等同于对使用频率的统计证明。

## 模型与产品名称

当前系列优先查官方目录：[OpenAI](https://developers.openai.com/api/docs/models)、[Anthropic](https://www.anthropic.com/claude/mythos)、[Gemini](https://ai.google.dev/gemini-api/docs/models)、[DeepSeek](https://www.deepseek.com/)、[通义](https://tongyi.aliyun.com/)、[Kimi](https://www.kimi.com/)、[MiniMax](https://www.minimaxi.com/)、[Z.AI](https://docs.z.ai/guides/overview/overview)。本轮据实际页面更新 GPT、Claude、Gemini、DeepSeek、GLM、MiniMax、Kimi 系列，去掉大批旧版本和日期后缀。Claude Mythos 官方页面注明受限访问。

开发生态直接读 [OpenClaw](https://github.com/openclaw/openclaw)、[Hermes Agent](https://github.com/NousResearch/hermes-agent)、[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)、[Agent Skills](https://agentskills.io/home)、[llama.cpp](https://github.com/ggml-org/llama.cpp)、[vLLM](https://docs.vllm.ai/en/latest/)、[SGLang](https://docs.sglang.ai/) 的原文。OpenClaw 和 Prompt Engineering Guide 另外询问过 DeepWiki，以原始代码和文档为最终依据。

## 中文实际用法

- [宝玉的分享](https://baoyu.io/)：核对 Hermes Agent、提示词缓存、AI 原生、PMF、GTM、FDE、规模化定律及科技人物的实际写法；相关正文逐条记录在来源表。
- [李不凯的 Agent Skills 指南](https://github.com/libukai/awesome-agent-skills)：观察中文开发者社区对 Skill、技能、Harness 及工具名称的使用。
- [菜鸟教程 AI Agent 术语](https://www.runoob.com/ai-agent/ai-terminology.html)和 [Harness Engineering](https://www.runoob.com/ai-agent/harness-engineering.html)：核对人在回路、氛围编程、上下文工程、驾驭工程等已出现的中英写法。教程中的译法不是强制的行业标准。
- [量子位 2026-10-16 机器人报道](https://www.qbitai.com/2026/10/503865.html)、[模型报道](https://www.qbitai.com/2026/10/503701.html)和 [2026-10-13 创投报道](https://www.qbitai.com/2026/10/503093.html)：补充近期世界模型、VLA、具身智能、种子轮和投后估值等话题。只取词语，不为报道中的预测背书。
- NVIDIA、AMD、Intel、高通和宇树的中文官方页面用于品牌与家族名。硬件保留架构、母词与常用家族，不复制完整型号目录。

中文译名存在分歧时保持克制。例如 harness 暂时保留英文母词，harness engineering 另保留已经出现的“驾驭工程”；没有证据支持的中文产品音译不加入。公众人物可保留英文名，已有实际中文称呼的如黄仁勋、杨立昆另列别称。

## 探索过的发现渠道

| 渠道 | 本轮观察 | 处理方式 |
| --- | --- | --- |
| [Hugging Face trending](https://huggingface.co/models?sort=trending) | 当日趋势 API 可读，包含新模型和生成生态 | 发现候选，再查名称；不逐个收 checkpoint |
| [Product Hunt](https://www.producthunt.com/) | 首页有日、周、月榜 | 可发现新产品；一次发布上榜不等于口语高频，未批量导入 |
| [awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) | 活跃的中文生态与工具索引 | 适合发现新名称，仍需筛选母词 |
| [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 教程和基础概念丰富 | 可核对术语，不作为最新产品榜单 |
| [ai-glossary-mandarin](https://github.com/eugenesiow/ai-glossary-mandarin) | 观察到最后推送为 2020-12-18，且采用 CC-BY-SA-4.0 | 不适合直接充当当前热词源，未复制其词表 |

这些来源仍然碎片化。本轮没有找到一个可以直接照搬、同时满足前沿时效、中文实际用法和口语精简要求的开源词库，也没有把热门榜单自动等同于收录名单。

## 边界与排除

网站会更新、重定向或限制访问；核实日期只表示本轮观察时间。部分官方页面需要浏览器读取，不能只凭 HTTP 状态推断内容不存在。杨立昆的中文写法通过搜索结果中的中文标题观察到，知乎正文受限；来源记录明确标注这一限制。Habitat-Lab 已不再由 Meta 主动维护，仅用于核对 embodied AI 英文写法，当前话题另有新报道。

本轮对指定来源没有完整确认的 Replit、HITL、Doubao、“通义千问”和“骁龙”写法暂不加入；这不表示这些名称无效。保留有来源的“豆包”“千问”“后训练”和 Snapdragon，不为追求双语完整度补造证据。SDK 语言组合、冗长 SKU、机械拼装短语和短期小众新品也不作为填充项。

