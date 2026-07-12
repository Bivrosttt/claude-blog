---
name: seo-keyword-research
description: Research Japanese SEO keywords from Google, Bing, YouTube, Search Console, and Rakkokeyword, then normalize, cluster, and score candidates for articles or free tools. Use when researching keywords, search intent, related questions, or content/tool opportunities.
---

# SEO Keyword Research

Use this skill to turn a seed problem into a dated, reproducible keyword research record. Keep raw observations separate from derived planning scores, and never present estimated volume or difficulty as a ranking guarantee.

## 1. Define the research question

Start with the user's language and the job they are trying to complete, for example `議事録を短くまとめたい` instead of only `議事録`. Record:

- seed phrases and the audience;
- desired output: article, free tool, landing page, or internal content;
- search intent: informational, utility, commercial, or navigational;
- location/language and retrieval date;
- existing pages that could compete with the candidate.

One candidate should represent one primary intent. Do not create a page for every spelling variant.

## 2. Choose a data source

Use the least expensive source that answers the question:

1. First-party Search Console export in `seo/data/gsc/latest.csv` when available.
2. Google, Bing, and YouTube public suggestions for discovery.
3. Rakkokeyword API for expanded suggestions, related terms, PAA/LSI, headings, or co-occurrence when an authorized key is available.
4. The Rakkokeyword browser UI when there is no API key. Record only visible, permitted results and do not bypass login, paywalls, rate limits, or robots.
5. Official and primary sources for policy, pricing, legal, product, and technical claims.

Metrics such as search volume and SEO difficulty can be stale or estimated. Store the metric date and label them as directional.

## 3. Rakkokeyword API

The bundled client reads `RAKKO_KEYWORD_API_KEY` from the environment and sends it only as `X-API-Key`. It never prints the key:

```bash
python3 skills/seo-keyword-research/scripts/rakko_keyword.py \
  --keyword '業務改善' --mode suggest --modes google,youtube --limit 200 --pretty
```

Available modes are `suggest`, `related`, `other`, `headline`, `cooccurrence`, and the explicit opt-in `bundle`. Do not run `bundle` casually because the provider may charge credits per endpoint.

If no key is configured, use the browser fallback at `https://rakkokeyword.com/` and save the seed, mode, result URL, visible row count, timestamp, and account/plan limitation.

## 4. Normalize and cluster

Normalize spacing, punctuation, full/half-width variants, obvious duplicates, and singular/plural equivalents. Keep the raw rows in a dated research file. Then cluster by:

- the same job to be done;
- the same expected input and output;
- the same stage in the user's workflow;
- whether the page should be an article, tool, comparison, or service page.

Use adjacent pages for adjacent jobs. For example, `画像圧縮`, `画像リサイズ`, and `画像変換` can form a workflow cluster, but should not be collapsed into one page if their tools and intents differ.

## 5. Score candidates

Use a planning heuristic, not a market fact. Score each candidate from 1 to 5 for:

- problem urgency;
- search-intent clarity;
- repeat-use potential;
- feasibility of a useful browser-local result;
- service fit;
- maintenance and compliance cost.

Prioritize the smallest cluster that can ship and be internally linked. Flag uncertainty instead of inventing volume or difficulty.

## 6. Research record

Store or return records with this shape:

```json
{
  "keyword": "議事録 AI",
  "source": "rakkokeyword-api|rakkokeyword-browser|google-suggest|gsc",
  "mode": "suggest|related|other|headline|cooccurrence",
  "retrieved_at": "2026-07-12T00:00:00+09:00",
  "search_volume": null,
  "seo_difficulty": null,
  "intent": "utility",
  "tool_candidate": true,
  "notes": "Metrics are directional and must retain their retrieval date."
}
```

Keep evidence, observations, and derived scores in separate fields. A score is a prioritization aid, not a prediction of traffic or ranking.

## 7. Hand off to the next skill

For a free browser tool, pass the selected cluster to `$free-tool-seo` with the primary keyword, job to be done, input/output, privacy model, related tools, and contextual CTA. For an article or broader content strategy, hand the research packet to `blog-brief`, `blog-outline`, `blog-cluster`, or `blog-write`.

## Browser research rules

When browser automation is required, use the `agent-browser` open → snapshot → interact → re-snapshot flow. Do not scrape private endpoints or automate around access controls. Mark browser-collected values as observed on the retrieval date.

## Output

Return a compact table with keyword, source/mode, intent, evidence date, candidate type, confidence, and next action. Follow it with the recommended cluster, cannibalization warnings, and a page brief for the next skill.
