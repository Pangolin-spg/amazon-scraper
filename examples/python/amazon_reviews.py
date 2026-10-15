#!/usr/bin/env python3
"""
Amazon review extraction via the Pangolinfo Scraper API.

Usage:
    export PANGOLIN_API_KEY="your-api-key-here"
    python amazon_reviews.py [ASIN] [MAX_PAGES]

The free tier (60 credits/month, no credit card) covers this call.
Get a key at https://www.pangolinfo.com  (Start Free Trial).
"""
import os
import sys

import requests

API_BASE = "https://api.pangolinfo.com/v1/amazon/reviews"


def get_reviews(asin: str, api_key: str, max_pages: int = 1) -> dict:
    """Fetch paginated reviews for one ASIN."""
    resp = requests.get(
        API_BASE,
        headers={"Authorization": f"Bearer {api_key}"},
        params={"asin": asin, "max_pages": max_pages},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def _review_list(payload: dict) -> list:
    """Extract the review list defensively — the API wraps it in a data object."""
    if isinstance(payload, list):
        return payload
    data = payload.get("data", payload)
    if isinstance(data, dict):
        for key in ("reviews", "items", "results"):
            if isinstance(data.get(key), list):
                return data[key]
    return []


def main() -> None:
    api_key = os.environ.get("PANGOLIN_API_KEY")
    if not api_key:
        sys.exit("Error: set the PANGOLIN_API_KEY environment variable first.")

    # Sample product: Apple AirPods Pro 3 (override with any ASIN)
    asin = sys.argv[1] if len(sys.argv) > 1 else "B0FQFB8FMG"
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    payload = get_reviews(asin, api_key, max_pages)
    reviews = _review_list(payload)

    print(f"ASIN {asin}: {len(reviews)} review(s) returned "
          f"(total reported: {payload.get('total', 'n/a')})")
    if reviews:
        first = reviews[0]
        print("-" * 60)
        print("First review snippet:")
        print("  Stars :", first.get("rating", first.get("stars")))
        print("  Date  :", first.get("date"))
        print("  Title :", first.get("title"))
        body = str(first.get("body", first.get("text", "")))
        print("  Body  :", body[:300] + ("..." if len(body) > 300 else ""))


if __name__ == "__main__":
    main()
