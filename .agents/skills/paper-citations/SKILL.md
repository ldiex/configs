---
name: paper-citations
description: Get all citation papers for a specific paper using the Semantic Scholar Graph API. Use this skill when a user asks to find, list, or export papers that cite a specific paper (via arXiv ID, DOI, Semantic Scholar ID, etc.).
---

# Paper Citations

## Overview

This skill enables Codex to retrieve the complete list of papers that cite a specific target paper (Citations) using the Semantic Scholar Graph API. It handles pagination automatically to ensure all citing papers are retrieved, even for highly cited works.

## Workflow: Retrieving Citations

When a user asks for papers that cite a specific paper, follow these steps:

### Step 1: Identify the Paper ID
Extract the paper identifier from the user's request. Semantic Scholar supports several formats. You must format the ID correctly:
- **ArXiv ID**: `ARXIV:{id}` (e.g., `ARXIV:2509.16117`)
- **DOI**: `10.{id}` (e.g., `10.1038/nrn3241`)
- **Semantic Scholar ID**: `{40-character hex string}`
- **MAG ID**: `MAG:{id}`
- **ACL ID**: `ACL:{id}`
- **PubMed ID**: `PMID:{id}`
- **Corpus ID**: `CorpusID:{id}`

### Step 2: Fetch Citations using the API
Use the `bash` tool with `curl` to call the Semantic Scholar API.

**Endpoint**: `GET https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations`

**Required Query Parameters**:
- `fields`: Comma-separated list of fields. Always request at least: `title,authors,year,url`. Other useful fields: `venue,citationCount,abstract,isOpenAccess`.
- `limit`: Set to `1000` (the maximum allowed) to minimize API calls.
- `offset`: Start at `0`.

**Bash Command Example**:
```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2509.16117/citations?fields=title,authors,year,url&limit=1000&offset=0"
```

### Step 3: Handle Pagination (If necessary)
Analyze the JSON response from the API.
- The response will contain a `data` array and an `offset` integer.
- If the length of the `data` array is exactly equal to your `limit` (e.g., 1000), there are likely more citations to fetch.
- To get the next page, make another API call by increasing the `offset` parameter by the `limit` (e.g., `offset=1000`, then `offset=2000`).
- Repeat this process until the returned `data` array is empty or smaller than the `limit`.

### Step 4: Parse and Format Results
Use the included `parse_citations.py` script to parse API responses and format output:

```bash
# Save and parse in one step using grep to extract JSON
curl -s "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2509.16117/citations?fields=title,authors,year,url,venue&limit=1000&offset=0" \
  | grep -o '{"offset".*}' \
  | python3 <skill_dir>/parse_citations.py /dev/stdin --format markdown
```

**Available formats:**
- `markdown` (default): Pretty-printed list with title, authors, year, venue, URL
- `json`: Structured JSON array
- `csv`: CSV with headers

## Handling Errors
- **404 Not Found**: The paper ID is incorrect or not found in Semantic Scholar's database. Check the prefix (e.g., ensure `ARXIV:` is capitalized) and ID format.
- **429 Too Many Requests**: Semantic Scholar has strict rate limits for unauthenticated requests. If this happens, wait a few seconds before trying again, or ask the user if they have an API key. (If they do, append it via the header `-H "x-api-key: YOUR_KEY"`).
