# Bivrosttt SEO extension

This repository is the Bivrosttt organization fork of [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog). The upstream `claude-blog` suite remains available under its MIT license. Bivrosttt adds two separate skills: `seo-keyword-research` for research and `free-tool-seo` for free-tool planning, implementation, and audits.

## Research coverage

`claude-blog` already includes research-oriented skills and agents:

- `blog-researcher`: current statistics, sources, SERP gaps, and image research.
- `blog-brief`, `blog-outline`, and `blog-strategy`: search intent, briefs, outlines, and positioning.
- `blog-cluster`: semantic topic clusters and hub-and-spoke planning.
- `blog-google`: Google Search Console, GA4, PageSpeed, YouTube, and keyword-related API workflows when credentials are configured.
- `blog-factcheck`, `blog-cannibalization`, `blog-seo-check`, `blog-audit`, and `blog-geo`: evidence, overlap, on-page SEO, site health, and AI-citation checks.

The upstream suite is broad, but it is not a Japanese free-keyword collection CLI that works without paid credentials. `seo-keyword-research` fills that research gap:

- Google, Bing, and YouTube suggestion collection through the repository's manual SEO workflow.
- Optional Rakkokeyword API support through `scripts/rakko_keyword.py`.
- Browser fallback guidance for `https://rakkokeyword.com/` when no API key is available.
The separate `free-tool-seo` skill consumes that research packet and focuses on:

- Free-tool page specifications, AMIX-style page structure, internal links, privacy language, and service CTAs.
- Browser-local implementation, accessibility, responsive behavior, and tool/page audits.
- AI顧問室's local factory loop when used inside a repository containing `seo/config.json`.

## Install the Bivrosttt extension

To install the research skill into Codex:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Bivrosttt/claude-blog \
  --path skills/seo-keyword-research
```

To install the free-tool implementation skill:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Bivrosttt/claude-blog \
  --path skills/free-tool-seo
```

The upstream blog skills can be installed from the same repository by selecting the directories under `skills/`, or the full repository can be used as a Claude Code plugin. Never commit `RAKKO_KEYWORD_API_KEY`; the script reads it from the environment and never prints it.

## Attribution

Upstream source: [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog). Keep the upstream `LICENSE`, `NOTICE`, and attribution when redistributing or updating the fork.
