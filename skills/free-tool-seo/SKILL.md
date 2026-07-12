---
name: free-tool-seo
description: Design, build, and audit browser-based free-tool SEO pages with explanatory content, internal links, privacy language, and contextual service CTAs. Use after keyword research when planning a free-tool library or implementing an SEO landing/tool page.
---

# Free Tool SEO

Use this skill to turn a validated search-intent cluster into a useful browser tool and a page that explains it. Keyword discovery belongs to `$seo-keyword-research`; this skill consumes its research packet and focuses on product/page design, implementation, and verification.

## 1. Inspect the reference and current product

Start from real pages and repository files. For each representative page, record:

- title, meta description, canonical URL, indexability signals, and primary keyword;
- the tool UI, inputs/outputs, and whether processing is browser-local or server-side;
- heading tree and explanation blocks after the tool;
- FAQ, limitations, privacy/security claims, related-tool links, service links, and footer links;
- mobile behavior, load cost, dependencies, empty/error states, and conversion path.

Use `agent-browser` for live pages and `rg --files` for local implementations. Keep observed facts separate from hypotheses. Do not copy another site's text, visual assets, branding, or code.

## 2. Accept a research packet

Before implementation, require a compact packet from `$seo-keyword-research` or an equivalent first-party export:

```text
primary keyword:
job to be done:
secondary variants:
search intent:
tool input/output:
privacy model:
evidence and retrieval date:
related tools:
service CTA and why it is earned:
```

Check search-intent overlap with existing pages. One page should focus on one job. Link adjacent jobs in the order users naturally work.

## 3. Build the AMIX-style page structure

Adapt this structure to the tool:

1. **Tool shell** — one clear H1, one-line promise, immediate UI, sensible defaults, keyboard support, accessible labels, and a visible result state.
2. **Explanation A: what it solves** — use cases, supported inputs, limits, expected output, and who should use it.
3. **Explanation B: how it works** — short technical explanation, browser-local/server-processing behavior, security caveats, and FAQ.
4. **Contextual service CTA** — link to a specific service only when the tool reveals a deeper need. The page must be useful before the CTA.
5. **Related tools** — link to the next operation with one-sentence descriptions, then the tool index, terms/privacy, contact, and operating brand.

Do not pad pages with keyword-stuffed text, false claims, or generic FAQs. State limitations and privacy behavior visibly.

## 4. Implement the smallest useful tool first

- Prefer browser-local processing for personal files and form data when practical; state clearly whether bytes leave the device.
- Keep first interaction fast. Lazy-load heavyweight libraries and avoid uploading files for a client-side transform.
- Use semantic headings, labels, focus states, error messages, downloadable results, and mobile layouts.
- Add unique title/description/canonical, descriptive URLs, Open Graph basics, and structured data only when it describes visible content.
- Use WebP/AVIF for generated raster assets. Keep exact labels, numbers, formulas, and process steps in HTML/SVG when accessibility and searchability matter.

## 5. AI顧問室 repository loop

When the current repository contains `seo/config.json`, use the manual factory instead of keeping research in chat:

```bash
python3 seo/scripts/run_daily.py --root .
```

Read `seo/data/runs/YYYY-MM-DD/daily-brief.md`, inspect raw observations and audit evidence, then select one candidate. Create a reviewed JSON spec under `seo/tool-specs/` and generate the page only after checking overlap:

```bash
python3 seo/scripts/generate_tool_page.py \
  --spec seo/tool-specs/<reviewed-spec>.json \
  --root . --output-dir tools
```

The factory is review-first: research and structural audits may run unattended, but generated pages must be tested and approved before deployment. Put a Search Console CSV export at `seo/data/gsc/latest.csv` to add first-party opportunities.

## 6. Article support

For an article that supports a tool, keep one primary intent and route readers through `answer → evidence → example → free tool → next action`. Use the keyword packet and first-party Search Console data where available. Prefer official/primary sources for policy, pricing, legal, grants, and product specifications.

Use one or two supporting visuals per article when useful. Save assets under `assets/articles/<slug>/`, add descriptive alt text, and verify mobile rendering and file weight. Exact Japanese labels and numerical diagrams should remain accessible HTML/SVG whenever possible.

## 7. Verify before shipping

Test the real interaction on desktop and mobile:

- page source, title, meta description, canonical, OGP, schema, and robots behavior;
- internal-link targets and no broken local links;
- empty, invalid, and normal input states;
- privacy text and actual network behavior;
- keyboard/focus behavior and tap targets;
- CTA and related-tool links;
- image dimensions, format, file weight, and alt text;
- `python3 seo/scripts/site_audit.py --root .` for the repository baseline.

## Output

Report the selected research packet, page structure, implementation files, privacy model, internal-link map, service CTA rationale, and verification results. Ship the smallest useful tool page first, then add explanatory and navigation layers.
