# Keyword research reference

## Data-source choice

Use the official Rakkokeyword API when an authorized `RAKKO_KEYWORD_API_KEY` is present. The API documentation lists `X-API-Key` authentication and these useful operations:

| Operation | Use it for | Typical role |
|---|---|---|
| `suggest-keywords` | Google/YouTube/Amazon/etc. suggestions | discover variants and modifiers |
| `related-keywords` | large partial/phrase/prefix matches | expand a validated seed |
| `other-keywords` | LSI and Google PAA questions | uncover latent needs and FAQ topics |
| `headline` | headings from ranking pages | competitor/topic coverage |
| `co-occurrence` | recurring words on ranking pages | content completeness check |

The provider documents search-volume and SEO-difficulty values as potentially stale for some responses. Treat them as directional until refreshed, and store the retrieval date. Do not present a metric as a guarantee of traffic or ranking.

If the API is unavailable, use `https://rakkokeyword.com/` with `agent-browser`. Keep browser research reproducible: record the seed, mode, URL, visible result count, date/time, and any account/plan limitation. Do not automate around rate limits or access controls.

## Recommended research pass

For a new tool cluster:

1. Run `suggest` on 3–8 seed phrasings.
2. Merge and normalize the results (spacing, punctuation, full/half width, singular/plural equivalents, and obvious duplicates).
3. Run `other` on the strongest 1–3 seeds to collect questions and latent needs.
4. Use `headline` and `co-occurrence` only for candidates that will become a real page; these are content-design signals, not a license to copy competitor wording.
5. Use `related` for breadth after a seed has a clear tool job.
6. Cluster by intent and user workflow; do not create a page for every spelling variant.

## Research record

Store or return records with these fields:

```json
{
  "keyword": "画像圧縮",
  "source": "rakkokeyword-api|rakkokeyword-browser",
  "mode": "suggest|related|other|headline|co-occurrence",
  "retrieved_at": "2026-07-12T00:00:00+09:00",
  "search_volume": null,
  "seo_difficulty": null,
  "intent": "utility",
  "tool_candidate": true,
  "notes": "Keep the metric date and caveats."
}
```

Separate raw observations from derived scores. A useful derived score can combine urgency, repeat use, clarity of input/output, service fit, and build cost, but it must be labeled as a planning heuristic rather than a market fact.
