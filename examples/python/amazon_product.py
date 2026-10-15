#!/usr/bin/env python3
"""
Amazon product lookup via the Pangolinfo Scraper API.

Usage:
    export PANGOLIN_API_KEY="your-api-key-here"
    python amazon_product.py [ASIN]

The free tier (60 credits/month, no credit card) covers this call.
Get a key at https://www.pangolinfo.com  (Start Free Trial).
"""
import os
import sys

import requests

API_BASE = "https://api.pangolinfo.com/v1/amazon/product"


def get_product(asin: str, api_key: str, marketplace: str = "US") -> dict:
    """Fetch structured product data for one ASIN."""
    resp = requests.get(
        API_BASE,
        headers={"Authorization": f"Bearer {api_key}"},
        params={
            "asin": asin,
            "marketplace": marketplace,
            "fields": "title,price,rating,images",
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    api_key = os.environ.get("PANGOLIN_API_KEY")
    if not api_key:
        sys.exit("Error: set the PANGOLIN_API_KEY environment variable first.")

    # Sample product: Apple AirPods Pro 3 (override with any ASIN)
    asin = sys.argv[1] if len(sys.argv) > 1 else "B0FQFB8FMG"

    product = get_product(asin, api_key)

    # Print the headline fields; the full JSON has much more.
    print("Title :", product.get("title"))
    print("Price :", product.get("price"))
    print("Rating:", product.get("rating"))


if __name__ == "__main__":
    main()
