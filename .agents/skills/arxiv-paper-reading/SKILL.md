---
name: arxiv-paper-reading
description: Read and analyze arXiv papers from ID or URL, convert papers to Markdown with arxiv2md API, and produce structured outputs for one-sentence contribution, problem background, method details, and critical analysis. Use when users ask to read, summarize, extract key points, dissect architecture/modules, or discuss strengths, limitations, and research impact of arXiv papers.
---

# Arxiv Paper Reading

## Overview

Fetch the paper as Markdown first, then answer with a fixed analysis structure: core contribution, background, method details, and critical thinking. Prioritize evidence from the paper text and keep claims grounded.

Default to detailed, high-resolution explanations unless the user explicitly asks for brevity.

## Response Style and Depth

- Write in the tone of a well-read professor: calm, precise, and explanatory rather than slogan-like.
- Keep language fluent and concrete; prefer mechanism-level explanations over vague summaries.
- For difficult concepts, use analogies to improve intuition, but use them sparingly and always map the analogy back to the exact technical object.
- Do not overuse bullet points. Prefer coherent paragraphs for reasoning, and use bullets only when list structure materially improves clarity (for example, side-by-side comparisons or explicit checklists).
- When uncertainty exists, state it clearly and explain what is known vs. unknown from the paper.

## Markdown Acquisition (Required First Step)

Always convert the paper to Markdown before analysis.

1. Normalize input to an arXiv identifier.
   - Example: `2509.16117` is the arXiv ID for `https://arxiv.org/abs/2509.16117`.
   - `abs`, `pdf`, and `html` URLs map to the same ID.
2. Use local conversion with `uvx` first:
  - `uvx --from arxiv2markdown arxiv2md <ARXIV_ID> --remove-refs -o {paper-title}-{arxiv-id}.md`

Preferred example:

```bash
uvx --from arxiv2markdown arxiv2md 2509.16117 --remove-refs -o title_2509.16117.md
```

Do not use python libraries or other tools for fetching/conversion to avoid inconsistencies. Prefer `uvx --from arxiv2markdown arxiv2md` for this step.

## Fallback Rules

- If `uvx` is unavailable or conversion fails, call arxiv2md API with `curl`:
  - `curl -s "https://arxiv2md.org/api/markdown?url=<ARXIV_ID>" > paper.md`
- Then read and analyze from `paper.md` directly.
- Example fallback command:
  - `curl -s "https://arxiv2md.org/api/markdown?url=2509.16117" > paper.md`

## Reading Workflow

1. Locate key sections in order: Abstract, Introduction, Method, Experiments, Limitations/Conclusion.
2. Extract explicit evidence lines for each claim before writing conclusions.
3. Distinguish paper claims from your own inference.
4. If a requested detail is missing, say it is not specified instead of guessing.

## Output Template

Use this exact section order unless the user asks otherwise.

### 1) 一句话核心贡献

- One sentence only.

### 2) 问题背景

- 要解决什么问题
- 之前方法的主要不足
- 作者为什么认为他们的方法可行

Cover each item with evidence-oriented explanation. Prefer short paragraphs; use bullets only if comparison becomes clearer.

### 3) 方法详解

- 模型架构
  - Backbone 是什么
  - 基于什么已有模型/范式改进
- 新增模块逐项拆解
  - 动机
  - 具体实现
  - 与原模型交互方式

For each module, prefer this format:
- 模块名
- 动机
- 实现
- 代价/复杂度影响

When writing, avoid turning every module into a flat checklist; start with a concise intuition paragraph, then provide the structured fields.

### 4) 批判性思考

- 最大亮点
- 局限性
- 可行改进方向
- 对 community 的价值与 high-level insight

Separate "paper-supported" and "your inference" when needed.

## Quality Bar

- Do not fabricate numbers, datasets, or ablation results.
- When citing performance, include metric + benchmark/task context.
- Mark uncertainty explicitly if table/figure parsing is ambiguous.
- Be detailed by default, with enough context that a graduate-level reader can follow the argument without reopening the paper.
