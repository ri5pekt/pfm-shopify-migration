# Particle For Men — Shopify migration docs

This folder holds migration planning artifacts (feature inventory) derived from the WordPress/WooCommerce codebase.

## Contents

- **`shopify-migration-features-inventory.md`** — Full capabilities list (sections, relevance, transferability) for Shopify discussions.
- **`shopify-migration-features-inventory.pdf`** — Same document as PDF for easy sharing (regenerate locally if needed).
- **`generate-shopify-inventory.py`** — Regenerates the Markdown from this WordPress project root (`wp-content/plugins`, theme under `wp-content/themes/particleformen`).
- **`_pfm-panel-section.md`** — Snippet injected into the generated inventory for `pfm-panel` REST routes (edit when routes change).

## Regenerate

From the WordPress project root (`particleformen/`):

```bash
python docs/generate-shopify-inventory.py
```

## Public mirror

Updates for stakeholders may be pushed to: [github.com/ri5pekt/pfm-shopify-migration](https://github.com/ri5pekt/pfm-shopify-migration).
