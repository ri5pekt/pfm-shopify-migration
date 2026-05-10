# Shopify migration — features inventory (Particle For Men)

This document lists **what the current website and back office can do** so your team can talk to Shopify with fewer surprises. It was built from a technical review of the store code; this version is written so **non‑technical readers can follow the story**.

**What each block means**

- **Description** — In plain words: what customers, support, or the warehouse experience because of this item.
- **Relevance** — **High** = touches money, legal, shipping, languages, or subscriptions; **Medium** = marketing, content, or important experience; **Low** = small convenience or something only the old website needed.
- **Transferability** — How hard it is to get the same outcome on Shopify. **Easy move** means Shopify or a common partner already has a close match. **Expect some work** means apps or a short custom project. **Needs a fresh build** means we design it again on top of Shopify. **Not part of Shopify** means it belongs to the old hosting setup and simply goes away when WordPress is retired.

Theme wiring and checkout templates are described **in one summary each** (we do not list every technical file). The long list in section 11 is almost every installed “package” name—even boring ones—with a short note there for the few folders this inventory deliberately skips (unused gift‑card package, licensing updater, and WPML strings explained in section 0).

## Legend (quick read)

- **High** — Shoppers, revenue, tax, fraud checks, shipping, languages/currencies, subscriptions, or daily operations depend on it.
- **Medium** — Marketing, reviews, emails, landing pages, SEO, or noticeable shopper experience.
- **Low** — Editor helpers, old hosting tools, or things that rarely affect the customer journey.

## 0. Big moving parts (several add-ons work together)

These threads describe **whole workflows** that span many items in section 11. They are reminders for workshops—not a replacement for the detailed rows below.

### Many countries, many languages, many currencies

- **Description:** Today the store can show different languages and charge in different currencies depending on where someone shops. That touches the header language picker, product links, cart, and how prices convert. On Shopify this becomes **Markets** (and careful planning for links people already bookmarked). Some wording also comes from **inside** add-ons (see the next thread)—not only from normal page editors.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify handles the idea well, but the exact setup and redirects need a dedicated project.

### Translating text that comes from inside add-ons (not from normal pages)

- **Description:** Besides translating whole pages, the team can translate **short strings** that originate inside plugins or the theme—things like a button label baked into an add-on, a checkout message, or a tiny widget line. On WordPress this is part of the same multilingual story as page translation; on Shopify the same outcome is usually **theme locale files**, **translation apps**, or Markets-aware copy in apps—planned together with the main language rollout.
- **Relevance:** High
- **Transferability:** **Expect some work** — bundle it with Markets and your translation process so no “mystery English” is left in foreign storefronts.

### Subscribe & save (recurring orders)

- **Description:** Customers can put products on a schedule with renewals, price changes over time, and self‑service changes. Several add‑ons and custom tools support that today—including internal staff screens for fixes and notes.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify has subscription tools, but every billing rule must be checked one by one.

### Fraud and risky orders

- **Description:** Before an order is accepted, outside services score risk; bots can be blocked and some checkout steps are watched closely.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify has built‑in fraud signals; some partners (Signifyd, Kount, etc.) are re‑connected via apps.

### Getting the box out the door (and telling the customer where it is)

- **Description:** ShipBob, tracking emails, Narvar, AfterShip, warehouse exports, and the link to the Priority business system all feed this story. **Note:** a ShipStation add‑on exists in the code folder but **Particle does not use ShipStation**, so it should not be budgeted on Shopify.
- **Relevance:** High
- **Transferability:** **Expect some work** — Connectors and emails are rebuilt using Shopify’s order updates plus partner apps.

### Ads, pixels, and “who clicked what”

- **Description:** Google Tag Manager, Meta/TikTok pixels, affiliate tools, pop‑ups, and similar tags feed marketing teams.
- **Relevance:** High
- **Transferability:** **Expect some work** — Most partners publish a Shopify‑ready snippet; still needs QA so sales numbers stay trustworthy.

## 1. The storefront “glue” (theme code)

### Custom Particle theme wiring

- **Description:** About **24** small code modules load with every page to connect the design to real store behavior—cart, checkout, languages, coupons, Klaviyo emails, address checks, SEO, quizzes, A/B tests, and more. Think of this as the **instruction list behind the scenes**; shoppers never see the filenames. Engineers use the theme’s `functions.php` file if they need the exact list.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify replaces the whole engine, but each shopper-facing habit must be checked so nothing is lost.

## 2. Special rules baked into the old checkout & blog

### Language picks the default currency

- **Description:** When someone picks a country/language, the store quietly switches which currency prices use (for example Australia → Australian dollars, Japan → yen, EU countries → euros).
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Markets handles the same idea with a cleaner setup.

### Lighter blog reading mode

- **Description:** Certain magazine-style articles load without heavy shop scripts so they feel faster on slow phones.
- **Relevance:** Low
- **Transferability:** **Expect some work** — recreate with a simple Shopify blog template if still wanted.

### Blocked test phone numbers at checkout

- **Description:** A short internal list of phone numbers is rejected at checkout to stop known bad actors.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — rebuild as a Shopify Flow rule or checkout validation app.

### Extra coupon bookkeeping

- **Description:** Custom logic changes how some coupon details are stored in the database—usually tied to a promotion partner. Business stakeholders should confirm **why** it exists before copying anything.
- **Relevance:** High
- **Transferability:** **Needs a fresh build** — must be understood before promising the same behavior on Shopify.

### Magazine helpers & SEO tweaks

- **Description:** Related articles, breadcrumbs, and a few Yoast SEO settings that change how old URLs behave.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — rebuild redirects and metadata inside Shopify.

## 3. Campaign & landing page layouts

### Special WordPress page layouts

- **Description:** The merchandising team can attach **18** custom layouts to normal WordPress pages for big campaigns—examples include Build‑Your‑Own Bundle, Marsmen‑style product stories, commercials, consultations, Amazon gift flows, and thank‑you pages. File names for reference: `after-quiz.php`, `code-tests.php`, `content-post.php`, `gravite-landing-page-2.php`, `gravite-landing-page-ty.php`, `gravite-landing-page.php`, `single-product-marsmen.php`, `tmp-amazon-gift-landing-page.php`, `tmp-amazon-lp-ty.php`, `tmp-book-consultation-2.php`, `tmp-book-consultation.php`, `tmp-build-your-own-bundle.php`, `tmp-commercials.php`, `tmp-face-analyzer.php`, `tmp-first-purchase-anniversary.php`, `tmp-gravite-commercial.php`, `tmp-life-drive-lp.php`, `tmp-sport-page.php`.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — rebuild as Shopify pages with reusable sections and plan URL redirects.

## 4. Drag‑and‑drop content blocks for editors

### Custom content blocks (Gutenberg)

- **Description:** Editors have **70** reusable blocks for rich storytelling—best sellers, bundles, FAQs, reviews, quizzes, Gravité‑specific promos, sliders, press logos, Instagram grids, post‑purchase thank‑you snippets, ingredients, clinical claims, and more. Sample block names: `ab-test-html`, `about-awkward`, `about-head`, `about-video`, `action-coffee-block`, `affiliates-block`, `after-quiz-bundle`, `all-products-block`, `banner-blue`, `benefits-block`, `best-sellers-block`, `blue-banner-text`, `bundle-products-list`, `bundle-save`, `bundles-block`, `clinical-trial`, `coffee-ingredients-block`, `coffee-innovate-block`, `comparison-block`, `confirmation-block`, `contact-block`, `custom-editor`, `difference-block`, `faq-block`, `faq-items`, `faq-new`, `gravite-banner-block`, `gravite-carousel-block`, `gravite-header-block`, `gravite-horizontal-accordion`, `gravite-sale-block`, `header-top`, `how-to-use-new`, `how-use`, `ingredients-block`, `ingredients-premium-block`, `instagram-block`, `logos-slider-block`, `magazin-block`, `more-product` …and **30** more..
- **Relevance:** Medium
- **Transferability:** **Expect some work** — rebuild as Shopify sections or metaobject‑driven content.

## 5. Cart, checkout, and “my account” screens

### Branded shopping funnel templates

- **Description:** The Particle design replaces **69** of WooCommerce’s default screens—cart drawer, checkout (including older vs newer versions), subscription renewals, customer account area, product detail layouts, and galleries. Shoppers experience this as “the Particle checkout,” not as individual files.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify checkout + customer accounts look different; plan a UX review, not a copy‑paste.

## 6. Landing page content type

### “Landing pages” content bucket

- **Description:** A dedicated content type powers long‑form campaign URLs that start with `/lpage/…`, separate from normal products.
- **Relevance:** High
- **Transferability:** **Expect some work** — map to Shopify pages or landing apps and redirect old links.

## 7. Behind‑the‑scenes data feeds & webhooks

_These are invisible to shoppers but important for marketing, warehouse, or finance._

### Text messages (Twilio)

- **Description:** Lets the site send or verify SMS messages (for example two‑step flows).
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Klaviyo profile updates

- **Description:** Keeps Klaviyo profiles in sync when someone fills out special forms or promotions.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Email verification for promotions

- **Description:** Confirms email addresses before certain promotions unlock.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Braintree dispute alerts

- **Description:** When Braintree flags a payment dispute, the site can attach notes to the matching order.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Order and subscription notes for staff tools

- **Description:** Lets trusted internal tools read or write internal notes on orders or subscriptions.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### AI and search crawler visit analytics

- **Description:** Aggregates stored crawler traffic (which URLs were visited and how often over time) for monitoring and SEO-related visibility—shoppers never see this screen.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### ShipBob warehouse callbacks

- **Description:** ShipBob tells WordPress when a parcel ships, is delayed, or is delivered.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Secondary warehouse feed (“Green”)

- **Description:** Another warehouse integration speaks the same “shipped” language for a different 3PL.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Monday.com coupon bridge

- **Description:** Creates or updates coupons when the Monday.com workflow says so.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Yotpo coupon automation

- **Description:** Lets Yotpo loyalty create or cancel coupon codes automatically.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Miscellaneous staff helper APIs

- **Description:** Small one-off hooks used by internal dashboards—engineering should confirm which are still called.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Chargeback lookup

- **Description:** Looks up chargeback status for a given order for finance/support.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Geo privacy gate

- **Description:** Controls what appears based on privacy / geography rules.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Sellence product & coupon feed

- **Description:** Exposes catalog/coupon data for an external partner system.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Wunderkind product feed

- **Description:** Sends catalog data to Wunderkind for onsite personalization.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Order summary widget

- **Description:** Feeds a small admin widget with order totals.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### OptinMonster map helper

- **Description:** Helps OptinMonster campaigns map to WordPress content if enabled.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Klaviyo plugin APIs

- **Description:** Official Klaviyo endpoints bundled with their WordPress plugin.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Yoast / WP Rocket maintenance APIs

- **Description:** Background housekeeping for SEO cache plugins—rarely shopper facing.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

## 8. Always‑on WordPress “safety” files

### Always‑on file: `pfm-braintree-api-access.php`

- **Description:** Lets trusted server jobs talk to Braintree with the right credentials.
- **Relevance:** High
- **Transferability:** **Expect some work:** move secrets to the new hosting model; reconnect Braintree where still needed.

### Always‑on file: `redirections.php`

- **Description:** Guesses the shopper’s language, fixes URLs, and remembers `store_switch` choices for WPML.
- **Relevance:** High
- **Transferability:** **Expect some work:** rebuild with Shopify Markets + redirect import.

### Always‑on file: `pfm-performance.php`

- **Description:** Small performance tweaks specific to this host/theme combo.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** Shopify handles performance differently.

### Always‑on file: `custom_plugin_organizer.php`

- **Description:** Controls which heavy plugins load during AJAX, and fixes cart redirects when languages are involved.
- **Relevance:** High
- **Transferability:** **Expect some work:** not needed on Shopify, but behaviors (like redirects) must be reproduced if shoppers rely on them.

### Always‑on file: `woocommerce-additional.php`

- **Description:** Extra WooCommerce hooks loaded very early—confirm with engineering what they still do.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** validate before cutover.

### Always‑on file: `om-map-output.php`

- **Description:** Optional helper for OptinMonster mapping.
- **Relevance:** Low
- **Transferability:** **Expect some work:** only if OptinMonster stays in the marketing stack.

### WP Engine hosting bundles

- **Description:** Caching, forced security patches, login helpers, and other tools injected by the WP Engine host. They keep WordPress healthy but are invisible to shoppers.
- **Relevance:** Low for the Shopify project itself
- **Transferability:** **Not part of Shopify:** disappears when WordPress is retired.

## 9. Saved HTML snapshots (research only)

- **Description:** A folder of frozen HTML captures from the live site helps double‑check which marketing tags, languages, and subscription links appear in the real storefront. Path on disk: `C:\Users\denis_particleformen\Desktop\Cursor Projects\particleformen-scrape\output\html`.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** reference material only.

## 10. Internal tools your team uses inside WordPress (`pfm-panel`)

Support and operations use a private staff control panel wired into WordPress. It is not a shopper-facing storefront; it centralizes order, subscription, and customer work that today happens outside Shopify Admin. After migration, the same jobs belong in **Shopify Admin**, **Shopify Flow**, partner **apps**, or a small custom internal tool—with staff authentication and permissions designed on purpose.

### Orders: search, open, edit, and back-office actions

- **Description:** Staff browse and search orders, open a single order, update fields, see previews, and run operational steps in one place—for example re-run address validation, push an order into the warehouse export path, retry failed payments, issue refunds (including refunds that post as store credit), resend transactional emails, inspect Braintree payment metadata, and resolve Narvar tracking links when that post-purchase experience is in use. Bulk operations and simple “create order” flows live here, along with lightweight helpers such as “newest order” checks for older dashboards and internal order notes for handoffs between teams.
- **Relevance:** High
- **Transferability:** **Needs a fresh build** for anything that assumes WooCommerce order records and custom integrations; map each behavior to Shopify Admin, fulfillment apps, and the Admin API.

### Subscriptions: list, change, pause or cancel, and notes

- **Description:** Staff list subscriptions, open one, adjust line items or schedules where policy allows, run lifecycle actions such as pause or cancel, see which catalog items are offered on subscription, pull subscriptions for a given customer, and attach internal notes on the contract.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify’s subscription model differs; plan with your subscription app and contract APIs rather than expecting a one-to-one copy of this screen.

### Customers: search, profiles, support views, credits, and loyalty

- **Description:** Staff search for customers, open profiles for read and update, and sometimes work in a “support as customer” mode for troubleshooting. The panel ties into Yotpo loyalty for point adjustments and into Woo store credit ledgers with the ability to post adjustments—finance and support use these for refunds-as-credit and goodwill gestures.
- **Relevance:** High
- **Transferability:** **Expect some work** — customer identity, staff impersonation rules, credits, and loyalty spread across Shopify Admin and partner apps on the new stack.

### Replacement orders (exchanges and reships)

- **Description:** A parallel workflow mirrors much of the order toolkit for replacements—creating and tracking replacement orders, notes, edits, warehouse export, address revalidation, carrier links, and email touches. Lookups describe why a replacement was opened and which staff roles typically create them.
- **Relevance:** High
- **Transferability:** **Expect some work** — rebuild with an exchange or replacement app, Shopify-native returns, or a focused custom flow depending on policy.

### Coupons, catalog pickers, and internal reporting

- **Description:** Coupon search and category metadata help campaigns and support apply the right incentives. Product pickers power internal screens that need “what is in this category” lists. Staff can run ad hoc reports and file-based export pipelines, upload inputs where an integration expects them, and review history of those jobs; separate summaries chart order volume over time for operations reviews.
- **Relevance:** Medium to High (depends how much ops still rely on bespoke in-panel reporting versus BI tools)
- **Transferability:** **Expect some work** for discounts and catalog surfacing (Shopify discount and product APIs); treat reporting that only lives here as **needs a fresh build** against Shopify data exports or analytics tools.

### Audit trail for staff actions

- **Description:** Records which staff accounts performed sensitive actions—useful for internal quality control and answering “who changed this?” without digging through raw logs.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — combine Shopify staff activity where it applies with app event logs or compliance tooling you standardize on.

_Implementation note for engineers: these capabilities are implemented as WordPress REST routes registered for the `pfm-panel` integration; migration planning should inventory live callers in code and monitoring, not recreate every route name in stakeholder documents._

## 11. Installed plugins (exhaustive)
_**149** add-ons below (alphabetical). The bold name is the technical folder name—think of it as the “package label.” If a line sounds vague, that only means the name does not explain itself; your web partner maps it to the real vendor or feature._
_Omitted from this list on purpose: an unused YITH gift‑card package, the WPMU DEV updater client (licensing only, not storefront behavior), and the separate WPML “strings” package—**translating text that lives inside buttons and add-ons** is described in section 0 instead so stakeholders read the capability once, not under two technical folder names._

### `PriorityAPI`

- **Description:** Priority ERP API integration.
- **Relevance:** High
- **Transferability:** **Expect some work:** middleware posting Shopify orders to Priority.

### `PriorityApiCustomCode`

- **Description:** Custom code layer on Priority API.
- **Relevance:** High
- **Transferability:** **Needs a fresh build:** port to middleware.

### `WooCommercePriorityAPI`

- **Description:** Alternate or layered Priority Woo bridge — confirm active.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `account-page-recommended-products`

- **Description:** Recommended products on account page.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** personalization app or theme.

### `add-search-to-menu`

- **Description:** This add-on (folder name **add-search-to-menu**) plugs into today’s WordPress store. It may show up for shoppers, staff, or only behind the scenes. Someone who knows the live admin should confirm whether it is turned on and what it is used for. On Shopify we will match what it does with either a built‑in Shopify feature, a well‑known app, or a small custom project.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify usually covers the need, but not always “out of the box”—often an app or short custom setup.

### `add_upsells_option_ms`

- **Description:** Adds upsell options to subscription/cart flows (custom).
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `advanced-cron-manager`

- **Description:** Cron UI for WP.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** Shopify scheduled jobs via apps.

### `advanced-custom-fields-pro`

- **Description:** ACF Pro fields on pages/products/options.
- **Relevance:** High
- **Transferability:** **Expect some work:** metafields + metaobject definitions + admin UI.

### `afterpay-gateway-for-woocommerce`

- **Description:** Afterpay / Clearpay BNPL.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shop Pay Installments / Afterpay Shopify.

### `aftership-woocommerce-tracking`

- **Description:** AfterShip tracking.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** AfterShip app.

### `alert-system`

- **Description:** Internal alerts.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Slack/email from Flow.

### `all-upsells`

- **Description:** Upsell flows: thank-you page, post-purchase, BAS/PPU modules (see `includes/`).
- **Relevance:** High
- **Transferability:** **Expect some work:** post-purchase apps, checkout upsell extensions.

### `blotout-edgetag`

- **Description:** Blotout EdgeTag / customer data platform.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify Customer Privacy + server pixels.

### `bluesnap-payment-gateway-for-woocommerce`

- **Description:** BlueSnap payment gateway.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify payment provider availability; may require different PSP.

### `braintree-saved-token-gateway`

- **Description:** Braintree vaulted cards / gateway.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Payments vs Braintree; token migration project.

### `card-checkout-ms`

- **Description:** Checkout card UI / testimonial carousel (custom).
- **Relevance:** Medium
- **Transferability:** **Expect some work:** theme + checkout extensions.

### `cart-sidebar`

- **Description:** Slide-out cart UI; integrates WPML/WCML currency and product ID mapping.
- **Relevance:** High
- **Transferability:** **Expect some work:** cart drawer theme + AJAX cart APIs on Shopify.

### `cart-sidebar-v2`

- **Description:** Alternate cart sidebar implementation — confirm which is primary in production.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `codepress-admin-columns`

- **Description:** Admin list column customization.
- **Relevance:** Low
- **Transferability:** N/A

### `complyt-address-validator`

- **Description:** Complyt address validation.
- **Relevance:** High
- **Transferability:** **Expect some work:** address validation at checkout.

### `custom-coupon`

- **Description:** Custom coupon logic beyond core Woo coupons.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Discount Functions / discount apps.

### `duracelltomi-google-tag-manager`

- **Description:** GTM container injection and dataLayer.
- **Relevance:** High
- **Transferability:** **Easy move:** GTM in theme or Shopify app.

### `empty-cart-upsells`

- **Description:** Upsells when cart empty.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `export-refunds-to-csv`

- **Description:** Export refunds to CSV.
- **Relevance:** Low
- **Transferability:** **Expect some work:** reporting export from Shopify.

### `export-stats`

- **Description:** Export stats to Google Sheets.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Analytics API / Sheets.

### `facebook-store-integration`

- **Description:** Facebook / Meta catalog integration.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Meta sales channel.

### `fermiac-siftscience-for-woocommerce`

- **Description:** Sift Science integration for Woo.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Fraud / third-party.

### `force-default-variant-for-woocommerce`

- **Description:** Forces default variation selection when variations exist.
- **Relevance:** Low
- **Transferability:** **Expect some work:** rarely needed if SKUs are simple; confirm use.

### `force-regenerate-thumbnails`

- **Description:** Regenerate attachment sizes.
- **Relevance:** Low
- **Transferability:** N/A

### `gravite-landing-pages`

- **Description:** Gravité-specific landing page templates.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `impact-partnership-cloud`

- **Description:** Impact affiliate / partnership tracking.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Impact Shopify integration.

### `inspect-http-requests`

- **Description:** Inspect HTTP requests in admin.
- **Relevance:** Low
- **Transferability:** N/A

### `japan-landing-pages`

- **Description:** Japan market landing pages.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Markets + templates.

### `kadence-woocommerce-email-designer`

- **Description:** Kadence Woo email template designer.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify Notifications customization.

### `klaviyo`

- **Description:** Klaviyo official Woo plugin: events, lists, forms.
- **Relevance:** High
- **Transferability:** **Easy move:** Klaviyo Shopify integration.

### `klaviyo-wp`

- **Description:** Additional Klaviyo WordPress integration package.
- **Relevance:** High
- **Transferability:** Full

### `kount-fraud-prevention`

- **Description:** Kount fraud screening on checkout.
- **Relevance:** High
- **Transferability:** **Expect some work:** Kount for Shopify or equivalent.

### `kount-orders-report`

- **Description:** This add-on (folder name **kount-orders-report**) plugs into today’s WordPress store. It may show up for shoppers, staff, or only behind the scenes. Someone who knows the live admin should confirm whether it is turned on and what it is used for. On Shopify we will match what it does with either a built‑in Shopify feature, a well‑known app, or a small custom project.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify usually covers the need, but not always “out of the box”—often an app or short custom setup.

### `landing-pages`

- **Description:** Landing page plugin with blocks and templates (e.g. Marsmen-like LP).
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Pages + metaobjects + theme sections.

### `livecart-by-wp-engine`

- **Description:** WP Engine LiveCart integration.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** host-specific.

### `loco-translate`

- **Description:** Translate theme/plugin strings locally.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** locale JSON / Markets.

### `log-http-requests`

- **Description:** Logs outbound HTTP for debugging.
- **Relevance:** Low
- **Transferability:** N/A

### `login-visit-counter`

- **Description:** Tracks login visits.
- **Relevance:** Low
- **Transferability:** N/A

### `metorik-helper`

- **Description:** Metorik analytics helper for Woo.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Metorik Shopify.

### `metronet-profile-picture`

- **Description:** Profile pictures for users.
- **Relevance:** Low
- **Transferability:** **Expect some work:** customer account profile apps.

### `myplugin`

- **Description:** Placeholder or small custom plugin — audit contents.
- **Relevance:** Low
- **Transferability:** **Needs a fresh build:** ask engineering what this small package actually does.

### `myscripts`

- **Description:** Custom scripts plugin (site-specific).
- **Relevance:** Medium
- **Transferability:** **Needs a fresh build:** ask engineering what this small package actually does.

### `narvar-tracking-integration`

- **Description:** Narvar post-purchase tracking / comms.
- **Relevance:** High
- **Transferability:** **Expect some work:** Narvar Shopify integration.

### `newrelic-transaction-renamer`

- **Description:** Renames New Relic transactions for WP.
- **Relevance:** Low
- **Transferability:** N/A

### `optinmonster`

- **Description:** OptinMonster lead capture.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** OM Shopify embed.

### `orders-pay-verify`

- **Description:** Order pay verification flow.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `orderswidget-summary`

- **Description:** Small internal API that shows order summaries inside WordPress admin widgets.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** rebuild in a staff dashboard or BI tool if still needed.

### `outersignal-order-export`

- **Description:** Order export to Outersignal.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** webhooks.

### `package_protection_ms`

- **Description:** Package protection upsell on checkout.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** shipping protection apps.

### `particleformen-checkout`

- **Description:** Particle‑specific checkout tweaks layered on top of WooCommerce (together with the theme checkout code).
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Checkout allows apps and small UI extensions instead of the old PHP approach.

### `pfm-chargebacks-utils`

- **Description:** Chargeback utilities + REST.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** payment processor dashboards.

### `pfm-checkout-bot-block`

- **Description:** Bot blocking on checkout.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify bot protection + CAPTCHA apps.

### `pfm-checkout-observer`

- **Description:** Observes checkout events (logging / risk / analytics — confirm).
- **Relevance:** High
- **Transferability:** **Expect some work:** webhooks + Flow.

### `pfm-csv-uploader`

- **Description:** Admin CSV upload utilities.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** Shopify bulk import / Admin API.

### `pfm-geo-privacy`

- **Description:** Geo / privacy gate (REST namespace).
- **Relevance:** High
- **Transferability:** **Expect some work:** Markets + consent apps.

### `pfm-holiday-season`

- **Description:** Seasonal promos / toggles.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify scheduled discounts.

### `pfm-kill-injected-ui`

- **Description:** Hides stray admin or storefront UI injected by other tools.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** WordPress-only housekeeping.

### `pfm-klaviyo-monitor`

- **Description:** Monitoring / hooks for Klaviyo health.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** ops tooling; replace with monitoring on new stack.

### `pfm-monday-coupons`

- **Description:** REST-driven coupon integration (Monday workflow).
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Zapier/Flow + discount APIs.

### `pfm-panel`

- **Description:** The internal “mission control” staff use to search orders, resend emails, push refunds, adjust store credit, export to the warehouse, and similar day‑to‑day jobs.
- **Relevance:** High
- **Transferability:** **Needs a fresh build:** Shopify Admin plus Flow/partner apps—or a lightweight custom dashboard—replace this over time.

### `pfm-signifyd-integration`

- **Description:** Signifyd fraud scoring / order submission.
- **Relevance:** High
- **Transferability:** **Expect some work:** Signifyd Shopify app or custom integration.

### `pfm-skincare-quiz`

- **Description:** Particle skincare quiz templates and flow.
- **Relevance:** High
- **Transferability:** **Expect some work:** rebuild as theme section or app.

### `pfm-smarty-address-validator`

- **Description:** Smarty (USPS) address validation.
- **Relevance:** High
- **Transferability:** **Expect some work:** Smarty or equivalent on Shopify.

### `pfm-store-credits`

- **Description:** Store credit balance and checkout application (frontend + admin).
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify store credit / gift card primitives differ; likely app or custom.

### `pfm-tools-utils`

- **Description:** Misc internal tools + REST routes.
- **Relevance:** Medium
- **Transferability:** **Needs a fresh build:** review with engineering before promising dates.

### `pixelyoursite-pro`

- **Description:** PixelYourSite: Meta/CAPI/GA events.
- **Relevance:** High
- **Transferability:** **Expect some work:** PYS Shopify or server events.

### `pixelyoursite-super-pack`

- **Description:** PYS add-on pack.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `post-duplicator`

- **Description:** Duplicate posts/pages for editors.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** editor workflow.

### `post-orders-to-priority`

- **Description:** Pushes orders to Priority system.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `post-purchase-upsell`

- **Description:** Post-purchase one-click upsell.
- **Relevance:** High
- **Transferability:** **Expect some work:** post-purchase apps.

### `post-smtp`

- **Description:** SMTP mailer for WP emails.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** Shopify email domain; transactional via apps.

### `preorder-products`

- **Description:** Preorder selling for products.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** preorder apps.

### `product-guide`

- **Description:** Product guide experience.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** content pages + metafields.

### `product-landing-pages`

- **Description:** Product-scoped landing experiences.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `purchase-push-notifications`

- **Description:** Push notifications on purchase.
- **Relevance:** Low
- **Transferability:** **Expect some work:** mobile app channel if applicable.

### `quiz`

- **Description:** Generic quiz plugin for Particle.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `recaptcha-for-woocommerce`

- **Description:** reCAPTCHA on Woo checkout/account.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify bot challenge / apps.

### `redirection`

- **Description:** 301/302 redirect manager and logs.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify URL redirects (import).

### `richpanel-for-woocommerce`

- **Description:** Richpanel helpdesk + customer timeline for Woo orders.
- **Relevance:** High
- **Transferability:** **Expect some work:** Richpanel Shopify app.

### `scheduled-actions`

- **Description:** Action Scheduler tables (often bundled with Woo).
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** platform cron/queues differ.

### `sellence-api`

- **Description:** Sellence REST API (`/products`, `/coupons`).
- **Relevance:** Medium
- **Transferability:** **Expect some work:** custom app on Shopify.

### `shipbob-integration`

- **Description:** ShipBob fulfillment integration.
- **Relevance:** High
- **Transferability:** **Expect some work:** ShipBob Shopify connector or order webhook app.

### `show-current-template`

- **Description:** Dev: shows current PHP template.
- **Relevance:** Low
- **Transferability:** N/A

### `sift-wp`

- **Description:** Sift-related WordPress glue.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `sitemap-custom`

- **Description:** Custom sitemap generation for Particle.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify sitemap + hreflang via Markets.

### `sitepress-multilingual-cms`

- **Description:** Runs the store’s multiple languages—translated pages, menus, and the correct links for Google in each country.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Markets plus translation tools replace most of this, but bookmarks and URLs need a careful plan.

### `sky-wcs-no-periods`

- **Description:** Cleans subscription product titles (removes periods).
- **Relevance:** Low
- **Transferability:** **Expect some work:** naming in Shopify subscriptions.

### `smtp-mailgun-connector`

- **Description:** Mailgun SMTP connector.
- **Relevance:** Low
- **Transferability:** N/A

### `special-shipping-methods`

- **Description:** Custom shipping methods / rules.
- **Relevance:** High
- **Transferability:** **Expect some work:** carrier service + Functions or shipping apps.

### `stampedio`

- **Description:** Stamped.io reviews widgets / integration.
- **Relevance:** High
- **Transferability:** **Expect some work:** Stamped Shopify.

### `stampedio-product-reviews`

- **Description:** Stamped product reviews companion.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `sticky-cta`

- **Description:** Sticky CTA bar.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** theme.

### `subscriptions-utils`

- **Description:** Particle‑specific helpers that tweak how subscriptions behave behind the scenes.
- **Relevance:** High
- **Transferability:** **Needs a fresh build:** replan each behavior inside Shopify Flow, a subscription partner, or a small custom service.

### `tax-helper`

- **Description:** Tax helper utilities for Woo.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `ticket-submissions`

- **Description:** Support ticket submission from site.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** forms app / Zendesk / Gorgias.

### `tiktok-shop-integration`

- **Description:** TikTok Shop / catalog sync.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** TikTok for Shopify.

### `tinymce-advanced`

- **Description:** Classic editor enhancements.
- **Relevance:** Low
- **Transferability:** N/A

### `trustpilot-integration`

- **Description:** Trustpilot integration glue.
- **Relevance:** Medium
- **Transferability:** Full

### `trustpilot-widget`

- **Description:** Trustpilot widget embed.
- **Relevance:** Medium
- **Transferability:** **Easy move:** Trustpilot Shopify app/widget.

### `try-before-you-buy`

- **Description:** Try before you buy program.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** TBYB apps.

### `two-factor-authentication-premium`

- **Description:** 2FA for WP admin/logins.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** Shopify org security; customer 2FA via apps if needed.

### `user-role-editor`

- **Description:** WP role/capability editor.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** Shopify staff permissions.

### `user-switching`

- **Description:** Switch user for support testing.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** Shopify staff impersonation patterns differ.

### `walmart-marketplace-integration`

- **Description:** Walmart marketplace listing / orders.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Walmart Shopify channel.

### `warehouse-export`

- **Description:** Warehouse export + REST webhooks (ShipBob, Green warehouse classes).
- **Relevance:** High
- **Transferability:** **Expect some work:** OMS integration via Shopify webhooks + custom middleware.

### `wc-admin-product-note`

- **Description:** Product notes in admin for ops.
- **Relevance:** Low
- **Transferability:** **Expect some work:** Shopify order/product notes pattern.

### `wc-remove-oldest-orders`

- **Description:** Housekeeping: remove old orders from DB.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** WP-only maintenance.

### `webp-express`

- **Description:** WebP image conversion/delivery.
- **Relevance:** Low
- **Transferability:** **Expect some work:** Shopify image CDN handles formats.

### `woo-discount-rules`

- **Description:** Discount Rules for WooCommerce (conditional cart rules).
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Functions + discount apps.

### `woo-discount-rules-pro`

- **Description:** Pro tier for Discount Rules (extra rule types).
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `woo-payment-gateway`

- **Description:** Payment gateway package (often card UI / blocks).
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `woocommerce`

- **Description:** WooCommerce core (cart, checkout, products, orders). Entire commerce layer to be replaced by Shopify.
- **Relevance:** High
- **Transferability:** **Needs a fresh build:** platform replacement.

### `woocommerce-avatax`

- **Description:** Avalara AvaTax for Woo.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Avalara Shopify.

### `woocommerce-cart-page`

- **Description:** Custom cart page behavior/routing.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify cart template + apps.

### `woocommerce-checkout-userdata`

- **Description:** Extra checkout user data capture.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** checkout UI extensions + metafields.

### `woocommerce-complyt-tax`

- **Description:** Complyt tax calculation.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Tax / tax apps.

### `woocommerce-coupons-utils`

- **Description:** Utilities for coupon management/reporting.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `woocommerce-gateway-paypal-express-checkout`

- **Description:** PayPal Express checkout.
- **Relevance:** High
- **Transferability:** **Easy move:** PayPal on Shopify.

### `woocommerce-google-address`

- **Description:** Google Places autocomplete on address fields.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify address autocomplete / apps.

### `woocommerce-legacy-rest-api`

- **Description:** Legacy Woo REST API compatibility.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** any consumers must move to Shopify Admin API.

### `woocommerce-magazine`

- **Description:** Magazine / editorial integration with Woo (see plugin).
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify blog Online Store.

### `woocommerce-multilingual`

- **Description:** Pairs languages with the right currency and exchange rates so visitors see familiar money symbols.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify Markets covers the same idea with different settings; any special rules must be re‑entered.

### `woocommerce-my-account`

- **Description:** Custom My Account SPA/loader and flows.
- **Relevance:** High
- **Transferability:** **Expect some work:** Customer Account API / legacy customer accounts strategy.

### `woocommerce-quiz`

- **Description:** Quiz tied to Woo products.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** third-party quiz app or custom theme.

### `woocommerce-reminder-pro`

- **Description:** Abandoned cart or reminder emails.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Klaviyo + Shopify checkout abandonment.

### `woocommerce-replacement-orders`

- **Description:** Replacement order workflow tied to Woo orders.
- **Relevance:** High
- **Transferability:** **Expect some work:** draft orders / exchanges apps / custom.

### `woocommerce-services`

- **Description:** WooCommerce Shipping / tax (USPS etc. depending on config).
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Shopify Shipping.

### `woocommerce-shipment-tracking`

- **Description:** Woo shipment tracking meta on orders.
- **Relevance:** High
- **Transferability:** **Expect some work:** native tracking + carrier apps.

### `woocommerce-shipstation-integration`

- **Description:** WooCommerce ShipStation plugin folder exists in the repo; **Particle does not use ShipStation** operationally—no migration to Shopify ShipStation. Deactivate/uninstall with WordPress.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** not in scope; remove dead plugin during decommission.

### `woocommerce-siftscience-extensions`

- **Description:** Extensions for Sift + Woo.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `woocommerce-smart-coupons`

- **Description:** Smart Coupons: store credit, gift certificates, bulk coupons, blocks.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify gift cards / discount combinations via apps.

### `woocommerce-subscription`

- **Description:** Companion tools that sit next to the main subscription engine—confirm with the web team whether both are active.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `woocommerce-subscriptions`

- **Description:** Powers subscribe‑and‑save: renewals, failed payment retries, and customer self‑service for delivery schedules.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify’s subscription tools are close, but every price and interval must be checked.

### `woocommerce-zapier`

- **Description:** Zapier triggers/actions for Woo.
- **Relevance:** Medium
- **Transferability:** **Easy move:** Shopify Zapier.

### `woofunnels-order-bump`

- **Description:** FunnelKit / WooFunnels order bumps.
- **Relevance:** High
- **Transferability:** **Expect some work:** checkout upsell apps.

### `wordpress-seo`

- **Description:** Yoast SEO Free: meta, schema, sitemaps, redirects UI.
- **Relevance:** High
- **Transferability:** **Expect some work:** Shopify SEO fields + redirects JSON.

### `wordpress-seo-premium`

- **Description:** Yoast Premium: redirects, internal linking, AI features.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `wp-rocket`

- **Description:** Caching and performance (HTML/CSS/JS optimization).
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** Shopify CDN/hosting; different model.

### `wp-sitemap-page`

- **Description:** HTML sitemap page shortcode/plugin.
- **Relevance:** Low
- **Transferability:** **Expect some work:** theme page.

### `wp-smush-pro`

- **Description:** Image compression.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify:** Shopify image pipeline.

### `wpml-media-translation`

- **Description:** Lets each language version of the site use its own photos or PDFs when needed.
- **Relevance:** Medium
- **Transferability:** **Expect some work:**

### `wpseo-woocommerce`

- **Description:** Yoast WooCommerce SEO extension.
- **Relevance:** High
- **Transferability:** **Expect some work:**

### `wunderkind-integration`

- **Description:** Wunderkind (BounceX) behavioral marketing.
- **Relevance:** Medium
- **Transferability:** **Expect some work:** Wunderkind Shopify.

### `yotpo-integration`

- **Description:** Yotpo handles loyalty points, product reviews, SMS messages, and can create or cancel coupon codes from its system.
- **Relevance:** High
- **Transferability:** **Expect some work:** Yotpo’s own Shopify apps reconnect most of this.


---

_This file is generated. Engineers can refresh it after plugins or the theme change by running `python docs/generate-shopify-inventory.py` from the WordPress project folder._
