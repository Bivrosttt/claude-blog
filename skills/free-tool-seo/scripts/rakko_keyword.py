#!/usr/bin/env python3
"""Small, dependency-free client for the Rakkokeyword API.

The key is read from RAKKO_KEYWORD_API_KEY (or --api-key-env) and sent only
as the X-API-Key header. Results are printed as JSON for piping into jq or a
research notebook.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any


BASE_URL = "https://api.rakkokeyword.com"


def build_body(mode: str, args: argparse.Namespace) -> dict[str, Any]:
    body: dict[str, Any] = {"keyword": args.keyword}
    if mode == "suggest":
        body.update(
            {
                "modes": [m.strip() for m in args.modes.split(",") if m.strip()],
                "increaseKeyword": args.increase,
            }
        )
    elif mode == "related":
        body["matchType"] = args.match_type
    elif mode == "headline":
        body.update({"lessHeadlines": args.less_headlines, "lessCharacters": args.less_characters})
    elif mode == "cooccurrence":
        body["getDetails"] = args.details
    if args.limit is not None and mode != "other":
        body["limit"] = args.limit
    return body


def request(mode: str, body: dict[str, Any], api_key: str, timeout: float) -> dict[str, Any]:
    endpoint = {
        "suggest": "/v1/suggest-keywords",
        "related": "/v1/related-keywords",
        "other": "/v1/other-keywords",
        "headline": "/v1/headline",
        "cooccurrence": "/v1/co-occurrence",
    }[mode]
    payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL + endpoint,
        data=payload,
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-Key": api_key,
            "User-Agent": "free-tool-seo/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            detail: Any = json.loads(raw)
        except json.JSONDecodeError:
            detail = raw
        raise RuntimeError(f"Rakkokeyword API returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Rakkokeyword API: {exc.reason}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Query Rakkokeyword for SEO research data.")
    parser.add_argument("--keyword", required=True, help="Seed keyword")
    parser.add_argument(
        "--mode",
        choices=["suggest", "related", "other", "headline", "cooccurrence", "bundle"],
        default="suggest",
    )
    parser.add_argument("--modes", default="google", help="Comma-separated suggest sources")
    parser.add_argument("--increase", action="store_true", help="Request expanded suggestions")
    parser.add_argument("--match-type", default="partialMatch")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--less-headlines", action="store_true")
    parser.add_argument("--less-characters", action="store_true")
    parser.add_argument("--details", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--api-key-env", default="RAKKO_KEYWORD_API_KEY")
    parser.add_argument("--api-key", help=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get(args.api_key_env)
    if not api_key:
        print(
            f"Missing API key. Set {args.api_key_env}; otherwise use the browser fallback at "
            "https://rakkokeyword.com/ (do not bypass limits).",
            file=sys.stderr,
        )
        return 2

    modes = ["suggest", "related", "other", "headline", "cooccurrence"] if args.mode == "bundle" else [args.mode]
    results: dict[str, Any] = {
        "keyword": args.keyword,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": "rakkokeyword-api",
        "results": {},
    }
    try:
        for mode in modes:
            results["results"][mode] = request(mode, build_body(mode, args), api_key, args.timeout)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    indent = 2 if args.pretty else None
    print(json.dumps(results, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
