---
name: free-tool-seo
description: Research keywords, design AMIX-style free-tool SEO clusters, and build or audit browser-based utility pages with explanatory content, internal links, and appropriate service CTAs. Use when planning a large free-tool library, analyzing a tool-SEO competitor, researching search intent, or implementing an SEO landing/tool page.
---

# Free Tool SEO

Use this skill to turn small, useful browser tools into a coherent search-acquisition system. Model the information architecture and decision logic; do not copy another site's text, visual assets, branding, or code.

## Workflow

### 1. Inspect the reference and the current product

Start from real pages, not assumptions. For each representative page, record:

- page title, meta description, canonical URL, indexability signals, and primary keyword;
- the tool UI and whether processing is local or server-side;
- the heading tree and the explanation blocks after the tool;
- FAQ, limitations, privacy/security claims, related-tool links, service links, and global footer links;
- mobile behavior, load cost, dependencies, and the primary conversion path.

Use `agent-browser` when a live page must be read or interacted with. Use `rg --files` and the actual project files when auditing a local implementation. Treat observed facts and hypotheses as separate fields in the report.

### 2. Research the keyword before designing a tool

Use this order:

1. Start with a small set of seed problems stated in the user's language (for example, `画像を軽くしたい`, not only `画像圧縮`).
2. Collect Google suggestions, related keywords, LSI/PAA questions, and—when the idea is already validated—competitor headings and co-occurring terms.
3. Add search volume and SEO difficulty only when the data source is available; label stale or estimated metrics instead of presenting them as facts.
4. Normalize and deduplicate variants, then group by one search intent and one tool job per candidate page.
5. Score candidates on problem urgency, tool feasibility, search-intent clarity, likely repeat use, service fit, and implementation/maintenance cost. Prioritize a small cluster that can be shipped and internally linked, not a vanity list of keywords.

#### Rakkokeyword API path

If `RAKKO_KEYWORD_API_KEY` is available, run the bundled script. It uses the official API and never prints the key:

```bash
python3 /Users/koki/.codex/skills/free-tool-seo/scripts/rakko_keyword.py \
  --keyword '業務改善' --mode bundle --pretty > /tmp/業務改善-keywords.json
```

Use a single mode when only one signal is needed:

```bash
python3 /Users/koki/.codex/skills/free-tool-seo/scripts/rakko_keyword.py \
  --keyword '画像圧縮' --mode suggest --modes google, youtube --limit 200
```

The API uses `https://api.rakkokeyword.com`, `X-API-Key`, and POST endpoints such as `/v1/suggest-keywords`, `/v1/related-keywords`, `/v1/other-keywords`, `/v1/headline`, and `/v1/co-occurrence`. API access requires an eligible plan and is for internal use under the provider's terms. Do not commit the key, put it in HTML, or expose it in browser JavaScript. Do not run the `bundle` mode casually: the provider charges credits per endpoint.

#### Browser fallback

If there is no API key or the API is unavailable, use the browser with the user's existing session:

1. Open `https://rakkokeyword.com/`.
2. Enter the seed in the search box and choose `サジェストキーワード（Google）`; capture the result URL and visible results.
3. Repeat with `関連キーワード`, `潜在的な検索キーワード/質問（LSI/PAA）`, and, where useful, `見出し抽出` and `共起語`.
4. Use the site's free tier only within its visible limits. Never bypass login, rate limits, paywalls, robots, or anti-abuse controls.
5. Save the raw result (URL, date, mode, seed, and visible rows) before summarizing. Mark browser-collected metrics as observed on that date.

Prefer official APIs or exported results over scraping private endpoints. If browser automation is needed, follow the `agent-browser` skill's open → snapshot → interact → re-snapshot loop.

### 3. Turn the research into a page cluster

For each proposed page, write a compact record:

```text
primary keyword:
job to be done:
secondary variants:
search intent: informational | utility | commercial | navigational
tool input/output:
privacy model: browser-local | server processing (explain retention)
related tools (next/previous job):
service CTA and why it is contextually earned:
evidence and date:
```

Keep one page focused on one job. Use adjacent pages for adjacent jobs (for example, compress → resize → convert → PDF), then link them in the order users naturally work.

### 4. Build the AMIX-style page structure

Use this as a default, adapting it to the task:

1. **Tool shell** — one clear H1, one-line promise, immediate UI, sensible defaults, keyboard and mobile support, and a result state.
2. **Explanation block A: what it solves** — plain-language use cases, supported formats, limits, and expected output.
3. **Explanation block B: why/how it works** — short technical explanation, security/privacy behavior, caveats, and FAQ. Add tables only when they clarify a choice.
4. **Contextual service CTA** — link to the relevant service only when the tool's job naturally reveals a deeper need. Use a specific destination (for example, a design service or consultation page), not a generic sales interruption.
5. **Related tools** — link to the next useful operations, with one-sentence descriptions. Finish with tool index, terms/privacy, contact, and the operating brand.

The page must be useful before the CTA. Do not pad pages with keyword-stuffed text, false claims, or generic FAQs. Include visible copyright/licensing and privacy language where the tool handles files or user input.

### 5. Implement and verify

- Prefer browser-local processing for personal files when technically practical; state clearly whether bytes leave the device.
- Keep the first interaction fast. Lazy-load heavyweight libraries and avoid uploading files merely to perform a client-side transform.
- Use semantic headings, labels, focus states, error messages, downloadable results, and mobile layouts.
- Add unique title/description/canonical, descriptive URLs, Open Graph basics, and structured data only when it describes visible content.
- Verify the real interaction on desktop and mobile, page source/meta, internal-link targets, empty/error states, and a production-like build. Check that the CTA, related links, privacy text, and limits are truthful.

## AI顧問室 repository loop

When the current repository contains `seo/config.json`, use its daily factory instead of keeping research in chat:

```bash
python3 seo/scripts/run_daily.py --root .
```

Read `seo/data/runs/YYYY-MM-DD/daily-brief.md`, inspect the raw observations and audit evidence, then select one candidate. Create a reviewed JSON spec under `seo/tool-specs/` and generate the page only after checking search-intent overlap:

```bash
python3 seo/scripts/generate_tool_page.py \
  --spec seo/tool-specs/<reviewed-spec>.json \
  --root . --output-dir tools
```

The factory is intentionally review-first: daily research and structural audits may run unattended, but generated pages must be tested and approved before deployment. Put a Search Console CSV export at `seo/data/gsc/latest.csv` to add first-party query opportunities to the daily brief.

## SEO article production

For article clusters supporting the tools, keep one primary search intent per article and route readers through `answer → evidence → example → free tool → next action`. Use Google/Bing/YouTube suggestions plus first-party Search Console data where available, and record retrieval dates for time-sensitive claims. Prefer official/primary sources for legal, policy, pricing, grants, and product specifications.

Use image generation for one or two supporting visuals per article (hero, editorial scene, or abstract concept). Keep exact Japanese labels, numbers, formulas, and process diagrams in HTML/SVG so they remain accessible, searchable, and accurate; do not rely on generated text inside an image. Save stable assets under `assets/articles/<slug>/`, give each image a descriptive alt, and verify mobile rendering and file weight before publishing.

## Output format

When asked for research, return a compact table of keyword, intent, tool idea, evidence source/date, and next action, followed by a recommended cluster and page outline. When asked to build, ship the smallest useful tool page first, then add the explanatory and navigation layers, and report what was verified.

## Bundled resources

- `scripts/rakko_keyword.py` — official Rakkokeyword API client for suggest/related/LSI/headline/co-occurrence research, including an explicit opt-in bundle.
- `references/keyword-research.md` — API/browser decision rules, metric caveats, and the research record schema.
