# Amazon Scraper

**Amazon Scraper** — extract structured product, review, and bestseller data from Amazon via API. No proxies to manage, no parsers to maintain, no CAPTCHAs to solve.

Built on [Pangolinfo's Amazon Scraper API](https://www.pangolinfo.com). **Free tier: 60 credits per month, reset monthly, no credit card required.**

## Free Amazon Scraper

You don't need to build your own scraper. Sign up free and start pulling real Amazon data in under two minutes:

1. Go to [pangolinfo.com](https://www.pangolinfo.com) and click **Start Free Trial** — this creates your account at tool.pangolinfo.com.
2. Copy your API key from the dashboard.
3. Run the example below. The free tier (60 credits/month, no card required) is enough to test product, review, and bestseller endpoints end to end.

## Quick Setup

### Prerequisites

- Python 3.8+ and `pip` (for the Python examples), or Node.js 18+ (for the Node.js example)
- A free Pangolinfo API key ([get one here](https://www.pangolinfo.com))

### Python

```bash
git clone https://github.com/Pangolin-spg/amazon-scraper.git
cd amazon-scraper
pip install -r requirements.txt
export PANGOLIN_API_KEY="your-api-key-here"
```

### Node.js

```bash
git clone https://github.com/Pangolin-spg/amazon-scraper.git
cd amazon-scraper/examples/nodejs
export PANGOLIN_API_KEY="your-api-key-here"
# no dependencies needed — uses native fetch (Node 18+)
```

> Never commit your API key to git. Keep it in an environment variable or a secrets manager.

## How to Scrape Amazon Data

### Product data

```bash
python examples/python/amazon_product.py
```

Returns structured JSON for any ASIN — title, price, rating, images, and more:

```python
import os
import requests

API_KEY = os.environ["PANGOLIN_API_KEY"]

resp = requests.get(
    "https://api.pangolinfo.com/v1/amazon/product",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={
        "asin": "B0FQFB8FMG",          # Apple AirPods Pro 3
        "marketplace": "US",
        "fields": "title,price,rating,images",
    },
    timeout=60,
)
resp.raise_for_status()
product = resp.json()
print(product["title"], "|", product.get("price"), "|", product.get("rating"))
```

### Review data

```bash
python examples/python/amazon_reviews.py
```

Pulls paginated reviews for an ASIN — text, star rating, date, verified-purchase flag:

```bash
# inside amazon_reviews.py — the only parameters you need:
params = {"asin": "B0FQFB8FMG", "max_pages": 1}
```

### Node.js

```bash
node examples/nodejs/amazon_product.js
```

Same product lookup using native `fetch` — zero dependencies.

### Bestsellers

```
GET https://api.pangolinfo.com/v1/amazon/bestsellers
Authorization: Bearer <API_KEY>
```

See the [docs](https://docs.pangolinfo.com) for the full parameter reference.

## What Data You Get

| Endpoint | Returns |
|---|---|
| `/v1/amazon/product` | Title, price, rating, review count, images, availability, and more per ASIN |
| `/v1/amazon/reviews` | Review text, star rating, date, verified-purchase flag, helpful votes — paginated |
| `/v1/amazon/bestsellers` | Category bestseller rankings |

All responses are structured JSON. No HTML parsing on your side.

## Why an API Beats DIY Scraping

- **No proxy management.** Amazon aggressively rate-limits datacenter IPs. The API routes every request through residential-grade infrastructure — you never touch a proxy.
- **No anti-bot warfare.** CAPTCHAs, JavaScript challenges, and fingerprinting are handled server-side. Your code just does `GET` and reads JSON.
- **No broken parsers.** Amazon changes its page layout regularly; every DIY XPath/CSS selector eventually rots. The API's parsers are maintained by the provider.
- **Predictable cost.** Per-request credit billing with a free tier (60 credits/month). A DIY scraper costs you proxy bills plus maintenance time — the math rarely wins.

## FAQ

**Is it free?**
Yes — the free tier gives you 60 credits per month, reset monthly, with no credit card required. That's enough to test the product, reviews, and bestseller endpoints and run small projects.

**Do I need an Amazon account?**
No. The API reads publicly accessible Amazon pages. You only need a Pangolinfo API key — never Amazon credentials.

**Which marketplaces are supported?**
Use the `marketplace` parameter (e.g. `US`, `UK`, `DE`, `JP`). Check the [docs](https://docs.pangolinfo.com) for the current list.

**How is this different from scraping Amazon myself with Selenium/BeautifulSoup?**
DIY scraping works until Amazon blocks your IP, serves a CAPTCHA, or changes its markup — then you're debugging instead of building. This repo's examples call a maintained API, so the same three lines of code keep working.

**Can I use this commercially?**
Yes, on any paid plan. See [pangolinfo.com pricing](https://www.pangolinfo.com) for details.

## Start Free

- [Get a free API key](https://www.pangolinfo.com) — 60 credits/month, no card required
- [Full API documentation](https://docs.pangolinfo.com)

---

*Built by [Pangolinfo](https://www.pangolinfo.com) — real-time Amazon data for developers, AI agents, and ecommerce teams.*
