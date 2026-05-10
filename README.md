# Particle For Men — Shopify migration docs

This folder holds migration planning artifacts (feature inventory) derived from the WordPress/WooCommerce codebase. The main inventory is written for **business and project stakeholders** first; **section 11 is a capability checklist** (not a list of WordPress plugin folder names).

On **GitHub**, the Markdown uses [alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts) (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`) and tables so the file is easier to scan than wall-of-bullet text. (GitHub’s README renderer does not support arbitrary colored HTML the way some wikis do; see [community discussion #31570](https://github.com/orgs/community/discussions/31570) for context on colored text limits.)

## Contents

- **`shopify-migration-features-inventory.md`** — Full capabilities list (**Description**, **Relevance**, **Transferability** per item—no separate “Evidence” column; theme PHP and Woo overrides are summarized in aggregate, not file-by-file).
- **`shopify-migration-features-inventory.pdf`** — Same document as PDF for easy sharing (regenerate locally if needed).
- **`generate-shopify-inventory.py`** — Regenerates the Markdown from this WordPress project root (theme under `wp-content/themes/particleformen` for dynamic counts; section 11 rows are curated in the script, not scraped from `wp-content/plugins`).
- **`_pfm-panel-section.md`** — Snippet injected for **internal staff tools** (section 10); edit when those workflows change.

## Regenerate

From the WordPress project root (`particleformen/`):

```bash
python docs/generate-shopify-inventory.py
```

## Public mirror

Updates for stakeholders may be pushed to: [github.com/ri5pekt/pfm-shopify-migration](https://github.com/ri5pekt/pfm-shopify-migration).
