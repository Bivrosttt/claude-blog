# claude-blog - AI Blog Creation Skill for Claude Code

![Claude Blog - AI-Powered Blog Creation](assets/header.jpeg)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skills-Compatible-blue)](https://agentskills.io)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-blog?label=public%20release)](https://github.com/AgriciDaniel/claude-blog/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/AgriciDaniel/claude-blog/ci.yml?branch=main&label=public%20CI)](https://github.com/AgriciDaniel/claude-blog/actions)
[![Community](https://img.shields.io/badge/AI%20Marketing%20Hub-Pro%20community-purple)](https://www.skool.com/ai-marketing-hub-pro)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)
![Sub-Skills](https://img.shields.io/badge/Sub--Skills-30-orange)

> **Two versions of this skill.** Choose the one that fits how you work:
>
> - 🌐 **Public open-source**: [`AgriciDaniel/claude-blog`](https://github.com/AgriciDaniel/claude-blog). MIT-licensed, public releases, open to anyone. Use this if you want the stable, downloadable, no-membership-required version.
> - 🔒 **Community private mirror** (this repo): [`AI-Marketing-Hub/claude-blog`](https://github.com/AI-Marketing-Hub/claude-blog). Early access to in-development work (v1.9.0+ Blog Delivery Contract, hero ladder, mutation-tested regression coverage), and direct collaboration with the [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) community. Requires membership.
>
> The badges above track the **public** repo (`AgriciDaniel/claude-blog`) since the private mirror isn't visible to shields.io. The publishing workflow (private dev → review → public release) is documented in [`docs/PUBLISHING.md`](docs/PUBLISHING.md).

> **Blog:** [See how claude-blog works](https://agricidaniel.com/blog/claude-code-blog-writer)

claude-blog is a Claude Code skill ecosystem for creating, optimizing, and managing blog content at scale. It generates complete articles, briefs, calendars, and schemas, dual-optimized for Google rankings and AI citation platforms (ChatGPT, Perplexity, AI Overviews).

## Table of Contents

- [Demo](#demo)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Integration](#integration)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Demo

[Watch the Demo on YouTube](https://www.youtube.com/watch?v=AeLC4iutG8w)

![Blog commands demo](assets/blog-command-demo.gif)

---

## Quick Start

> ℹ️ **Which version are you installing?**
>
> - **Not an AI Marketing Hub Pro member?** Install from the public repo instead: [`AgriciDaniel/claude-blog`](https://github.com/AgriciDaniel/claude-blog). All the install commands below work there too. Just swap `AI-Marketing-Hub/claude-blog` for `AgriciDaniel/claude-blog` and the plugin slug `claude-blog@ai-marketing-hub-claude-blog` for `claude-blog@agricidaniel-claude-blog`. Public releases ship there; this private mirror runs ahead of public releases.
> - **Pro member?** The commands below install the **community version** with early access to in-development features. They require an authenticated `gh auth login` (or GitHub PAT) session with access to the `AI-Marketing-Hub` org. If `/plugin marketplace add` fails with a 404, your account isn't in the org yet. DM in the [Skool community](https://www.skool.com/ai-marketing-hub-pro) to get added.

**Plugin Install (Claude Code 1.0.33+):**

```bash
# Add marketplace (one-time)
/plugin marketplace add AI-Marketing-Hub/claude-blog

# Install plugin
/plugin install claude-blog@ai-marketing-hub-claude-blog
```

**Recommended: clone then verify before installing** (lets you inspect
install.sh and pin a release tag, closing audit VULN-005):

```bash
git clone https://github.com/AI-Marketing-Hub/claude-blog.git
cd claude-blog
git checkout v1.9.0          # pin to a release tag (latest as of 2026-05-18)
chmod +x install.sh && ./install.sh
```

**One-Command Install (Unix/macOS):**

```bash
curl -fsSL https://raw.githubusercontent.com/AI-Marketing-Hub/claude-blog/main/install.sh | bash
```

**One-Command Install (Windows PowerShell):**

```powershell
irm https://raw.githubusercontent.com/AI-Marketing-Hub/claude-blog/main/install.ps1 | iex
```

> Note: piping curl/irm to a shell gives the script execution authority on your
> machine. The clone-then-checkout-tag flow above is safer because you
> can inspect what runs. Both flows authenticate against the private repo using
> your existing `gh auth` / GitHub credentials.

Restart Claude Code after installation to activate.

## Commands
![Blog write command demo](assets/blog-write-demo.gif)
| Command | Description |
|---------|-------------|
| `/blog write <topic>` | Write a new blog post from scratch |
| `/blog rewrite <file>` | Optimize an existing blog post |
| `/blog analyze <file>` | Quality audit with 0-100 score |
| `/blog brief <topic>` | Generate a detailed content brief |
| `/blog calendar` | Generate an editorial calendar |
| `/blog strategy <niche>` | Blog strategy and topic ideation |
| `/blog outline <topic>` | SERP-informed content outline |
| `/blog seo-check <file>` | Post-writing SEO validation |
| `/blog schema <file>` | Generate JSON-LD schema markup |
| `/blog repurpose <file>` | Repurpose for social, email, YouTube |
| `/blog geo <file>` | AI citation readiness audit |
| `/blog image [generate\|edit\|setup]` | AI image generation via Gemini |
| `/blog audit [directory]` | Full-site blog health assessment |
| `/blog cannibalization [directory]` | Detect keyword overlap across posts |
| `/blog factcheck <file>` | Verify statistics against cited sources |
| `/blog persona [create\|list\|apply]` | Manage writing personas and voice profiles |
| `/blog taxonomy [sync\|audit\|suggest]` | Tag/category CMS management |
| `/blog notebooklm <question>` | Query NotebookLM for source-grounded research |
| `/blog audio [generate\|voices\|setup]` | Generate audio narration via Gemini TTS |
| `/blog google [command] [args]` | Google API data: PSI, CrUX, GSC, GA4, NLP, YouTube, Keywords |
| `/blog cluster [plan\|execute] <seed>` | Semantic topic-cluster planning + execution (hub-and-spoke) |
| `/blog multilingual <topic> --languages <codes>` | Write + translate + localize + emit hreflang in one command |
| `/blog translate <file> --to <codes>` | SEO-optimized translation with format preservation |
| `/blog localize <file> --locale <code>` | Cultural deep-adaptation per locale |
| `/blog locale-audit <directory>` | Multilingual content QA (completeness, hreflang, parity, freshness) |
| `/blog flow [find\|optimize\|win\|prompts\|sync]` | FLOW framework prompts (evidence-led, 30 blog-applicable) |
| `/blog brand [init\|show\|update]` | Generate BRAND.md + VOICE.md context auto-loaded by all sub-skills (v1.8.0) |
| `/blog discourse <topic>` | API-free last-30-days discourse research; produces DISCOURSE.md (v1.8.0) |

> **30 sub-skill directories total**: 29 user-invokable (28 distinct slash commands above + `/blog update` aliased to rewrite) + 1 internal-only (`blog-chart`, invoked by blog-write/blog-rewrite for inline SVG charts). `blog-image` is user-invokable AND callable internally. v1.7.0 added `blog-cluster`, `blog-multilingual`, `blog-translate`, `blog-localize`, `blog-locale-audit`, and `blog-flow`. v1.8.0 added `blog-brand` and `blog-discourse`. v1.9.0 adds the 5-gate Blog Delivery Contract (see Architecture section below).

### Foundational methodologies (v1.8.0 references)

Five reference documents under `skills/blog/references/` define the editorial and research methodology applied across all sub-skills. They are loaded on demand by the orchestrator when relevant:

| Reference | Purpose | Used by |
|---|---|---|
| `ai-slop-detection.md` | Two-tier first-order (phrases) + second-order (structural rhythm) AI-content detection | `blog-rewrite`, `blog-reviewer`, `blog-analyze` |
| `editorial-heuristics.md` | 10 Nielsen-adapted editorial heuristics with 0-4 ordinal scoring + P0-P3 severity tagging | `blog-analyze --rubric` |
| `cognitive-load.md` | Per-section concept-density model (entities, numerics, jargon, forward refs, clause depth) | `blog-analyze --cognitive-load`, `scripts/cognitive_load.py` |
| `research-quality.md` | 5-dimension research rubric + 4 pre-flight keyword-trap classes + named-entity decomposition + cross-source clustering + 30/90-day freshness floors | `blog-researcher`, `blog-discourse`, `blog-brief`, `blog-strategy` |
| `synthesis-contract.md` | 6 LAWs governing research-synthesis output (no trailing Sources block, no invented titles, no em-dashes, no raw cluster dumps, inline `[name](url)` citations, discrete claims) | All research-synthesis sub-skills |

Adapted from `pbakaus/impeccable` (Apache 2.0) and `mvanhorn/last30days-skill` (MIT). See `CONTRIBUTORS.md` for the full attribution.

### Delivery contract (v1.9.0)

Every blog passes a 5-gate contract before being shown to the user. The user is never the first reviewer; the gates are.

| Gate | Enforces | Implementation |
|---|---|---|
| 1. Capability Discovery | Required tools and agents present before write | `scripts/blog_preflight.py --gate 1` |
| 2. Format Completeness | `.md` + `.html` + `.pdf` + real hero image | `scripts/blog_render.py`, `scripts/generate_hero.py` |
| 3. Visual Verification | No SVG overflow, valid JSON-LD, dark mode works | `patchright` at 3 viewport widths |
| 4. Content Review (BLOCKING) | `blog-reviewer` score 90+ AND zero P0 issues | `agents/blog-reviewer.md` (now blocking) |
| 5. Asset + Link Integrity | Every img resolves, og:image exists, links return 200 | `scripts/blog_preflight.py --gate 5` |

Hero image ladder: Banana MCP, direct Gemini API, premium stock (Unsplash, Pexels, Pixabay), Openverse public API. First available wins. Block-and-iterate up to 3 times on any gate failure before escalating to the user. Full spec: `skills/blog/references/blog-delivery-contract.md`.

## Features

### 12 Content Templates
Auto-selected based on topic and intent: how-to guide, listicle, case study, comparison, pillar page, product review, thought leadership, roundup, tutorial, news analysis, data research, FAQ knowledge base.

### 5-Category Quality Scoring (100 Points)
| Category | Points | Focus |
|----------|--------|-------|
| Content Quality | 30 | Depth, readability, originality, engagement |
| SEO Optimization | 25 | Headings, title, keywords, links, meta |
| E-E-A-T Signals | 15 | Author, citations, trust, experience |
| Technical Elements | 15 | Schema, images, speed, mobile, OG tags |
| AI Citation Readiness | 15 | Citability, Q&A format, entity clarity |

Scoring bands: Exceptional (90-100), Strong (80-89), Acceptable (70-79), Below Standard (60-69), Rewrite (<60).

### AI Content Detection
Burstiness scoring, known AI phrase detection (17 phrases), vocabulary diversity analysis (TTR). Flags content that reads as AI-generated.

### Persona-Driven Writing
Configurable writing personas with NNGroup 4-dimension tone framework. Manage voice profiles per blog or author, with readability bands (Consumer/Professional/Technical) and style enforcement.

### Fact-Checking Pipeline
Statistics verification that fetches cited source URLs and scores claim confidence (exact match, paraphrase, not found). Ensures every data point in your content is accurate and traceable.

### Keyword Cannibalization Detection
Identifies keyword overlap across blog posts using local grep analysis or DataForSEO API. Severity scoring with merge/differentiate recommendations to prevent posts from competing against each other.

### CMS Taxonomy Management
Tag and category management supporting WordPress REST, Shopify GraphQL, Ghost, Strapi, and Sanity. Includes tag suggestion, sync, and audit workflows.

### Dual Optimization
Every article targets both Google rankings and AI citation platforms:
- **Google**: December 2025 Core Update compliance, E-E-A-T, schema markup, internal linking
- **AI Citations**: Answer-first formatting, citation capsules, passage-level citability, FAQ schema

### Visual Media
- Pixabay/Unsplash/Pexels image sourcing with alt text
- AI image generation via Gemini (hero images, inline illustrations, social cards), optional, requires free Google AI API key
- Built-in SVG chart generation (bar, grouped bar, lollipop, donut, line, area, radar)
- YouTube video embedding with srcdoc lazy loading, noscript AI crawler fallback, and quality scoring
- Image density targets by content type
- Image URL verification (HTTP 200 check before embedding)

### Google API Integration (NEW in v1.6.5)
13 commands across 4 credential tiers, all free at normal usage:
- **Tier 0** (API key): PageSpeed Insights, CrUX Core Web Vitals (25-week history), YouTube video search, NLP entity analysis
- **Tier 1** (OAuth): Search Console performance, URL Inspection, Indexing API
- **Tier 2** (GA4): Organic traffic reports
- **Tier 3** (Ads): Google Ads Keyword Planner

### NotebookLM Research
Query Google NotebookLM for source-grounded research from user-uploaded documents. Tier 1 data quality with zero hallucination risk.

### Audio Narration
Generate audio narration via Gemini TTS. Three modes: summary (200-300 words), full article, and two-speaker dialogue. 30 voices, 80+ languages.

### Platform Support
Next.js/MDX, Astro, Hugo, Jekyll, WordPress, Ghost, 11ty, Gatsby, and static HTML.

## Architecture

```
claude-blog/
├── .claude-plugin/
│   └── plugin.json                     # Plugin metadata (name, description, author)
├── skills/
│   ├── blog/                           # Main orchestrator
│   │   ├── SKILL.md                    # Routes all 29 user-facing commands (28 distinct + `/blog update` alias)
│   │   ├── references/                 # 21 on-demand reference docs (5 new in v1.8.0, 1 new in v1.9.0)
│   │   └── templates/                  # 12 content type templates
│   ├── blog-write/SKILL.md            # Sub-skills (29 user-invokable + 1 internal-only blog-chart)
│   ├── blog-rewrite/SKILL.md
│   ├── blog-analyze/SKILL.md
│   ├── blog-brief/SKILL.md
│   ├── blog-calendar/SKILL.md
│   ├── blog-strategy/SKILL.md
│   ├── blog-outline/SKILL.md
│   ├── blog-seo-check/SKILL.md
│   ├── blog-schema/SKILL.md
│   ├── blog-repurpose/SKILL.md
│   ├── blog-geo/SKILL.md
│   ├── blog-audit/SKILL.md
│   ├── blog-chart/SKILL.md            # Internal: SVG chart generation
│   ├── blog-image/                    # AI image generation via Gemini
│   │   ├── SKILL.md
│   │   ├── references/                # 3 reference docs (models, tools, prompts)
│   │   └── scripts/                   # MCP setup and validation scripts
│   ├── blog-cannibalization/SKILL.md  # Keyword overlap detection
│   ├── blog-factcheck/SKILL.md        # Statistics verification
│   ├── blog-persona/SKILL.md          # Writing persona management
│   ├── blog-taxonomy/SKILL.md         # CMS taxonomy management
│   ├── blog-notebooklm/              # NotebookLM source-grounded research
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/                   # 10 Python scripts + venv wrapper
│   ├── blog-audio/                    # Audio narration via Gemini TTS
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/                   # 5 Python scripts + venv wrapper
│   └── blog-google/                   # Google API integration (NEW v1.6.5)
│       ├── SKILL.md                   # 13 commands, 4 credential tiers
│       ├── references/                # 3 reference docs (auth, API, quotas)
│       ├── scripts/                   # 11 Google API scripts + venv wrapper
│       └── assets/templates/          # 3 report templates
├── agents/                             # 5 specialized agents
│   ├── blog-researcher.md
│   ├── blog-writer.md
│   ├── blog-seo.md
│   ├── blog-reviewer.md
│   └── blog-translator.md             # v1.7.0; runs without Bash for blast-radius safety
├── scripts/
│   ├── analyze_blog.py                 # Python quality analysis (5-category scoring)
│   ├── blog_preflight.py               # 5-gate delivery contract runner (v1.9.0)
│   ├── blog_render.py                  # md -> html -> pdf renderer with XSS-safe JSON-LD (v1.9.0)
│   ├── cognitive_load.py               # Per-section concept-density analyzer (v1.8.0)
│   ├── discourse_research.py           # Discourse brief synthesis from SERP JSON (v1.8.0)
│   ├── generate_hero.py                # Hero image ladder: Banana -> Gemini -> stock -> Openverse (v1.9.0)
│   ├── load_untrusted_root.py          # Code-enforced BRAND/VOICE/DISCOURSE fencing helper (v1.8.3)
│   ├── lint_prose.py                   # CI prose-hygiene linter (v1.8.4; fence-aware)
│   └── sync_flow.py                    # FLOW reference sync (stdlib, sandboxed)
├── tests/                              # pytest test suite (160 tests, 0 skips)
│   ├── conftest.py
│   ├── test_analyze_blog.py
│   ├── test_blog_delivery_contract.py  # v1.9.0 (XSS / symlink / frontmatter mutation-verified)
│   ├── test_cognitive_load.py          # v1.8.0
│   ├── test_command_coherence.py       # v1.8.5 (SKILL.md <-> COMMANDS.md command-set parity)
│   ├── test_discourse_research.py      # v1.8.0
│   ├── test_installer_sync.py          # v1.8.6 (every scripts/*.py shipped + removed)
│   ├── test_lint_prose.py              # v1.8.4 (fence-aware prose-hygiene tests)
│   ├── test_load_untrusted_root.py     # v1.8.3 (behavioral nonce + sanitize tests)
│   ├── test_security_guardrails.py
│   ├── test_security_v1_8_0.py         # v1.8.0 (path traversal + DoS + contract regression)
│   └── test_version_coherence.py       # v1.8.5 (pyproject / plugin.json / CITATION / SKILL.md aligned)
├── docs/                               # 8 documentation files
├── .github/workflows/ci.yml           # CI pipeline
├── install.sh                          # Unix/macOS installer (fallback)
├── install.ps1                         # Windows PowerShell installer
├── pyproject.toml                      # Python project config
├── requirements.txt                    # Python dependencies
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed and configured
- Python 3.11+ (for `analyze_blog.py` quality scoring script)
- Optional: `pip install -r requirements.txt` for advanced analysis (readability scoring, schema detection)

### Quality Gates (CI-enforced on every PR)

1. **pytest**: 160 tests across security, behavioral, regression, and delivery-contract suites
2. **Plugin validation**: `claude plugin validate .` (when CLI available) + hand-rolled JSON/regex checks
3. **Stale-path lint**: catches drift in `references/` and `templates/` cross-references
4. **Prose hygiene**: `scripts/lint_prose.py` (fence-aware, backtick-aware) enforces CONTRIBUTING.md no-em-dash / no-en-dash / no-` -- ` rule
5. **Version coherence**: `tests/test_version_coherence.py` asserts pyproject.toml / plugin.json / CITATION.cff / `skills/blog/SKILL.md` frontmatter all match
6. **Command coherence**: `tests/test_command_coherence.py` asserts `skills/blog/SKILL.md` and `docs/COMMANDS.md` declare the same `/blog X` command set

Run locally before pushing:
```bash
python -m pytest tests/
python3 scripts/lint_prose.py
claude plugin validate .
```

## Uninstall

Unix/macOS:
```bash
chmod +x uninstall.sh && ./uninstall.sh
```

Windows (PowerShell):
```powershell
.\uninstall.ps1
```

## Integration

Chart generation and YouTube video embedding are built-in. Google API data requires a free API key (see `/blog google setup`).

**Optional companion skills** (for deeper analysis of published pages):

| Skill | Integration |
|-------|-------------|
| `/seo` | Deep SEO analysis of published blog pages |
| `/seo-schema` | Schema markup validation and generation |
| `/seo-geo` | AI citation optimization audit |
| `/seo-google` | Google API data (shared config with blog-google) |

## Documentation

Detailed documentation is available in [docs/](docs/):

- [Installation Guide](docs/INSTALLATION.md): Unix, macOS, Windows, manual install
- [Command Reference](docs/COMMANDS.md): Full command reference with examples
- [Architecture](docs/ARCHITECTURE.md): System design and component overview
- [Publishing Workflow](docs/PUBLISHING.md): Private-to-public release flow (Pro maintainers)
- [Templates](docs/TEMPLATES.md): Template reference and customization
- [Troubleshooting](docs/TROUBLESHOOTING.md): Common issues and fixes
- [MCP Integration](docs/MCP-INTEGRATION.md): Optional MCP server setup

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Built by [AgriciDaniel](https://github.com/AgriciDaniel) with Claude Code.

---

## Publishing Platform

For a full GUI-based content publishing workflow, see [Rankenstein](https://rankenstein.pro) - research to publish in one platform.

---

## Author

Built by [Agrici Daniel](https://agricidaniel.com/about) - AI Workflow Architect.

- [Blog](https://agricidaniel.com/blog) - Deep dives on AI marketing automation
- [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) - Free community, 2,800+ members
- [YouTube](https://www.youtube.com/@AgriciDaniel) - Tutorials and demos
- [All open-source tools](https://github.com/AgriciDaniel)
