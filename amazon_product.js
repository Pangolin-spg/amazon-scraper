#!/usr/bin/env node
/**
 * Amazon product lookup via the Pangolinfo Scraper API.
 *
 * Usage:
 *   export PANGOLIN_API_KEY="your-api-key-here"
 *   node amazon_product.js [ASIN]
 *
 * Requires Node.js 18+ (native fetch, zero dependencies).
 * The free tier (60 credits/month, no credit card) covers this call.
 * Get a key at https://www.pangolinfo.com  (Start Free Trial).
 */

const API_BASE = "https://api.pangolinfo.com/v1/amazon/product";

async function getProduct(asin, apiKey, marketplace = "US") {
  const url = new URL(API_BASE);
  url.searchParams.set("asin", asin);
  url.searchParams.set("marketplace", marketplace);
  url.searchParams.set("fields", "title,price,rating,images");

  const resp = await fetch(url, {
    headers: { Authorization: `Bearer ${apiKey}` },
  });
  if (!resp.ok) {
    throw new Error(`API error ${resp.status}: ${await resp.text()}`);
  }
  return resp.json();
}

async function main() {
  const apiKey = process.env.PANGOLIN_API_KEY;
  if (!apiKey) {
    console.error("Error: set the PANGOLIN_API_KEY environment variable first.");
    process.exit(1);
  }

  // Sample product: Apple AirPods Pro 3 (override with any ASIN)
  const asin = process.argv[2] || "B0FQFB8FMG";

  const product = await getProduct(asin, apiKey);

  // Print the headline fields; the full JSON has much more.
  console.log("Title :", product.title);
  console.log("Price :", product.price);
  console.log("Rating:", product.rating);
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
