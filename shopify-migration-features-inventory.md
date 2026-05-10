# Shopify migration — features inventory (Particle For Men)

_Generated from repository scan. Schema per item: **Title**, **Description**, **Relevance** (High / Medium / Low), **Transferability** (Full / Partial / Not transferable / N/A). Low relevance or N/A does **not** mean omit from migration planning — it marks Shopify non-parity or decommission work._

## Legend

- **High** — revenue, checkout, subscriptions, fraud, tax, fulfillment, i18n/currency, or ops-critical.
- **Medium** — marketing, CRM, merchandising, SEO, or important UX.
- **Low** — admin convenience, dev-only, host-only, or minor UX.

## 0. Cross-cutting thread index (additive)

These rows summarize behaviors implemented by **multiple** components listed later. **Do not remove** the underlying rows.

### Thread: WPML + WCML + language/currency + redirects

- **Description:** Multilingual URLs, `hreflang`, `?store_switch=`, cookie `wp-wpml_current_language`, `wcml_custom_currency` in theme `functions.php`, `mu-plugins/redirections.php`, cart redirect in `mu-plugins/custom_plugin_organizer.php`, WPML product ID memoization in `lib/optimization.php`, multi-currency reads in `lib/utils.php` and plugins such as `cart-sidebar`.
- **Relevance:** High
- **Transferability:** Partial — Shopify Markets + redirects import + theme locale strategy.

### Thread: Subscription commerce stack

- **Description:** `woocommerce-subscriptions`, `woocommerce-subscription`, `subscriptions-utils`, theme recurring checkout templates under `woocommerce/checkout/`, `pfm-panel` subscription REST, upsell plugins touching subscription options (`add_upsells_option_ms`).
- **Relevance:** High
- **Transferability:** Partial — Shopify Subscriptions; full plan matrix workshop required.

### Thread: Fraud and risk stack

- **Description:** Signifyd, Kount, Sift (multiple plugins), checkout observer/bot block, package protection.
- **Relevance:** High
- **Transferability:** Partial — combine Shopify Fraud with third-party apps and payment rules.

### Thread: Fulfillment and post-purchase visibility

- **Description:** ShipBob, ShipStation, shipment tracking, Narvar, AfterShip, warehouse-export webhooks, ERP Priority integrations.
- **Relevance:** High
- **Transferability:** Partial — OMS connectors and Shopify webhooks.

### Thread: Marketing and attribution pixels

- **Description:** GTM, PixelYourSite, Blotout, Impact, TikTok, Facebook channel, Wunderkind, OptinMonster, theme purchase events in `lib/utils.php`.
- **Relevance:** High
- **Transferability:** Partial — pixels in Customer Events / server-side partners.

## 1. Theme — PHP modules (`functions.php` includes)

### `lib/image-sizes.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/image-sizes.php`

### `lib/custom-post-types.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/custom-post-types.php`

### `lib/remove-trash.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/remove-trash.php`

### `lib/script-style.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/script-style.php`

### `lib/gutenberg/gutenberg.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/gutenberg/gutenberg.php`

### `lib/acf/acf.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/acf/acf.php`

### `lib/ajaxFunctions.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/ajaxFunctions.php`

### `lib/theme-setup.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/theme-setup.php`

### `lib/accessibility.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/accessibility.php`

### `lib/woocommerce-setup.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/woocommerce-setup.php`

### `lib/checkout.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/checkout.php`

### `lib/rest-api.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/rest-api.php`

### `lib/seo.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/seo.php`

### `lib/retention.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/retention.php`

### `lib/request-checker.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/request-checker.php`

### `lib/admin-dashboard.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/admin-dashboard.php`

### `lib/meta-shop-checkout.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/meta-shop-checkout.php`

### `lib/utils.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/utils.php`

### `lib/super-editor.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/super-editor.php`

### `lib/cart-functions.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/cart-functions.php`

### `lib/ab-tests.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/ab-tests.php`

### `lib/class-particle-klaviyo-helper.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/class-particle-klaviyo-helper.php`

### `lib/optimization.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/optimization.php`

### `lib/retention-lp-utils.php`

- **Description:** Theme logic loaded on every request (or as gated by internal includes). Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.
- **Relevance:** High (commerce + i18n surface area)
- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.
- **Evidence:** `wp-content/themes/particleformen/lib/retention-lp-utils.php`

## 2. Theme — `functions.php` root-level behaviors

### `wcml_custom_currency` filter

- **Description:** Maps `wpml_current_language` codes (`au`,`gb`,`br`,`ca`,`he`,`la`,`ja`,`fr`,`de`,`it`,`es`) to ISO currencies (AUD, GBP, BRL, CAD, ILS, MXN, JPY, EUR).
- **Relevance:** High
- **Transferability:** Partial — Shopify Markets pricing.

### Category `list` asset dequeue

- **Description:** On posts in category `list`, dequeues Woo + font + cookie scripts for lightweight reading experience.
- **Relevance:** Low
- **Transferability:** Partial — theme blog templates.

### Checkout phone blocklist (`njengah_custom_checkout_field_process`)

- **Description:** Blocks specific hard-coded `billing_phone` values at checkout validation.
- **Relevance:** Medium (fraud / abuse)
- **Transferability:** Partial — Flow or checkout validation app.

### `custom_coupon_query` SQL filter

- **Description:** Intercepts SQL containing INSERT into `woocommerce_order_itemmeta` for `coupon_data` and blanks query (custom coupon persistence behavior).
- **Relevance:** High
- **Transferability:** Not transferable — must understand business rule before replicating on Shopify.

### Magazine related posts + breadcrumbs + Yoast redirect slug + `remove_action` canonical

- **Description:** Editorial helpers, Yoast filter, disables old slug redirect and `redirect_canonical` on `init` priority 100.
- **Relevance:** Medium
- **Transferability:** Partial — SEO/redirect strategy on Shopify.

## 3. Theme — page templates (`template/*.php`)

### Page template file `after-quiz.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/after-quiz.php`

### Page template file `code-tests.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/code-tests.php`

### Page template file `content-post.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/content-post.php`

### Page template file `gravite-landing-page-2.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/gravite-landing-page-2.php`

### Page template file `gravite-landing-page-ty.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/gravite-landing-page-ty.php`

### Page template file `gravite-landing-page.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/gravite-landing-page.php`

### Page template file `single-product-marsmen.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/single-product-marsmen.php`

### Page template file `tmp-amazon-gift-landing-page.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-amazon-gift-landing-page.php`

### Page template file `tmp-amazon-lp-ty.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-amazon-lp-ty.php`

### Page template file `tmp-book-consultation-2.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-book-consultation-2.php`

### Page template file `tmp-book-consultation.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-book-consultation.php`

### Page template file `tmp-build-your-own-bundle.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-build-your-own-bundle.php`

### Page template file `tmp-commercials.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-commercials.php`

### Page template file `tmp-face-analyzer.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-face-analyzer.php`

### Page template file `tmp-first-purchase-anniversary.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-first-purchase-anniversary.php`

### Page template file `tmp-gravite-commercial.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-gravite-commercial.php`

### Page template file `tmp-life-drive-lp.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-life-drive-lp.php`

### Page template file `tmp-sport-page.php`

- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify page template or section set.
- **Evidence:** `wp-content/themes/particleformen/template/tmp-sport-page.php`

## 4. Theme — Gutenberg blocks (`app/blocks/*/block.php`)

_Block count: **70**._

### Block `ab-test-html`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/ab-test-html/`

### Block `about-awkward`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/about-awkward/`

### Block `about-head`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/about-head/`

### Block `about-video`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/about-video/`

### Block `action-coffee-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/action-coffee-block/`

### Block `affiliates-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/affiliates-block/`

### Block `after-quiz-bundle`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/after-quiz-bundle/`

### Block `all-products-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/all-products-block/`

### Block `banner-blue`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/banner-blue/`

### Block `benefits-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/benefits-block/`

### Block `best-sellers-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/best-sellers-block/`

### Block `blue-banner-text`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/blue-banner-text/`

### Block `bundle-products-list`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/bundle-products-list/`

### Block `bundle-save`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/bundle-save/`

### Block `bundles-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/bundles-block/`

### Block `clinical-trial`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/clinical-trial/`

### Block `coffee-ingredients-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/coffee-ingredients-block/`

### Block `coffee-innovate-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/coffee-innovate-block/`

### Block `comparison-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/comparison-block/`

### Block `confirmation-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/confirmation-block/`

### Block `contact-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/contact-block/`

### Block `custom-editor`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/custom-editor/`

### Block `difference-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/difference-block/`

### Block `faq-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/faq-block/`

### Block `faq-items`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/faq-items/`

### Block `faq-new`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/faq-new/`

### Block `gravite-banner-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/gravite-banner-block/`

### Block `gravite-carousel-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/gravite-carousel-block/`

### Block `gravite-header-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/gravite-header-block/`

### Block `gravite-horizontal-accordion`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/gravite-horizontal-accordion/`

### Block `gravite-sale-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/gravite-sale-block/`

### Block `header-top`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/header-top/`

### Block `how-to-use-new`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/how-to-use-new/`

### Block `how-use`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/how-use/`

### Block `ingredients-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/ingredients-block/`

### Block `ingredients-premium-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/ingredients-premium-block/`

### Block `instagram-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/instagram-block/`

### Block `logos-slider-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/logos-slider-block/`

### Block `magazin-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/magazin-block/`

### Block `more-product`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/more-product/`

### Block `more-products-new`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/more-products-new/`

### Block `order-bump-popup`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/order-bump-popup/`

### Block `performance-gear-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/performance-gear-block/`

### Block `perfume-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/perfume-block/`

### Block `perfume-block-footer`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/perfume-block-footer/`

### Block `perfume-top-hebrew`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/perfume-top-hebrew/`

### Block `press-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/press-block/`

### Block `privacy-policy`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/privacy-policy/`

### Block `product-actions`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/product-actions/`

### Block `products-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/products-block/`

### Block `products-head`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/products-head/`

### Block `quiz-container`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/quiz-container/`

### Block `reason-block-new`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/reason-block-new/`

### Block `reasons-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/reasons-block/`

### Block `recommend-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/recommend-block/`

### Block `refund-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/refund-block/`

### Block `reviews-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/reviews-block/`

### Block `section-products`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/section-products/`

### Block `slider-particle-men`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/slider-particle-men/`

### Block `slider-particle-men-v1`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/slider-particle-men-v1/`

### Block `specifically-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/specifically-block/`

### Block `stamped-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/stamped-block/`

### Block `submit-ticket-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/submit-ticket-block/`

### Block `support-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/support-block/`

### Block `tabs-scroll-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/tabs-scroll-block/`

### Block `tag-line`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/tag-line/`

### Block `thank-you`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/thank-you/`

### Block `tv-commercial-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/tv-commercial-block/`

### Block `video-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/video-block/`

### Block `video-reviews-block`

- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.
- **Evidence:** `wp-content/themes/particleformen/app/blocks/video-reviews-block/`

## 5. Theme — WooCommerce template overrides

_PHP files under `woocommerce/`: **69**._

### Override `woocommerce/archive-product.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/archive-product.php`

### Override `woocommerce/cart/cart-backup.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/cart-backup.php`

### Override `woocommerce/cart/cart-recurring-shipping.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/cart-recurring-shipping.php`

### Override `woocommerce/cart/cart-shipping.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/cart-shipping.php`

### Override `woocommerce/cart/cart-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/cart-totals.php`

### Override `woocommerce/cart/cart.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/cart.php`

### Override `woocommerce/cart/proceed-to-checkout-button.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/cart/proceed-to-checkout-button.php`

### Override `woocommerce/checkout/custom-payment-method.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/custom-payment-method.php`

### Override `woocommerce/checkout/form-billing.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/form-billing.php`

### Override `woocommerce/checkout/form-checkout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/form-checkout.php`

### Override `woocommerce/checkout/form-coupon.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/form-coupon.php`

### Override `woocommerce/checkout/form-pay.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/form-pay.php`

### Override `woocommerce/checkout/form-shipping.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/form-shipping.php`

### Override `woocommerce/checkout/payment-method.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/payment-method.php`

### Override `woocommerce/checkout/payment.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/payment.php`

### Override `woocommerce/checkout/recurring-coupon-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-coupon-totals.php`

### Override `woocommerce/checkout/recurring-fee-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-fee-totals.php`

### Override `woocommerce/checkout/recurring-itemized-tax-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-itemized-tax-totals.php`

### Override `woocommerce/checkout/recurring-subscription-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-subscription-totals.php`

### Override `woocommerce/checkout/recurring-subtotals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-subtotals.php`

### Override `woocommerce/checkout/recurring-tax-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-tax-totals.php`

### Override `woocommerce/checkout/recurring-totals.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/recurring-totals.php`

### Override `woocommerce/checkout/review-order.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/review-order.php`

### Override `woocommerce/checkout/versions/form-billing-v1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-billing-v1.php`

### Override `woocommerce/checkout/versions/form-billing-v2.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-billing-v2.php`

### Override `woocommerce/checkout/versions/form-checkout-v1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-checkout-v1.php`

### Override `woocommerce/checkout/versions/form-checkout-v2.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-checkout-v2.php`

### Override `woocommerce/checkout/versions/form-shipping-v1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-shipping-v1.php`

### Override `woocommerce/checkout/versions/form-shipping-v2.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/form-shipping-v2.php`

### Override `woocommerce/checkout/versions/review-order-v1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/review-order-v1.php`

### Override `woocommerce/checkout/versions/review-order-v2.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/checkout/versions/review-order-v2.php`

### Override `woocommerce/gallery-large-video-layout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/gallery-large-video-layout.php`

### Override `woocommerce/gallery.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/gallery.php`

### Override `woocommerce/myaccount/dashboard1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/dashboard1.php`

### Override `woocommerce/myaccount/downloads.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/downloads.php`

### Override `woocommerce/myaccount/form-add-payment-method1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-add-payment-method1.php`

### Override `woocommerce/myaccount/form-edit-account1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-edit-account1.php`

### Override `woocommerce/myaccount/form-edit-address.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-edit-address.php`

### Override `woocommerce/myaccount/form-login.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-login.php`

### Override `woocommerce/myaccount/form-lost-password.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-lost-password.php`

### Override `woocommerce/myaccount/form-reset-password.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/form-reset-password.php`

### Override `woocommerce/myaccount/lost-password-confirmation.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/lost-password-confirmation.php`

### Override `woocommerce/myaccount/my-account.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/my-account.php`

### Override `woocommerce/myaccount/my-address1.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/my-address1.php`

### Override `woocommerce/myaccount/my-downloads.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/my-downloads.php`

### Override `woocommerce/myaccount/my-orders.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/my-orders.php`

### Override `woocommerce/myaccount/navigation.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/navigation.php`

### Override `woocommerce/myaccount/orders.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/orders.php`

### Override `woocommerce/myaccount/payment-methods.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/payment-methods.php`

### Override `woocommerce/myaccount/view-order.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/myaccount/view-order.php`

### Override `woocommerce/new-gallery.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/new-gallery.php`

### Override `woocommerce/pdp-versions/default-layout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/default-layout.php`

### Override `woocommerce/pdp-versions/features-list-layout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/features-list-layout.php`

### Override `woocommerce/pdp-versions/single-image-layout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/single-image-layout.php`

### Override `woocommerce/pdp-versions/tabs-layout.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout.php`

### Override `woocommerce/pdp-versions/tabs-layout/_buy-box-gifts.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_buy-box-gifts.php`

### Override `woocommerce/pdp-versions/tabs-layout/_buy-box-regular.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_buy-box-regular.php`

### Override `woocommerce/pdp-versions/tabs-layout/_buy-box-sub-one-time.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_buy-box-sub-one-time.php`

### Override `woocommerce/pdp-versions/tabs-layout/_gallery.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_gallery.php`

### Override `woocommerce/pdp-versions/tabs-layout/_init.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_init.php`

### Override `woocommerce/pdp-versions/tabs-layout/_product-info.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_product-info.php`

### Override `woocommerce/pdp-versions/tabs-layout/_quiz-banner.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/pdp-versions/tabs-layout/_quiz-banner.php`

### Override `woocommerce/product-page/countdown.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/product-page/countdown.php`

### Override `woocommerce/product-page/lp-top-block.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/product-page/lp-top-block.php`

### Override `woocommerce/product-page/price-block.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/product-page/price-block.php`

### Override `woocommerce/single-product-2284761.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/single-product-2284761.php`

### Override `woocommerce/single-product-lifedrive.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/single-product-lifedrive.php`

### Override `woocommerce/single-product.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/single-product.php`

### Override `woocommerce/video-section.php`

- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.
- **Relevance:** High
- **Transferability:** Partial — Liquid / Checkout Extensibility.
- **Evidence:** `wp-content/themes/particleformen/woocommerce/video-section.php`

## 6. Custom post type (theme)

### CPT `landing_pages`

- **Description:** Registered in `lib/custom-post-types.php` with `rewrite.slug = lpage`. Public REST-enabled landing content type.
- **Relevance:** High
- **Transferability:** Partial — Shopify Pages or metaobject landing model + URL redirects.

## 7. REST and webhooks (non–pfm-panel highlights)

### `twilio-api/v1` verify & send

- **Description:** Theme `lib/rest-api.php` — SMS / verification flows.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `klaviyo-api/v1` profile, amazon, consultation, sweepstakes-webhook

- **Description:** Theme `lib/rest-api.php` — server-side Klaviyo profile updates.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `email/v1` verify_email

- **Description:** Theme `lib/rest-api.php`.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `braintree/v1` dispute-webhook

- **Description:** Theme `lib/rest-api.php` — Braintree disputes to orders.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `woo/v1` order-notes & subscription-notes

- **Description:** Theme `lib/rest-api.php`.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `get-data/v1` openai-crawlers/overview

- **Description:** Theme `lib/rest-api.php`.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `shipbob/v1` order_shipped, shipment_exception, shipment_delivered

- **Description:** `warehouse-export` plugin ShipBob class.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `v1` order-shipped/green

- **Description:** `warehouse-export` Green warehouse webhook.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `pfm-monday-coupons` REST

- **Description:** `pfm-monday-coupons` — coupon API for external automation.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `yotpo-integration/v1` create-coupon & cancel-coupon

- **Description:** Yotpo loyalty coupon lifecycle.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `pfm-tools-utils` REST

- **Description:** Multiple utility endpoints — read `pfm-tools-utils.php`.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `pfm-chargebacks-utils` REST

- **Description:** Chargeback lookup by order.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `pfm-geo-privacy` REST

- **Description:** Geo privacy endpoint.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `sellence-api` /products & /coupons

- **Description:** External catalog/coupon feed.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `wunderkind/v1` feed

- **Description:** Wunderkind product feed.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `orderswidget/v1` summary

- **Description:** Order summary widget API.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### `om-map/v1` map, bulk-map, nonce

- **Description:** mu-plugin OptinMonster map output if present.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### Klaviyo `class-wck-api.php` REST

- **Description:** Official Klaviyo plugin endpoints.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

### Yoast / WP Rocket REST

- **Description:** Admin-only REST for SEO/cache — low migration priority.
- **Relevance:** Medium to High depending on consumer systems.
- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.

## 8. MU-plugins and host (custom subset)

### MU-plugin `pfm-braintree-api-access.php`

- **Description:** Braintree API access helper for server-side operations.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/mu-plugins/pfm-braintree-api-access.php`

### MU-plugin `redirections.php`

- **Description:** WPML Redirect: language detection, `store_switch` cookie, URL fixes.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/mu-plugins/redirections.php`

### MU-plugin `pfm-performance.php`

- **Description:** Performance-related mu-plugin (theme-adjacent).
- **Relevance:** Medium
- **Transferability:** N/A
- **Evidence:** `wp-content/mu-plugins/pfm-performance.php`

### MU-plugin `custom_plugin_organizer.php`

- **Description:** Plugin load order, dashboard tweaks, cart removed_item redirect with WPML prefix.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/mu-plugins/custom_plugin_organizer.php`

### MU-plugin `woocommerce-additional.php`

- **Description:** Additional Woo hooks at mu level — audit contents.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/mu-plugins/woocommerce-additional.php`

### MU-plugin `om-map-output.php`

- **Description:** OptinMonster map REST if loaded.
- **Relevance:** Low
- **Transferability:** Partial
- **Evidence:** `wp-content/mu-plugins/om-map-output.php`

### WP Engine mu-plugins (`wpengine-*`, `wpe-*`, `slt-force-strong-passwords`, etc.)

- **Description:** Hosting vendor auto-loaded plugins: caching, SSO, security auditor, update source, etc.
- **Relevance:** Low for Shopify storefront parity
- **Transferability:** N/A — not part of Shopify; decommission with WP.

## 9. Static scrape inputs (reference)

- **Description:** Local HTML snapshots under `C:\Users\denis_particleformen\Desktop\Cursor Projects\particleformen-scrape\output\html` validate enqueued plugins, `hreflang` URL patterns, `?purchase-type=subscription`, `?store_switch=`.
- **Relevance:** Medium (evidence for Phase G validation)
- **Transferability:** N/A — research artifact.

## 10. `pfm-panel` REST API — individual routes (`pfm-panel/v1`)

Each route is an internal operations capability to map to **Shopify Admin API**, **custom app**, or **retired workflow**.

### `GET|POST /wp-json/pfm-panel/v1/orders`

- **Description:** Order collection or creation entrypoint (see `class-pfmp-rest-orders.php` for methods).
- **Relevance:** High
- **Transferability:** Not transferable — Admin API `orders.json` + app auth.

### `GET|PUT|PATCH /wp-json/pfm-panel/v1/orders/{id}`

- **Description:** Single order read/update.
- **Relevance:** High
- **Transferability:** Not transferable — Admin API orders.

### `GET /wp-json/pfm-panel/v1/orders/by-user/{user_id}`

- **Description:** Orders for a given WP user id.
- **Relevance:** High
- **Transferability:** Partial — Shopify customer order lookup.

### `POST /wp-json/pfm-panel/v1/orders/{order_id}/revalidate-address`

- **Description:** Re-run address validation for an order.
- **Relevance:** High
- **Transferability:** Partial — address validation app + order edit.

### `POST /wp-json/pfm-panel/v1/orders/{order_id}/export-to-warehouse`

- **Description:** Push order to warehouse / WMS export pipeline.
- **Relevance:** High
- **Transferability:** Partial — fulfillment webhooks.

### `POST /wp-json/pfm-panel/v1/orders/bulk`

- **Description:** Bulk order operations.
- **Relevance:** High
- **Transferability:** Partial — Bulk Admin API / background jobs.

### `POST /wp-json/pfm-panel/v1/orders/{id}/edit`

- **Description:** Edit order fields from internal panel.
- **Relevance:** High
- **Transferability:** Partial — order edits in Shopify admin / app.

### `GET /wp-json/pfm-panel/v1/products-by-category`

- **Description:** Product picker data for internal tools.
- **Relevance:** Medium
- **Transferability:** Partial — Admin API products query.

### `GET|POST /wp-json/pfm-panel/v1/orders/{order_id}/notes`

- **Description:** Order notes CRUD for ops.
- **Relevance:** Medium
- **Transferability:** Full — order notes exist on Shopify.

### `GET /wp-json/pfm-panel/v1/customers/search`

- **Description:** Search customers for support panel.
- **Relevance:** High
- **Transferability:** Partial — Admin API customer search.

### `GET /wp-json/pfm-panel/v1/orders/latest-id`

- **Description:** Polling helper for newest order id.
- **Relevance:** Medium
- **Transferability:** Not transferable — replace with webhooks.

### `GET /wp-json/pfm-panel/v1/orders/braintree-info`

- **Description:** Braintree payment metadata for an order.
- **Relevance:** High
- **Transferability:** Partial — payment app + order transactions.

### `GET /wp-json/pfm-panel/v1/orders/{order_id}/preview`

- **Description:** Order preview (HTML/PDF context — confirm in code).
- **Relevance:** Medium
- **Transferability:** Partial.

### `GET /wp-json/pfm-panel/v1/orders/{order_id}/narvar-tracking-url`

- **Description:** Resolve Narvar tracking link for order.
- **Relevance:** High
- **Transferability:** Partial — Narvar on Shopify.

### `POST /wp-json/pfm-panel/v1/orders/{id}/resend-email`

- **Description:** Resend transactional email for order.
- **Relevance:** Medium
- **Transferability:** Partial — notification APIs.

### `GET /wp-json/pfm-panel/v1/orders/status-counts`

- **Description:** Dashboard counts by order status.
- **Relevance:** Medium
- **Transferability:** Partial — GraphQL/Admin API aggregates.

### `GET|POST /wp-json/pfm-panel/v1/subscriptions`

- **Description:** Subscription list/create surface.
- **Relevance:** High
- **Transferability:** Partial — Shopify Subscriptions contract APIs.

### `GET|PUT|PATCH /wp-json/pfm-panel/v1/subscriptions/{id}`

- **Description:** Single subscription read/update.
- **Relevance:** High
- **Transferability:** Partial.

### `GET /wp-json/pfm-panel/v1/subscriptions/products`

- **Description:** Subscribable products listing for panel.
- **Relevance:** High
- **Transferability:** Partial — selling plans on products.

### `POST /wp-json/pfm-panel/v1/subscriptions/{id}/edit`

- **Description:** Subscription line / schedule edits.
- **Relevance:** High
- **Transferability:** Partial.

### `POST /wp-json/pfm-panel/v1/subscriptions/{id}/actions`

- **Description:** Subscription actions (pause, cancel, etc. — confirm in code).
- **Relevance:** High
- **Transferability:** Partial.

### `GET /wp-json/pfm-panel/v1/subscriptions/by-user/{id}`

- **Description:** Subscriptions for customer.
- **Relevance:** High
- **Transferability:** Partial.

### `GET|POST /wp-json/pfm-panel/v1/subscriptions/{subscription_id}/notes`

- **Description:** Subscription notes for ops.
- **Relevance:** Medium
- **Transferability:** Partial.

### `POST /wp-json/pfm-panel/v1/orders/{order_id}/retry-payment`

- **Description:** Retry failed renewal or order payment.
- **Relevance:** High
- **Transferability:** Partial — dunning in subscription app.

### `POST /wp-json/pfm-panel/v1/orders/{id}/refund`

- **Description:** Issue refund from panel.
- **Relevance:** High
- **Transferability:** Partial — Refund Admin API.

### `POST /wp-json/pfm-panel/v1/orders/{id}/refund-via-credits`

- **Description:** Refund path applying store credits.
- **Relevance:** High
- **Transferability:** Partial — gift card / credit patterns on Shopify.

### `GET|POST /wp-json/pfm-panel/v1/customers`

- **Description:** Customer list/create for internal tools.
- **Relevance:** High
- **Transferability:** Partial — Admin API customers.

### `GET|PUT /wp-json/pfm-panel/v1/customers/{id}`

- **Description:** Customer detail/update.
- **Relevance:** High
- **Transferability:** Partial.

### `POST /wp-json/pfm-panel/v1/customers/{id}/assume_user`

- **Description:** Support impersonation / switch-to-customer session helper.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify staff + customer merge policies.

### `GET|POST /wp-json/pfm-panel/v1/customers/{id}/yotpo` and `/yotpo-adjust`

- **Description:** Yotpo points or loyalty adjustments from panel.
- **Relevance:** Medium
- **Transferability:** Partial — Yotpo Shopify APIs.

### `GET|POST /wp-json/pfm-panel/v1/customers/{id}/store-credits` and `/store-credits-adjust`

- **Description:** View/adjust Woo store credit balance from panel.
- **Relevance:** High
- **Transferability:** Partial — Shopify store credit / gift cards.

### `GET|POST /wp-json/pfm-panel/v1/replacements` (collection + nested)

- **Description:** Replacement order workflow mirroring orders (list, get, notes, edit, export, revalidate, Narvar, resend).
- **Relevance:** High
- **Transferability:** Partial — exchanges/replacement apps or custom flows.

### `GET /wp-json/pfm-panel/v1/replacements/reasons` and `/creators`

- **Description:** Metadata for replacement reasons and creating agents.
- **Relevance:** Medium
- **Transferability:** Partial — metaobjects or app config.

### `GET|POST /wp-json/pfm-panel/v1/admin-actions` (+ `/action-types`, `/admins`, `/resource-types`)

- **Description:** Audit log / admin action tracking for internal compliance.
- **Relevance:** Medium
- **Transferability:** Partial — app event log.

### `POST /wp-json/pfm-panel/v1/reports/run` (+ `/upload`, `/history`)

- **Description:** Run or upload custom CSV/report pipelines from panel.
- **Relevance:** High
- **Transferability:** Not transferable — rebuild reporting against Shopify data export.

### `GET /wp-json/pfm-panel/v1/coupons` and `/coupons/categories`

- **Description:** Coupon search and category metadata for ops.
- **Relevance:** High
- **Transferability:** Partial — Discount Admin API.

### `GET /wp-json/pfm-panel/v1/stats/orders` and `/stats/orders/timeseries`

- **Description:** Internal analytics for order volume.
- **Relevance:** Medium
- **Transferability:** Partial — ShopifyQL / analytics apps.

## 11. Installed plugins (exhaustive)
_Total folders: **152** (alphabetical). Each row is one installable component._
### `PriorityAPI`
- **Description:** Priority ERP API integration.
- **Relevance:** High
- **Transferability:** Partial — middleware posting Shopify orders to Priority.
- **Evidence:** `wp-content/plugins/PriorityAPI`
### `PriorityApiCustomCode`
- **Description:** Custom code layer on Priority API.
- **Relevance:** High
- **Transferability:** Not transferable — port to middleware.
- **Evidence:** `wp-content/plugins/PriorityApiCustomCode`
### `WooCommercePriorityAPI`
- **Description:** Alternate or layered Priority Woo bridge — confirm active.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/WooCommercePriorityAPI`
### `account-page-recommended-products`
- **Description:** Recommended products on account page.
- **Relevance:** Medium
- **Transferability:** Partial — personalization app or theme.
- **Evidence:** `wp-content/plugins/account-page-recommended-products`
### `add-search-to-menu`
- **Description:** Third-party or vendor extension present in `wp-content/plugins/add-search-to-menu/`. Confirm active modules, license, and any customizations in production.
- **Relevance:** Medium
- **Transferability:** Partial — map to Shopify native feature, first-party channel, or app; validate data migration.
- **Evidence:** `wp-content/plugins/add-search-to-menu`
### `add_upsells_option_ms`
- **Description:** Adds upsell options to subscription/cart flows (custom).
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/add_upsells_option_ms`
### `advanced-cron-manager`
- **Description:** Cron UI for WP.
- **Relevance:** Low
- **Transferability:** N/A — Shopify scheduled jobs via apps.
- **Evidence:** `wp-content/plugins/advanced-cron-manager`
### `advanced-custom-fields-pro`
- **Description:** ACF Pro fields on pages/products/options.
- **Relevance:** High
- **Transferability:** Partial — metafields + metaobject definitions + admin UI.
- **Evidence:** `wp-content/plugins/advanced-custom-fields-pro`
### `afterpay-gateway-for-woocommerce`
- **Description:** Afterpay / Clearpay BNPL.
- **Relevance:** Medium
- **Transferability:** Partial — Shop Pay Installments / Afterpay Shopify.
- **Evidence:** `wp-content/plugins/afterpay-gateway-for-woocommerce`
### `aftership-woocommerce-tracking`
- **Description:** AfterShip tracking.
- **Relevance:** Medium
- **Transferability:** Partial — AfterShip app.
- **Evidence:** `wp-content/plugins/aftership-woocommerce-tracking`
### `alert-system`
- **Description:** Internal alerts.
- **Relevance:** Medium
- **Transferability:** Partial — Slack/email from Flow.
- **Evidence:** `wp-content/plugins/alert-system`
### `all-upsells`
- **Description:** Upsell flows: thank-you page, post-purchase, BAS/PPU modules (see `includes/`).
- **Relevance:** High
- **Transferability:** Partial — post-purchase apps, checkout upsell extensions.
- **Evidence:** `wp-content/plugins/all-upsells`
### `blotout-edgetag`
- **Description:** Blotout EdgeTag / customer data platform.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify Customer Privacy + server pixels.
- **Evidence:** `wp-content/plugins/blotout-edgetag`
### `bluesnap-payment-gateway-for-woocommerce`
- **Description:** BlueSnap payment gateway.
- **Relevance:** High
- **Transferability:** Partial — Shopify payment provider availability; may require different PSP.
- **Evidence:** `wp-content/plugins/bluesnap-payment-gateway-for-woocommerce`
### `braintree-saved-token-gateway`
- **Description:** Braintree vaulted cards / gateway.
- **Relevance:** High
- **Transferability:** Partial — Shopify Payments vs Braintree; token migration project.
- **Evidence:** `wp-content/plugins/braintree-saved-token-gateway`
### `card-checkout-ms`
- **Description:** Checkout card UI / testimonial carousel (custom).
- **Relevance:** Medium
- **Transferability:** Partial — theme + checkout extensions.
- **Evidence:** `wp-content/plugins/card-checkout-ms`
### `cart-sidebar`
- **Description:** Slide-out cart UI; integrates WPML/WCML currency and product ID mapping.
- **Relevance:** High
- **Transferability:** Partial — cart drawer theme + AJAX cart APIs on Shopify.
- **Evidence:** `wp-content/plugins/cart-sidebar`
### `cart-sidebar-v2`
- **Description:** Alternate cart sidebar implementation — confirm which is primary in production.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/cart-sidebar-v2`
### `codepress-admin-columns`
- **Description:** Admin list column customization.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/codepress-admin-columns`
### `complyt-address-validator`
- **Description:** Complyt address validation.
- **Relevance:** High
- **Transferability:** Partial — address validation at checkout.
- **Evidence:** `wp-content/plugins/complyt-address-validator`
### `custom-coupon`
- **Description:** Custom coupon logic beyond core Woo coupons.
- **Relevance:** High
- **Transferability:** Partial — Shopify Discount Functions / discount apps.
- **Evidence:** `wp-content/plugins/custom-coupon`
### `duracelltomi-google-tag-manager`
- **Description:** GTM container injection and dataLayer.
- **Relevance:** High
- **Transferability:** Full — GTM in theme or Shopify app.
- **Evidence:** `wp-content/plugins/duracelltomi-google-tag-manager`
### `empty-cart-upsells`
- **Description:** Upsells when cart empty.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/empty-cart-upsells`
### `export-refunds-to-csv`
- **Description:** Export refunds to CSV.
- **Relevance:** Low
- **Transferability:** Partial — reporting export from Shopify.
- **Evidence:** `wp-content/plugins/export-refunds-to-csv`
### `export-stats`
- **Description:** Export stats to Google Sheets.
- **Relevance:** Medium
- **Transferability:** Partial — Analytics API / Sheets.
- **Evidence:** `wp-content/plugins/export-stats`
### `facebook-store-integration`
- **Description:** Facebook / Meta catalog integration.
- **Relevance:** Medium
- **Transferability:** Partial — Meta sales channel.
- **Evidence:** `wp-content/plugins/facebook-store-integration`
### `fermiac-siftscience-for-woocommerce`
- **Description:** Sift Science integration for Woo.
- **Relevance:** High
- **Transferability:** Partial — Shopify Fraud / third-party.
- **Evidence:** `wp-content/plugins/fermiac-siftscience-for-woocommerce`
### `force-default-variant-for-woocommerce`
- **Description:** Forces default variation selection when variations exist.
- **Relevance:** Low
- **Transferability:** Partial — rarely needed if SKUs are simple; confirm use.
- **Evidence:** `wp-content/plugins/force-default-variant-for-woocommerce`
### `force-regenerate-thumbnails`
- **Description:** Regenerate attachment sizes.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/force-regenerate-thumbnails`
### `gravite-landing-pages`
- **Description:** Gravité-specific landing page templates.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/gravite-landing-pages`
### `impact-partnership-cloud`
- **Description:** Impact affiliate / partnership tracking.
- **Relevance:** Medium
- **Transferability:** Partial — Impact Shopify integration.
- **Evidence:** `wp-content/plugins/impact-partnership-cloud`
### `inspect-http-requests`
- **Description:** Inspect HTTP requests in admin.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/inspect-http-requests`
### `japan-landing-pages`
- **Description:** Japan market landing pages.
- **Relevance:** Medium
- **Transferability:** Partial — Markets + templates.
- **Evidence:** `wp-content/plugins/japan-landing-pages`
### `kadence-woocommerce-email-designer`
- **Description:** Kadence Woo email template designer.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify Notifications customization.
- **Evidence:** `wp-content/plugins/kadence-woocommerce-email-designer`
### `klaviyo`
- **Description:** Klaviyo official Woo plugin: events, lists, forms.
- **Relevance:** High
- **Transferability:** Full — Klaviyo Shopify integration.
- **Evidence:** `wp-content/plugins/klaviyo`
### `klaviyo-wp`
- **Description:** Additional Klaviyo WordPress integration package.
- **Relevance:** High
- **Transferability:** Full
- **Evidence:** `wp-content/plugins/klaviyo-wp`
### `kount-fraud-prevention`
- **Description:** Kount fraud screening on checkout.
- **Relevance:** High
- **Transferability:** Partial — Kount for Shopify or equivalent.
- **Evidence:** `wp-content/plugins/kount-fraud-prevention`
### `kount-orders-report`
- **Description:** Third-party or vendor extension present in `wp-content/plugins/kount-orders-report/`. Confirm active modules, license, and any customizations in production.
- **Relevance:** Medium
- **Transferability:** Partial — map to Shopify native feature, first-party channel, or app; validate data migration.
- **Evidence:** `wp-content/plugins/kount-orders-report`
### `landing-pages`
- **Description:** Landing page plugin with blocks and templates (e.g. Marsmen-like LP).
- **Relevance:** High
- **Transferability:** Partial — Shopify Pages + metaobjects + theme sections.
- **Evidence:** `wp-content/plugins/landing-pages`
### `livecart-by-wp-engine`
- **Description:** WP Engine LiveCart integration.
- **Relevance:** Low
- **Transferability:** N/A — host-specific.
- **Evidence:** `wp-content/plugins/livecart-by-wp-engine`
### `loco-translate`
- **Description:** Translate theme/plugin strings locally.
- **Relevance:** Medium
- **Transferability:** Partial — locale JSON / Markets.
- **Evidence:** `wp-content/plugins/loco-translate`
### `log-http-requests`
- **Description:** Logs outbound HTTP for debugging.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/log-http-requests`
### `login-visit-counter`
- **Description:** Tracks login visits.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/login-visit-counter`
### `metorik-helper`
- **Description:** Metorik analytics helper for Woo.
- **Relevance:** Medium
- **Transferability:** Partial — Metorik Shopify.
- **Evidence:** `wp-content/plugins/metorik-helper`
### `metronet-profile-picture`
- **Description:** Profile pictures for users.
- **Relevance:** Low
- **Transferability:** Partial — customer account profile apps.
- **Evidence:** `wp-content/plugins/metronet-profile-picture`
### `myplugin`
- **Description:** Placeholder or small custom plugin — audit contents.
- **Relevance:** Low
- **Transferability:** Not transferable — audit contents.
- **Evidence:** `wp-content/plugins/myplugin`
### `myscripts`
- **Description:** Custom scripts plugin (site-specific).
- **Relevance:** Medium
- **Transferability:** Not transferable — audit contents.
- **Evidence:** `wp-content/plugins/myscripts`
### `narvar-tracking-integration`
- **Description:** Narvar post-purchase tracking / comms.
- **Relevance:** High
- **Transferability:** Partial — Narvar Shopify integration.
- **Evidence:** `wp-content/plugins/narvar-tracking-integration`
### `newrelic-transaction-renamer`
- **Description:** Renames New Relic transactions for WP.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/newrelic-transaction-renamer`
### `optinmonster`
- **Description:** OptinMonster lead capture.
- **Relevance:** Medium
- **Transferability:** Partial — OM Shopify embed.
- **Evidence:** `wp-content/plugins/optinmonster`
### `orders-pay-verify`
- **Description:** Order pay verification flow.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/orders-pay-verify`
### `orderswidget-summary`
- **Description:** REST `orderswidget/v1/summary` for order summaries.
- **Relevance:** Low
- **Transferability:** Not transferable
- **Evidence:** `wp-content/plugins/orderswidget-summary`
### `outersignal-order-export`
- **Description:** Order export to Outersignal.
- **Relevance:** Medium
- **Transferability:** Partial — webhooks.
- **Evidence:** `wp-content/plugins/outersignal-order-export`
### `package_protection_ms`
- **Description:** Package protection upsell on checkout.
- **Relevance:** Medium
- **Transferability:** Partial — shipping protection apps.
- **Evidence:** `wp-content/plugins/package_protection_ms`
### `particleformen-checkout`
- **Description:** Custom checkout behaviors for Particle (see plugin + theme `lib/checkout.php`).
- **Relevance:** High
- **Transferability:** Partial — Shopify Checkout extensibility (UI extensions, Functions) + apps.
- **Evidence:** `wp-content/plugins/particleformen-checkout`
### `pfm-chargebacks-utils`
- **Description:** Chargeback utilities + REST.
- **Relevance:** Medium
- **Transferability:** Partial — payment processor dashboards.
- **Evidence:** `wp-content/plugins/pfm-chargebacks-utils`
### `pfm-checkout-bot-block`
- **Description:** Bot blocking on checkout.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify bot protection + CAPTCHA apps.
- **Evidence:** `wp-content/plugins/pfm-checkout-bot-block`
### `pfm-checkout-observer`
- **Description:** Observes checkout events (logging / risk / analytics — confirm).
- **Relevance:** High
- **Transferability:** Partial — webhooks + Flow.
- **Evidence:** `wp-content/plugins/pfm-checkout-observer`
### `pfm-csv-uploader`
- **Description:** Admin CSV upload utilities.
- **Relevance:** Medium
- **Transferability:** N/A — Shopify bulk import / Admin API.
- **Evidence:** `wp-content/plugins/pfm-csv-uploader`
### `pfm-geo-privacy`
- **Description:** Geo / privacy gate (REST namespace).
- **Relevance:** High
- **Transferability:** Partial — Markets + consent apps.
- **Evidence:** `wp-content/plugins/pfm-geo-privacy`
### `pfm-holiday-season`
- **Description:** Seasonal promos / toggles.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify scheduled discounts.
- **Evidence:** `wp-content/plugins/pfm-holiday-season`
### `pfm-kill-injected-ui`
- **Description:** Removes unwanted injected admin or frontend UI.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/pfm-kill-injected-ui`
### `pfm-klaviyo-monitor`
- **Description:** Monitoring / hooks for Klaviyo health.
- **Relevance:** Low
- **Transferability:** N/A — ops tooling; replace with monitoring on new stack.
- **Evidence:** `wp-content/plugins/pfm-klaviyo-monitor`
### `pfm-monday-coupons`
- **Description:** REST-driven coupon integration (Monday workflow).
- **Relevance:** Medium
- **Transferability:** Partial — Zapier/Flow + discount APIs.
- **Evidence:** `wp-content/plugins/pfm-monday-coupons`
### `pfm-panel`
- **Description:** Internal operations REST API (`pfm-panel/v1`): orders, subscriptions, refunds, customers, coupons, replacements, reports, warehouse export, Narvar, Braintree info, stats, admin actions.
- **Relevance:** High
- **Transferability:** Not transferable — replace with Shopify Admin API + custom internal app or Retool.
- **Evidence:** `wp-content/plugins/pfm-panel`
### `pfm-signifyd-integration`
- **Description:** Signifyd fraud scoring / order submission.
- **Relevance:** High
- **Transferability:** Partial — Signifyd Shopify app or custom integration.
- **Evidence:** `wp-content/plugins/pfm-signifyd-integration`
### `pfm-skincare-quiz`
- **Description:** Particle skincare quiz templates and flow.
- **Relevance:** High
- **Transferability:** Partial — rebuild as theme section or app.
- **Evidence:** `wp-content/plugins/pfm-skincare-quiz`
### `pfm-smarty-address-validator`
- **Description:** Smarty (USPS) address validation.
- **Relevance:** High
- **Transferability:** Partial — Smarty or equivalent on Shopify.
- **Evidence:** `wp-content/plugins/pfm-smarty-address-validator`
### `pfm-store-credits`
- **Description:** Store credit balance and checkout application (frontend + admin).
- **Relevance:** High
- **Transferability:** Partial — Shopify store credit / gift card primitives differ; likely app or custom.
- **Evidence:** `wp-content/plugins/pfm-store-credits`
### `pfm-tools-utils`
- **Description:** Misc internal tools + REST routes.
- **Relevance:** Medium
- **Transferability:** Not transferable
- **Evidence:** `wp-content/plugins/pfm-tools-utils`
### `pixelyoursite-pro`
- **Description:** PixelYourSite: Meta/CAPI/GA events.
- **Relevance:** High
- **Transferability:** Partial — PYS Shopify or server events.
- **Evidence:** `wp-content/plugins/pixelyoursite-pro`
### `pixelyoursite-super-pack`
- **Description:** PYS add-on pack.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/pixelyoursite-super-pack`
### `post-duplicator`
- **Description:** Duplicate posts/pages for editors.
- **Relevance:** Low
- **Transferability:** N/A — editor workflow.
- **Evidence:** `wp-content/plugins/post-duplicator`
### `post-orders-to-priority`
- **Description:** Pushes orders to Priority system.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/post-orders-to-priority`
### `post-purchase-upsell`
- **Description:** Post-purchase one-click upsell.
- **Relevance:** High
- **Transferability:** Partial — post-purchase apps.
- **Evidence:** `wp-content/plugins/post-purchase-upsell`
### `post-smtp`
- **Description:** SMTP mailer for WP emails.
- **Relevance:** Medium
- **Transferability:** N/A — Shopify email domain; transactional via apps.
- **Evidence:** `wp-content/plugins/post-smtp`
### `preorder-products`
- **Description:** Preorder selling for products.
- **Relevance:** Medium
- **Transferability:** Partial — preorder apps.
- **Evidence:** `wp-content/plugins/preorder-products`
### `product-guide`
- **Description:** Product guide experience.
- **Relevance:** Medium
- **Transferability:** Partial — content pages + metafields.
- **Evidence:** `wp-content/plugins/product-guide`
### `product-landing-pages`
- **Description:** Product-scoped landing experiences.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/product-landing-pages`
### `purchase-push-notifications`
- **Description:** Push notifications on purchase.
- **Relevance:** Low
- **Transferability:** Partial — mobile app channel if applicable.
- **Evidence:** `wp-content/plugins/purchase-push-notifications`
### `quiz`
- **Description:** Generic quiz plugin for Particle.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/quiz`
### `recaptcha-for-woocommerce`
- **Description:** reCAPTCHA on Woo checkout/account.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify bot challenge / apps.
- **Evidence:** `wp-content/plugins/recaptcha-for-woocommerce`
### `redirection`
- **Description:** 301/302 redirect manager and logs.
- **Relevance:** High
- **Transferability:** Partial — Shopify URL redirects (import).
- **Evidence:** `wp-content/plugins/redirection`
### `richpanel-for-woocommerce`
- **Description:** Richpanel helpdesk + customer timeline for Woo orders.
- **Relevance:** High
- **Transferability:** Partial — Richpanel Shopify app.
- **Evidence:** `wp-content/plugins/richpanel-for-woocommerce`
### `scheduled-actions`
- **Description:** Action Scheduler tables (often bundled with Woo).
- **Relevance:** Medium
- **Transferability:** N/A — platform cron/queues differ.
- **Evidence:** `wp-content/plugins/scheduled-actions`
### `sellence-api`
- **Description:** Sellence REST API (`/products`, `/coupons`).
- **Relevance:** Medium
- **Transferability:** Partial — custom app on Shopify.
- **Evidence:** `wp-content/plugins/sellence-api`
### `shipbob-integration`
- **Description:** ShipBob fulfillment integration.
- **Relevance:** High
- **Transferability:** Partial — ShipBob Shopify connector or order webhook app.
- **Evidence:** `wp-content/plugins/shipbob-integration`
### `show-current-template`
- **Description:** Dev: shows current PHP template.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/show-current-template`
### `sift-wp`
- **Description:** Sift-related WordPress glue.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/sift-wp`
### `sitemap-custom`
- **Description:** Custom sitemap generation for Particle.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify sitemap + hreflang via Markets.
- **Evidence:** `wp-content/plugins/sitemap-custom`
### `sitepress-multilingual-cms`
- **Description:** WPML core: multilingual posts, menus, hreflang, translation workflow. Deep integration in theme (`wpml_*` filters), cart, optimization.
- **Relevance:** High
- **Transferability:** Partial — Shopify Markets + Translate & Adapt (or third-party); URL/hreflang rules must be redesigned.
- **Evidence:** `wp-content/plugins/sitepress-multilingual-cms`
### `sky-wcs-no-periods`
- **Description:** Cleans subscription product titles (removes periods).
- **Relevance:** Low
- **Transferability:** Partial — naming in Shopify subscriptions.
- **Evidence:** `wp-content/plugins/sky-wcs-no-periods`
### `smtp-mailgun-connector`
- **Description:** Mailgun SMTP connector.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/smtp-mailgun-connector`
### `special-shipping-methods`
- **Description:** Custom shipping methods / rules.
- **Relevance:** High
- **Transferability:** Partial — carrier service + Functions or shipping apps.
- **Evidence:** `wp-content/plugins/special-shipping-methods`
### `stampedio`
- **Description:** Stamped.io reviews widgets / integration.
- **Relevance:** High
- **Transferability:** Partial — Stamped Shopify.
- **Evidence:** `wp-content/plugins/stampedio`
### `stampedio-product-reviews`
- **Description:** Stamped product reviews companion.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/stampedio-product-reviews`
### `sticky-cta`
- **Description:** Sticky CTA bar.
- **Relevance:** Medium
- **Transferability:** Partial — theme.
- **Evidence:** `wp-content/plugins/sticky-cta`
### `subscriptions-utils`
- **Description:** Custom utilities around Woo subscriptions (see plugin code for hooks).
- **Relevance:** High
- **Transferability:** Not transferable — rebuild in Shopify Flow / subscription app / custom app as needed.
- **Evidence:** `wp-content/plugins/subscriptions-utils`
### `tax-helper`
- **Description:** Tax helper utilities for Woo.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/tax-helper`
### `ticket-submissions`
- **Description:** Support ticket submission from site.
- **Relevance:** Medium
- **Transferability:** Partial — forms app / Zendesk / Gorgias.
- **Evidence:** `wp-content/plugins/ticket-submissions`
### `tiktok-shop-integration`
- **Description:** TikTok Shop / catalog sync.
- **Relevance:** Medium
- **Transferability:** Partial — TikTok for Shopify.
- **Evidence:** `wp-content/plugins/tiktok-shop-integration`
### `tinymce-advanced`
- **Description:** Classic editor enhancements.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/tinymce-advanced`
### `trustpilot-integration`
- **Description:** Trustpilot integration glue.
- **Relevance:** Medium
- **Transferability:** Full
- **Evidence:** `wp-content/plugins/trustpilot-integration`
### `trustpilot-widget`
- **Description:** Trustpilot widget embed.
- **Relevance:** Medium
- **Transferability:** Full — Trustpilot Shopify app/widget.
- **Evidence:** `wp-content/plugins/trustpilot-widget`
### `try-before-you-buy`
- **Description:** Try before you buy program.
- **Relevance:** Medium
- **Transferability:** Partial — TBYB apps.
- **Evidence:** `wp-content/plugins/try-before-you-buy`
### `two-factor-authentication-premium`
- **Description:** 2FA for WP admin/logins.
- **Relevance:** Medium
- **Transferability:** N/A — Shopify org security; customer 2FA via apps if needed.
- **Evidence:** `wp-content/plugins/two-factor-authentication-premium`
### `user-role-editor`
- **Description:** WP role/capability editor.
- **Relevance:** Low
- **Transferability:** N/A — Shopify staff permissions.
- **Evidence:** `wp-content/plugins/user-role-editor`
### `user-switching`
- **Description:** Switch user for support testing.
- **Relevance:** Low
- **Transferability:** N/A — Shopify staff impersonation patterns differ.
- **Evidence:** `wp-content/plugins/user-switching`
### `walmart-marketplace-integration`
- **Description:** Walmart marketplace listing / orders.
- **Relevance:** Medium
- **Transferability:** Partial — Walmart Shopify channel.
- **Evidence:** `wp-content/plugins/walmart-marketplace-integration`
### `warehouse-export`
- **Description:** Warehouse export + REST webhooks (ShipBob, Green warehouse classes).
- **Relevance:** High
- **Transferability:** Partial — OMS integration via Shopify webhooks + custom middleware.
- **Evidence:** `wp-content/plugins/warehouse-export`
### `wc-admin-product-note`
- **Description:** Product notes in admin for ops.
- **Relevance:** Low
- **Transferability:** Partial — Shopify order/product notes pattern.
- **Evidence:** `wp-content/plugins/wc-admin-product-note`
### `wc-remove-oldest-orders`
- **Description:** Housekeeping: remove old orders from DB.
- **Relevance:** Low
- **Transferability:** N/A — WP-only maintenance.
- **Evidence:** `wp-content/plugins/wc-remove-oldest-orders`
### `webp-express`
- **Description:** WebP image conversion/delivery.
- **Relevance:** Low
- **Transferability:** Partial — Shopify image CDN handles formats.
- **Evidence:** `wp-content/plugins/webp-express`
### `woo-discount-rules`
- **Description:** Discount Rules for WooCommerce (conditional cart rules).
- **Relevance:** High
- **Transferability:** Partial — Shopify Functions + discount apps.
- **Evidence:** `wp-content/plugins/woo-discount-rules`
### `woo-discount-rules-pro`
- **Description:** Pro tier for Discount Rules (extra rule types).
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/woo-discount-rules-pro`
### `woo-payment-gateway`
- **Description:** Payment gateway package (often card UI / blocks).
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/woo-payment-gateway`
### `woocommerce`
- **Description:** WooCommerce core (cart, checkout, products, orders). Entire commerce layer to be replaced by Shopify.
- **Relevance:** High
- **Transferability:** Not transferable — platform replacement.
- **Evidence:** `wp-content/plugins/woocommerce`
### `woocommerce-avatax`
- **Description:** Avalara AvaTax for Woo.
- **Relevance:** Medium
- **Transferability:** Partial — Avalara Shopify.
- **Evidence:** `wp-content/plugins/woocommerce-avatax`
### `woocommerce-cart-page`
- **Description:** Custom cart page behavior/routing.
- **Relevance:** High
- **Transferability:** Partial — Shopify cart template + apps.
- **Evidence:** `wp-content/plugins/woocommerce-cart-page`
### `woocommerce-checkout-userdata`
- **Description:** Extra checkout user data capture.
- **Relevance:** Medium
- **Transferability:** Partial — checkout UI extensions + metafields.
- **Evidence:** `wp-content/plugins/woocommerce-checkout-userdata`
### `woocommerce-complyt-tax`
- **Description:** Complyt tax calculation.
- **Relevance:** High
- **Transferability:** Partial — Shopify Tax / tax apps.
- **Evidence:** `wp-content/plugins/woocommerce-complyt-tax`
### `woocommerce-coupons-utils`
- **Description:** Utilities for coupon management/reporting.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/woocommerce-coupons-utils`
### `woocommerce-gateway-paypal-express-checkout`
- **Description:** PayPal Express checkout.
- **Relevance:** High
- **Transferability:** Full — PayPal on Shopify.
- **Evidence:** `wp-content/plugins/woocommerce-gateway-paypal-express-checkout`
### `woocommerce-google-address`
- **Description:** Google Places autocomplete on address fields.
- **Relevance:** High
- **Transferability:** Partial — Shopify address autocomplete / apps.
- **Evidence:** `wp-content/plugins/woocommerce-google-address`
### `woocommerce-legacy-rest-api`
- **Description:** Legacy Woo REST API compatibility.
- **Relevance:** Low
- **Transferability:** N/A — any consumers must move to Shopify Admin API.
- **Evidence:** `wp-content/plugins/woocommerce-legacy-rest-api`
### `woocommerce-magazine`
- **Description:** Magazine / editorial integration with Woo (see plugin).
- **Relevance:** Medium
- **Transferability:** Partial — Shopify blog Online Store.
- **Evidence:** `wp-content/plugins/woocommerce-magazine`
### `woocommerce-multilingual`
- **Description:** WCML: multi-currency with WPML, exchange rates, client currency. Theme `wcml_custom_currency` maps language codes to ISO currencies.
- **Relevance:** High
- **Transferability:** Partial — Shopify Markets handles currency/locale differently; custom language→currency matrix must be reimplemented or dropped.
- **Evidence:** `wp-content/plugins/woocommerce-multilingual`
### `woocommerce-my-account`
- **Description:** Custom My Account SPA/loader and flows.
- **Relevance:** High
- **Transferability:** Partial — Customer Account API / legacy customer accounts strategy.
- **Evidence:** `wp-content/plugins/woocommerce-my-account`
### `woocommerce-quiz`
- **Description:** Quiz tied to Woo products.
- **Relevance:** Medium
- **Transferability:** Partial — third-party quiz app or custom theme.
- **Evidence:** `wp-content/plugins/woocommerce-quiz`
### `woocommerce-reminder-pro`
- **Description:** Abandoned cart or reminder emails.
- **Relevance:** Medium
- **Transferability:** Partial — Klaviyo + Shopify checkout abandonment.
- **Evidence:** `wp-content/plugins/woocommerce-reminder-pro`
### `woocommerce-replacement-orders`
- **Description:** Replacement order workflow tied to Woo orders.
- **Relevance:** High
- **Transferability:** Partial — draft orders / exchanges apps / custom.
- **Evidence:** `wp-content/plugins/woocommerce-replacement-orders`
### `woocommerce-services`
- **Description:** WooCommerce Shipping / tax (USPS etc. depending on config).
- **Relevance:** Medium
- **Transferability:** Partial — Shopify Shipping.
- **Evidence:** `wp-content/plugins/woocommerce-services`
### `woocommerce-shipment-tracking`
- **Description:** Woo shipment tracking meta on orders.
- **Relevance:** High
- **Transferability:** Partial — native tracking + carrier apps.
- **Evidence:** `wp-content/plugins/woocommerce-shipment-tracking`
### `woocommerce-shipstation-integration`
- **Description:** ShipStation labels and tracking.
- **Relevance:** High
- **Transferability:** Partial — ShipStation Shopify app.
- **Evidence:** `wp-content/plugins/woocommerce-shipstation-integration`
### `woocommerce-siftscience-extensions`
- **Description:** Extensions for Sift + Woo.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/woocommerce-siftscience-extensions`
### `woocommerce-smart-coupons`
- **Description:** Smart Coupons: store credit, gift certificates, bulk coupons, blocks.
- **Relevance:** High
- **Transferability:** Partial — Shopify gift cards / discount combinations via apps.
- **Evidence:** `wp-content/plugins/woocommerce-smart-coupons`
### `woocommerce-subscription`
- **Description:** Additional subscription-related plugin (custom or companion) alongside WCS — verify relationship in admin.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/woocommerce-subscription`
### `woocommerce-subscriptions`
- **Description:** WooCommerce Subscriptions: recurring orders, renewal payments, subscription products, customer portal hooks. Theme has recurring checkout templates.
- **Relevance:** High
- **Transferability:** Partial — Shopify Subscriptions / selling plans; plan matrix and dunning must be mapped.
- **Evidence:** `wp-content/plugins/woocommerce-subscriptions`
### `woocommerce-zapier`
- **Description:** Zapier triggers/actions for Woo.
- **Relevance:** Medium
- **Transferability:** Full — Shopify Zapier.
- **Evidence:** `wp-content/plugins/woocommerce-zapier`
### `woofunnels-order-bump`
- **Description:** FunnelKit / WooFunnels order bumps.
- **Relevance:** High
- **Transferability:** Partial — checkout upsell apps.
- **Evidence:** `wp-content/plugins/woofunnels-order-bump`
### `wordpress-seo`
- **Description:** Yoast SEO Free: meta, schema, sitemaps, redirects UI.
- **Relevance:** High
- **Transferability:** Partial — Shopify SEO fields + redirects JSON.
- **Evidence:** `wp-content/plugins/wordpress-seo`
### `wordpress-seo-premium`
- **Description:** Yoast Premium: redirects, internal linking, AI features.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/wordpress-seo-premium`
### `wp-rocket`
- **Description:** Caching and performance (HTML/CSS/JS optimization).
- **Relevance:** Medium
- **Transferability:** N/A — Shopify CDN/hosting; different model.
- **Evidence:** `wp-content/plugins/wp-rocket`
### `wp-sitemap-page`
- **Description:** HTML sitemap page shortcode/plugin.
- **Relevance:** Low
- **Transferability:** Partial — theme page.
- **Evidence:** `wp-content/plugins/wp-sitemap-page`
### `wp-smush-pro`
- **Description:** Image compression.
- **Relevance:** Low
- **Transferability:** N/A — Shopify image pipeline.
- **Evidence:** `wp-content/plugins/wp-smush-pro`
### `wpml-media-translation`
- **Description:** WPML Media Translation for translated attachments.
- **Relevance:** Medium
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/wpml-media-translation`
### `wpml-string-translation`
- **Description:** WPML String Translation for UI strings and plugin strings.
- **Relevance:** High
- **Transferability:** Partial — theme locale files / Markets; no direct port.
- **Evidence:** `wp-content/plugins/wpml-string-translation`
### `wpmudev-updates`
- **Description:** WPMU DEV update client.
- **Relevance:** Low
- **Transferability:** N/A
- **Evidence:** `wp-content/plugins/wpmudev-updates`
### `wpseo-woocommerce`
- **Description:** Yoast WooCommerce SEO extension.
- **Relevance:** High
- **Transferability:** Partial
- **Evidence:** `wp-content/plugins/wpseo-woocommerce`
### `wunderkind-integration`
- **Description:** Wunderkind (BounceX) behavioral marketing.
- **Relevance:** Medium
- **Transferability:** Partial — Wunderkind Shopify.
- **Evidence:** `wp-content/plugins/wunderkind-integration`
### `yith-woocommerce-gift-cards-premium`
- **Description:** YITH gift cards premium.
- **Relevance:** Medium
- **Transferability:** Partial — Shopify gift cards.
- **Evidence:** `wp-content/plugins/yith-woocommerce-gift-cards-premium`
### `yotpo-integration`
- **Description:** Yotpo loyalty/reviews/SMS hooks; includes REST coupon routes.
- **Relevance:** High
- **Transferability:** Partial — Yotpo Shopify stack.
- **Evidence:** `wp-content/plugins/yotpo-integration`

---

_End of inventory. Re-run `python docs/generate-shopify-inventory.py` after plugin/theme changes._
