# Skills Collection Index

> 本仓库收录了多个 Claude Code / AI Agent 技能合集，按功能聚类分类，每个聚类内按综合评分排名。
> 基于 `skills-registry.json` 自动生成 | 更新时间: 2026-04-19

**Fallback 机制**: 同一聚类内，优先使用排名靠前的 skill；如果首选 skill 失败（依赖缺失/API 报错），自动降级到下一个。

**总计**: 15 个聚类, 524 个技能

---

## 1. 内容创作与写作

文章撰写、文案生成、风格提取、小说写作等创作场景

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-comic | baoyu-skills | 84 | Knowledge comic creator supporting multiple art styles an... | 首选 |
| 2 | content-humanizer | claude-skills0418 | 81 | Makes AI-generated content sound genuinely human — not ju... | 备选 |
| 3 | content-production | claude-skills0418 | 81 | Full content production pipeline — takes a topic from bla... |  |
| 4 | copy-editing | claude-skills0418 | 81 | When the user wants to edit, review, or improve existing ... |  |
| 5 | copywriting | claude-skills0418 | 81 | When the user wants to write, rewrite, or improve marketi... |  |
| 6 | novel-writer | wpsnote-skills | 81 | AI 陪伴式长篇小说创作助手，结合 WPS 笔记实现有记忆、懂上下文、不穿帮的持续创作。触发词：帮我写小说、我想写... |  |
| 7 | content-strategy | claude-skills0418 | 78 | When the user wants to plan a content strategy, decide wh... |  |
| 8 | content-creator | claude-skills0418 | 77 | Deprecated redirect skill that routes legacy 'content cre... |  |
| 9 | novel-writer-cli | wpsnote-skills | 71 | AI 陪伴式长篇小说创作助手（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记，实现有... |  |
| 10 | wechat-tech-writer | wechat_article_skills | 71 | 自动搜索、抓取、改写技术内容，生成适合微信公众号的中文科普文章。涵盖AI大模型、GitHub开源工具、技术话题。当... |  |
| 11 | humanizer | agent-toolkit | 69 | | |  |
| 12 | ljg-writes | ljg-skills | 68 | 写作引擎。像手术刀剖开一个观点，一层层剥到底。1000-1500 字。 |  |
| 13 | wechat-product-manager-writer | wechat_article_skills | 66 | 从 AI 产品经理视角撰写微信公众号文章。涵盖 AI 产品拆解、场景解决方案、效率提升实战、产品方法论、行业观察。... |  |
| 14 | founder-sales | lenny-skills | 66 | Help founders close their first customers and build repea... |  |
| 15 | written-communication | lenny-skills | 66 | Help users communicate more effectively in writing. Use w... |  |
| 16 | writing-north-star-metrics | lenny-skills | 66 | Help users define their North Star metric. Use when someo... |  |
| 17 | writing-specs-designs | lenny-skills | 65 | Help users write effective specs and design documents. Us... |  |
| 18 | working-backwards | lenny-skills | 65 | Help users apply the working backwards methodology. Use w... |  |
| 19 | video-content-strategist | claude-skills0418 | 65 | Use when planning video content strategy, writing video s... |  |
| 20 | writing-job-descriptions | lenny-skills | 64 | Help users write effective job descriptions. Use when som... |  |
| 21 | writing-prds | lenny-skills | 64 | Help users write effective PRDs. Use when someone is docu... |  |
| 22 | building-with-llms | lenny-skills | 63 | Help users build effective AI applications. Use when some... |  |
| 23 | domain-name-brainstormer | agent-toolkit | 62 | Generates creative domain name ideas for your project and... |  |
| 24 | short-video-copywriter | wpsnote-skills | 61 | | |  |
| 25 | crafting-effective-readmes | agent-toolkit | 60 | Use when writing or improving README files. Not all READM... |  |
| 26 | content-creator | wpsnote-skills | 60 | | |  |
| 27 | naming-analyzer | agent-toolkit | 60 | Suggest better variable, function, and class names based ... |  |
| 28 | writing-clearly-and-concisely | agent-toolkit | 59 | Use when writing prose humans will read—documentation, co... |  |
| 29 | wechat-style-profiler | wechat-skills | 59 | 面向公众号作者的文风 DNA 梳理技能。用于从 3-10 篇参考文章中建立可复用的风格画像，输出 14 维分析、标... |  |
| 30 | wechat-topic-outline-planner | wechat-skills | 55 | 公众号选题与大纲策划技能。用于把一个粗点子、资料包、语音底稿或采访纪要，转成 2-3 个高价值选题角度、1 个推荐... |  |
| 31 | wechat-title-generator | wechat-skills | 53 | 公众号标题生成与评估技能。用于基于已确认的选题、大纲和目标读者，生成 8 个标题候选，筛掉低质标题，并推荐 1 个... |  |
| 32 | contract-and-proposal-writer | claude-skills0418 | 53 | Contract & Proposal Writer |  |
| 33 | wechat-draft-writer | wechat-skills | 52 | 公众号初稿写作技能。用于在选题和大纲已确认后，基于参考资料、语音底稿和文风 DNA 生成一版高保真初稿。适用于正文... |  |
| 34 | status | claude-skills0418 | 50 | Memory health dashboard showing line counts, topic files,... | 保底 |

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
| 7 | design-system-starter | agent-toolkit | 81 | Create and evolve design systems with design tokens, comp... |  |
| 8 | culture-architect | claude-skills0418 | 80 | Build, measure, and evolve company culture as operational... |  |
| 9 | shader-dev | MiniMax-skills | 78 | Comprehensive GLSL shader techniques for creating stunnin... |  |
| 10 | baoyu-image-gen | baoyu-skills | 78 | AI image generation with OpenAI, Azure OpenAI, Google, Op... |  |
| 11 | baoyu-imagine | baoyu-skills | 78 | AI image generation with OpenAI, Azure OpenAI, Google, Op... |  |
| 12 | logo-design | marketing-skills | 78 | Design professional logos as SVG code with browser previe... |  |
| 13 | brand-guidelines | claude-skills0418 | 76 | When the user wants to apply, document, or enforce brand ... |  |
| 14 | ljg-card | ljg-skills | 73 | Content caster (铸). Transforms content into PNG visuals. ... |  |
| 15 | marp-slide | agent-toolkit | 71 | Create professional Marp presentation slides with 7 beaut... |  |
| 16 | mermaid-diagrams | agent-toolkit | 71 | Comprehensive guide for creating software diagrams using ... |  |
| 17 | sales-engineer | claude-skills0418 | 71 | Analyzes RFP/RFI responses for coverage gaps, builds comp... |  |
| 18 | tc-tracker | claude-skills0418 | 71 | Use when the user asks to track technical changes, create... |  |
| 19 | senior-computer-vision | claude-skills0418 | 71 | Computer vision engineering skill for object detection, i... |  |
| 20 | ui-design-system | claude-skills0418 | 71 | UI design system toolkit for Senior UI Designer including... |  |
| 21 | slide-making-skill | MiniMax-skills | 68 | Implement single-slide PowerPoint pages with PptxGenJS. U... |  |
| 22 | draw-io | agent-toolkit | 68 | draw.io diagram creation, editing, and review. Use for .d... |  |
| 23 | mmx-cli | MiniMax-skills | 66 | Use mmx to generate text, images, video, speech, and musi... |  |
| 24 | meme-factory | agent-toolkit | 66 | Generate memes using the memegen.link API. Use when users... |  |
| 25 | baoyu-diagram | baoyu-skills | 66 | Create professional, dark-themed SVG diagrams of any type... |  |
| 26 | giving-presentations | lenny-skills | 66 | Help users create and deliver compelling presentations. U... |  |
| 27 | xiaohongshu-note-creator | wpsnote-skills | 65 | | |  |
| 28 | excalidraw | agent-toolkit | 65 | Use when working with *.excalidraw or *.excalidraw.json f... |  |
| 29 | defining-product-vision | lenny-skills | 65 | Help users create compelling product visions. Use when so... |  |
| 30 | managing-imposter-syndrome | lenny-skills | 65 | Help users work through feelings of inadequacy and self-d... |  |
| 31 | organizational-design | lenny-skills | 65 | Help users design effective organizational structures. Us... |  |
| 32 | product-discovery | claude-skills0418 | 63 | Use when validating product opportunities, mapping assump... |  |
| 33 | baoyu-danger-gemini-web | baoyu-skills | 60 | Generates images and text via reverse-engineered Gemini W... | 实验性 |
| 34 | image-gen | wpsnote-skills | 56 | | |  |
| 35 | gif-sticker-maker | MiniMax-skills | 54 | | |  |
| 36 | vision-analysis | MiniMax-skills | 49 | > |  |
| 37 | run | claude-skills0418 | 48 | Run a single experiment iteration. Edit the target file, ... |  |
| 38 | coverage | claude-skills0418 | 41 | >- | 保底 |

---

## 3. 社交媒体与营销投放

微信/微博/X/小红书发布、付费广告、SEO、邮件营销、着陆页、转化优化

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | marketing-demand-acquisition | claude-skills0418 | 81 | Creates demand generation campaigns, optimizes paid ad sp... | 首选 |
| 2 | ad-creative | claude-skills0418 | 81 | When the user needs to generate, iterate, or scale ad cre... | 备选 |
| 3 | campaign-analytics | claude-skills0418 | 81 | Analyzes campaign performance with multi-touch attributio... |  |
| 4 | churn-prevention | claude-skills0418 | 81 | Reduce voluntary and involuntary churn through cancel flo... |  |
| 5 | cold-email | claude-skills0418 | 81 | When the user wants to write, improve, or build a sequenc... |  |
| 6 | form-cro | claude-skills0418 | 81 | When the user wants to optimize any form that is NOT sign... |  |
| 7 | free-tool-strategy | claude-skills0418 | 81 | When the user wants to build a free tool for marketing — ... |  |
| 8 | paid-ads | claude-skills0418 | 81 | When the user wants help with paid advertising campaigns ... |  |
| 9 | popup-cro | claude-skills0418 | 81 | When the user wants to create or optimize popups, modals,... |  |
| 10 | referral-program | claude-skills0418 | 81 | When the user wants to design, launch, or optimize a refe... |  |
| 11 | schema-markup | claude-skills0418 | 81 | When the user wants to implement, audit, or validate stru... |  |
| 12 | signup-flow-cro | claude-skills0418 | 81 | When the user wants to optimize signup, registration, acc... |  |
| 13 | site-architecture | claude-skills0418 | 81 | When the user wants to audit, redesign, or plan their web... |  |
| 14 | social-content | claude-skills0418 | 81 | When the user wants help creating, scheduling, or optimiz... |  |
| 15 | x-twitter-growth | claude-skills0418 | 81 | X/Twitter growth engine for building audience, crafting v... |  |
| 16 | baoyu-markdown-to-html | baoyu-skills | 80 | Converts Markdown to styled HTML with WeChat-compatible t... |  |
| 17 | seo-audit | claude-skills0418 | 79 | When the user wants to audit, review, or diagnose SEO iss... |  |
| 18 | baoyu-post-to-wechat | baoyu-skills | 78 | Posts content to WeChat Official Account (微信公众号) via API ... |  |
| 19 | baoyu-post-to-x | baoyu-skills | 78 | Posts content and articles to X (Twitter). Supports regul... |  |
| 20 | email-sequence | claude-skills0418 | 78 | When the user wants to create or optimize an email sequen... |  |
| 21 | programmatic-seo | claude-skills0418 | 78 | When the user wants to create SEO-driven pages at scale u... |  |
| 22 | paywall-upgrade-cro | claude-skills0418 | 77 | When the user wants to create or optimize in-app paywalls... |  |
| 23 | ai-seo | claude-skills0418 | 76 | Optimize content to get cited by AI search engines — Chat... |  |
| 24 | launch-strategy | claude-skills0418 | 75 | When the user wants to plan a product launch, feature ann... |  |
| 25 | page-cro | claude-skills0418 | 75 | When the user wants to optimize, improve, or increase con... |  |
| 26 | social-media-manager | claude-skills0418 | 74 | When the user wants to develop social media strategy, pla... |  |
| 27 | marketing-ops | claude-skills0418 | 74 | Central router for the marketing skill ecosystem. Use whe... |  |
| 28 | minimax-xlsx | MiniMax-skills | 73 | Open, create, read, analyze, edit, or validate Excel/spre... |  |
| 29 | marketing-skills | claude-skills0418 | 72 | 42 marketing agent skills and plugins for Claude Code, Co... |  |
| 30 | behuman | claude-skills0418 | 71 | Use when the user wants more human-like AI responses — le... |  |
| 31 | app-store-optimization | claude-skills0418 | 71 | App Store Optimization (ASO) toolkit for researching keyw... |  |
| 32 | social-media-analyzer | claude-skills0418 | 71 | Social media campaign analysis and performance tracking. ... |  |
| 33 | landing-page-generator | claude-skills0418 | 71 | Generates high-converting landing pages as complete Next.... |  |
| 34 | baoyu-post-to-weibo | baoyu-skills | 70 | Posts content to Weibo (微博). Supports regular posts with ... |  |
| 35 | wechat-publisher | wpsnote-skills | 69 | | |  |
| 36 | wechat-article-formatter | wechat_article_skills | 68 | 将Markdown文章转换为美化的HTML格式，适配微信公众号发布。应用专业CSS样式、代码高亮、优化排版。当用户... |  |
| 37 | thesis-word-formatter | wechat-skills | 64 | 大学生毕业论文 Word 排版技能。用于先收集学校 Word 模板、学院规范、任务书或示例论文，再对本科或硕士毕业... |  |
| 38 | demo-video | claude-skills0418 | 62 | Use when the user asks to create a demo video, product wa... |  |
| 39 | email-template-builder | claude-skills0418 | 54 | Email Template Builder |  |
| 40 | wechat-draft-publisher | wechat_article_skills | 53 | 自动将 HTML 文章发布到微信公众号草稿箱，支持封面图上传、标题、作者和元数据管理。当用户说"推送到微信"、"发... | 保底 |

---

## 4. 翻译与格式转换

翻译、白话改写、Markdown格式化、图片压缩、文件格式转换

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | baoyu-format-markdown | baoyu-skills | 84 | Formats plain text or markdown files with frontmatter, ti... | 首选 |
| 2 | baoyu-translate | baoyu-skills | 84 | Translates articles and documents between languages with ... | 备选 |
| 3 | ljg-plain | ljg-skills | 79 | Cognitive atom: Plain (白). Rewrites any content so a smar... |  |
| 4 | information-security-manager-iso27001 | claude-skills0418 | 71 | ISO 27001 ISMS implementation and cybersecurity governanc... |  |
| 5 | baoyu-compress-image | baoyu-skills | 70 | Compresses images to WebP (default) or PNG with automatic... |  |
| 6 | behavioral-product-design | lenny-skills | 65 | Help users apply behavioral science to product design. Us... |  |
| 7 | organizational-transformation | lenny-skills | 65 | Help users transform organizations toward modern product ... |  |
| 8 | enterprise-sales | lenny-skills | 64 | Help users navigate enterprise sales. Use when someone is... |  |
| 9 | web-to-markdown | agent-toolkit | 61 | Use ONLY when the user explicitly says: 'use the skill we... |  |
| 10 | qiaomu-markdown-proxy | markdown-proxy | 52 | | |  |
| 11 | minimax-pdf | MiniMax-skills | 45 | > |  |
| 12 | anything-to-md | anything-to-md | 45 | | |  |
| 13 | html-to-pdf | marketing-skills | 36 | > | 保底 |

---

## 5. 信息采集与知识提取

网页抓取、论文阅读、新闻解读、内容摘要、视频字幕、媒体下载

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | ljg-paper | ljg-skills | 92 | Paper reader for non-academics. Takes a paper and extract... | 首选 |
| 2 | content-digest | wpsnote-skills | 87 | 将任意内容提炼为结构化知识笔记，自动保存到 WPS 笔记。只要用户给出任何内容（链接、图片、本地文件、粘贴文字）并... | 备选 |
| 3 | live-transcript-summary | wpsnote-skills | 84 | 边听边总结：实时监听当前 WPS 笔记中的音频转写，每 60 秒自动循环一次，识别场景后按对应模板整理内容，并写回... |  |
| 4 | baoyu-url-to-markdown | baoyu-skills | 84 | Fetch any URL and convert to markdown using baoyu-fetch C... |  |
| 5 | autoresearch-agent | claude-skills0418 | 84 | Autonomous experiment loop that optimizes any file by a m... |  |
| 6 | ljg-paper-river | ljg-skills | 83 | 论文倒读法：给一篇论文，递归找出它批判和改进的前序论文（最多5层），再找它之后的最新进展，从源头正向讲述问题演化史... |  |
| 7 | ljg-read | ljg-skills | 82 | Reading companion agent. Accompanies user through any tex... |  |
| 8 | research-summarizer | claude-skills0418 | 81 | Structured research summarization agent skill for non-dev... |  |
| 9 | ljg-travel | ljg-skills | 78 | Deep travel research workflow for museums and ancient arc... |  |
| 10 | ljg-paper-flow | ljg-skills | 72 | Paper workflow: read papers + cast cards in one go. Takes... |  |
| 11 | literature-reader | wpsnote-skills | 72 | 阅读、分析并总结学术文献（PDF论文），生成结构化的文献概要笔记。核心能力：论文元信息提取、研究问题识别、方法论梳... |  |
| 12 | ux-researcher-designer | claude-skills0418 | 71 | UX research and design toolkit for Senior UX Designer/Res... |  |
| 13 | doc-importer | wpsnote-skills | 70 | > |  |
| 14 | baoyu-danger-x-to-markdown | baoyu-skills | 68 | Converts X (Twitter) tweets and articles to markdown with... | 实验性 |
| 15 | meeting-analyzer | claude-skills0418 | 67 | Analyzes meeting transcripts and recordings to surface be... |  |
| 16 | analyzing-user-feedback | lenny-skills | 66 | Help users synthesize and act on customer feedback. Use w... |  |
| 17 | stakeholder-alignment | lenny-skills | 66 | Help users align stakeholders and get buy-in. Use when so... |  |
| 18 | running-effective-meetings | lenny-skills | 65 | Help users run more effective meetings. Use when someone ... |  |
| 19 | paper-researcher | wpsnote-skills | 62 | 学术论文全流程助手：搜索论文、下载 PDF、存入 WPS 笔记、精读分析。当用户说"搜论文"、"找论文"、"下载论... |  |
| 20 | perplexity | agent-toolkit | 61 | Web search and research using Perplexity AI. Use when use... |  |
| 21 | baoyu-youtube-transcript | baoyu-skills | 59 | Downloads YouTube video transcripts/subtitles and cover i... |  |
| 22 | web-importer | wpsnote-skills | 53 | > |  |
| 23 | setup | claude-skills0418 | 52 | Set up a new autoresearch experiment interactively. Colle... |  |
| 24 | news-to-note | wpsnote-skills | 51 | > | 保底 |

---

## 6. 笔记管理与知识整理

笔记美化、标签整理、知识关联、灵感发现、记忆系统、内部 wiki

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | llm-wiki | claude-skills0418 | 80 | Use when building or maintaining a persistent personal kn... | 首选 |
| 2 | note-calendar | wpsnote-skills | 79 | 在 macOS 上打通 WPS 笔记与系统日历。支持查询日程、创建/移动/删除日历事件，以及笔记与日历的双向联动：... | 备选 |
| 3 | wps-note | wpsnote-skills | 79 | 通过 MCP 工具读取、编辑和管理 WPS 笔记，基于 block 文档模型，所有内容以 |  |
| 4 | context-engine | claude-skills0418 | 78 | Loads and manages company context for all C-suite advisor... |  |
| 5 | wpsnote-beautifier | wpsnote-skills | 77 | 智能美化 WPS 笔记文档，采用克制统一的配色风格（全文仅1种主色调，不混用多色系）。核心能力：优化标题层级结构、... |  |
| 6 | tag-organize-cli | wpsnote-skills | 77 | 笔记标签整理的核心原则与完整工作流程（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记... |  |
| 7 | note-copilot | wpsnote-skills | 72 | 笔记协作助手：帮用户打磨当前 WPS 笔记，识别并处理笔记中的 *** 和 /// 援助标记，同时在发现明显逻辑错... |  |
| 8 | decision-logger | claude-skills0418 | 72 | Two-layer memory architecture for board meeting decisions... |  |
| 9 | ie-engine | wpsnote-skills | 71 | 灵感引擎的统一入口，串联记忆检索、想法连接和洞见生成的完整流水线。当用户提到"灵感引擎"、"激发灵感"、"conn... |  |
| 10 | clawiser | ClaWiser | 70 | Agent 记忆与工作流增强套件。包含 8 个模块：记忆系统（memory-deposit、retrieval-e... |  |
| 11 | tag-organize | wpsnote-skills | 68 | 笔记标签整理的核心原则与完整工作流程。当用户提到"整理笔记标签"、"清理标签"、"标签太乱"、"标签太多"、"帮我... |  |
| 12 | wps-deep-search | wpsnote-skills | 65 | | |  |
| 13 | noise-reduction | ClaWiser | 63 | > |  |
| 14 | ljg-think | ljg-skills | 62 | 追本之箭——纵向深钻思维工具。给一个观点、现象或问题，像箭一样一路向下钻到不可再分的本质。Use when use... |  |
| 15 | code-tour | claude-skills0418 | 62 | Use when the user asks to create a CodeTour .tour file — ... |  |
| 16 | ie-generate-insight | wpsnote-skills | 59 | 将推理分析结果转化为可阅读的洞见文本，生成下一步探索建议，展示想法的演化路径。当用户提到"生成洞见"、"给我灵感"... |  |
| 17 | ie-connect-dots | wpsnote-skills | 58 | 对笔记和想法进行语义聚类、发现想法之间的隐含连接、识别长期重复出现的主题模式。当用户提到"连接想法"、"发现关联"... |  |
| 18 | context-engineering | agent-skills | 58 | Optimizes agent context setup. Use when starting a new se... |  |
| 19 | review-notes | wpsnote-skills | 57 | 作为 coding-assistant 的子 skill，生成或更新 WPS 技术文档。笔记必须完整且包含 7 个... |  |
| 20 | memory-deposit | ClaWiser | 55 | > |  |
| 21 | ie-retrieve-memory | wpsnote-skills | 55 | 从用户的 WPS 笔记中检索历史知识和过去的想法。当用户提到"回忆过去的笔记"、"之前写过什么"、"历史想法"、"... |  |
| 22 | remember | claude-skills0418 | 54 | Explicitly save important knowledge to auto-memory with t... |  |
| 23 | promote | claude-skills0418 | 53 | Graduate a proven pattern from auto-memory (MEMORY.md) to... |  |
| 24 | review | claude-skills0418 | 52 | Analyze auto-memory for promotion candidates, stale entri... |  |
| 25 | class-note-builder | wpsnote-skills | 51 | 当用户希望把课堂逐字稿、OCR 笔记、截图资料或零散学习内容整理成结构化的 WPS 学习笔记时使用此 Skill。... |  |
| 26 | save-game | ClaWiser | 50 | > |  |
| 27 | load-game | ClaWiser | 50 | > |  |
| 28 | notes-to-lesson-plan | wpsnote-skills | 48 | 当用户希望把 WPS 学习笔记整理成一份可讲给别人听的讲解结构、迷你教案或 teach-back 提纲时使用此 S... |  |
| 29 | insight-recaller | wpsnote-skills | 47 | 当用户在 WPS 里写新内容、做专题复习、准备讲稿或整理研究思路时，希望把过去真正有用的旧笔记重新召回到眼前，就使... |  |
| 30 | study-note-linker | wpsnote-skills | 47 | 当用户希望把当前 WPS 学习笔记和已有旧笔记连起来，而不是让新笔记继续孤立存在时使用此 Skill。适合复习串讲... |  |
| 31 | notes-to-flashcards | wpsnote-skills | 47 | 当用户希望把 WPS 笔记转成可主动回忆的复习卡片时使用此 Skill。适合课程笔记复习、概念记忆、考前冲刺、误解... | 保底 |

---

## 7. 学习与教育

概念解剖、单词精通、闪卡、知识漏洞诊断等学习辅助

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | ljg-word-flow | ljg-skills | 72 | Word flow: deep-dive word analysis + infograph card in on... | 首选 |
| 2 | jira | agent-toolkit | 71 | Use when the user mentions Jira issues (e.g., "PROJ-123")... | 备选 |
| 3 | ship-learn-next | agent-toolkit | 70 | Transform learning content (like YouTube transcripts, art... |  |
| 4 | ljg-word | ljg-skills | 68 | Deep-dive English word mastery tool. Deconstructs a singl... |  |
| 5 | lesson-learned | agent-toolkit | 67 | Analyze recent code changes via git history and extract s... |  |
| 6 | ljg-learn | ljg-skills | 59 | Deep concept anatomist that deconstructs any concept thro... |  |
| 7 | misconception-finder | wpsnote-skills | 48 | 当用户希望检查一篇 WPS 学习笔记里是否存在理解错误、概念混淆、逻辑跳步或表述过虚时使用此 Skill。适合课后... |  |
| 8 | prerequisite-gap-finder | wpsnote-skills | 47 | 当用户觉得一个主题看不懂、学得卡住，或者想知道自己到底缺了哪些前置基础时使用此 Skill。适合课程复习、自学卡点... |  |
| 9 | lecture-focus-extractor | wpsnote-skills | 46 | 当用户手上已经有一篇较长的课堂笔记、逐字稿或学习记录，但只想提取最值得复习的重点时使用此 Skill。适合课程录音... | 保底 |

---

## 8. 开发与工程

前端/移动端/全栈开发、代码审查、测试、调试、Office自动化、子代理编排

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | agenthub | claude-skills0418 | 84 | Multi-agent collaboration plugin that spawns N parallel s... | 首选 |
| 2 | karpathy-coder | claude-skills0418 | 81 | Use when writing, reviewing, or committing code to enforc... | 备选 |
| 3 | android-native-dev | MiniMax-skills | 81 | Android native application development and UI design guid... |  |
| 4 | fullstack-dev | MiniMax-skills | 81 | | |  |
| 5 | pptx-generator | MiniMax-skills | 81 | Generate, edit, and read PowerPoint presentations. Create... |  |
| 6 | dependency-updater | agent-toolkit | 81 | Smart dependency management for any language. Auto-detect... |  |
| 7 | react-dev | agent-toolkit | 81 | This skill should be used when building React components ... |  |
| 8 | agent-protocol | claude-skills0418 | 81 | Inter-agent communication protocol for C-suite agent team... |  |
| 9 | docker-development | claude-skills0418 | 81 | Docker and container development agent skill and plugin f... |  |
| 10 | prompt-engineer-toolkit | claude-skills0418 | 78 | Analyzes and rewrites prompts for better AI output, creat... |  |
| 11 | frontend-dev | MiniMax-skills | 75 | | |  |
| 12 | ljg-skill-map | ljg-skills | 72 | Skill map viewer. Scans all installed skills and renders ... |  |
| 13 | adversarial-reviewer | claude-skills0418 | 72 | Adversarial code review that breaks the self-review monoc... |  |
| 14 | code-review-and-quality | agent-skills | 71 | Conducts multi-axis code review. Use before merging any c... |  |
| 15 | command-creator | agent-toolkit | 71 | This skill should be used when creating a Claude Code sla... |  |
| 16 | database-schema-designer | agent-toolkit | 71 | Design robust, scalable database schemas for SQL and NoSQ... |  |
| 17 | gepetto | agent-toolkit | 71 | Creates detailed, sectionized implementation plans throug... |  |
| 18 | mui | agent-toolkit | 71 | Material-UI v7 component library patterns including sx pr... |  |
| 19 | openapi-to-typescript | agent-toolkit | 71 | Converts OpenAPI 3.0 JSON/YAML to TypeScript interfaces a... |  |
| 20 | plugin-forge | agent-toolkit | 71 | Create and manage Claude Code plugins with proper structu... |  |
| 21 | skill-judge | agent-toolkit | 71 | Evaluate Agent Skill design quality against official spec... |  |
| 22 | release-manager | claude-skills0418 | 71 | Use when the user asks to plan releases, manage changelog... |  |
| 23 | spec-driven-workflow | claude-skills0418 | 71 | Use when the user asks to write specs before code, define... |  |
| 24 | senior-architect | claude-skills0418 | 71 | This skill should be used when the user asks to "design s... |  |
| 25 | senior-backend | claude-skills0418 | 71 | Designs and implements backend systems including REST API... |  |
| 26 | senior-data-engineer | claude-skills0418 | 71 | Data engineering skill for building scalable data pipelin... |  |
| 27 | senior-data-scientist | claude-skills0418 | 71 | World-class senior data scientist skill specialising in s... |  |
| 28 | senior-frontend | claude-skills0418 | 71 | Frontend development skill for React, Next.js, TypeScript... |  |
| 29 | senior-fullstack | claude-skills0418 | 71 | Fullstack development toolkit with project scaffolding fo... |  |
| 30 | senior-ml-engineer | claude-skills0418 | 71 | ML engineering skill for productionizing models, building... |  |
| 31 | snowflake-development | claude-skills0418 | 71 | Use when writing Snowflake SQL, building data pipelines w... |  |
| 32 | saas-scaffolder | claude-skills0418 | 71 | Generates complete, production-ready SaaS project boilerp... |  |
| 33 | capa-officer | claude-skills0418 | 71 | CAPA system management for medical device QMS. Covers roo... |  |
| 34 | skill-creator | wpsnote-skills | 71 | Create new skills, modify and improve existing skills, an... |  |
| 35 | agent-designer | claude-skills0418 | 70 | Use when the user asks to design multi-agent systems, cre... |  |
| 36 | tech-stack-evaluator | claude-skills0418 | 70 | Technology stack evaluation and comparison with TCO analy... |  |
| 37 | code-simplification | agent-skills | 70 | Simplifies code for clarity. Use when refactoring code fo... |  |
| 38 | database-designer | claude-skills0418 | 70 | Use when the user asks to design database schemas, plan d... |  |
| 39 | frontend-ui-engineering | agent-skills | 70 | Builds production-quality UIs. Use when building or modif... |  |
| 40 | focused-fix | claude-skills0418 | 70 | Use when the user asks to fix, debug, or make a specific ... |  |
| 41 | shipping-and-launch | agent-skills | 69 | Prepares production launches. Use when preparing to deplo... |  |
| 42 | debugging-and-error-recovery | agent-skills | 69 | Guides systematic root-cause debugging. Use when tests fa... |  |
| 43 | api-and-interface-design | agent-skills | 69 | Guides stable API and interface design. Use when designin... |  |
| 44 | documentation-and-adrs | agent-skills | 68 | Records decisions and documentation. Use when making arch... |  |
| 45 | migration-architect | claude-skills0418 | 67 | Migration Architect |  |
| 46 | code-to-prd | claude-skills0418 | 67 | | |  |
| 47 | database-schema-designer | claude-skills0418 | 67 | Use when the user asks to create ERD diagrams, normalize ... |  |
| 48 | tech-debt-tracker | claude-skills0418 | 66 | Scan codebases for technical debt, score severity, track ... |  |
| 49 | incremental-implementation | agent-skills | 66 | Delivers changes incrementally. Use when implementing any... |  |
| 50 | agent-md-refactor | agent-toolkit | 66 | Refactor bloated AGENTS.md, CLAUDE.md, or similar agent i... |  |
| 51 | ci-cd-and-automation | agent-skills | 66 | Automates CI/CD pipeline setup. Use when setting up or mo... |  |
| 52 | performance-optimization | agent-skills | 66 | Optimizes application performance. Use when performance r... |  |
| 53 | test-driven-development | agent-skills | 66 | Drives development with tests. Use when implementing any ... |  |
| 54 | c4-architecture | agent-toolkit | 66 | Generate architecture documentation using C4 model Mermai... |  |
| 55 | qa-test-planner | agent-toolkit | 66 | Generate comprehensive test plans, manual test cases, reg... |  |
| 56 | browser-automation | claude-skills0418 | 66 | Use when the user asks to automate browser tasks, scrape ... |  |
| 57 | rag-architect | claude-skills0418 | 66 | Use when the user asks to design RAG pipelines, optimize ... |  |
| 58 | sql-database-assistant | claude-skills0418 | 66 | Use when the user asks to write SQL queries, optimize dat... |  |
| 59 | a11y-audit | claude-skills0418 | 66 | Accessibility audit skill for scanning, fixing, and verif... |  |
| 60 | security-pen-testing | claude-skills0418 | 66 | Use when the user asks to perform security audits, penetr... |  |
| 61 | senior-prompt-engineer | claude-skills0418 | 66 | This skill should be used when the user asks to "optimize... |  |
| 62 | senior-qa | claude-skills0418 | 66 | Generates unit tests, integration tests, and E2E tests fo... |  |
| 63 | tdd-guide | claude-skills0418 | 66 | Test-driven development skill for writing unit tests, gen... |  |
| 64 | spec-to-repo | claude-skills0418 | 66 | Use when the user says 'build me an app', 'create a proje... |  |
| 65 | ai-product-strategy | lenny-skills | 66 | Help users define AI product strategy. Use when someone i... |  |
| 66 | session-handoff | agent-toolkit | 66 | Creates comprehensive handoff documents for seamless AI a... |  |
| 67 | evaluating-candidates | lenny-skills | 66 | Help users make better hiring decisions. Use when someone... |  |
| 68 | evaluating-trade-offs | lenny-skills | 66 | Help users make better decisions between competing option... |  |
| 69 | managing-tech-debt | lenny-skills | 66 | Help users manage technical debt strategically. Use when ... |  |
| 70 | shipping-products | lenny-skills | 66 | Help users ship products faster and with higher quality. ... |  |
| 71 | prompt-governance | claude-skills0418 | 65 | Use when managing prompts in production at scale: version... |  |
| 72 | career-transitions | lenny-skills | 65 | Help users navigate career changes and pivots. Use when s... |  |
| 73 | usability-testing | lenny-skills | 65 | Help users conduct effective usability testing. Use when ... |  |
| 74 | code-reviewer | claude-skills0418 | 65 | Code review automation for TypeScript, JavaScript, Python... |  |
| 75 | conducting-interviews | lenny-skills | 65 | Help users conduct effective hiring interviews. Use when ... |  |
| 76 | engineering-culture | lenny-skills | 65 | Help users build strong engineering culture. Use when som... |  |
| 77 | product-taste-intuition | lenny-skills | 65 | Help users develop product taste and intuition. Use when ... |  |
| 78 | running-design-reviews | lenny-skills | 65 | Help users run effective design reviews and critiques. Us... |  |
| 79 | vibe-coding | lenny-skills | 65 | Help users build software using AI coding tools. Use when... |  |
| 80 | interview-system-designer | claude-skills0418 | 65 | This skill should be used when the user asks to "design i... |  |
| 81 | deprecation-and-migration | agent-skills | 65 | Manages deprecation and migration. Use when removing old ... |  |
| 82 | startup-ideation | lenny-skills | 65 | Help users generate and evaluate startup ideas. Use when ... |  |
| 83 | commit-work | agent-toolkit | 64 | Create high-quality git commits: review/stage intended ch... |  |
| 84 | engineering-skills | claude-skills0418 | 64 | 23 engineering agent skills and plugins for Claude Code, ... |  |
| 85 | spec-driven-development | agent-skills | 64 | Creates specs before coding. Use when starting a new proj... |  |
| 86 | ppt-editing-skill | MiniMax-skills | 64 | Edit existing PowerPoint files or templates with XML-safe... |  |
| 87 | browser-testing-with-devtools | agent-skills | 64 | Tests in real browsers. Use when building or debugging an... |  |
| 88 | source-driven-development | agent-skills | 64 | Grounds every implementation decision in official documen... |  |
| 89 | frontend-to-backend-requirements | agent-toolkit | 64 | Document frontend data needs for backend developers. Use ... |  |
| 90 | self-eval | claude-skills0418 | 63 | Honestly evaluate AI work quality using a two-axis scorin... |  |
| 91 | reducing-entropy | agent-toolkit | 63 | Manual-only skill for minimizing total codebase size. Onl... |  |
| 92 | api-test-suite-builder | claude-skills0418 | 63 | Use when the user asks to generate API tests, create inte... |  |
| 93 | evaluating-new-technology | lenny-skills | 63 | Help users evaluate emerging technologies. Use when someo... |  |
| 94 | git-workflow-and-versioning | agent-skills | 62 | Structures git workflow practices. Use when making any co... |  |
| 95 | skill-tester | claude-skills0418 | 62 | Skill Tester |  |
| 96 | color-font-skill | MiniMax-skills | 62 | Choose presentation-ready color palettes and font pairing... |  |
| 97 | ppt-orchestra-skill | MiniMax-skills | 62 | Plan and orchestrate multi-slide PowerPoint creation from... |  |
| 98 | pr-review-expert | claude-skills0418 | 62 | Use when the user asks to review pull requests, analyze c... |  |
| 99 | minimax-docx | MiniMax-skills | 61 | > |  |
| 100 | backend-to-frontend-handoff-docs | agent-toolkit | 61 | Create API handoff documentation for frontend developers.... |  |
| 101 | dependency-auditor | claude-skills0418 | 60 | Dependency Auditor |  |
| 102 | react-native-dev | MiniMax-skills | 60 | | |  |
| 103 | datadog-cli | agent-toolkit | 60 | Datadog CLI for searching logs, querying metrics, tracing... |  |
| 104 | api-design-reviewer | claude-skills0418 | 59 | API Design Reviewer |  |
| 105 | ai-evals | lenny-skills | 59 | Help users create and run AI evaluations. Use when someon... |  |
| 106 | flutter-dev | MiniMax-skills | 59 | | |  |
| 107 | coding-assistant | wpsnote-skills | 59 | 多平台编码助手。遵循各平台官方文档做编码规范、单测与编译/lint；协助将核心技术梳理为完整 WPS 笔记技术文档... |  |
| 108 | llm-cost-optimizer | claude-skills0418 | 59 | Use when you need to reduce LLM API spend, control token ... |  |
| 109 | using-agent-skills | agent-skills | 58 | Discovers and invokes agent skills. Use when starting a s... |  |
| 110 | retrieval-enhance | ClaWiser | 58 | 检索系统守护。静默运行——agent 自主判断何时激活。三种场景：(1) 首次搭建时初始化 memorySearc... |  |
| 111 | self-improving-agent | claude-skills0418 | 58 | Curate Claude Code's auto-memory into durable project kno... |  |
| 112 | react-useeffect | agent-toolkit | 57 | React useEffect best practices from official docs. Use wh... |  |
| 113 | ios-application-dev | MiniMax-skills | 56 | | |  |
| 114 | extract | claude-skills0418 | 56 | Turn a proven pattern or debugging solution into a standa... |  |
| 115 | git-worktree-manager | claude-skills0418 | 54 | Git Worktree Manager |  |
| 116 | performance-profiler | claude-skills0418 | 53 | Performance Profiler |  |
| 117 | changelog-generator | claude-skills0418 | 52 | Changelog Generator |  |
| 118 | mcp-server-builder | claude-skills0418 | 52 | MCP Server Builder |  |
| 119 | playwright-pro | claude-skills0418 | 51 | Production-grade Playwright testing toolkit. Use when the... |  |
| 120 | run | claude-skills0418 | 51 | One-shot lifecycle command that chains init → baseline → ... |  |
| 121 | stress-test | claude-skills0418 | 50 | /em -stress-test — Business Assumption Stress Testing |  |
| 122 | monorepo-navigator | claude-skills0418 | 49 | Monorepo Navigator |  |
| 123 | agent-workflow-designer | claude-skills0418 | 49 | Agent Workflow Designer |  |
| 124 | init | claude-skills0418 | 49 | Create a new AgentHub collaboration session with task, ag... |  |
| 125 | merge | claude-skills0418 | 48 | Merge the winning agent's branch into base, archive loser... |  |
| 126 | runbook-generator | claude-skills0418 | 48 | Runbook Generator |  |
| 127 | spawn | claude-skills0418 | 48 | Launch N parallel subagents in isolated git worktrees to ... |  |
| 128 | eval | claude-skills0418 | 47 | Evaluate and rank agent results by metric or LLM judge fo... |  |
| 129 | status | claude-skills0418 | 46 | Show DAG state, agent progress, and branch status for an ... |  |
| 130 | design-style-skill | MiniMax-skills | 46 | > |  |
| 131 | browserstack | claude-skills0418 | 39 | >- |  |
| 132 | migrate | claude-skills0418 | 38 | >- |  |
| 133 | fix | claude-skills0418 | 36 | >- |  |
| 134 | testrail | claude-skills0418 | 32 | >- | 保底 |

---

## 9. DevOps 与云基础设施

DevOps、SRE、Docker/K8s、Terraform、AWS/Azure/GCP、CI/CD、监控与密钥

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | helm-chart-builder | claude-skills0418 | 81 | Helm chart development agent skill and plugin for Claude ... | 首选 |
| 2 | analytics-tracking | claude-skills0418 | 81 | Set up, audit, and debug analytics tracking implementatio... | 备选 |
| 3 | terraform-patterns | claude-skills0418 | 76 | Terraform infrastructure-as-code agent skill and plugin f... |  |
| 4 | aws-solution-architect | claude-skills0418 | 71 | Design AWS architectures for startups using serverless pa... |  |
| 5 | azure-cloud-architect | claude-skills0418 | 71 | Design Azure architectures for startups and enterprises. ... |  |
| 6 | gcp-cloud-architect | claude-skills0418 | 71 | Design GCP architectures for startups and enterprises. Us... |  |
| 7 | google-workspace-cli | claude-skills0418 | 71 | Google Workspace administration via the gws CLI. Install,... |  |
| 8 | incident-response | claude-skills0418 | 71 | Use when a security incident has been detected or declare... |  |
| 9 | ms365-tenant-manager | claude-skills0418 | 71 | Microsoft 365 tenant administration for Global Administra... |  |
| 10 | senior-devops | claude-skills0418 | 71 | Comprehensive DevOps skill for CI/CD, infrastructure auto... |  |
| 11 | atlassian-admin | claude-skills0418 | 71 | Atlassian Administrator for managing and organizing Atlas... |  |
| 12 | atlassian-templates | claude-skills0418 | 71 | Atlassian Template and Files Creator/Modifier expert for ... |  |
| 13 | confluence-expert | claude-skills0418 | 71 | Atlassian Confluence expert for creating and managing spa... |  |
| 14 | jira-expert | claude-skills0418 | 71 | Atlassian Jira expert for creating and managing projects,... |  |
| 15 | engineering-advanced-skills | claude-skills0418 | 68 | 25 advanced engineering agent skills and plugins for Clau... |  |
| 16 | incident-commander | claude-skills0418 | 68 | Incident Commander Skill |  |
| 17 | secrets-vault-manager | claude-skills0418 | 66 | Use when the user asks to set up secret management infras... |  |
| 18 | stripe-integration-expert | claude-skills0418 | 60 | Stripe Integration Expert |  |
| 19 | observability-designer | claude-skills0418 | 59 | Observability Designer (POWERFUL) |  |
| 20 | env-secrets-manager | claude-skills0418 | 52 | Env & Secrets Manager |  |
| 21 | ci-cd-pipeline-builder | claude-skills0418 | 52 | CI/CD Pipeline Builder |  |
| 22 | postmortem | claude-skills0418 | 50 | /em -postmortem — Honest Analysis of What Went Wrong | 保底 |

---

## 10. 安全与合规

安全架构、渗透测试、威胁建模、代码/依赖审计、合规（SOC2/GDPR/ISO27001/HIPAA）

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | cloud-security | claude-skills0418 | 71 | Use when assessing cloud infrastructure for security misc... | 首选 |
| 2 | red-team | claude-skills0418 | 71 | Use when planning or executing authorized red team engage... | 备选 |
| 3 | threat-detection | claude-skills0418 | 71 | Use when hunting for threats in an environment, analyzing... |  |
| 4 | gdpr-dsgvo-expert | claude-skills0418 | 71 | GDPR and German DSGVO compliance automation. Scans codeba... |  |
| 5 | isms-audit-expert | claude-skills0418 | 71 | Information Security Management System (ISMS) audit exper... |  |
| 6 | mdr-745-specialist | claude-skills0418 | 71 | EU MDR 2017/745 compliance specialist for medical device ... |  |
| 7 | qms-audit-expert | claude-skills0418 | 71 | ISO 13485 internal audit expertise for medical device QMS... |  |
| 8 | quality-documentation-manager | claude-skills0418 | 71 | Document control system management for medical device QMS... |  |
| 9 | quality-manager-qmr | claude-skills0418 | 71 | Senior Quality Manager Responsible Person (QMR) for Healt... |  |
| 10 | quality-manager-qms-iso13485 | claude-skills0418 | 71 | ISO 13485 Quality Management System implementation and ma... |  |
| 11 | regulatory-affairs-head | claude-skills0418 | 71 | Senior Regulatory Affairs Manager for HealthTech and MedT... |  |
| 12 | risk-management-specialist | claude-skills0418 | 71 | Medical device risk management specialist implementing IS... |  |
| 13 | soc2-compliance | claude-skills0418 | 71 | Use when the user asks to prepare for SOC 2 audits, map T... |  |
| 14 | ra-qm-skills | claude-skills0418 | 68 | 12 regulatory & QM agent skills and plugins for Claude Co... |  |
| 15 | security-and-hardening | agent-skills | 66 | Hardens code against vulnerabilities. Use when handling u... |  |
| 16 | ai-security | claude-skills0418 | 66 | Use when assessing AI/ML systems for prompt injection, ja... |  |
| 17 | senior-secops | claude-skills0418 | 66 | Senior SecOps engineer skill for application security, vu... |  |
| 18 | senior-security | claude-skills0418 | 66 | Security engineering toolkit for threat modeling, vulnera... |  |
| 19 | skill-security-auditor | claude-skills0418 | 51 | > | 保底 |

---

## 11. 产品管理与敏捷开发

产品管理、敏捷/Scrum、Sprint 规划、OKR、路线图、用户研究、实验设计

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | scrum-master | claude-skills0418 | 84 | Advanced Scrum Master skill for data-driven agile team an... | 首选 |
| 2 | ab-test-setup | claude-skills0418 | 81 | When the user wants to plan, design, or implement an A/B ... | 备选 |
| 3 | saas-metrics-coach | claude-skills0418 | 76 | SaaS financial health advisor. Use when a user shares rev... |  |
| 4 | pricing-strategy | claude-skills0418 | 76 | Design, optimize, and communicate SaaS pricing — tier str... |  |
| 5 | apple-hig-expert | claude-skills0418 | 72 | Expert guidance on Apple Human Interface Guidelines (HIG)... |  |
| 6 | daily-meeting-update | agent-toolkit | 71 | Interactive daily standup/meeting update generator. Use w... |  |
| 7 | difficult-workplace-conversations | agent-toolkit | 71 | Structured approach to workplace conflicts, performance d... |  |
| 8 | feedback-mastery | agent-toolkit | 71 | Navigate difficult conversations and deliver constructive... |  |
| 9 | professional-communication | agent-toolkit | 71 | Guide technical communication for software developers. Co... |  |
| 10 | agile-product-owner | claude-skills0418 | 71 | Agile product ownership for backlog management and sprint... |  |
| 11 | product-manager-toolkit | claude-skills0418 | 71 | Comprehensive toolkit for product managers including RICE... |  |
| 12 | product-strategist | claude-skills0418 | 71 | Strategic product leadership toolkit for Head of Product ... |  |
| 13 | senior-pm | claude-skills0418 | 71 | Senior Project Manager for enterprise software, SaaS, and... |  |
| 14 | requirements-clarity | agent-toolkit | 70 | Clarify ambiguous requirements through focused dialogue b... |  |
| 15 | epic-design | claude-skills0418 | 70 | > |  |
| 16 | product-skills | claude-skills0418 | 68 | 10 product agent skills and plugins for Claude Code, Code... |  |
| 17 | pm-skills | claude-skills0418 | 68 | 6 project management agent skills and plugins for Claude ... |  |
| 18 | game-changing-features | agent-toolkit | 67 | Find 10x product opportunities and high-leverage improvem... |  |
| 19 | setting-okrs-goals | lenny-skills | 66 | Help users set effective OKRs and goals. Use when someone... |  |
| 20 | planning-and-task-breakdown | agent-skills | 65 | Breaks work into ordered tasks. Use when you have a spec ... |  |
| 21 | prioritizing-roadmap | lenny-skills | 65 | Help users prioritize product roadmaps and backlogs. Use ... |  |
| 22 | pricing-strategy | lenny-skills | 65 | Help users design and optimize pricing strategies. Use wh... |  |
| 23 | post-mortems-retrospectives | lenny-skills | 65 | Help users run effective post-mortems and retrospectives.... |  |
| 24 | product-analytics | claude-skills0418 | 65 | Use when defining product KPIs, building metric dashboard... |  |
| 25 | dogfooding | lenny-skills | 64 | Help users implement effective dogfooding practices. Use ... |  |
| 26 | personal-productivity | lenny-skills | 64 | Help users manage their time and tasks more effectively. ... |  |
| 27 | experiment-designer | claude-skills0418 | 64 | Use when planning product experiments, writing testable h... |  |
| 28 | technical-roadmaps | lenny-skills | 63 | Help users create technical roadmaps. Use when someone is... |  |
| 29 | roadmap-communicator | claude-skills0418 | 61 | Use when preparing roadmap narratives, release notes, cha... |  |
| 30 | idea-refine | agent-skills | 57 | Refines ideas iteratively. Refine ideas through structure... | 保底 |

---

## 12. 商业诊断与分析

商业模式诊断、市场调研、投资分析、产品创新、竞品情报、增长策略

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | market-sizing | marketing-skills | 84 | Produce a rigorous, sourced TAM/SAM/SOM market sizing for... | 首选 |
| 2 | competitive-intel | claude-skills0418 | 81 | Systematic competitor tracking that feeds CMO positioning... | 备选 |
| 3 | internal-narrative | claude-skills0418 | 81 | Build and maintain one coherent company story across all ... |  |
| 4 | scenario-war-room | claude-skills0418 | 81 | Cross-functional what-if modeling for cascading multi-var... |  |
| 5 | strategic-alignment | claude-skills0418 | 81 | Cascades strategy from boardroom to individual contributo... |  |
| 6 | competitor-alternatives | claude-skills0418 | 81 | When the user wants to create competitor comparison or al... |  |
| 7 | org-health-diagnostic | claude-skills0418 | 81 | Cross-functional organizational health check combining si... |  |
| 8 | marketing-psychology | claude-skills0418 | 78 | When the user wants to apply psychological principles, me... |  |
| 9 | intl-expansion | claude-skills0418 | 77 | International market expansion strategy. Market selection... |  |
| 10 | ma-playbook | claude-skills0418 | 76 | M&A strategy for acquiring companies or being acquired. D... |  |
| 11 | marketing-ideas | claude-skills0418 | 76 | When the user needs marketing ideas, inspiration, or stra... |  |
| 12 | marketing-context | claude-skills0418 | 73 | Create and maintain the marketing context document that a... |  |
| 13 | revenue-operations | claude-skills0418 | 71 | Analyzes sales pipeline health, revenue forecasting accur... |  |
| 14 | data-quality-auditor | claude-skills0418 | 71 | Audit datasets for completeness, consistency, accuracy, a... |  |
| 15 | statistical-analyst | claude-skills0418 | 71 | Run hypothesis tests, analyze A/B experiment results, cal... |  |
| 16 | marketing-strategy-pmm | claude-skills0418 | 71 | Product marketing skill for positioning, GTM strategy, co... |  |
| 17 | fda-consultant-specialist | claude-skills0418 | 71 | FDA regulatory consultant for medical device companies. P... |  |
| 18 | dbs-xhs-title | dbskill | 70 | | |  |
| 19 | competitive-teardown | claude-skills0418 | 70 | Analyzes competitor products and companies by synthesizin... |  |
| 20 | financial-analyst | claude-skills0418 | 69 | Performs financial ratio analysis, DCF valuation, budget ... |  |
| 21 | business-growth-skills | claude-skills0418 | 68 | 4 business growth agent skills and plugins for Claude Cod... |  |
| 22 | product-rnd | marketing-skills | 68 | End-to-end Product Innovation R&D workflow — inspiration ... |  |
| 23 | ljg-rank | ljg-skills | 67 | 给一个领域，找出背后真正撑着它的几根独立的力。十几个现象砍到不可再少的生成器——砍完能把现象一个个生回来，才算数。... |  |
| 24 | finance-skills | claude-skills0418 | 66 | Financial analyst agent skill and plugin for Claude Code,... |  |
| 25 | conducting-user-interviews | lenny-skills | 66 | Help users run better customer and user interviews. Use w... |  |
| 26 | atypica-user-interview | marketing-skills | 66 | Run AI-simulated user interviews and focus group discussi... |  |
| 27 | having-difficult-conversations | lenny-skills | 66 | Help users navigate tough feedback, performance conversat... |  |
| 28 | launch-marketing | lenny-skills | 66 | Help users plan and execute product launches. Use when so... |  |
| 29 | managing-up | lenny-skills | 66 | Help users work effectively with their manager and execut... |  |
| 30 | finding-mentors-sponsors | lenny-skills | 66 | Help users build relationships with mentors and sponsors ... |  |
| 31 | brand-storytelling | lenny-skills | 66 | Help users craft compelling brand narratives. Use when so... |  |
| 32 | building-a-promotion-case | lenny-skills | 66 | Help users get promoted at work. Use when someone is prep... |  |
| 33 | managing-timelines | lenny-skills | 66 | Help users set and hit realistic deadlines. Use when some... |  |
| 34 | measuring-product-market-fit | lenny-skills | 66 | Help users assess and achieve product-market fit. Use whe... |  |
| 35 | cross-functional-collaboration | lenny-skills | 65 | Help users work effectively across functions. Use when so... |  |
| 36 | partnership-bd | lenny-skills | 65 | Help users build strategic partnerships and business deve... |  |
| 37 | building-sales-team | lenny-skills | 65 | Help users build and scale their sales organization. Use ... |  |
| 38 | community-building | lenny-skills | 65 | Help users build and grow product communities. Use when s... |  |
| 39 | competitive-analysis | lenny-skills | 65 | Help users understand and respond to competition. Use whe... |  |
| 40 | designing-growth-loops | lenny-skills | 65 | Help users design and optimize growth loops. Use when som... |  |
| 41 | planning-under-uncertainty | lenny-skills | 65 | Help users plan products and strategy when outcomes are u... |  |
| 42 | problem-definition | lenny-skills | 65 | Help users define problems clearly before jumping to solu... |  |
| 43 | business-investment-advisor | claude-skills0418 | 65 | Business investment analysis and capital allocation advis... |  |
| 44 | building-team-culture | lenny-skills | 65 | Help users build and maintain strong team culture. Use wh... |  |
| 45 | running-decision-processes | lenny-skills | 65 | Help users run effective decision-making processes. Use w... |  |
| 46 | positioning-messaging | lenny-skills | 65 | Help users craft product positioning and messaging. Use w... |  |
| 47 | retention-engagement | lenny-skills | 65 | Help users improve retention and engagement metrics. Use ... |  |
| 48 | systems-thinking | lenny-skills | 65 | Help users think in systems and understand complex dynami... |  |
| 49 | platform-strategy | lenny-skills | 65 | Help users design and execute platform business strategie... |  |
| 50 | running-effective-1-1s | lenny-skills | 65 | Help users run effective one-on-one meetings. Use when so... |  |
| 51 | energy-management | lenny-skills | 65 | Help users manage their energy for sustained performance.... |  |
| 52 | team-rituals | lenny-skills | 65 | Help users design effective team rituals. Use when someon... |  |
| 53 | negotiating-offers | lenny-skills | 65 | Help users negotiate job offers and compensation. Use whe... |  |
| 54 | platform-infrastructure | lenny-skills | 65 | Help users build and scale internal platforms and technic... |  |
| 55 | product-led-sales | lenny-skills | 65 | Help users implement product-led sales motions. Use when ... |  |
| 56 | product-operations | lenny-skills | 65 | Help users build and scale product operations functions. ... |  |
| 57 | running-offsites | lenny-skills | 65 | Help users plan and run effective team offsites. Use when... |  |
| 58 | sales-compensation | lenny-skills | 65 | Help users design sales compensation plans. Use when some... |  |
| 59 | sales-qualification | lenny-skills | 65 | Help users qualify sales leads effectively. Use when some... |  |
| 60 | startup-pivoting | lenny-skills | 65 | Help users decide when and how to pivot their startup. Us... |  |
| 61 | marketplace-liquidity | lenny-skills | 65 | Help users build and manage marketplace liquidity. Use wh... |  |
| 62 | media-relations | lenny-skills | 65 | Help users build relationships with journalists and get p... |  |
| 63 | fundraising | lenny-skills | 64 | Help founders raise capital and build investor relationsh... |  |
| 64 | design-engineering | lenny-skills | 64 | Help users understand and build design engineering capabi... |  |
| 65 | content-marketing | lenny-skills | 64 | Help users build content marketing strategies. Use when s... |  |
| 66 | scoping-cutting | lenny-skills | 64 | Help users scope projects and cut features effectively. U... |  |
| 67 | design-systems | lenny-skills | 64 | Help users build and scale design systems. Use when someo... |  |
| 68 | coaching-pms | lenny-skills | 64 | Help users develop and coach product managers. Use when s... |  |
| 69 | delegating-work | lenny-skills | 63 | Help users delegate effectively. Use when someone is stru... |  |
| 70 | plan-as-consultant | marketing-skills | 62 | Plan a business research study the way a professional con... |  |
| 71 | designing-surveys | lenny-skills | 61 | Help users design effective surveys. Use when someone is ... |  |
| 72 | ljg-invest | ljg-skills | 61 | 投资分析, 生成一份深度投资分析报告。不做传统投资分析——核心判断是项目是否是一台「秩序创造机器」。Use whe... |  |
| 73 | dbs-diagnosis | dbskill | 60 | | |  |
| 74 | dbs-hook | dbskill | 50 | | |  |
| 75 | dbs-agent-migration | dbskill | 50 | | |  |
| 76 | ljg-roundtable | ljg-skills | 49 | >- |  |
| 77 | dbs-ai-check | dbskill | 49 | | |  |
| 78 | ljg-relationship | ljg-skills | 48 | >- |  |
| 79 | dbs-chatroom | dbskill | 48 | 定向聊天室：根据话题推荐或接受用户指定的专家，模拟多角色对话。触发方式：/dbs-chatroom、/定向聊天室、... |  |
| 80 | dbs-action | dbskill | 47 | | |  |
| 81 | dbs-slowisfast | dbskill | 47 | | |  |
| 82 | dbs-deconstruct | dbskill | 47 | | |  |
| 83 | dbs-content | dbskill | 46 | | |  |
| 84 | dbs-benchmark | dbskill | 46 | | |  |
| 85 | dbs-chatroom-austrian | dbskill | 44 | | |  |
| 86 | dbs | dbskill | 40 | | | 保底 |

---

## 13. 高管顾问与领导力

CEO/CTO/CFO/CMO/CIO/COO/CISO/CRO/CPO/CHRO 顾问、董事会、创始人辅导、组织健康

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | cto-advisor | claude-skills0418 | 84 | Technical leadership guidance for engineering teams, arch... | 首选 |
| 2 | ceo-advisor | claude-skills0418 | 82 | Executive leadership guidance for strategic decision-maki... | 备选 |
| 3 | change-management | claude-skills0418 | 81 | Framework for rolling out organizational changes without ... |  |
| 4 | company-os | claude-skills0418 | 81 | The meta-framework for how a company runs — the connectiv... |  |
| 5 | cpo-advisor | claude-skills0418 | 81 | Product leadership for scaling companies. Product vision,... |  |
| 6 | founder-coach | claude-skills0418 | 81 | Personal leadership development for founders and first-ti... |  |
| 7 | board-deck-builder | claude-skills0418 | 80 | Assembles comprehensive board and investor update decks b... |  |
| 8 | cro-advisor | claude-skills0418 | 80 | Revenue leadership for B2B SaaS companies. Revenue foreca... |  |
| 9 | chief-of-staff | claude-skills0418 | 80 | C-suite orchestration layer. Routes founder questions to ... |  |
| 10 | cmo-advisor | claude-skills0418 | 80 | Marketing leadership for scaling companies. Brand positio... |  |
| 11 | board-meeting | claude-skills0418 | 79 | Multi-agent board meeting protocol for strategic decision... |  |
| 12 | chro-advisor | claude-skills0418 | 79 | People leadership for scaling companies. Hiring strategy,... |  |
| 13 | executive-mentor | claude-skills0418 | 79 | Adversarial thinking partner for founders and executives.... |  |
| 14 | cfo-advisor | claude-skills0418 | 78 | Financial leadership for startups and scaling companies. ... |  |
| 15 | coo-advisor | claude-skills0418 | 78 | Operations leadership for scaling companies. Process desi... |  |
| 16 | ciso-advisor | claude-skills0418 | 78 | Security leadership for growth-stage companies. Risk quan... |  |
| 17 | cs-onboard | claude-skills0418 | 77 | Founder onboarding interview that captures company contex... |  |
| 18 | onboarding-cro | claude-skills0418 | 77 | When the user wants to optimize post-signup onboarding, u... |  |
| 19 | c-level-advisor | claude-skills0418 | 75 | 10 C-level advisory agent skills and plugins for Claude C... |  |
| 20 | onboarding-new-hires | lenny-skills | 66 | Help users onboard new team members effectively. Use when... |  |
| 21 | team-communications | claude-skills0418 | 65 | Write internal company communications — 3P updates (Progr... |  |
| 22 | user-onboarding | lenny-skills | 65 | Help users design effective product onboarding. Use when ... |  |
| 23 | hard-call | claude-skills0418 | 49 | /em -hard-call — Framework for Decisions With No Good Opt... |  |
| 24 | codebase-onboarding | claude-skills0418 | 49 | Codebase Onboarding |  |
| 25 | challenge | claude-skills0418 | 48 | /em -challenge — Pre-Mortem Plan Analysis |  |
| 26 | board | claude-skills0418 | 48 | Read, write, and browse the AgentHub message board for ag... |  |
| 27 | board-prep | claude-skills0418 | 47 | /em -board-prep — Board Meeting Preparation |  |
| 28 | status | claude-skills0418 | 46 | Show experiment dashboard with results, active loops, and... | 保底 |

---

## 14. 简历与专业文档

简历生成、流程监控等专业文档场景

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | customer-success-manager | claude-skills0418 | 81 | Monitors customer health, predicts churn risk, and identi... | 首选 |
| 2 | process-monitor | James-Skills | 60 | 流程智能监控设计专家。基于用户提供的流程信息和业务目标，引导完成监控指标定义、异常阈值设置、预警规则设计、根因分析... | 备选 |
| 3 | codex | agent-toolkit | 53 | Use when the user asks to run Codex CLI (codex exec, code... |  |
| 4 | resume | claude-skills0418 | 49 | Resume a paused experiment. Checkout the experiment branc... | 保底 |

---

## 15. 未分类

暂未归入明确聚类的技能

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | minimax-music-gen | MiniMax-skills | 67 | > | 首选 |
| 2 | hdd | ClaWiser | 65 | > | 备选 |
| 3 | gemini | agent-toolkit | 65 | Use when the user asks to run Gemini CLI for code review,... |  |
| 4 | buddy-sings | MiniMax-skills | 62 | > |  |
| 5 | minimax-music-playlist | MiniMax-skills | 59 | > |  |
| 6 | loop | claude-skills0418 | 54 | Start an autonomous experiment loop with user-selected in... |  |
| 7 | project-skill-pairing | ClaWiser | 51 | > |  |
| 8 | sdd | ClaWiser | 50 | > |  |
| 9 | init | claude-skills0418 | 41 | >- |  |
| 10 | generate | claude-skills0418 | 38 | >- |  |
| 11 | report | claude-skills0418 | 37 | >- |  |
| 12 | review | claude-skills0418 | 36 | >- | 保底 |

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
