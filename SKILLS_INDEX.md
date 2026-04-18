# Skills Collection Index

> 本仓库收录了多个 Claude Code / AI Agent 技能合集，按功能聚类分类，每个聚类内按综合评分排名。
> 基于 `skills-registry.json` 自动生成 | 更新时间: 2026-04-19

**Fallback 机制**: 同一聚类内，优先使用排名靠前的 skill；如果首选 skill 失败（依赖缺失/API 报错），自动降级到下一个。

**总计**: 15 个聚类, 519 个技能

---

## 1. 内容创作与写作

文章撰写、文案生成、风格提取、小说写作等创作场景

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | humanizer | agent-toolkit | 84 | Remove signs of AI-generated writing from text. Use when ... | 首选 |
| 2 | baoyu-comic | baoyu-skills | 84 | Knowledge comic creator supporting multiple art styles an... | 备选 |
| 3 | content-humanizer | claude-skills0418 | 81 | Makes AI-generated content sound genuinely human — not ju... |  |
| 4 | content-production | claude-skills0418 | 81 | Full content production pipeline — takes a topic from bla... |  |
| 5 | copy-editing | claude-skills0418 | 81 | When the user wants to edit, review, or improve existing ... |  |
| 6 | copywriting | claude-skills0418 | 81 | When the user wants to write, rewrite, or improve marketi... |  |
| 7 | novel-writer | wpsnote-skills | 81 | AI 陪伴式长篇小说创作助手，结合 WPS 笔记实现有记忆、懂上下文、不穿帮的持续创作。触发词：帮我写小说、我想写... |  |
| 8 | short-video-copywriter | wpsnote-skills | 80 | 将用户粘贴的原稿（文章/新闻/长文）改写为短视频口播文案，支持分镜脚本生成并用 AI 生图为每个分镜配插图。 自动... |  |
| 9 | content-creator | wpsnote-skills | 79 | 【内容创作起点】用户想要写文章/公众号/文案时的首选skill。 触发词："帮我写""我想写""准备写""开始写"... |  |
| 10 | content-strategy | claude-skills0418 | 78 | When the user wants to plan a content strategy, decide wh... |  |
| 11 | content-creator | claude-skills0418 | 77 | Deprecated redirect skill that routes legacy 'content cre... |  |
| 12 | minimax-music-gen | MiniMax-skills | 76 | Use when user wants to generate music, songs, or audio tr... |  |
| 13 | novel-writer-cli | wpsnote-skills | 71 | AI 陪伴式长篇小说创作助手（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记，实现有... |  |
| 14 | wechat-tech-writer | wechat_article_skills | 71 | 自动搜索、抓取、改写技术内容，生成适合微信公众号的中文科普文章。涵盖AI大模型、GitHub开源工具、技术话题。当... |  |
| 15 | ljg-writes | ljg-skills | 68 | 写作引擎。像手术刀剖开一个观点，一层层剥到底。1000-1500 字。 |  |
| 16 | wechat-product-manager-writer | wechat_article_skills | 66 | 从 AI 产品经理视角撰写微信公众号文章。涵盖 AI 产品拆解、场景解决方案、效率提升实战、产品方法论、行业观察。... |  |
| 17 | founder-sales | lenny-skills | 66 | Help founders close their first customers and build repea... |  |
| 18 | written-communication | lenny-skills | 66 | Help users communicate more effectively in writing. Use w... |  |
| 19 | writing-north-star-metrics | lenny-skills | 66 | Help users define their North Star metric. Use when someo... |  |
| 20 | writing-specs-designs | lenny-skills | 65 | Help users write effective specs and design documents. Us... |  |
| 21 | working-backwards | lenny-skills | 65 | Help users apply the working backwards methodology. Use w... |  |
| 22 | video-content-strategist | claude-skills0418 | 65 | Use when planning video content strategy, writing video s... |  |
| 23 | writing-job-descriptions | lenny-skills | 64 | Help users write effective job descriptions. Use when som... |  |
| 24 | writing-prds | lenny-skills | 64 | Help users write effective PRDs. Use when someone is docu... |  |
| 25 | building-with-llms | lenny-skills | 63 | Help users build effective AI applications. Use when some... |  |
| 26 | domain-name-brainstormer | agent-toolkit | 62 | Generates creative domain name ideas for your project and... |  |
| 27 | crafting-effective-readmes | agent-toolkit | 60 | Use when writing or improving README files. Not all READM... |  |
| 28 | naming-analyzer | agent-toolkit | 60 | Suggest better variable, function, and class names based ... |  |
| 29 | writing-clearly-and-concisely | agent-toolkit | 59 | Use when writing prose humans will read—documentation, co... |  |
| 30 | wechat-style-profiler | wechat-skills | 59 | 面向公众号作者的文风 DNA 梳理技能。用于从 3-10 篇参考文章中建立可复用的风格画像，输出 14 维分析、标... |  |
| 31 | wechat-topic-outline-planner | wechat-skills | 55 | 公众号选题与大纲策划技能。用于把一个粗点子、资料包、语音底稿或采访纪要，转成 2-3 个高价值选题角度、1 个推荐... |  |
| 32 | wechat-title-generator | wechat-skills | 53 | 公众号标题生成与评估技能。用于基于已确认的选题、大纲和目标读者，生成 8 个标题候选，筛掉低质标题，并推荐 1 个... |  |
| 33 | contract-and-proposal-writer | claude-skills0418 | 53 | Contract & Proposal Writer |  |
| 34 | wechat-draft-writer | wechat-skills | 52 | 公众号初稿写作技能。用于在选题和大纲已确认后，基于参考资料、语音底稿和文风 DNA 生成一版高保真初稿。适用于正文... |  |
| 35 | status | claude-skills0418 | 50 | Memory health dashboard showing line counts, topic files,... | 保底 |

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
| 14 | image-gen | wpsnote-skills | 75 | AI 图像生成助手，支持文生图和图生图，对接 OpenRouter / 阿里云百炼 / 火山方舟 / Google... |  |
| 15 | gif-sticker-maker | MiniMax-skills | 73 | Convert photos (people, pets, objects, logos) into 4 anim... |  |
| 16 | ljg-card | ljg-skills | 73 | Content caster (铸). Transforms content into PNG visuals. ... |  |
| 17 | marp-slide | agent-toolkit | 71 | Create professional Marp presentation slides with 7 beaut... |  |
| 18 | mermaid-diagrams | agent-toolkit | 71 | Comprehensive guide for creating software diagrams using ... |  |
| 19 | sales-engineer | claude-skills0418 | 71 | Analyzes RFP/RFI responses for coverage gaps, builds comp... |  |
| 20 | tc-tracker | claude-skills0418 | 71 | Use when the user asks to track technical changes, create... |  |
| 21 | senior-computer-vision | claude-skills0418 | 71 | Computer vision engineering skill for object detection, i... |  |
| 22 | ui-design-system | claude-skills0418 | 71 | UI design system toolkit for Senior UI Designer including... |  |
| 23 | slide-making-skill | MiniMax-skills | 68 | Implement single-slide PowerPoint pages with PptxGenJS. U... |  |
| 24 | vision-analysis | MiniMax-skills | 68 | Analyze, describe, and extract information from images us... |  |
| 25 | draw-io | agent-toolkit | 68 | draw.io diagram creation, editing, and review. Use for .d... |  |
| 26 | mmx-cli | MiniMax-skills | 66 | Use mmx to generate text, images, video, speech, and musi... |  |
| 27 | meme-factory | agent-toolkit | 66 | Generate memes using the memegen.link API. Use when users... |  |
| 28 | baoyu-diagram | baoyu-skills | 66 | Create professional, dark-themed SVG diagrams of any type... |  |
| 29 | giving-presentations | lenny-skills | 66 | Help users create and deliver compelling presentations. U... |  |
| 30 | excalidraw | agent-toolkit | 65 | Use when working with *.excalidraw or *.excalidraw.json f... |  |
| 31 | defining-product-vision | lenny-skills | 65 | Help users create compelling product visions. Use when so... |  |
| 32 | managing-imposter-syndrome | lenny-skills | 65 | Help users work through feelings of inadequacy and self-d... |  |
| 33 | organizational-design | lenny-skills | 65 | Help users design effective organizational structures. Us... |  |
| 34 | product-discovery | claude-skills0418 | 63 | Use when validating product opportunities, mapping assump... |  |
| 35 | baoyu-danger-gemini-web | baoyu-skills | 60 | Generates images and text via reverse-engineered Gemini W... | 实验性 |

---

## 3. 社交媒体与营销投放

微信/微博/X/小红书发布、付费广告、SEO、邮件营销、着陆页、转化优化

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | marketing-demand-acquisition | claude-skills0418 | 81 | Creates demand generation campaigns, optimizes paid ad sp... | 首选 |
| 2 | wechat-publisher | wpsnote-skills | 81 | 【公众号发布助手】将 WPS 笔记排版并导出为微信公众号 HTML。 当用户说"发公众号""排版公众号""导出到公... | 备选 |
| 3 | ad-creative | claude-skills0418 | 81 | When the user needs to generate, iterate, or scale ad cre... |  |
| 4 | campaign-analytics | claude-skills0418 | 81 | Analyzes campaign performance with multi-touch attributio... |  |
| 5 | churn-prevention | claude-skills0418 | 81 | Reduce voluntary and involuntary churn through cancel flo... |  |
| 6 | cold-email | claude-skills0418 | 81 | When the user wants to write, improve, or build a sequenc... |  |
| 7 | form-cro | claude-skills0418 | 81 | When the user wants to optimize any form that is NOT sign... |  |
| 8 | free-tool-strategy | claude-skills0418 | 81 | When the user wants to build a free tool for marketing — ... |  |
| 9 | paid-ads | claude-skills0418 | 81 | When the user wants help with paid advertising campaigns ... |  |
| 10 | popup-cro | claude-skills0418 | 81 | When the user wants to create or optimize popups, modals,... |  |
| 11 | referral-program | claude-skills0418 | 81 | When the user wants to design, launch, or optimize a refe... |  |
| 12 | schema-markup | claude-skills0418 | 81 | When the user wants to implement, audit, or validate stru... |  |
| 13 | signup-flow-cro | claude-skills0418 | 81 | When the user wants to optimize signup, registration, acc... |  |
| 14 | site-architecture | claude-skills0418 | 81 | When the user wants to audit, redesign, or plan their web... |  |
| 15 | social-content | claude-skills0418 | 81 | When the user wants help creating, scheduling, or optimiz... |  |
| 16 | x-twitter-growth | claude-skills0418 | 81 | X/Twitter growth engine for building audience, crafting v... |  |
| 17 | baoyu-markdown-to-html | baoyu-skills | 80 | Converts Markdown to styled HTML with WeChat-compatible t... |  |
| 18 | seo-audit | claude-skills0418 | 79 | When the user wants to audit, review, or diagnose SEO iss... |  |
| 19 | baoyu-post-to-wechat | baoyu-skills | 78 | Posts content to WeChat Official Account (微信公众号) via API ... |  |
| 20 | baoyu-post-to-x | baoyu-skills | 78 | Posts content and articles to X (Twitter). Supports regul... |  |
| 21 | email-sequence | claude-skills0418 | 78 | When the user wants to create or optimize an email sequen... |  |
| 22 | programmatic-seo | claude-skills0418 | 78 | When the user wants to create SEO-driven pages at scale u... |  |
| 23 | paywall-upgrade-cro | claude-skills0418 | 77 | When the user wants to create or optimize in-app paywalls... |  |
| 24 | ai-seo | claude-skills0418 | 76 | Optimize content to get cited by AI search engines — Chat... |  |
| 25 | launch-strategy | claude-skills0418 | 75 | When the user wants to plan a product launch, feature ann... |  |
| 26 | page-cro | claude-skills0418 | 75 | When the user wants to optimize, improve, or increase con... |  |
| 27 | social-media-manager | claude-skills0418 | 74 | When the user wants to develop social media strategy, pla... |  |
| 28 | marketing-ops | claude-skills0418 | 74 | Central router for the marketing skill ecosystem. Use whe... |  |
| 29 | minimax-xlsx | MiniMax-skills | 73 | Open, create, read, analyze, edit, or validate Excel/spre... |  |
| 30 | marketing-skills | claude-skills0418 | 72 | 42 marketing agent skills and plugins for Claude Code, Co... |  |
| 31 | behuman | claude-skills0418 | 71 | Use when the user wants more human-like AI responses — le... |  |
| 32 | app-store-optimization | claude-skills0418 | 71 | App Store Optimization (ASO) toolkit for researching keyw... |  |
| 33 | social-media-analyzer | claude-skills0418 | 71 | Social media campaign analysis and performance tracking. ... |  |
| 34 | landing-page-generator | claude-skills0418 | 71 | Generates high-converting landing pages as complete Next.... |  |
| 35 | baoyu-post-to-weibo | baoyu-skills | 70 | Posts content to Weibo (微博). Supports regular posts with ... |  |
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
| 5 | qiaomu-markdown-proxy | markdown-proxy | 70 | Fetch any URL as clean Markdown via proxy services or bui... |  |
| 6 | baoyu-compress-image | baoyu-skills | 70 | Compresses images to WebP (default) or PNG with automatic... |  |
| 7 | behavioral-product-design | lenny-skills | 65 | Help users apply behavioral science to product design. Us... |  |
| 8 | organizational-transformation | lenny-skills | 65 | Help users transform organizations toward modern product ... |  |
| 9 | minimax-pdf | MiniMax-skills | 64 | Use this skill when visual quality and design identity ma... |  |
| 10 | anything-to-md | anything-to-md | 64 | Universal document to Markdown converter. Convert any fil... |  |
| 11 | enterprise-sales | lenny-skills | 64 | Help users navigate enterprise sales. Use when someone is... |  |
| 12 | web-to-markdown | agent-toolkit | 61 | Use ONLY when the user explicitly says: 'use the skill we... |  |
| 13 | html-to-pdf | marketing-skills | 55 | Convert an HTML file to a PDF using headless Chrome (Pupp... | 保底 |

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
| 8 | doc-importer | wpsnote-skills | 82 | 将本地文档批量导入到 WPS 笔记。支持扫描 Obsidian Vault、思源笔记、微信公众号存档、 下载目录或... |  |
| 9 | research-summarizer | claude-skills0418 | 81 | Structured research summarization agent skill for non-dev... |  |
| 10 | ljg-travel | ljg-skills | 78 | Deep travel research workflow for museums and ancient arc... |  |
| 11 | web-importer | wpsnote-skills | 72 | 将网页内容高质量导入到 WPS 笔记，保留原文颜色、粗体、标题格式，图片按原文位置插入。 支持微信公众号文章、X/... |  |
| 12 | ljg-paper-flow | ljg-skills | 72 | Paper workflow: read papers + cast cards in one go. Takes... |  |
| 13 | literature-reader | wpsnote-skills | 72 | 阅读、分析并总结学术文献（PDF论文），生成结构化的文献概要笔记。核心能力：论文元信息提取、研究问题识别、方法论梳... |  |
| 14 | ux-researcher-designer | claude-skills0418 | 71 | UX research and design toolkit for Senior UX Designer/Res... |  |
| 15 | baoyu-danger-x-to-markdown | baoyu-skills | 68 | Converts X (Twitter) tweets and articles to markdown with... | 实验性 |
| 16 | meeting-analyzer | claude-skills0418 | 67 | Analyzes meeting transcripts and recordings to surface be... |  |
| 17 | analyzing-user-feedback | lenny-skills | 66 | Help users synthesize and act on customer feedback. Use w... |  |
| 18 | stakeholder-alignment | lenny-skills | 66 | Help users align stakeholders and get buy-in. Use when so... |  |
| 19 | running-effective-meetings | lenny-skills | 65 | Help users run more effective meetings. Use when someone ... |  |
| 20 | paper-researcher | wpsnote-skills | 62 | 学术论文全流程助手：搜索论文、下载 PDF、存入 WPS 笔记、精读分析。当用户说"搜论文"、"找论文"、"下载论... |  |
| 21 | perplexity | agent-toolkit | 61 | Web search and research using Perplexity AI. Use when use... |  |
| 22 | baoyu-youtube-transcript | baoyu-skills | 59 | Downloads YouTube video transcripts/subtitles and cover i... |  |
| 23 | setup | claude-skills0418 | 52 | Set up a new autoresearch experiment interactively. Colle... | 保底 |

---

## 6. 笔记管理与知识整理

笔记美化、标签整理、知识关联、灵感发现、记忆系统、内部 wiki

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | llm-wiki | claude-skills0418 | 80 | Use when building or maintaining a persistent personal kn... | 首选 |
| 2 | noise-reduction | ClaWiser | 80 | 对话数据降噪（Noise Reduction）。诊断当前环境的噪声模式，编写降噪规则，验证降噪效果。 适用于：首次... | 备选 |
| 3 | note-calendar | wpsnote-skills | 79 | 在 macOS 上打通 WPS 笔记与系统日历。支持查询日程、创建/移动/删除日历事件，以及笔记与日历的双向联动：... |  |
| 4 | wps-note | wpsnote-skills | 79 | 通过 MCP 工具读取、编辑和管理 WPS 笔记，基于 block 文档模型，所有内容以 XML 格式交换。当用户... |  |
| 5 | context-engine | claude-skills0418 | 78 | Loads and manages company context for all C-suite advisor... |  |
| 6 | wps-deep-search | wpsnote-skills | 77 | 【深度搜索】深挖笔记关联，构建知识图谱的 WPS 笔记查询助手。 当用户说"深度搜索""帮我深挖""关联查询""全... |  |
| 7 | wpsnote-beautifier | wpsnote-skills | 77 | 智能美化 WPS 笔记文档，采用克制统一的配色风格（全文仅1种主色调，不混用多色系）。核心能力：优化标题层级结构、... |  |
| 8 | tag-organize-cli | wpsnote-skills | 77 | 笔记标签整理的核心原则与完整工作流程（CLI 版）。通过系统命令行调用 wpsnote-cli 操作 WPS 笔记... |  |
| 9 | xiaohongshu-note-creator | wpsnote-skills | 76 | 【笔记/文章转小红书】将用户已有的 WPS 笔记或文章内容，改写压缩为小红书图文方案。 核心特征：用户已有原文内容... |  |
| 10 | memory-deposit | ClaWiser | 74 | 记忆系统搭建与健康检查（Memory Deposit）。检查并补齐 6 层记忆系统，确保 workspace 的记... |  |
| 11 | note-copilot | wpsnote-skills | 72 | 笔记协作助手：帮用户打磨当前 WPS 笔记，识别并处理笔记中的 *** 和 /// 援助标记，同时在发现明显逻辑错... |  |
| 12 | decision-logger | claude-skills0418 | 72 | Two-layer memory architecture for board meeting decisions... |  |
| 13 | ie-engine | wpsnote-skills | 71 | 灵感引擎的统一入口，串联记忆检索、想法连接和洞见生成的完整流水线。当用户提到"灵感引擎"、"激发灵感"、"conn... |  |
| 14 | clawiser | ClaWiser | 70 | Agent 记忆与工作流增强套件。包含 8 个模块：记忆系统（memory-deposit、retrieval-e... |  |
| 15 | save-game | ClaWiser | 69 | 项目存档（Save Game）。审视→反思→调整→写交接，不只是抄状态。 适用于：工作段结束需要保存进展、comp... |  |
| 16 | load-game | ClaWiser | 69 | 项目读档（Load Game）。从 HANDOFF.md 恢复项目上下文，对比计划与实际，识别偏差并调整。 适用于... |  |
| 17 | news-to-note | wpsnote-skills | 68 | 基于 WPS 笔记知识库的新闻智能解读。将新闻存入笔记，搜索用户整个笔记库找到关联内容， 产出个性化 insigh... |  |
| 18 | tag-organize | wpsnote-skills | 68 | 笔记标签整理的核心原则与完整工作流程。当用户提到"整理笔记标签"、"清理标签"、"标签太乱"、"标签太多"、"帮我... |  |
| 19 | ljg-think | ljg-skills | 62 | 追本之箭——纵向深钻思维工具。给一个观点、现象或问题，像箭一样一路向下钻到不可再分的本质。Use when use... |  |
| 20 | code-tour | claude-skills0418 | 62 | Use when the user asks to create a CodeTour .tour file — ... |  |
| 21 | ie-generate-insight | wpsnote-skills | 59 | 将推理分析结果转化为可阅读的洞见文本，生成下一步探索建议，展示想法的演化路径。当用户提到"生成洞见"、"给我灵感"... |  |
| 22 | ie-connect-dots | wpsnote-skills | 58 | 对笔记和想法进行语义聚类、发现想法之间的隐含连接、识别长期重复出现的主题模式。当用户提到"连接想法"、"发现关联"... |  |
| 23 | context-engineering | agent-skills | 58 | Optimizes agent context setup. Use when starting a new se... |  |
| 24 | review-notes | wpsnote-skills | 57 | 作为 coding-assistant 的子 skill，生成或更新 WPS 技术文档。笔记必须完整且包含 7 个... |  |
| 25 | ie-retrieve-memory | wpsnote-skills | 55 | 从用户的 WPS 笔记中检索历史知识和过去的想法。当用户提到"回忆过去的笔记"、"之前写过什么"、"历史想法"、"... |  |
| 26 | remember | claude-skills0418 | 54 | Explicitly save important knowledge to auto-memory with t... |  |
| 27 | promote | claude-skills0418 | 53 | Graduate a proven pattern from auto-memory (MEMORY.md) to... |  |
| 28 | review | claude-skills0418 | 52 | Analyze auto-memory for promotion candidates, stale entri... |  |
| 29 | class-note-builder | wpsnote-skills | 51 | 当用户希望把课堂逐字稿、OCR 笔记、截图资料或零散学习内容整理成结构化的 WPS 学习笔记时使用此 Skill。... |  |
| 30 | notes-to-lesson-plan | wpsnote-skills | 48 | 当用户希望把 WPS 学习笔记整理成一份可讲给别人听的讲解结构、迷你教案或 teach-back 提纲时使用此 S... |  |
| 31 | insight-recaller | wpsnote-skills | 47 | 当用户在 WPS 里写新内容、做专题复习、准备讲稿或整理研究思路时，希望把过去真正有用的旧笔记重新召回到眼前，就使... |  |
| 32 | study-note-linker | wpsnote-skills | 47 | 当用户希望把当前 WPS 学习笔记和已有旧笔记连起来，而不是让新笔记继续孤立存在时使用此 Skill。适合复习串讲... |  |
| 33 | notes-to-flashcards | wpsnote-skills | 47 | 当用户希望把 WPS 笔记转成可主动回忆的复习卡片时使用此 Skill。适合课程笔记复习、概念记忆、考前冲刺、误解... | 保底 |

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
| 4 | fullstack-dev | MiniMax-skills | 81 | Full-stack backend architecture and frontend-backend inte... |  |
| 5 | pptx-generator | MiniMax-skills | 81 | Generate, edit, and read PowerPoint presentations. Create... |  |
| 6 | dependency-updater | agent-toolkit | 81 | Smart dependency management for any language. Auto-detect... |  |
| 7 | react-dev | agent-toolkit | 81 | This skill should be used when building React components ... |  |
| 8 | agent-protocol | claude-skills0418 | 81 | Inter-agent communication protocol for C-suite agent team... |  |
| 9 | docker-development | claude-skills0418 | 81 | Docker and container development agent skill and plugin f... |  |
| 10 | react-native-dev | MiniMax-skills | 79 | React Native and Expo development guide covering componen... |  |
| 11 | prompt-engineer-toolkit | claude-skills0418 | 78 | Analyzes and rewrites prompts for better AI output, creat... |  |
| 12 | flutter-dev | MiniMax-skills | 78 | Flutter cross-platform development guide covering widget ... |  |
| 13 | frontend-dev | MiniMax-skills | 76 | Full-stack frontend development combining premium UI desi... |  |
| 14 | minimax-docx | MiniMax-skills | 76 | Professional DOCX document creation, editing, and formatt... |  |
| 15 | ios-application-dev | MiniMax-skills | 75 | iOS application development guide covering UIKit, SnapKit... |  |
| 16 | ljg-skill-map | ljg-skills | 72 | Skill map viewer. Scans all installed skills and renders ... |  |
| 17 | adversarial-reviewer | claude-skills0418 | 72 | Adversarial code review that breaks the self-review monoc... |  |
| 18 | code-review-and-quality | agent-skills | 71 | Conducts multi-axis code review. Use before merging any c... |  |
| 19 | command-creator | agent-toolkit | 71 | This skill should be used when creating a Claude Code sla... |  |
| 20 | database-schema-designer | agent-toolkit | 71 | Design robust, scalable database schemas for SQL and NoSQ... |  |
| 21 | gepetto | agent-toolkit | 71 | Creates detailed, sectionized implementation plans throug... |  |
| 22 | mui | agent-toolkit | 71 | Material-UI v7 component library patterns including sx pr... |  |
| 23 | openapi-to-typescript | agent-toolkit | 71 | Converts OpenAPI 3.0 JSON/YAML to TypeScript interfaces a... |  |
| 24 | plugin-forge | agent-toolkit | 71 | Create and manage Claude Code plugins with proper structu... |  |
| 25 | skill-judge | agent-toolkit | 71 | Evaluate Agent Skill design quality against official spec... |  |
| 26 | release-manager | claude-skills0418 | 71 | Use when the user asks to plan releases, manage changelog... |  |
| 27 | spec-driven-workflow | claude-skills0418 | 71 | Use when the user asks to write specs before code, define... |  |
| 28 | senior-architect | claude-skills0418 | 71 | This skill should be used when the user asks to "design s... |  |
| 29 | senior-backend | claude-skills0418 | 71 | Designs and implements backend systems including REST API... |  |
| 30 | senior-data-engineer | claude-skills0418 | 71 | Data engineering skill for building scalable data pipelin... |  |
| 31 | senior-data-scientist | claude-skills0418 | 71 | World-class senior data scientist skill specialising in s... |  |
| 32 | senior-frontend | claude-skills0418 | 71 | Frontend development skill for React, Next.js, TypeScript... |  |
| 33 | senior-fullstack | claude-skills0418 | 71 | Fullstack development toolkit with project scaffolding fo... |  |
| 34 | senior-ml-engineer | claude-skills0418 | 71 | ML engineering skill for productionizing models, building... |  |
| 35 | snowflake-development | claude-skills0418 | 71 | Use when writing Snowflake SQL, building data pipelines w... |  |
| 36 | saas-scaffolder | claude-skills0418 | 71 | Generates complete, production-ready SaaS project boilerp... |  |
| 37 | capa-officer | claude-skills0418 | 71 | CAPA system management for medical device QMS. Covers roo... |  |
| 38 | skill-creator | wpsnote-skills | 71 | Create new skills, modify and improve existing skills, an... |  |
| 39 | agent-designer | claude-skills0418 | 70 | Use when the user asks to design multi-agent systems, cre... |  |
| 40 | tech-stack-evaluator | claude-skills0418 | 70 | Technology stack evaluation and comparison with TCO analy... |  |
| 41 | code-simplification | agent-skills | 70 | Simplifies code for clarity. Use when refactoring code fo... |  |
| 42 | database-designer | claude-skills0418 | 70 | Use when the user asks to design database schemas, plan d... |  |
| 43 | frontend-ui-engineering | agent-skills | 70 | Builds production-quality UIs. Use when building or modif... |  |
| 44 | focused-fix | claude-skills0418 | 70 | Use when the user asks to fix, debug, or make a specific ... |  |
| 45 | shipping-and-launch | agent-skills | 69 | Prepares production launches. Use when preparing to deplo... |  |
| 46 | debugging-and-error-recovery | agent-skills | 69 | Guides systematic root-cause debugging. Use when tests fa... |  |
| 47 | api-and-interface-design | agent-skills | 69 | Guides stable API and interface design. Use when designin... |  |
| 48 | documentation-and-adrs | agent-skills | 68 | Records decisions and documentation. Use when making arch... |  |
| 49 | migration-architect | claude-skills0418 | 67 | Migration Architect |  |
| 50 | database-schema-designer | claude-skills0418 | 67 | Use when the user asks to create ERD diagrams, normalize ... |  |
| 51 | tech-debt-tracker | claude-skills0418 | 66 | Scan codebases for technical debt, score severity, track ... |  |
| 52 | incremental-implementation | agent-skills | 66 | Delivers changes incrementally. Use when implementing any... |  |
| 53 | agent-md-refactor | agent-toolkit | 66 | Refactor bloated AGENTS.md, CLAUDE.md, or similar agent i... |  |
| 54 | ci-cd-and-automation | agent-skills | 66 | Automates CI/CD pipeline setup. Use when setting up or mo... |  |
| 55 | performance-optimization | agent-skills | 66 | Optimizes application performance. Use when performance r... |  |
| 56 | test-driven-development | agent-skills | 66 | Drives development with tests. Use when implementing any ... |  |
| 57 | c4-architecture | agent-toolkit | 66 | Generate architecture documentation using C4 model Mermai... |  |
| 58 | qa-test-planner | agent-toolkit | 66 | Generate comprehensive test plans, manual test cases, reg... |  |
| 59 | browser-automation | claude-skills0418 | 66 | Use when the user asks to automate browser tasks, scrape ... |  |
| 60 | rag-architect | claude-skills0418 | 66 | Use when the user asks to design RAG pipelines, optimize ... |  |
| 61 | sql-database-assistant | claude-skills0418 | 66 | Use when the user asks to write SQL queries, optimize dat... |  |
| 62 | a11y-audit | claude-skills0418 | 66 | Accessibility audit skill for scanning, fixing, and verif... |  |
| 63 | security-pen-testing | claude-skills0418 | 66 | Use when the user asks to perform security audits, penetr... |  |
| 64 | senior-prompt-engineer | claude-skills0418 | 66 | This skill should be used when the user asks to "optimize... |  |
| 65 | senior-qa | claude-skills0418 | 66 | Generates unit tests, integration tests, and E2E tests fo... |  |
| 66 | tdd-guide | claude-skills0418 | 66 | Test-driven development skill for writing unit tests, gen... |  |
| 67 | spec-to-repo | claude-skills0418 | 66 | Use when the user says 'build me an app', 'create a proje... |  |
| 68 | ai-product-strategy | lenny-skills | 66 | Help users define AI product strategy. Use when someone i... |  |
| 69 | session-handoff | agent-toolkit | 66 | Creates comprehensive handoff documents for seamless AI a... |  |
| 70 | evaluating-candidates | lenny-skills | 66 | Help users make better hiring decisions. Use when someone... |  |
| 71 | evaluating-trade-offs | lenny-skills | 66 | Help users make better decisions between competing option... |  |
| 72 | managing-tech-debt | lenny-skills | 66 | Help users manage technical debt strategically. Use when ... |  |
| 73 | shipping-products | lenny-skills | 66 | Help users ship products faster and with higher quality. ... |  |
| 74 | prompt-governance | claude-skills0418 | 65 | Use when managing prompts in production at scale: version... |  |
| 75 | career-transitions | lenny-skills | 65 | Help users navigate career changes and pivots. Use when s... |  |
| 76 | usability-testing | lenny-skills | 65 | Help users conduct effective usability testing. Use when ... |  |
| 77 | code-reviewer | claude-skills0418 | 65 | Code review automation for TypeScript, JavaScript, Python... |  |
| 78 | conducting-interviews | lenny-skills | 65 | Help users conduct effective hiring interviews. Use when ... |  |
| 79 | engineering-culture | lenny-skills | 65 | Help users build strong engineering culture. Use when som... |  |
| 80 | product-taste-intuition | lenny-skills | 65 | Help users develop product taste and intuition. Use when ... |  |
| 81 | running-design-reviews | lenny-skills | 65 | Help users run effective design reviews and critiques. Us... |  |
| 82 | vibe-coding | lenny-skills | 65 | Help users build software using AI coding tools. Use when... |  |
| 83 | design-style-skill | MiniMax-skills | 65 | Select a consistent visual design system for PPT slides u... |  |
| 84 | interview-system-designer | claude-skills0418 | 65 | This skill should be used when the user asks to "design i... |  |
| 85 | deprecation-and-migration | agent-skills | 65 | Manages deprecation and migration. Use when removing old ... |  |
| 86 | startup-ideation | lenny-skills | 65 | Help users generate and evaluate startup ideas. Use when ... |  |
| 87 | commit-work | agent-toolkit | 64 | Create high-quality git commits: review/stage intended ch... |  |
| 88 | engineering-skills | claude-skills0418 | 64 | 23 engineering agent skills and plugins for Claude Code, ... |  |
| 89 | spec-driven-development | agent-skills | 64 | Creates specs before coding. Use when starting a new proj... |  |
| 90 | ppt-editing-skill | MiniMax-skills | 64 | Edit existing PowerPoint files or templates with XML-safe... |  |
| 91 | browser-testing-with-devtools | agent-skills | 64 | Tests in real browsers. Use when building or debugging an... |  |
| 92 | source-driven-development | agent-skills | 64 | Grounds every implementation decision in official documen... |  |
| 93 | frontend-to-backend-requirements | agent-toolkit | 64 | Document frontend data needs for backend developers. Use ... |  |
| 94 | self-eval | claude-skills0418 | 63 | Honestly evaluate AI work quality using a two-axis scorin... |  |
| 95 | reducing-entropy | agent-toolkit | 63 | Manual-only skill for minimizing total codebase size. Onl... |  |
| 96 | api-test-suite-builder | claude-skills0418 | 63 | Use when the user asks to generate API tests, create inte... |  |
| 97 | evaluating-new-technology | lenny-skills | 63 | Help users evaluate emerging technologies. Use when someo... |  |
| 98 | git-workflow-and-versioning | agent-skills | 62 | Structures git workflow practices. Use when making any co... |  |
| 99 | skill-tester | claude-skills0418 | 62 | Skill Tester |  |
| 100 | color-font-skill | MiniMax-skills | 62 | Choose presentation-ready color palettes and font pairing... |  |
| 101 | ppt-orchestra-skill | MiniMax-skills | 62 | Plan and orchestrate multi-slide PowerPoint creation from... |  |
| 102 | pr-review-expert | claude-skills0418 | 62 | Use when the user asks to review pull requests, analyze c... |  |
| 103 | backend-to-frontend-handoff-docs | agent-toolkit | 61 | Create API handoff documentation for frontend developers.... |  |
| 104 | dependency-auditor | claude-skills0418 | 60 | Dependency Auditor |  |
| 105 | datadog-cli | agent-toolkit | 60 | Datadog CLI for searching logs, querying metrics, tracing... |  |
| 106 | api-design-reviewer | claude-skills0418 | 59 | API Design Reviewer |  |
| 107 | ai-evals | lenny-skills | 59 | Help users create and run AI evaluations. Use when someon... |  |
| 108 | coding-assistant | wpsnote-skills | 59 | 多平台编码助手。遵循各平台官方文档做编码规范、单测与编译/lint；协助将核心技术梳理为完整 WPS 笔记技术文档... |  |
| 109 | llm-cost-optimizer | claude-skills0418 | 59 | Use when you need to reduce LLM API spend, control token ... |  |
| 110 | using-agent-skills | agent-skills | 58 | Discovers and invokes agent skills. Use when starting a s... |  |
| 111 | retrieval-enhance | ClaWiser | 58 | 检索系统守护。静默运行——agent 自主判断何时激活。三种场景：(1) 首次搭建时初始化 memorySearc... |  |
| 112 | self-improving-agent | claude-skills0418 | 58 | Curate Claude Code's auto-memory into durable project kno... |  |
| 113 | react-useeffect | agent-toolkit | 57 | React useEffect best practices from official docs. Use wh... |  |
| 114 | init | claude-skills0418 | 57 | Set up Playwright in a project. Use when user says "set u... |  |
| 115 | browserstack | claude-skills0418 | 56 | Run tests on BrowserStack. Use when user mentions "browse... |  |
| 116 | coverage | claude-skills0418 | 56 | Analyze test coverage gaps. Use when user says "test cove... |  |
| 117 | extract | claude-skills0418 | 56 | Turn a proven pattern or debugging solution into a standa... |  |
| 118 | generate | claude-skills0418 | 56 | Generate Playwright tests. Use when user says "write test... |  |
| 119 | migrate | claude-skills0418 | 56 | Migrate from Cypress or Selenium to Playwright. Use when ... |  |
| 120 | git-worktree-manager | claude-skills0418 | 54 | Git Worktree Manager |  |
| 121 | fix | claude-skills0418 | 53 | Fix failing or flaky Playwright tests. Use when user says... |  |
| 122 | performance-profiler | claude-skills0418 | 53 | Performance Profiler |  |
| 123 | changelog-generator | claude-skills0418 | 52 | Changelog Generator |  |
| 124 | mcp-server-builder | claude-skills0418 | 52 | MCP Server Builder |  |
| 125 | playwright-pro | claude-skills0418 | 51 | Production-grade Playwright testing toolkit. Use when the... |  |
| 126 | run | claude-skills0418 | 51 | One-shot lifecycle command that chains init → baseline → ... |  |
| 127 | stress-test | claude-skills0418 | 50 | /em -stress-test — Business Assumption Stress Testing |  |
| 128 | monorepo-navigator | claude-skills0418 | 49 | Monorepo Navigator |  |
| 129 | agent-workflow-designer | claude-skills0418 | 49 | Agent Workflow Designer |  |
| 130 | testrail | claude-skills0418 | 49 | Sync tests with TestRail. Use when user mentions "testrai... |  |
| 131 | merge | claude-skills0418 | 48 | Merge the winning agent's branch into base, archive loser... |  |
| 132 | runbook-generator | claude-skills0418 | 48 | Runbook Generator |  |
| 133 | spawn | claude-skills0418 | 48 | Launch N parallel subagents in isolated git worktrees to ... |  |
| 134 | eval | claude-skills0418 | 47 | Evaluate and rank agent results by metric or LLM judge fo... | 保底 |

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
| 14 | skill-security-auditor | claude-skills0418 | 70 | Security audit and vulnerability scanner for AI agent ski... |  |
| 15 | ra-qm-skills | claude-skills0418 | 68 | 12 regulatory & QM agent skills and plugins for Claude Co... |  |
| 16 | security-and-hardening | agent-skills | 66 | Hardens code against vulnerabilities. Use when handling u... |  |
| 17 | ai-security | claude-skills0418 | 66 | Use when assessing AI/ML systems for prompt injection, ja... |  |
| 18 | senior-secops | claude-skills0418 | 66 | Senior SecOps engineer skill for application security, vu... |  |
| 19 | senior-security | claude-skills0418 | 66 | Security engineering toolkit for threat modeling, vulnera... | 保底 |

---

## 11. 产品管理与敏捷开发

产品管理、敏捷/Scrum、Sprint 规划、OKR、路线图、用户研究、实验设计

| # | 技能 | 来源 | 评分 | 说明 | Fallback |
|---|------|------|------|------|----------|
| 1 | scrum-master | claude-skills0418 | 84 | Advanced Scrum Master skill for data-driven agile team an... | 首选 |
| 2 | epic-design | claude-skills0418 | 81 | Build immersive, cinematic 2.5D interactive websites usin... | 备选 |
| 3 | ab-test-setup | claude-skills0418 | 81 | When the user wants to plan, design, or implement an A/B ... |  |
| 4 | minimax-music-playlist | MiniMax-skills | 78 | Generate personalized music playlists by analyzing the us... |  |
| 5 | saas-metrics-coach | claude-skills0418 | 76 | SaaS financial health advisor. Use when a user shares rev... |  |
| 6 | pricing-strategy | claude-skills0418 | 76 | Design, optimize, and communicate SaaS pricing — tier str... |  |
| 7 | apple-hig-expert | claude-skills0418 | 72 | Expert guidance on Apple Human Interface Guidelines (HIG)... |  |
| 8 | daily-meeting-update | agent-toolkit | 71 | Interactive daily standup/meeting update generator. Use w... |  |
| 9 | difficult-workplace-conversations | agent-toolkit | 71 | Structured approach to workplace conflicts, performance d... |  |
| 10 | feedback-mastery | agent-toolkit | 71 | Navigate difficult conversations and deliver constructive... |  |
| 11 | professional-communication | agent-toolkit | 71 | Guide technical communication for software developers. Co... |  |
| 12 | agile-product-owner | claude-skills0418 | 71 | Agile product ownership for backlog management and sprint... |  |
| 13 | code-to-prd | claude-skills0418 | 71 | Reverse-engineer any codebase into a complete Product Req... |  |
| 14 | product-manager-toolkit | claude-skills0418 | 71 | Comprehensive toolkit for product managers including RICE... |  |
| 15 | product-strategist | claude-skills0418 | 71 | Strategic product leadership toolkit for Head of Product ... |  |
| 16 | senior-pm | claude-skills0418 | 71 | Senior Project Manager for enterprise software, SaaS, and... |  |
| 17 | requirements-clarity | agent-toolkit | 70 | Clarify ambiguous requirements through focused dialogue b... |  |
| 18 | product-skills | claude-skills0418 | 68 | 10 product agent skills and plugins for Claude Code, Code... |  |
| 19 | pm-skills | claude-skills0418 | 68 | 6 project management agent skills and plugins for Claude ... |  |
| 20 | game-changing-features | agent-toolkit | 67 | Find 10x product opportunities and high-leverage improvem... |  |
| 21 | setting-okrs-goals | lenny-skills | 66 | Help users set effective OKRs and goals. Use when someone... |  |
| 22 | planning-and-task-breakdown | agent-skills | 65 | Breaks work into ordered tasks. Use when you have a spec ... |  |
| 23 | prioritizing-roadmap | lenny-skills | 65 | Help users prioritize product roadmaps and backlogs. Use ... |  |
| 24 | pricing-strategy | lenny-skills | 65 | Help users design and optimize pricing strategies. Use wh... |  |
| 25 | post-mortems-retrospectives | lenny-skills | 65 | Help users run effective post-mortems and retrospectives.... |  |
| 26 | product-analytics | claude-skills0418 | 65 | Use when defining product KPIs, building metric dashboard... |  |
| 27 | dogfooding | lenny-skills | 64 | Help users implement effective dogfooding practices. Use ... |  |
| 28 | personal-productivity | lenny-skills | 64 | Help users manage their time and tasks more effectively. ... |  |
| 29 | experiment-designer | claude-skills0418 | 64 | Use when planning product experiments, writing testable h... |  |
| 30 | technical-roadmaps | lenny-skills | 63 | Help users create technical roadmaps. Use when someone is... |  |
| 31 | roadmap-communicator | claude-skills0418 | 61 | Use when preparing roadmap narratives, release notes, cha... |  |
| 32 | idea-refine | agent-skills | 57 | Refines ideas iteratively. Refine ideas through structure... | 保底 |

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
| 8 | hdd | ClaWiser | 79 | Hypothesis-Driven Development (HDD) — 假设驱动开发方法论。当任务涉及不确定性... |  |
| 9 | marketing-psychology | claude-skills0418 | 78 | When the user wants to apply psychological principles, me... |  |
| 10 | intl-expansion | claude-skills0418 | 77 | International market expansion strategy. Market selection... |  |
| 11 | ma-playbook | claude-skills0418 | 76 | M&A strategy for acquiring companies or being acquired. D... |  |
| 12 | marketing-ideas | claude-skills0418 | 76 | When the user needs marketing ideas, inspiration, or stra... |  |
| 13 | marketing-context | claude-skills0418 | 73 | Create and maintain the marketing context document that a... |  |
| 14 | revenue-operations | claude-skills0418 | 71 | Analyzes sales pipeline health, revenue forecasting accur... |  |
| 15 | data-quality-auditor | claude-skills0418 | 71 | Audit datasets for completeness, consistency, accuracy, a... |  |
| 16 | statistical-analyst | claude-skills0418 | 71 | Run hypothesis tests, analyze A/B experiment results, cal... |  |
| 17 | marketing-strategy-pmm | claude-skills0418 | 71 | Product marketing skill for positioning, GTM strategy, co... |  |
| 18 | fda-consultant-specialist | claude-skills0418 | 71 | FDA regulatory consultant for medical device companies. P... |  |
| 19 | dbs-diagnosis | dbskill | 71 | dontbesilent 商业模式诊断。两种模式：问诊（消解你的问题）和体检（拆解你的商业模式）。 触发方式：/d... |  |
| 20 | dbs-xhs-title | dbskill | 71 | 小红书标题公式工具。从 75 个验证过的爆款公式中，帮你挑对的、用对的、理解为什么用这个。 触发方式：/dbs-x... |  |
| 21 | competitive-teardown | claude-skills0418 | 70 | Analyzes competitor products and companies by synthesizin... |  |
| 22 | dbs-hook | dbskill | 69 | dontbesilent 短视频开头优化。诊断开头问题 + 生成优化方案。 触发方式：/dbs-hook、/hoo... |  |
| 23 | financial-analyst | claude-skills0418 | 69 | Performs financial ratio analysis, DCF valuation, budget ... |  |
| 24 | dbs-agent-migration | dbskill | 69 | Agent 工作台迁移。把任意项目整理成 Claude Code / Codex 双端一致、可长期维护的 Agen... |  |
| 25 | ljg-roundtable | ljg-skills | 68 | Structured roundtable discussion framework with a truth-s... |  |
| 26 | business-growth-skills | claude-skills0418 | 68 | 4 business growth agent skills and plugins for Claude Cod... |  |
| 27 | dbs-ai-check | dbskill | 68 | dontbesilent AI 写作特征识别。扫描文案中的 AI 生成痕迹，输出检测报告。默认只诊断不改。 触发方... |  |
| 28 | product-rnd | marketing-skills | 68 | End-to-end Product Innovation R&D workflow — inspiration ... |  |
| 29 | ljg-rank | ljg-skills | 67 | 给一个领域，找出背后真正撑着它的几根独立的力。十几个现象砍到不可再少的生成器——砍完能把现象一个个生回来，才算数。... |  |
| 30 | ljg-relationship | ljg-skills | 67 | Relationship analyst combining structural diagnostics (5-... |  |
| 31 | finance-skills | claude-skills0418 | 66 | Financial analyst agent skill and plugin for Claude Code,... |  |
| 32 | conducting-user-interviews | lenny-skills | 66 | Help users run better customer and user interviews. Use w... |  |
| 33 | dbs-action | dbskill | 66 | dontbesilent 执行力诊断。用阿德勒心理学框架诊断你「知道该做什么但就是不做」的真正原因。 触发方式：/... |  |
| 34 | atypica-user-interview | marketing-skills | 66 | Run AI-simulated user interviews and focus group discussi... |  |
| 35 | having-difficult-conversations | lenny-skills | 66 | Help users navigate tough feedback, performance conversat... |  |
| 36 | launch-marketing | lenny-skills | 66 | Help users plan and execute product launches. Use when so... |  |
| 37 | managing-up | lenny-skills | 66 | Help users work effectively with their manager and execut... |  |
| 38 | dbs-slowisfast | dbskill | 66 | dontbesilent 慢就是快。帮创业者找到看起来更慢但长期更快的方法，用摩擦建造资产。 触发方式：/dbs-... |  |
| 39 | finding-mentors-sponsors | lenny-skills | 66 | Help users build relationships with mentors and sponsors ... |  |
| 40 | dbs-deconstruct | dbskill | 66 | dontbesilent 概念拆解。用维特根斯坦 + 奥派经济学的方法，把模糊的商业概念拆到原子级别。 触发方式：... |  |
| 41 | brand-storytelling | lenny-skills | 66 | Help users craft compelling brand narratives. Use when so... |  |
| 42 | building-a-promotion-case | lenny-skills | 66 | Help users get promoted at work. Use when someone is prep... |  |
| 43 | managing-timelines | lenny-skills | 66 | Help users set and hit realistic deadlines. Use when some... |  |
| 44 | measuring-product-market-fit | lenny-skills | 66 | Help users assess and achieve product-market fit. Use whe... |  |
| 45 | dbs-content | dbskill | 65 | dontbesilent 内容创作诊断。选题通过后，诊断怎么把这个选题做成好内容。 触发方式：/dbs-conte... |  |
| 46 | cross-functional-collaboration | lenny-skills | 65 | Help users work effectively across functions. Use when so... |  |
| 47 | partnership-bd | lenny-skills | 65 | Help users build strategic partnerships and business deve... |  |
| 48 | building-sales-team | lenny-skills | 65 | Help users build and scale their sales organization. Use ... |  |
| 49 | community-building | lenny-skills | 65 | Help users build and grow product communities. Use when s... |  |
| 50 | competitive-analysis | lenny-skills | 65 | Help users understand and respond to competition. Use whe... |  |
| 51 | designing-growth-loops | lenny-skills | 65 | Help users design and optimize growth loops. Use when som... |  |
| 52 | planning-under-uncertainty | lenny-skills | 65 | Help users plan products and strategy when outcomes are u... |  |
| 53 | problem-definition | lenny-skills | 65 | Help users define problems clearly before jumping to solu... |  |
| 54 | business-investment-advisor | claude-skills0418 | 65 | Business investment analysis and capital allocation advis... |  |
| 55 | dbs-benchmark | dbskill | 65 | dontbesilent 对标分析。用五重过滤法帮你找到值得模仿的对标，排除一切关于「我」的噪音。 触发方式：/d... |  |
| 56 | building-team-culture | lenny-skills | 65 | Help users build and maintain strong team culture. Use wh... |  |
| 57 | running-decision-processes | lenny-skills | 65 | Help users run effective decision-making processes. Use w... |  |
| 58 | positioning-messaging | lenny-skills | 65 | Help users craft product positioning and messaging. Use w... |  |
| 59 | retention-engagement | lenny-skills | 65 | Help users improve retention and engagement metrics. Use ... |  |
| 60 | systems-thinking | lenny-skills | 65 | Help users think in systems and understand complex dynami... |  |
| 61 | platform-strategy | lenny-skills | 65 | Help users design and execute platform business strategie... |  |
| 62 | running-effective-1-1s | lenny-skills | 65 | Help users run effective one-on-one meetings. Use when so... |  |
| 63 | energy-management | lenny-skills | 65 | Help users manage their energy for sustained performance.... |  |
| 64 | team-rituals | lenny-skills | 65 | Help users design effective team rituals. Use when someon... |  |
| 65 | negotiating-offers | lenny-skills | 65 | Help users negotiate job offers and compensation. Use whe... |  |
| 66 | platform-infrastructure | lenny-skills | 65 | Help users build and scale internal platforms and technic... |  |
| 67 | product-led-sales | lenny-skills | 65 | Help users implement product-led sales motions. Use when ... |  |
| 68 | product-operations | lenny-skills | 65 | Help users build and scale product operations functions. ... |  |
| 69 | running-offsites | lenny-skills | 65 | Help users plan and run effective team offsites. Use when... |  |
| 70 | sales-compensation | lenny-skills | 65 | Help users design sales compensation plans. Use when some... |  |
| 71 | sales-qualification | lenny-skills | 65 | Help users qualify sales leads effectively. Use when some... |  |
| 72 | startup-pivoting | lenny-skills | 65 | Help users decide when and how to pivot their startup. Us... |  |
| 73 | marketplace-liquidity | lenny-skills | 65 | Help users build and manage marketplace liquidity. Use wh... |  |
| 74 | media-relations | lenny-skills | 65 | Help users build relationships with journalists and get p... |  |
| 75 | fundraising | lenny-skills | 64 | Help founders raise capital and build investor relationsh... |  |
| 76 | design-engineering | lenny-skills | 64 | Help users understand and build design engineering capabi... |  |
| 77 | content-marketing | lenny-skills | 64 | Help users build content marketing strategies. Use when s... |  |
| 78 | scoping-cutting | lenny-skills | 64 | Help users scope projects and cut features effectively. U... |  |
| 79 | design-systems | lenny-skills | 64 | Help users build and scale design systems. Use when someo... |  |
| 80 | coaching-pms | lenny-skills | 64 | Help users develop and coach product managers. Use when s... |  |
| 81 | dbs-chatroom-austrian | dbskill | 63 | 哈耶克 × 米塞斯 × Claude 三人对话。奥派经济学视角的多角色讨论。 触发方式：/dbs-chatroom... |  |
| 82 | delegating-work | lenny-skills | 63 | Help users delegate effectively. Use when someone is stru... |  |
| 83 | plan-as-consultant | marketing-skills | 62 | Plan a business research study the way a professional con... |  |
| 84 | designing-surveys | lenny-skills | 61 | Help users design effective surveys. Use when someone is ... |  |
| 85 | ljg-invest | ljg-skills | 61 | 投资分析, 生成一份深度投资分析报告。不做传统投资分析——核心判断是项目是否是一台「秩序创造机器」。Use whe... |  |
| 86 | dbs | dbskill | 58 | dontbesilent 商业工具箱主入口。根据你的问题自动路由到最合适的诊断工具。 触发方式：/dbs、/商业、... |  |
| 87 | dbs-chatroom | dbskill | 48 | 定向聊天室：根据话题推荐或接受用户指定的专家，模拟多角色对话。触发方式：/dbs-chatroom、/定向聊天室、... | 保底 |

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
| 23 | report | claude-skills0418 | 50 | Generate test report. Use when user says "test report", "... |  |
| 24 | hard-call | claude-skills0418 | 49 | /em -hard-call — Framework for Decisions With No Good Opt... |  |
| 25 | codebase-onboarding | claude-skills0418 | 49 | Codebase Onboarding |  |
| 26 | challenge | claude-skills0418 | 48 | /em -challenge — Pre-Mortem Plan Analysis |  |
| 27 | board | claude-skills0418 | 48 | Read, write, and browse the AgentHub message board for ag... |  |
| 28 | board-prep | claude-skills0418 | 47 | /em -board-prep — Board Meeting Preparation | 保底 |

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
| 1 | buddy-sings | MiniMax-skills | 76 | Use when user wants their Claude Code pet (/buddy) to sin... | 首选 |
| 2 | project-skill-pairing | ClaWiser | 70 | 项目与 Skill 的双向绑定（Project-Skill Pairing）。新建 Skill 时挂靠项目，新建项... | 备选 |
| 3 | sdd | ClaWiser | 68 | 场景驱动开发（Scenario-Driven Development）。动手之前，先想清楚三层：场景是什么、用户真... |  |
| 4 | gemini | agent-toolkit | 65 | Use when the user asks to run Gemini CLI for code review,... |  |
| 5 | loop | claude-skills0418 | 54 | Start an autonomous experiment loop with user-selected in... | 保底 |

---

## 仓库来源

| 目录 | GitHub 仓库 | 简介 |
|------|-------------|------|
| (根目录) | wpsnote/wpsnote-skills | WPS笔记全套AI技能（36技能） |
| lenny-skills/ | RefoundAI/lenny-skills | 商业/产品/市场/工程/领导力套装（86技能） |
| claude-skills0418/ | dy9759/claude-skills0418 | 聚合型技能库：高管顾问、工程团队、QM/RA、敏捷等（238技能） |
| agent-toolkit/ | softaworks/agent-toolkit | 通用工程/协作 skill 工具包（43技能） |
| baoyu-skills/ | JimLiu/baoyu-skills | 内容生成/翻译/社交媒体发布套件 |
| MiniMax-skills/ | MiniMax-AI/skills | 全栈开发与多模态生成技能 |
| agent-skills/ | addyosmani/agent-skills | Addy Osmani 的工程 Agent 技能集（21技能） |
| ljg-skills/ | lijigang/ljg-skills | 李继刚个人技能集（17技能） |
| dbskill/ | dontbesilent2025/dbskill | 商业诊断工具箱 |
| ClaWiser/ | MattWenJun/ClaWiser | Agent记忆与工作流增强 |
| marketing-skills/ | atypica-ai/marketing-skills | 市场调研/用户访谈/产品创新（6技能） |
| wechat-skills/ | gainubi/wechat-skills | 微信公众号写作四件套 |
| wechat_article_skills/ | BND-1/wechat_article_skills | 微信公众号写作与发布工具链 |
| markdown-proxy/ | joeseesun/markdown-proxy | URL转Markdown代理服务 |
| anything-to-md/ | 1596941391qq/anything-to-md | 万能文件转Markdown |
| James-Skills/ | James19890801/Skills | 简历生成与流程监控 |
| awesome-claude-code-subagents/ | VoltAgent/awesome-claude-code-subagents | Claude Code 子代理清单（curated list，无 SKILL.md） |
| awesome-agent-skills/ | heilcheng/awesome-agent-skills | Agent Skill 资源清单（curated list，无 SKILL.md） |

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
