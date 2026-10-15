# Repo setup checklist — `amazon-scraper`

Create this repo under the **Pangolin-spg** org (it already hosts `amazon-data-mcp` and `openclaw-skills`). Everything in this folder is ready to push as-is.

## 1. Create the repository

- **Name:** `amazon-scraper`
- **Visibility:** Public
- **Description** (repo tagline — shows in Google results, keep the keyword up front):
  `Free Amazon Scraper — extract product, review & bestseller data via API. 60 free credits/month.`
- **Website field:** `https://www.pangolinfo.com`
- **License:** MIT (add via GitHub's license picker on creation)

## 2. Topics (repo Settings → Topics — these feed GitHub search)

Add all five:
`amazon-scraper` · `amazon-api` · `web-scraping` · `ecommerce` · `price-monitoring`

## 3. Push the files

Upload the contents of this folder to the repo root:

```
README.md                  ← the landing page (keyword: "Amazon Scraper" in H1)
requirements.txt
examples/python/amazon_product.py
examples/python/amazon_reviews.py
examples/nodejs/amazon_product.js
examples/nodejs/package.json
```

## 4. Sanity checks after push

- [ ] README renders with the H1 "Amazon Scraper" at the top
- [ ] "Free" section states **60 credits/month, reset monthly, no credit card** (matches current free-tier spec — update here if the spec changes)
- [ ] No API key committed anywhere (`grep -ri "pgl_"` should return nothing)
- [ ] All outbound links point to `https://www.pangolinfo.com` or `https://docs.pangolinfo.com`

## 5. Optional (do later, not on day one)

- Pin the repo on the Pangolin-spg org profile
- Add a `CONTRIBUTING.md` if outside PRs arrive
- Link it from the docs site's GitHub section for the backlink

## Why this works (for reference)

Competitors ranking for "Amazon Scraper GitHub" (Bright Data's `luminati-io/Amazon-scraper`, Decodo's `Amazon-scraper`) use the exact same shape: repo name = keyword, README = landing page with free-tool angle + runnable quickstart + free-trial CTA. github.com's domain authority does the ranking; the README does the converting.
