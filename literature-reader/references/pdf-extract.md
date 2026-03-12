# PDF 文本提取指南

当 Cursor 内置 Read 工具无法正常读取 PDF（返回空内容、乱码、或严重截断）时，使用本指南中的备选方案提取文本。

## 前置条件

- Python 3.8+
- pdfplumber 库

安装依赖：

```bash
pip3 install pdfplumber
```

如果权限不足：

```bash
pip3 install --user pdfplumber
```

如果使用 conda：

```bash
conda install -c conda-forge pdfplumber
```

## 提取脚本

脚本路径：`~/.cursor/skills/literature-reader/scripts/extract_pdf.py`

### 基本用法

提取全文并输出到终端：

```bash
python3 ~/.cursor/skills/literature-reader/scripts/extract_pdf.py "/path/to/paper.pdf"
```

提取全文并保存到文件：

```bash
python3 ~/.cursor/skills/literature-reader/scripts/extract_pdf.py "/path/to/paper.pdf" --output /tmp/paper_text.txt
```

预期输出：`Extracted text saved to: /tmp/paper_text.txt`

保存后使用 Read 工具读取提取结果：

```
Read tool → path: "/tmp/paper_text.txt"
```

### 指定页码范围

只提取第 1-5 页：

```bash
python3 ~/.cursor/skills/literature-reader/scripts/extract_pdf.py "/path/to/paper.pdf" --pages 1-5
```

只提取第 3 页：

```bash
python3 ~/.cursor/skills/literature-reader/scripts/extract_pdf.py "/path/to/paper.pdf" --pages 3
```

### 完整参数列表

| 参数 | 缩写 | 说明 | 默认值 |
|------|------|------|--------|
| `pdf_path` | — | PDF 文件路径（必填） | — |
| `--output` | `-o` | 输出文件路径 | stdout |
| `--pages` | `-p` | 页码范围，如 `1-5` 或 `3` | 全部页面 |

## 提取能力说明

脚本基于 pdfplumber，具备以下能力：

- **正文提取**：逐页提取文本，按 `--- Page X/Y ---` 分隔
- **表格提取**：自动识别页面中的表格并转为 Markdown 格式，标注为 `[Table N on Page X]`
- **路径支持**：支持 `~` 展开和相对路径自动解析

## 判断何时使用本方案

按以下顺序尝试，优先使用 Read 工具：

1. **先用 Read 工具**：`Read tool → path: "/path/to/paper.pdf"` — 大多数 PDF 可以正常读取
2. **Read 返回空或乱码** → 使用本脚本提取
3. **本脚本也无法提取**（扫描件/纯图片 PDF）→ 告知用户需要先用 OCR 工具转换

### 常见需要本方案的场景

- 扫描件 PDF（图片嵌入型，Read 工具无法解析）
- 复杂排版 PDF（多栏、大量公式、特殊字体）
- 加密或受保护的 PDF（Read 工具可能无法处理）
- Read 工具提取后丢失表格结构

## 故障排查

### 错误：`pdfplumber not installed`

```
Error: pdfplumber not installed. Run: pip3 install pdfplumber
```

解决：执行 `pip3 install pdfplumber`，确认安装的 Python 环境与运行脚本的是同一个。

### 错误：`File not found`

```
Error: File not found: /path/to/paper.pdf
```

解决：检查文件路径是否正确，注意空格需要用引号包裹。

### 提取结果为空

原因：PDF 为纯图片扫描件，不含可提取的文本层。
解决：告知用户需要先用 OCR 工具（如 Adobe Acrobat、Tesseract）将扫描件转为可搜索 PDF，再重新提取。

### 表格提取不完整

原因：pdfplumber 对复杂合并单元格的表格支持有限。
解决：手动查看原始 PDF 中的表格，补充缺失数据到概要中。
