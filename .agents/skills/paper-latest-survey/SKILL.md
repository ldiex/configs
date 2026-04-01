---
name: paper-latest-survey
description: Survey the latest follow-up work for a target paper by first retrieving recent citations, listing the newest 20 cited papers for user selection, then reading the selected papers and summarizing their directions and how they extend the original paper. Use when the user asks things like "调研一下某篇 paper 的最新工作", "看看这篇论文最近有哪些 follow-up", "列出这篇论文最新 citations 并帮我读几篇", or wants a citation-driven literature update around a seed paper.
---

# Paper Latest Survey

## Overview

Use this skill to turn a seed paper into a citation-driven mini survey.
Always first gather recent citing papers, then let the user choose what to read, and only after selection analyze the chosen papers in relation to the seed paper.

## Workflow

### 1. Normalize the seed paper

Extract the seed paper identifier from the user request.
Accept arXiv URL, arXiv id, DOI, or Semantic Scholar id.
If the paper is an arXiv paper, normalize it to the bare arXiv id for reading and to `ARXIV:{id}` for citation lookup.

### 2. Retrieve citations first

Invoke the `paper-citations` skill first.
Use it to fetch citation papers for the seed paper.
Prefer the newest papers by publication date when available; otherwise sort by year descending and keep recent results first.

If no citations are found, tell the user there are no indexed citations yet and stop.

### 3. Present the newest 20 papers for selection

From the citation list, produce a shortlist of at most 20 newest papers.
For each paper, include:
- index number
- title
- year or publication date
- arXiv id or URL if available
- one short phrase on the apparent topic if inferable from title

Then ask the user which papers they want to read.
Support selection by:
- index numbers
- title fragments
- "top k"
- all papers in the shortlist

Do not read papers before the user selects them unless the user explicitly asks for automatic reading.

### 4. Read selected papers

For every selected arXiv paper, invoke the `arxiv-paper-reading` skill.
If a selected citation is not on arXiv, say that this workflow currently reads arXiv papers directly and ask whether to skip it or replace it with another shortlisted paper.

When multiple selected papers are available, read them one by one and keep notes on:
- core problem
- key method idea
- main claimed gain
- relation to the seed paper

### 5. Synthesize the mini survey

After reading the selected papers, summarize them in two layers.

First give a per-paper summary using this compact structure:
- 论文
- 方向
- 相比原论文的发展点
- 核心方法变化
- 值得注意的局限或不确定点

Then provide a cross-paper synthesis:
- 这些 follow-up work 可以分成哪些方向
- 每个方向相对原论文在解决什么新问题
- 整体趋势是什么
- 哪些方向最值得继续读

Always distinguish paper-supported claims from your own inference when the relation is not explicitly stated by the citing paper.

## Output pattern

When showing the shortlist, use a concise numbered list.
When summarizing selected papers, keep each paper to a short block, then end with a grouped trend summary.

## Guardrails

Do not fabricate citation metadata.
Do not assume every citation is truly technically relevant; some may be only loosely connected.
If the citation list contains obviously unrelated papers, mention that relevance is based on citation indexing plus title-level inspection unless the paper was actually read.
If publication date and year disagree, prefer the more specific publication date.
