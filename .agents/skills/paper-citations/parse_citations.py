#!/usr/bin/env python3
"""
Parse Semantic Scholar citations API response and format output.

Usage:
    python3 parse_citations.py <input_file> [--format markdown|json|csv]

Output formats:
    - markdown: Pretty-printed list (default)
    - json: Raw JSON with structured data
    - csv: CSV with title,authors,year,venue,url
"""

import json
import sys
import csv
import re
from pathlib import Path


def extract_json(content: str) -> dict:
    """Extract valid JSON from potentially noisy response using jq or regex."""
    import subprocess
    try:
        result = subprocess.run(['jq', '.'], input=content, capture_output=True, text=True)
        if result.returncode == 0:
            return json.loads(result.stdout)
    except FileNotFoundError:
        pass
    
    match = re.search(r'\{.*"data":\s*\[', content, re.DOTALL)
    if match:
        start = match.start()
        try:
            return json.loads(content[start:])
        except json.JSONDecodeError:
            pass
    
    match = re.search(r'(\{"offset".*?\})\s*$', content, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    
    raise ValueError("Could not extract valid JSON from content")


def parse_citations(data: dict) -> list:
    """Parse API response into structured citation list."""
    citations = []
    for item in data.get('data', []):
        paper = item.get('citingPaper', {})
        authors = paper.get('authors', [])
        citations.append({
            'title': paper.get('title', 'N/A'),
            'authors': ', '.join([a['name'] for a in authors[:5]]) + ('...' if len(authors) > 5 else ''),
            'year': paper.get('year', 'N/A'),
            'venue': paper.get('venue', ''),
            'url': paper.get('url', ''),
            'citationCount': paper.get('citationCount', 0),
        })
    return citations


def format_markdown(citations: list) -> str:
    """Format citations as Markdown list."""
    lines = [f'## 共找到 {len(citations)} 篇引用论文\n']
    for i, c in enumerate(citations, 1):
        lines.append(f"{i}. **{c['title']}**")
        lines.append(f"   - Authors: {c['authors']}")
        lines.append(f"   - Year: {c['year']} | Venue: {c['venue'] or 'N/A'}")
        lines.append(f"   - URL: {c['url']}\n")
    return '\n'.join(lines)


def format_json(citations: list) -> str:
    """Format citations as JSON."""
    return json.dumps(citations, indent=2, ensure_ascii=False)


def format_csv(citations: list) -> str:
    """Format citations as CSV."""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['title', 'authors', 'year', 'venue', 'url', 'citationCount'])
    writer.writeheader()
    writer.writerows(citations)
    return output.getvalue()


def main():
    import argparse
    import io
    
    parser = argparse.ArgumentParser(description='Parse Semantic Scholar citations')
    parser.add_argument('input_file', help='Input JSON file from API')
    parser.add_argument('--format', choices=['markdown', 'json', 'csv'], default='markdown',
                       help='Output format (default: markdown)')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        content = f.read()
    
    data = extract_json(content)
    citations = parse_citations(data)
    
    if args.format == 'json':
        print(format_json(citations))
    elif args.format == 'csv':
        print(format_csv(citations))
    else:
        print(format_markdown(citations))


if __name__ == '__main__':
    main()
