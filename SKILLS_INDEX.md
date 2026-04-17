# Skills Collection Index

> 本仓库收录了多个 Claude Code / AI Agent 技能合集，按功能聚类分类，每个聚类内按综合评分排名。
> 基于 `skills-registry.json` 自动生成 | 更新时间: 2026-04-17

**Fallback 机制**: 同一聚类内，优先使用排名靠前的 skill；如果首选 skill 失败（依赖缺失/API 报错），自动降级到下一个。

**总计**: 11 个聚类, 222 个技能

---

## 1. 内容创作与写作

文章撰写、文案生成、风格提取、小说写作等创作场景

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-comic | baoyu-skills | 84 | Knowledge comic creator supporting multiple art styles an... | 首选 |
| 2 | novel-writer | wpsnote-skills | 81 | AI 陪伴式长篇小说创作助手，结合 WPS 笔记实现有记忆、懂上下文、不穿帮的持续创作。触发词：帮我写小说、我想写... | 备选 |
| 3 | novel-writer-cli | wpsnote-skills | 71 | AI 陪伴式长篇小说创作助手（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记，实现有... |  |
| 4 | wechat-tech-writer | wechat_article_skills | 71 | 自动搜索、抓取、改写技术内容，生成适合微信公众号的中文科普文章。涵盖AI大模型、GitHub开源工具、技术话题。当... |  |
| 5 | ljg-writes | ljg-skills | 68 | 写作引擎。像手术刀剖开一个观点，一层层剥到底。1000-1500 字。 |  |
| 6 | wechat-product-manager-writer | wechat_article_skills | 66 | 从 AI 产品经理视角撰写微信公众号文章。涵盖 AI 产品拆解、场景解决方案、效率提升实战、产品方法论、行业观察。... |  |
| 7 | founder-sales | lenny-skills | 66 | Help founders close their first customers and build repea... |  |
| 8 | written-communication | lenny-skills | 66 | Help users communicate more effectively in writing. Use w... |  |
| 9 | managing-tech-debt | lenny-skills | 66 | Help users manage technical debt strategically. Use when ... |  |
| 10 | writing-north-star-metrics | lenny-skills | 66 | Help users define their North Star metric. Use when someo... |  |
| 11 | writing-specs-designs | lenny-skills | 65 | Help users write effective specs and design documents. Us... |  |
| 12 | working-backwards | lenny-skills | 65 | Help users apply the working backwards methodology. Use w... |  |
| 13 | writing-job-descriptions | lenny-skills | 64 | Help users write effective job descriptions. Use when som... |  |
| 14 | writing-prds | lenny-skills | 64 | Help users write effective PRDs. Use when someone is docu... |  |
| 15 | building-with-llms | lenny-skills | 63 | Help users build effective AI applications. Use when some... |  |
| 16 | short-video-copywriter | wpsnote-skills | 61 | | |  |
| 17 | content-creator | wpsnote-skills | 60 | | |  |
| 18 | wechat-style-profiler | wechat-skills | 59 | 面向公众号作者的文风 DNA 梳理技能。用于从 3-10 篇参考文章中建立可复用的风格画像，输出 14 维分析、标... |  |
| 19 | wechat-topic-outline-planner | wechat-skills | 55 | 公众号选题与大纲策划技能。用于把一个粗点子、资料包、语音底稿或采访纪要，转成 2-3 个高价值选题角度、1 个推荐... |  |
| 20 | wechat-title-generator | wechat-skills | 53 | 公众号标题生成与评估技能。用于基于已确认的选题、大纲和目标读者，生成 8 个标题候选，筛掉低质标题，并推荐 1 个... |  |
| 21 | wechat-draft-writer | wechat-skills | 52 | 公众号初稿写作技能。用于在选题和大纲已确认后，基于参考资料、语音底稿和文风 DNA 生成一版高保真初稿。适用于正文... | 保底 |

---

## 2. 图片与视觉生成

AI绘图、信息图、封面、卡片、幻灯片等视觉内容生成与分析

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-cover-image | baoyu-skills | 88 | Generates article cover images with 5 dimensions (type, p... | 首选 |
| 2 | baoyu-image-cards | baoyu-skills | 88 | Generates infographic image card series with 12 visual st... | 备选 |
| 3 | baoyu-xhs-images | baoyu-skills | 88 | Generates Xiaohongshu (Little Red Book) image card series... |  |
| 4 | baoyu-infographic | baoyu-skills | 84 | Generates professional infographics with 21 layout types ... |  |
| 5 | baoyu-slide-deck | baoyu-skills | 84 | Generates professional slide deck images from content. Cr... |  |
| 6 | baoyu-article-illustrator | baoyu-skills | 83 | Analyzes article structure, identifies positions requirin... |  |
| 7 | shader-dev | MiniMax-skills | 78 | Comprehensive GLSL shader techniques for creating stunnin... |  |
| 8 | baoyu-image-gen | baoyu-skills | 78 | AI image generation with OpenAI, Azure OpenAI, Google, Op... |  |
| 9 | baoyu-imagine | baoyu-skills | 78 | AI image generation with OpenAI, Azure OpenAI, Google, Op... |  |
| 10 | logo-design | marketing-skills | 78 | Design professional logos as SVG code with browser previe... |  |
| 11 | ljg-card | ljg-skills | 73 | Content caster (铸). Transforms content into PNG visuals. ... |  |
| 12 | slide-making-skill | MiniMax-skills | 68 | Implement single-slide PowerPoint pages with PptxGenJS. U... |  |
| 13 | mmx-cli | MiniMax-skills | 66 | Use mmx to generate text, images, video, speech, and musi... |  |
| 14 | baoyu-diagram | baoyu-skills | 66 | Create professional, dark-themed SVG diagrams of any type... |  |
| 15 | giving-presentations | lenny-skills | 66 | Help users create and deliver compelling presentations. U... |  |
| 16 | xiaohongshu-note-creator | wpsnote-skills | 65 | | |  |
| 17 | defining-product-vision | lenny-skills | 65 | Help users create compelling product visions. Use when so... |  |
| 18 | managing-imposter-syndrome | lenny-skills | 65 | Help users work through feelings of inadequacy and self-d... |  |
| 19 | organizational-design | lenny-skills | 65 | Help users design effective organizational structures. Us... |  |
| 20 | baoyu-danger-gemini-web | baoyu-skills | 60 | Generates images and text via reverse-engineered Gemini W... | 实验性 |
| 21 | image-gen | wpsnote-skills | 56 | | |  |
| 22 | gif-sticker-maker | MiniMax-skills | 54 | | |  |
| 23 | vision-analysis | MiniMax-skills | 49 | > | 保底 |

---

## 3. 社交媒体发布与排版

微信公众号、微博、X(Twitter)、小红书等平台的发布与格式化

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-markdown-to-html | baoyu-skills | 80 | Converts Markdown to styled HTML with WeChat-compatible t... | 首选 |
| 2 | baoyu-post-to-wechat | baoyu-skills | 78 | Posts content to WeChat Official Account (微信公众号) via API ... | 备选 |
| 3 | baoyu-post-to-x | baoyu-skills | 78 | Posts content and articles to X (Twitter). Supports regul... |  |
| 4 | baoyu-post-to-weibo | baoyu-skills | 70 | Posts content to Weibo (微博). Supports regular posts with ... |  |
| 5 | wechat-publisher | wpsnote-skills | 69 | | |  |
| 6 | wechat-article-formatter | wechat_article_skills | 68 | 将Markdown文章转换为美化的HTML格式，适配微信公众号发布。应用专业CSS样式、代码高亮、优化排版。当用户... |  |
| 7 | thesis-word-formatter | wechat-skills | 64 | 大学生毕业论文 Word 排版技能。用于先收集学校 Word 模板、学院规范、任务书或示例论文，再对本科或硕士毕业... |  |
| 8 | wechat-draft-publisher | wechat_article_skills | 53 | 自动将 HTML 文章发布到微信公众号草稿箱，支持封面图上传、标题、作者和元数据管理。当用户说"推送到微信"、"发... | 保底 |

---

## 4. 翻译与格式转换

翻译、白话改写、Markdown格式化、图片压缩、文件格式转换

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-format-markdown | baoyu-skills | 84 | Formats plain text or markdown files with frontmatter, ti... | 首选 |
| 2 | baoyu-translate | baoyu-skills | 84 | Translates articles and documents between languages with ... | 备选 |
| 3 | ljg-plain | ljg-skills | 79 | Cognitive atom: Plain (白). Rewrites any content so a smar... |  |
| 4 | minimax-xlsx | MiniMax-skills | 73 | Open, create, read, analyze, edit, or validate Excel/spre... |  |
| 5 | baoyu-compress-image | baoyu-skills | 70 | Compresses images to WebP (default) or PNG with automatic... |  |
| 6 | behavioral-product-design | lenny-skills | 65 | Help users apply behavioral science to product design. Us... |  |
| 7 | organizational-transformation | lenny-skills | 65 | Help users transform organizations toward modern product ... |  |
| 8 | enterprise-sales | lenny-skills | 64 | Help users navigate enterprise sales. Use when someone is... |  |
| 9 | qiaomu-markdown-proxy | markdown-proxy | 52 | | |  |
| 10 | minimax-pdf | MiniMax-skills | 45 | > |  |
| 11 | anything-to-md | anything-to-md | 45 | | |  |
| 12 | html-to-pdf | marketing-skills | 36 | > | 保底 |

---

## 5. 信息采集与知识提取

网页抓取、论文阅读、新闻解读、内容摘要、视频字幕、媒体下载

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | ljg-paper | ljg-skills | 92 | Paper reader for non-academics. Takes a paper and extract... | 首选 |
| 2 | content-digest | wpsnote-skills | 87 | 将任意内容提炼为结构化知识笔记，自动保存到 WPS 笔记。只要用户给出任何内容（链接、图片、本地文件、粘贴文字）并... | 备选 |
| 3 | live-transcript-summary | wpsnote-skills | 84 | 边听边总结：实时监听当前 WPS 笔记中的音频转写，每 60 秒自动循环一次，识别场景后按对应模板整理内容，并写回... |  |
| 4 | baoyu-url-to-markdown | baoyu-skills | 84 | Fetch any URL and convert to markdown using baoyu-fetch C... |  |
| 5 | ljg-paper-river | ljg-skills | 83 | 论文倒读法：给一篇论文，递归找出它批判和改进的前序论文（最多5层），再找它之后的最新进展，从源头正向讲述问题演化史... |  |
| 6 | ljg-read | ljg-skills | 82 | Reading companion agent. Accompanies user through any tex... |  |
| 7 | ljg-travel | ljg-skills | 78 | Deep travel research workflow for museums and ancient arc... |  |
| 8 | ljg-paper-flow | ljg-skills | 72 | Paper workflow: read papers + cast cards in one go. Takes... |  |
| 9 | literature-reader | wpsnote-skills | 72 | 阅读、分析并总结学术文献（PDF论文），生成结构化的文献概要笔记。核心能力：论文元信息提取、研究问题识别、方法论梳... |  |
| 10 | doc-importer | wpsnote-skills | 70 | > |  |
| 11 | baoyu-danger-x-to-markdown | baoyu-skills | 68 | Converts X (Twitter) tweets and articles to markdown with... | 实验性 |
| 12 | analyzing-user-feedback | lenny-skills | 66 | Help users synthesize and act on customer feedback. Use w... |  |
| 13 | stakeholder-alignment | lenny-skills | 66 | Help users align stakeholders and get buy-in. Use when so... |  |
| 14 | running-effective-meetings | lenny-skills | 65 | Help users run more effective meetings. Use when someone ... |  |
| 15 | paper-researcher | wpsnote-skills | 62 | 学术论文全流程助手：搜索论文、下载 PDF、存入 WPS 笔记、精读分析。当用户说"搜论文"、"找论文"、"下载论... |  |
| 16 | baoyu-youtube-transcript | baoyu-skills | 59 | Downloads YouTube video transcripts/subtitles and cover i... |  |
| 17 | web-importer | wpsnote-skills | 53 | > |  |
| 18 | news-to-note | wpsnote-skills | 51 | > | 保底 |

---

## 6. 笔记管理与知识整理

笔记美化、标签整理、知识关联、灵感发现、记忆系统

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | note-calendar | wpsnote-skills | 79 | 在 macOS 上打通 WPS 笔记与系统日历。支持查询日程、创建/移动/删除日历事件，以及笔记与日历的双向联动：... | 首选 |
| 2 | wps-note | wpsnote-skills | 79 | 通过 MCP 工具读取、编辑和管理 WPS 笔记，基于 block 文档模型，所有内容以 | 备选 |
| 3 | wpsnote-beautifier | wpsnote-skills | 77 | 智能美化 WPS 笔记文档，采用克制统一的配色风格（全文仅1种主色调，不混用多色系）。核心能力：优化标题层级结构、... |  |
| 4 | tag-organize-cli | wpsnote-skills | 77 | 笔记标签整理的核心原则与完整工作流程（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记... |  |
| 5 | note-copilot | wpsnote-skills | 72 | 笔记协作助手：帮用户打磨当前 WPS 笔记，识别并处理笔记中的 *** 和 /// 援助标记，同时在发现明显逻辑错... |  |
| 6 | ie-engine | wpsnote-skills | 71 | 灵感引擎的统一入口，串联记忆检索、想法连接和洞见生成的完整流水线。当用户提到"灵感引擎"、"激发灵感"、"conn... |  |
| 7 | clawiser | ClaWiser | 70 | Agent 记忆与工作流增强套件。包含 8 个模块：记忆系统（memory-deposit、retrieval-e... |  |
| 8 | tag-organize | wpsnote-skills | 68 | 笔记标签整理的核心原则与完整工作流程。当用户提到"整理笔记标签"、"清理标签"、"标签太乱"、"标签太多"、"帮我... |  |
| 9 | wps-deep-search | wpsnote-skills | 65 | | |  |
| 10 | noise-reduction | ClaWiser | 63 | > |  |
| 11 | ie-generate-insight | wpsnote-skills | 59 | 将推理分析结果转化为可阅读的洞见文本，生成下一步探索建议，展示想法的演化路径。当用户提到"生成洞见"、"给我灵感"... |  |
| 12 | ie-connect-dots | wpsnote-skills | 58 | 对笔记和想法进行语义聚类、发现想法之间的隐含连接、识别长期重复出现的主题模式。当用户提到"连接想法"、"发现关联"... |  |
| 13 | retrieval-enhance | ClaWiser | 58 | 检索系统守护。静默运行——agent 自主判断何时激活。三种场景：(1) 首次搭建时初始化 memorySearc... |  |
| 14 | review-notes | wpsnote-skills | 57 | 作为 coding-assistant 的子 skill，生成或更新 WPS 技术文档。笔记必须完整且包含 7 个... |  |
| 15 | memory-deposit | ClaWiser | 55 | > |  |
| 16 | ie-retrieve-memory | wpsnote-skills | 55 | 从用户的 WPS 笔记中检索历史知识和过去的想法。当用户提到"回忆过去的笔记"、"之前写过什么"、"历史想法"、"... |  |
| 17 | class-note-builder | wpsnote-skills | 51 | 当用户希望把课堂逐字稿、OCR 笔记、截图资料或零散学习内容整理成结构化的 WPS 学习笔记时使用此 Skill。... |  |
| 18 | save-game | ClaWiser | 50 | > |  |
| 19 | load-game | ClaWiser | 50 | > |  |
| 20 | notes-to-lesson-plan | wpsnote-skills | 48 | 当用户希望把 WPS 学习笔记整理成一份可讲给别人听的讲解结构、迷你教案或 teach-back 提纲时使用此 S... |  |
| 21 | insight-recaller | wpsnote-skills | 47 | 当用户在 WPS 里写新内容、做专题复习、准备讲稿或整理研究思路时，希望把过去真正有用的旧笔记重新召回到眼前，就使... |  |
| 22 | study-note-linker | wpsnote-skills | 47 | 当用户希望把当前 WPS 学习笔记和已有旧笔记连起来，而不是让新笔记继续孤立存在时使用此 Skill。适合复习串讲... |  |
| 23 | notes-to-flashcards | wpsnote-skills | 47 | 当用户希望把 WPS 笔记转成可主动回忆的复习卡片时使用此 Skill。适合课程笔记复习、概念记忆、考前冲刺、误解... | 保底 |

---

## 7. 学习与教育

概念解剖、单词精通、闪卡、知识漏洞诊断等学习辅助

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | ljg-word-flow | ljg-skills | 72 | Word flow: deep-dive word analysis + infograph card in on... | 首选 |
| 2 | ljg-word | ljg-skills | 68 | Deep-dive English word mastery tool. Deconstructs a singl... | 备选 |
| 3 | post-mortems-retrospectives | lenny-skills | 65 | Help users run effective post-mortems and retrospectives.... |  |
| 4 | ljg-learn | ljg-skills | 59 | Deep concept anatomist that deconstructs any concept thro... |  |
| 5 | misconception-finder | wpsnote-skills | 48 | 当用户希望检查一篇 WPS 学习笔记里是否存在理解错误、概念混淆、逻辑跳步或表述过虚时使用此 Skill。适合课后... |  |
| 6 | prerequisite-gap-finder | wpsnote-skills | 47 | 当用户觉得一个主题看不懂、学得卡住，或者想知道自己到底缺了哪些前置基础时使用此 Skill。适合课程复习、自学卡点... |  |
| 7 | lecture-focus-extractor | wpsnote-skills | 46 | 当用户手上已经有一篇较长的课堂笔记、逐字稿或学习记录，但只想提取最值得复习的重点时使用此 Skill。适合课程录音... | 保底 |

---

## 8. 开发与工程

前端/移动端/全栈开发、Office自动化、子代理编排、技能管理

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | android-native-dev | MiniMax-skills | 81 | Android native application development and UI design guid... | 首选 |
| 2 | fullstack-dev | MiniMax-skills | 81 | | | 备选 |
| 3 | pptx-generator | MiniMax-skills | 81 | Generate, edit, and read PowerPoint presentations. Create... |  |
| 4 | frontend-dev | MiniMax-skills | 75 | | |  |
| 5 | ljg-skill-map | ljg-skills | 72 | Skill map viewer. Scans all installed skills and renders ... |  |
| 6 | skill-creator | wpsnote-skills | 71 | Create new skills, modify and improve existing skills, an... |  |
| 7 | engineering-culture | lenny-skills | 65 | Help users build strong engineering culture. Use when som... |  |
| 8 | vibe-coding | lenny-skills | 65 | Help users build software using AI coding tools. Use when... |  |
| 9 | ppt-editing-skill | MiniMax-skills | 64 | Edit existing PowerPoint files or templates with XML-safe... |  |
| 10 | color-font-skill | MiniMax-skills | 62 | Choose presentation-ready color palettes and font pairing... |  |
| 11 | ppt-orchestra-skill | MiniMax-skills | 62 | Plan and orchestrate multi-slide PowerPoint creation from... |  |
| 12 | minimax-docx | MiniMax-skills | 61 | > |  |
| 13 | react-native-dev | MiniMax-skills | 60 | | |  |
| 14 | flutter-dev | MiniMax-skills | 59 | | |  |
| 15 | coding-assistant | wpsnote-skills | 59 | 多平台编码助手。遵循各平台官方文档做编码规范、单测与编译/lint；协助将核心技术梳理为完整 WPS 笔记技术文档... |  |
| 16 | ios-application-dev | MiniMax-skills | 56 | | |  |
| 17 | design-style-skill | MiniMax-skills | 46 | > | 保底 |

---

## 9. 商业诊断与分析

商业模式诊断、市场调研、用户访谈、投资分析、产品创新、咨询框架

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | market-sizing | marketing-skills | 84 | Produce a rigorous, sourced TAM/SAM/SOM market sizing for... | 首选 |
| 2 | dbs-xhs-title | dbskill | 70 | | | 备选 |
| 3 | product-rnd | marketing-skills | 68 | End-to-end Product Innovation R&D workflow — inspiration ... |  |
| 4 | conducting-user-interviews | lenny-skills | 66 | Help users run better customer and user interviews. Use w... |  |
| 5 | atypica-user-interview | marketing-skills | 66 | Run AI-simulated user interviews and focus group discussi... |  |
| 6 | ai-product-strategy | lenny-skills | 66 | Help users define AI product strategy. Use when someone i... |  |
| 7 | having-difficult-conversations | lenny-skills | 66 | Help users navigate tough feedback, performance conversat... |  |
| 8 | ljg-rank | ljg-skills | 66 | 给一个领域，找出背后真正撑着它的几根独立的力。十几个现象砍到不可再少的生成器——砍完能把现象一个个生回来，才算数。... |  |
| 9 | evaluating-candidates | lenny-skills | 66 | Help users make better hiring decisions. Use when someone... |  |
| 10 | evaluating-trade-offs | lenny-skills | 66 | Help users make better decisions between competing option... |  |
| 11 | launch-marketing | lenny-skills | 66 | Help users plan and execute product launches. Use when so... |  |
| 12 | managing-up | lenny-skills | 66 | Help users work effectively with their manager and execut... |  |
| 13 | finding-mentors-sponsors | lenny-skills | 66 | Help users build relationships with mentors and sponsors ... |  |
| 14 | brand-storytelling | lenny-skills | 66 | Help users craft compelling brand narratives. Use when so... |  |
| 15 | building-a-promotion-case | lenny-skills | 66 | Help users get promoted at work. Use when someone is prep... |  |
| 16 | managing-timelines | lenny-skills | 66 | Help users set and hit realistic deadlines. Use when some... |  |
| 17 | measuring-product-market-fit | lenny-skills | 66 | Help users assess and achieve product-market fit. Use whe... |  |
| 18 | onboarding-new-hires | lenny-skills | 66 | Help users onboard new team members effectively. Use when... |  |
| 19 | setting-okrs-goals | lenny-skills | 66 | Help users set effective OKRs and goals. Use when someone... |  |
| 20 | shipping-products | lenny-skills | 66 | Help users ship products faster and with higher quality. ... |  |
| 21 | career-transitions | lenny-skills | 65 | Help users navigate career changes and pivots. Use when s... |  |
| 22 | cross-functional-collaboration | lenny-skills | 65 | Help users work effectively across functions. Use when so... |  |
| 23 | partnership-bd | lenny-skills | 65 | Help users build strategic partnerships and business deve... |  |
| 24 | building-sales-team | lenny-skills | 65 | Help users build and scale their sales organization. Use ... |  |
| 25 | community-building | lenny-skills | 65 | Help users build and grow product communities. Use when s... |  |
| 26 | competitive-analysis | lenny-skills | 65 | Help users understand and respond to competition. Use whe... |  |
| 27 | designing-growth-loops | lenny-skills | 65 | Help users design and optimize growth loops. Use when som... |  |
| 28 | planning-under-uncertainty | lenny-skills | 65 | Help users plan products and strategy when outcomes are u... |  |
| 29 | prioritizing-roadmap | lenny-skills | 65 | Help users prioritize product roadmaps and backlogs. Use ... |  |
| 30 | problem-definition | lenny-skills | 65 | Help users define problems clearly before jumping to solu... |  |
| 31 | usability-testing | lenny-skills | 65 | Help users conduct effective usability testing. Use when ... |  |
| 32 | building-team-culture | lenny-skills | 65 | Help users build and maintain strong team culture. Use wh... |  |
| 33 | conducting-interviews | lenny-skills | 65 | Help users conduct effective hiring interviews. Use when ... |  |
| 34 | running-decision-processes | lenny-skills | 65 | Help users run effective decision-making processes. Use w... |  |
| 35 | positioning-messaging | lenny-skills | 65 | Help users craft product positioning and messaging. Use w... |  |
| 36 | pricing-strategy | lenny-skills | 65 | Help users design and optimize pricing strategies. Use wh... |  |
| 37 | retention-engagement | lenny-skills | 65 | Help users improve retention and engagement metrics. Use ... |  |
| 38 | systems-thinking | lenny-skills | 65 | Help users think in systems and understand complex dynami... |  |
| 39 | platform-strategy | lenny-skills | 65 | Help users design and execute platform business strategie... |  |
| 40 | product-taste-intuition | lenny-skills | 65 | Help users develop product taste and intuition. Use when ... |  |
| 41 | running-design-reviews | lenny-skills | 65 | Help users run effective design reviews and critiques. Us... |  |
| 42 | running-effective-1-1s | lenny-skills | 65 | Help users run effective one-on-one meetings. Use when so... |  |
| 43 | energy-management | lenny-skills | 65 | Help users manage their energy for sustained performance.... |  |
| 44 | team-rituals | lenny-skills | 65 | Help users design effective team rituals. Use when someon... |  |
| 45 | user-onboarding | lenny-skills | 65 | Help users design effective product onboarding. Use when ... |  |
| 46 | negotiating-offers | lenny-skills | 65 | Help users negotiate job offers and compensation. Use whe... |  |
| 47 | platform-infrastructure | lenny-skills | 65 | Help users build and scale internal platforms and technic... |  |
| 48 | product-led-sales | lenny-skills | 65 | Help users implement product-led sales motions. Use when ... |  |
| 49 | product-operations | lenny-skills | 65 | Help users build and scale product operations functions. ... |  |
| 50 | running-offsites | lenny-skills | 65 | Help users plan and run effective team offsites. Use when... |  |
| 51 | sales-compensation | lenny-skills | 65 | Help users design sales compensation plans. Use when some... |  |
| 52 | sales-qualification | lenny-skills | 65 | Help users qualify sales leads effectively. Use when some... |  |
| 53 | startup-pivoting | lenny-skills | 65 | Help users decide when and how to pivot their startup. Us... |  |
| 54 | marketplace-liquidity | lenny-skills | 65 | Help users build and manage marketplace liquidity. Use wh... |  |
| 55 | media-relations | lenny-skills | 65 | Help users build relationships with journalists and get p... |  |
| 56 | startup-ideation | lenny-skills | 65 | Help users generate and evaluate startup ideas. Use when ... |  |
| 57 | fundraising | lenny-skills | 64 | Help founders raise capital and build investor relationsh... |  |
| 58 | dogfooding | lenny-skills | 64 | Help users implement effective dogfooding practices. Use ... |  |
| 59 | design-engineering | lenny-skills | 64 | Help users understand and build design engineering capabi... |  |
| 60 | personal-productivity | lenny-skills | 64 | Help users manage their time and tasks more effectively. ... |  |
| 61 | content-marketing | lenny-skills | 64 | Help users build content marketing strategies. Use when s... |  |
| 62 | scoping-cutting | lenny-skills | 64 | Help users scope projects and cut features effectively. U... |  |
| 63 | design-systems | lenny-skills | 64 | Help users build and scale design systems. Use when someo... |  |
| 64 | coaching-pms | lenny-skills | 64 | Help users develop and coach product managers. Use when s... |  |
| 65 | technical-roadmaps | lenny-skills | 63 | Help users create technical roadmaps. Use when someone is... |  |
| 66 | delegating-work | lenny-skills | 63 | Help users delegate effectively. Use when someone is stru... |  |
| 67 | evaluating-new-technology | lenny-skills | 63 | Help users evaluate emerging technologies. Use when someo... |  |
| 68 | plan-as-consultant | marketing-skills | 62 | Plan a business research study the way a professional con... |  |
| 69 | designing-surveys | lenny-skills | 61 | Help users design effective surveys. Use when someone is ... |  |
| 70 | ljg-invest | ljg-skills | 61 | 投资分析, 生成一份深度投资分析报告。不做传统投资分析——核心判断是项目是否是一台「秩序创造机器」。Use whe... |  |
| 71 | dbs-diagnosis | dbskill | 60 | | |  |
| 72 | ai-evals | lenny-skills | 59 | Help users create and run AI evaluations. Use when someon... |  |
| 73 | dbs-hook | dbskill | 50 | | |  |
| 74 | dbs-agent-migration | dbskill | 50 | | |  |
| 75 | ljg-roundtable | ljg-skills | 49 | >- |  |
| 76 | dbs-ai-check | dbskill | 49 | | |  |
| 77 | ljg-relationship | ljg-skills | 48 | >- |  |
| 78 | dbs-chatroom | dbskill | 48 | 定向聊天室：根据话题推荐或接受用户指定的专家，模拟多角色对话。触发方式：/dbs-chatroom、/定向聊天室、... |  |
| 79 | dbs-action | dbskill | 47 | | |  |
| 80 | dbs-slowisfast | dbskill | 47 | | |  |
| 81 | dbs-deconstruct | dbskill | 47 | | |  |
| 82 | dbs-content | dbskill | 46 | | |  |
| 83 | dbs-benchmark | dbskill | 46 | | |  |
| 84 | dbs-chatroom-austrian | dbskill | 44 | | |  |
| 85 | dbs | dbskill | 40 | | | 保底 |

---

## 10. 简历与专业文档

简历生成、流程监控等专业文档场景

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | process-monitor | James-Skills | 60 | 流程智能监控设计专家。基于用户提供的流程信息和业务目标，引导完成监控指标定义、异常阈值设置、预警规则设计、根因分析... | 首选 |

---

## 11. 未分类

暂未归入明确聚类的技能

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | minimax-music-gen | MiniMax-skills | 67 | > | 首选 |
| 2 | hdd | ClaWiser | 65 | > | 备选 |
| 3 | buddy-sings | MiniMax-skills | 62 | > |  |
| 4 | ljg-think | ljg-skills | 62 | 追本之箭——纵向深钻思维工具。给一个观点、现象或问题，像箭一样一路向下钻到不可再分的本质。Use when use... |  |
| 5 | minimax-music-playlist | MiniMax-skills | 59 | > |  |
| 6 | project-skill-pairing | ClaWiser | 51 | > |  |
| 7 | sdd | ClaWiser | 50 | > | 保底 |

---

## 仓库来源

| 目录 | GitHub 仓库 | 简介 |
|------|-------------|------|
| (根目录) | wpsnote/wpsnote-skills | WPS笔记全套AI技能（30+技能） |
| baoyu-skills/ | JimLiu/baoyu-skills | 内容生成/翻译/社交媒体发布套件 |
| James-Skills/ | James19890801/Skills | 简历生成与流程监控 |
| wechat_article_skills/ | BND-1/wechat_article_skills | 微信公众号写作与发布工具链 |
| ClaWiser/ | MattWenJun/ClaWiser | Agent记忆与工作流增强 |
| wechat-skills/ | gainubi/wechat-skills | 微信公众号写作四件套 |
| awesome-claude-code-subagents/ | VoltAgent/awesome-claude-code-subagents | 127+专业Claude Code子代理 |
| MiniMax-skills/ | MiniMax-AI/skills | 全栈开发与多模态生成技能 |
| dbskill/ | dontbesilent2025/dbskill | 商业诊断工具箱 |
| markdown-proxy/ | joeseesun/markdown-proxy | URL转Markdown代理服务 |
| ljg-skills/ | lijigang/ljg-skills | 个人技能集（15技能） |
| anything-to-md/ | 1596941391qq/anything-to-md | 万能文件转Markdown |
| marketing-skills/ | atypica-ai/marketing-skills | 市场调研/用户访谈/产品创新（6技能） |

---

## 线上推荐 Skills（未下载，仅索引）

> 详见 [feishu-skills-recommend.md](feishu-skills-recommend.md)，来源：[飞书文档](https://my.feishu.cn/wiki/Mqsuw5G4ViNpCokHP5FcoPrWnYe)

| 分类 | 技能 | 说明 |
|------|------|------|
| 技能管理 | skill-vetter, find-skills, skill-creator, model-usage, free-ride | 安全审查、技能搜索、创建、Token追踪、免费模型 |
| 搜索与研究 | tavily-search, brave-search, multi-search-engine, summarize, web-search-exa | 多引擎搜索、内容摘要、结构化查询 |
| 文案与营销 | copywriting, social-content, product-marketing | 文案润色、社媒适配、营销策略 |
| 设计与体验 | ui-ux-pro-max, nano-banana-pro, frontend-design, diagram-generator | UI设计、AI绘图、前端组件、流程图 |
| 文档与办公 | pdf, docx, xlsx | PDF处理、Word/Excel生成 |
