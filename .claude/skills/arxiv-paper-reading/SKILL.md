---
name: arxiv-paper-reading
description: Read and analyze arXiv papers from ID or URL, convert papers to Markdown with arxiv2md API, and produce structured outputs for one-sentence contribution, problem background, method details, and critical analysis. Use when users ask to read, summarize, extract key points, dissect architecture/modules, or discuss strengths, limitations, and research impact of arXiv papers.
---

# Arxiv Paper Reading

## Overview

Fetch the paper as Markdown first, then answer with a fixed analysis structure: core contribution, background, method details, and critical thinking. Prioritize evidence from the paper text and keep claims grounded.

## Markdown Acquisition (Required First Step)

Always convert the paper to Markdown before analysis.

1. Normalize input to an arXiv identifier.
   - Example: `2509.16117` is the arXiv ID for `https://arxiv.org/abs/2509.16117`.
   - `abs`, `pdf`, and `html` URLs map to the same ID.
2. Call arxiv2md API:
   - `curl -s "https://arxiv2md.org/api/markdown?url=<ARXIV_ID> > {paper-title}-{arxiv-id}.md`

Preferred example:

```bash
curl -s "https://arxiv2md.org/api/markdown?url=2509.16117" > title_2509.16117.md
```

Do not use python libraries or other tools for fetching/conversion to avoid inconsistencies. Always rely on `curl` and the arxiv2md API for this step.

## Fallback Rules

- If API output is empty, malformed, or unavailable, use local conversion:
  - `uvx --from arxiv2markdown arxiv2md <ARXIV_ID> --remove-refs -o paper.md`
- Then read and analyze from `paper.md` directly.
- Example fallback command:
  - `uvx --from arxiv2markdown arxiv2md 2509.16117 --remove-refs -o paper.md`

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

Write each as 2-4 bullet points with evidence-oriented wording.

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
- Keep concise by default, expand only when user asks for deep dive.
