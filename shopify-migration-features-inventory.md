# Shopify migration — features inventory (Particle For Men)

> [!NOTE]
> This document lists **what the current website and back office can do** so your team can talk to Shopify with fewer surprises. It was built from a technical review of the store code; this version is written so **non‑technical readers can follow the story**.

### How to read each row

| Column | What it means |
| --- | --- |
| **Description** | In plain words: what customers, support, or the warehouse experience because of this item. |
| **Relevance** | **High** — money, legal, shipping, languages, or subscriptions. **Medium** — marketing, content, or important experience. **Low** — small convenience or mostly internal. |
| **Transferability** | **Easy move** — close match in Shopify or a common partner. **Expect some work** — apps or a short custom project. **Needs a fresh build** — redesign on Shopify. **Not part of Shopify** — goes away when WordPress is retired. |

Theme wiring and checkout templates are summarized **once each** (not every PHP filename). **Section 11** is a **capability checklist** (what the business must still have on Shopify)—not a list of WordPress package names.

---

## Legend (quick read)

| Level | Typical scope |
| --- | --- |
| **High** | Shoppers, revenue, tax, fraud, shipping, languages/currencies, subscriptions, or day‑to‑day operations. |
| **Medium** | Marketing, reviews, email, landing pages, SEO, or noticeable shopper experience. |
| **Low** | Editor helpers, host‑specific tools, or things that rarely affect the customer journey. |

---

## 0. Big moving parts (several add-ons work together)

> [!TIP]
> These threads describe **whole workflows** that align with the capability checklist in section 11. Use them in workshops; they do not replace the detailed rows below.

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
- **Transferability:** **Expect some work** — Shopify has built‑in fraud signals; reconnect your chosen fraud vendors via apps.

### Getting the box out the door (and telling the customer where it is)

- **Description:** Primary 3PL, tracking communications, warehouse export jobs, and ERP order posting together keep shoppers, warehouse, and finance aligned on fulfillment state.
- **Relevance:** High
- **Transferability:** **Expect some work** — Connectors and emails are rebuilt using Shopify’s order updates plus partner apps.

> [!CAUTION]
> A **ShipStation** add‑on exists in the code folder, but **Particle does not use ShipStation**—do not budget it for Shopify unless you explicitly adopt that product.

### Ads, pixels, and “who clicked what”

- **Description:** Google Tag Manager, Meta/TikTok pixels, affiliate tools, pop‑ups, and similar tags feed marketing teams.
- **Relevance:** High
- **Transferability:** **Expect some work** — Most partners publish a Shopify‑ready snippet; still needs QA so sales numbers stay trustworthy.

## 1. The storefront “glue” (theme code)

### Custom Particle theme wiring

- **Description:** About **24** small code modules load with every page to connect the design to real store behavior—cart, checkout, languages, coupons, marketing‑automation emails, address checks, SEO, quizzes, A/B tests, and more. Think of this as the **instruction list behind the scenes**; shoppers never see the filenames. Engineers use the theme’s `functions.php` file if they need the exact list.
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

- **Description:** Related articles, breadcrumbs, and legacy SEO/editor settings that change how some URLs and snippets behave.
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

> [!TIP]
> Shoppers never see these feeds, but **marketing, warehouse, and finance** often depend on them.

### SMS send and verification

- **Description:** Lets the site send or verify text messages (for example two‑step flows) via a messaging gateway.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Email platform profile sync from forms

- **Description:** Keeps marketing‑database profiles in sync when someone completes special forms or promotions.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Email verification for promotions

- **Description:** Confirms email addresses before certain promotions unlock.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Payment processor dispute signals

- **Description:** When the card processor flags a dispute, the site can attach notes to the matching order for finance.
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

### Primary warehouse shipment callbacks

- **Description:** The main 3PL tells the site when a parcel ships, is delayed, or is delivered so statuses and emails stay accurate.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Secondary warehouse shipment callbacks

- **Description:** A second logistics partner uses the same style of shipped/delivered signals.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Project‑tool‑driven coupon creation

- **Description:** Creates or updates coupons when an external project or ops workflow reaches the right state.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Loyalty‑driven coupon automation

- **Description:** Creates or cancels discount codes automatically when loyalty rules fire.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Miscellaneous staff helper hooks

- **Description:** Small one-off endpoints used by internal dashboards—engineering should confirm which are still called.
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

### Partner catalog and coupon export

- **Description:** Exposes catalog and coupon data for an external partner system.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Behavioral marketing product feed

- **Description:** Sends catalog snapshots to a partner that powers browse‑based onsite campaigns.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Order summary widget

- **Description:** Feeds a small admin widget with order totals.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Lead‑capture campaign mapping

- **Description:** Maps lead‑capture campaigns to the right storefront content when that integration is enabled.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### Email marketing platform maintenance hooks

- **Description:** Server endpoints keep the email platform in sync with forms, lists, and custom events—rarely shopper facing.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

### SEO and performance tooling maintenance hooks

- **Description:** Background jobs for search metadata, sitemaps, or HTML/asset cache housekeeping—rarely shopper facing.
- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.
- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.

## 8. Always‑on WordPress “safety” files

### Always‑on file: `pfm-braintree-api-access.php`

- **Description:** Lets trusted server jobs talk to Braintree with the right credentials.
- **Relevance:** High
- **Transferability:** **Expect some work:** move secrets to the new hosting model; reconnect Braintree where still needed.

### Always‑on file: `redirections.php`

- **Description:** Guesses the shopper’s language, fixes URLs, and remembers multilingual `store_switch` choices.
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

- **Description:** Optional helper for lead‑capture campaign mapping.
- **Relevance:** Low
- **Transferability:** **Expect some work:** only if the same lead‑capture tooling stays in the marketing stack.

### WP Engine hosting bundles

- **Description:** Caching, forced security patches, login helpers, and other tools injected by the WP Engine host. They keep WordPress healthy but are invisible to shoppers.
- **Relevance:** Low for the Shopify project itself
- **Transferability:** **Not part of Shopify:** disappears when WordPress is retired.

## 9. Saved HTML snapshots (research only)

- **Description:** A folder of frozen HTML captures from the live site helps double‑check which marketing tags, languages, and subscription links appear in the real storefront. Path on disk: `C:\Users\denis_particleformen\Desktop\Cursor Projects\particleformen-scrape\output\html`.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify:** reference material only.

---

## 10. Internal tools your team uses inside WordPress (`pfm-panel`)

> [!NOTE]
> Support and operations use a private **staff control panel** wired into WordPress. It is not a shopper-facing storefront; it centralizes order, subscription, and customer work that today happens outside Shopify Admin. After migration, the same jobs belong in **Shopify Admin**, **Shopify Flow**, partner **apps**, or a small custom internal tool—with staff authentication and permissions designed on purpose.

### Orders: search, open, edit, and back-office actions

- **Description:** Staff browse and search orders, open a single order, update fields, see previews, and run operational steps in one place—for example re-run address validation, push an order into the warehouse export path, retry failed payments, issue refunds (including refunds that post as store credit), resend transactional emails, inspect Braintree payment metadata, and resolve Narvar tracking links when that post-purchase experience is in use. Bulk operations and simple “create order” flows live here, along with lightweight helpers such as “newest order” checks for older dashboards and internal order notes for handoffs between teams.
- **Relevance:** High
- **Transferability:** **Needs a fresh build** for anything that assumes WooCommerce order records and custom integrations; map each behavior to Shopify Admin, fulfillment apps, and the Admin API.

### Subscriptions: list, change, pause or cancel, and notes

- **Description:** Staff list subscriptions, open one, adjust line items or schedules where policy allows, run lifecycle actions such as pause or cancel, see which catalog items are offered on subscription, pull subscriptions for a given customer, and attach internal notes on the contract.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify’s subscription model differs; plan with your subscription app and contract APIs rather than expecting a one-to-one copy of this screen.

### Customers: search, profiles, support views, credits, and loyalty

- **Description:** Staff search for customers, open profiles for read and update, and sometimes work in a “support as customer” mode for troubleshooting. The panel ties into the **loyalty program** for point adjustments and into **store credit** ledgers with the ability to post adjustments—finance and support use these for refunds-as-credit and goodwill gestures.
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

> [!TIP]
> **For engineers:** these capabilities are implemented as WordPress REST routes registered for the `pfm-panel` integration. Migration planning should inventory live callers in code and monitoring, not recreate every route name in stakeholder documents.

---

## 11. Store capabilities to re‑home on Shopify (no plugin names)

> [!NOTE]
> This section is **only business capabilities**—things shoppers, marketing, finance, or ops need after migration. It intentionally **does not** name WordPress plugin folders, SEO suites, cache plugins, image optimizers, or translation packages; those are implementation details. Map each capability to Shopify native features, first‑party channels, or an app category.

### Core catalog, cart, checkout, and orders

- **Description:** Shoppers discover products, configure variants, use a cart, complete checkout, and receive confirmations; staff rely on order records, statuses, and customer-visible order history.
- **Relevance:** High
- **Transferability:** **Needs a fresh build** — Shopify becomes the commerce system of record; every edge case must be re‑validated.

### Multilingual storefront and market-aware pricing

- **Description:** URLs, navigation, and product copy follow the shopper’s language; prices and settlement currency follow market rules.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Markets plus translation workflow; plan redirects and bookmarks.

### Locale-specific media when marketing differs by country

- **Description:** Some regions need different hero images, PDFs, or downloads than the default language—not only translated text.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — metafields, metaobjects, or per‑market content in the theme.

### Search engine metadata, structured data, XML sitemaps, and hreflang

- **Description:** Pages expose correct titles/descriptions, rich results where appropriate, crawlable sitemaps, and language alternates for Google.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify SEO fields, JSON‑LD apps or theme logic, sitemap + Markets hreflang strategy.

### Redirect management and legacy URL hygiene

- **Description:** 301/302 rules and logs when campaigns end or paths change; avoids broken inbound links.
- **Relevance:** High
- **Transferability:** **Expect some work** — import redirects into Shopify; keep a governance process.

### Full‑page and asset performance (caching, compression, script bundling)

- **Description:** HTML and static assets are cached and minified so repeat visits feel fast on real devices.
- **Relevance:** Medium
- **Transferability:** **Not part of Shopify 1:1** — Shopify’s CDN and theme performance replace host‑specific caching; still needs tuning.

### Image weight and modern formats in the storefront

- **Description:** Images are resized, compressed, and served in efficient formats where browsers support them.
- **Relevance:** Low
- **Transferability:** **Easy move / expect some work** — Shopify’s image pipeline covers most needs; confirm art direction and breakpoints.

### Human-readable HTML sitemap for visitors

- **Description:** A browsable index of important pages for people (distinct from the machine XML sitemap).
- **Relevance:** Low
- **Transferability:** **Expect some work** — single theme page or lightweight app section.

### Subscribe & save and recurring billing

- **Description:** Customers enroll in schedules, renewals charge automatically, failed payments retry, and shoppers self‑serve changes where allowed.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify subscription contracts plus your chosen subscription partner.

### Store credit, gift value, and coupon strategies beyond simple codes

- **Description:** Balances can be held on the customer, applied at checkout, combined with promotions, and sometimes issued from support workflows.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify store credit / gift cards plus discount apps or Functions as needed.

### Complex cart discount rules (conditions, stacks, exclusions)

- **Description:** Discounts depend on cart composition, customer segments, channels, or time windows—not only a single promo code.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Discount Functions, Shopify Scripts successors, or discount apps.

### In‑funnel and post‑purchase upsells

- **Description:** Additional offers appear in the cart drawer, checkout path, or immediately after purchase to raise basket size.
- **Relevance:** High
- **Transferability:** **Expect some work** — checkout UI extensions and post‑purchase offer apps.

### Branded checkout with many payment options and vaulted cards

- **Description:** Checkout matches brand guidelines; shoppers may use cards on file, wallets, BNPL, or regional methods with a smooth UX.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Payments and enabled gateways; token migration where legally allowed.

### Third‑party fraud signals, manual review hooks, and dispute workflows

- **Description:** Orders are scored before capture; high‑risk flows are flagged; chargebacks produce finance‑friendly notes on the order.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Protect / fraud filters plus whichever third‑party fraud vendor you standardize on.

### Checkout abuse and bot mitigation

- **Description:** Automated checkout abuse is throttled with challenges or risk checks tuned for cosmetics/beauty traffic.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Shopify bot protection, Flow rules, or CAPTCHA/checkout apps.

### Tax determination and checkout address validation

- **Description:** Taxes follow the ship‑to jurisdiction; addresses are validated or corrected before fulfillment to cut carrier fees.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Tax plus carrier‑grade address validation apps.

### Warehouse and 3PL order lifecycle (export, ship, callback)

- **Description:** Orders are pushed to fulfillment partners; partners send ship, delay, or delivery signals back so statuses and emails stay accurate.
- **Relevance:** High
- **Transferability:** **Expect some work** — fulfillment apps and order webhooks; middleware only where ERP rules require it.

### Customer-facing shipment tracking and post‑purchase communications

- **Description:** After purchase, shoppers get tracking pages, proactive delay notices, and branded delivery experiences where configured.
- **Relevance:** High
- **Transferability:** **Expect some work** — post‑purchase tracking and delivery‑comms apps on Shopify plus transactional email design.

### ERP or finance system order posting

- **Description:** Accepted orders land in the corporate ERP for allocation, invoicing, or manufacturing—without manual re‑typing.
- **Relevance:** High
- **Transferability:** **Expect some work** — middleware or iPaaS posting Shopify orders into your ERP’s APIs.

### Email and SMS automation tied to storefront behavior

- **Description:** Browse, cart, checkout, and post‑purchase events drive segments, flows, and consent-aware messaging.
- **Relevance:** High
- **Transferability:** **Easy move / expect some work** — connect your ESP to Shopify; re‑wire events and consent carefully.

### Pop‑ups, banners, and gated lead capture

- **Description:** Campaigns show targeted overlays or forms based on URL, segment, or behavior; leads sync to marketing lists.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — embedded capture tools or Shopify‑native forms plus segmentation.

### Behavioral onsite personalization and triggered campaigns

- **Description:** Browse patterns change which creatives, reminders, or incentives a returning visitor sees across sessions.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — personalization vendors with Shopify connectors plus first‑party data hygiene.

### Product reviews, ratings, and Q&A surfaces

- **Description:** PDPs and landing blocks show syndicated or first‑party reviews with moderation and schema where needed.
- **Relevance:** High
- **Transferability:** **Expect some work** — review platforms on Shopify with import/migration planning.

### Loyalty points, tiers, and promotion codes generated from loyalty events

- **Description:** Customers earn and burn points; the stack can mint or revoke discount codes when loyalty rules fire.
- **Relevance:** High
- **Transferability:** **Expect some work** — loyalty suite on Shopify; align coupon policies with finance.

### Embedded third‑party trust and syndicated review portals

- **Description:** Trustpilot or similar widgets appear where marketing wants social proof beyond native reviews.
- **Relevance:** Medium
- **Transferability:** **Easy move** — vendor’s Shopify snippet or theme embed.

### Affiliate and partnership attribution

- **Description:** Partner links and conversions are tracked for commission reporting without double‑counting paid channels.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — affiliate/partner platforms with Shopify integration plus UTM governance.

### Social and ads catalog feeds (Meta, TikTok, etc.)

- **Description:** Product catalogs stay in sync with social commerce channels for ads and shoppable experiences.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Shopify sales channels and feed QA.

### Tag management and multi‑pixel measurement with server‑side options

- **Description:** GTM plus ad pixels (Meta, GA, etc.) fire consistently; server‑side or CAPI‑style events reduce loss from blockers.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Customer Privacy + partner pixels; validate revenue in QA.

### Helpdesk with full order timeline for agents

- **Description:** Support sees orders, tags, and key events beside tickets to answer “where is my order?” quickly.
- **Relevance:** High
- **Transferability:** **Expect some work** — helpdesk apps that sync the full order timeline from Shopify.

### Customer issue intake forms routed to support tooling

- **Description:** Shoppers submit structured requests (returns, product questions) that arrive in the ticketing stack.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — forms apps or native forms + Flow.

### Structured merchandising and editorial fields (repeatable promos, ingredients, claims)

- **Description:** Merch teams edit rich modules without developers—clinical claims, press logos, bundles, ingredients blocks, etc.
- **Relevance:** High
- **Transferability:** **Expect some work** — metafields, metaobjects, and theme sections; optional visual page builder.

### Campaign landing URLs separate from core PDP templates

- **Description:** Long‑form `/lpage/…` style experiences for launches, bundles, or partnerships with their own layout system.
- **Relevance:** High
- **Transferability:** **Expect some work** — Shopify Pages + sections; redirect legacy URLs.

### Guided quizzes and recommendation flows

- **Description:** Interactive questionnaires map answers to SKUs or routines (e.g., skincare quiz).
- **Relevance:** High
- **Transferability:** **Expect some work** — quiz app or custom theme flow writing to cart or line‑item properties.

### Editorial magazine content alongside commerce

- **Description:** Articles, series, and related reading patterns that cross‑link products without slowing every page.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Online Store blog templates and linking strategy.

### Rich “My account” area (subscriptions, orders, recommendations)

- **Description:** Logged‑in shoppers manage payment methods, subscriptions, reorders, and personalized picks in a branded shell.
- **Relevance:** High
- **Transferability:** **Expect some work** — new customer accounts strategy + subscription portal apps.

### Replacement, exchange, and reship workflows

- **Description:** Operations create parallel fulfillment records with reasons, notes, warehouse export, and customer comms like normal orders.
- **Relevance:** High
- **Transferability:** **Expect some work** — returns/exchange apps or draft‑order patterns; rebuild staff steps from section 10.

### Region-specific shipping methods and business rules

- **Description:** Certain countries get unique carriers, free‑shipping thresholds, or restrictions driven by policy.
- **Relevance:** High
- **Transferability:** **Expect some work** — carrier service configuration, Functions, or shipping apps.

### Carrier rate shopping and label generation where used

- **Description:** Some flows buy labels or show live carrier rates at checkout depending on origin/destination.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Shopify Shipping and/or multi‑carrier apps.

### Pre‑orders and launch windows

- **Description:** Shoppers can buy before inventory arrives with clear ship dates or authorization holds.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — preorder apps or selling plan APIs.

### Try‑before‑buy or trial programs (if offered)

- **Description:** Special fulfillment or authorization models for sampling programs.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — dedicated trial/tBYB apps; confirm legal and payment capture rules.

### Project‑tool‑driven coupon issuance

- **Description:** When a row in internal planning/ops workflow reaches “approved,” the store receives a ready‑to‑use discount aligned to that campaign.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Shopify Flow, discount API, or middleware listening to the project tool.

### Optional shipping protection upsell at checkout

- **Description:** Shoppers can add parcel insurance or protection for a fee before paying.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — shipping protection apps or checkout line‑item.

### Address autocomplete and formatting in checkout

- **Description:** Reduces typos and speeds mobile checkout using a lookup provider.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — checkout extension or app providing suggestions.

### Seasonal merchandising toggles

- **Description:** Timed banners, product grids, or promos flip on/off for holidays without code deploys.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — theme settings, metaobject flags, or scheduling apps.

### Abandoned checkout and browse recovery messaging

- **Description:** Shoppers who drop receive timed reminders with cart contents and compliance with consent.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — ESP‑driven recovery plus Shopify checkout abandonment features.

### No‑code automations between the store and other SaaS

- **Description:** Zapier‑style triggers move orders, tags, or customers into spreadsheets, Slack, or databases.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — Shopify Flow plus native Zapier/Make connectors.

### Operations analytics beyond native Shopify reports

- **Description:** Finance and ops export cohorts, LTV views, or custom slices for weekly reviews.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — ShopifyQL, BI export, or analytics vendors with Shopify connectors.

### Optional marketplace listing sync

- **Description:** Selected SKUs sync to external marketplaces with inventory guards.
- **Relevance:** Medium
- **Transferability:** **Expect some work** — marketplace connector apps per channel.

### WordPress editorial ergonomics (admin columns, duplicating posts, SMTP)

- **Description:** Editors work faster inside WP admin; transactional mail uses a dedicated SMTP provider.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify** — replace with Shopify admin patterns and Shopify/email vendor settings.

### Staff login hardening (two‑factor, role granularity)

- **Description:** Extra protection and fine roles for large content/marketing teams.
- **Relevance:** Low
- **Transferability:** **Not part of Shopify** — map to Shopify org security and staff permissions.


---

> [!TIP]
> **Regenerate this file** after the theme or integrations change: from the WordPress project folder run `python docs/generate-shopify-inventory.py`.
