#!/usr/bin/env python3
"""Emit docs/shopify-migration-features-inventory.md (theme summaries + capability rows, no plugin folder list)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "wp-content" / "themes" / "particleformen"


def emit_capability_inventory() -> str:
    """Section 11: business capabilities — no WordPress package names."""
    rows: list[tuple[str, str, str, str]] = [
        (
            "Core catalog, cart, checkout, and orders",
            "Shoppers discover products, configure variants, use a cart, complete checkout, and receive confirmations; "
            "staff rely on order records, statuses, and customer-visible order history.",
            "High",
            "**Needs a fresh build** — Shopify becomes the commerce system of record; every edge case must be re‑validated.",
        ),
        (
            "Multilingual storefront and market-aware pricing",
            "URLs, navigation, and product copy follow the shopper’s language; prices and settlement currency follow market rules.",
            "High",
            "**Expect some work** — Shopify Markets plus translation workflow; plan redirects and bookmarks.",
        ),
        (
            "Locale-specific media when marketing differs by country",
            "Some regions need different hero images, PDFs, or downloads than the default language—not only translated text.",
            "Medium",
            "**Expect some work** — metafields, metaobjects, or per‑market content in the theme.",
        ),
        (
            "Search engine metadata, structured data, XML sitemaps, and hreflang",
            "Pages expose correct titles/descriptions, rich results where appropriate, crawlable sitemaps, and language alternates for Google.",
            "High",
            "**Expect some work** — Shopify SEO fields, JSON‑LD apps or theme logic, sitemap + Markets hreflang strategy.",
        ),
        (
            "Redirect management and legacy URL hygiene",
            "301/302 rules and logs when campaigns end or paths change; avoids broken inbound links.",
            "High",
            "**Expect some work** — import redirects into Shopify; keep a governance process.",
        ),
        (
            "Full‑page and asset performance (caching, compression, script bundling)",
            "HTML and static assets are cached and minified so repeat visits feel fast on real devices.",
            "Medium",
            "**Not part of Shopify 1:1** — Shopify’s CDN and theme performance replace host‑specific caching; still needs tuning.",
        ),
        (
            "Image weight and modern formats in the storefront",
            "Images are resized, compressed, and served in efficient formats where browsers support them.",
            "Low",
            "**Easy move / expect some work** — Shopify’s image pipeline covers most needs; confirm art direction and breakpoints.",
        ),
        (
            "Human-readable HTML sitemap for visitors",
            "A browsable index of important pages for people (distinct from the machine XML sitemap).",
            "Low",
            "**Expect some work** — single theme page or lightweight app section.",
        ),
        (
            "Subscribe & save and recurring billing",
            "Customers enroll in schedules, renewals charge automatically, failed payments retry, and shoppers self‑serve changes where allowed.",
            "High",
            "**Expect some work** — Shopify subscription contracts plus your chosen subscription partner.",
        ),
        (
            "Store credit, gift value, and coupon strategies beyond simple codes",
            "Balances can be held on the customer, applied at checkout, combined with promotions, and sometimes issued from support workflows.",
            "High",
            "**Expect some work** — Shopify store credit / gift cards plus discount apps or Functions as needed.",
        ),
        (
            "Complex cart discount rules (conditions, stacks, exclusions)",
            "Discounts depend on cart composition, customer segments, channels, or time windows—not only a single promo code.",
            "High",
            "**Expect some work** — Shopify Discount Functions, Shopify Scripts successors, or discount apps.",
        ),
        (
            "In‑funnel and post‑purchase upsells",
            "Additional offers appear in the cart drawer, checkout path, or immediately after purchase to raise basket size.",
            "High",
            "**Expect some work** — checkout UI extensions and post‑purchase offer apps.",
        ),
        (
            "Branded checkout with many payment options and vaulted cards",
            "Checkout matches brand guidelines; shoppers may use cards on file, wallets, BNPL, or regional methods with a smooth UX.",
            "High",
            "**Expect some work** — Shopify Payments and enabled gateways; token migration where legally allowed.",
        ),
        (
            "Third‑party fraud signals, manual review hooks, and dispute workflows",
            "Orders are scored before capture; high‑risk flows are flagged; chargebacks produce finance‑friendly notes on the order.",
            "High",
            "**Expect some work** — Shopify Protect / fraud filters plus whichever third‑party fraud vendor you standardize on.",
        ),
        (
            "Checkout abuse and bot mitigation",
            "Automated checkout abuse is throttled with challenges or risk checks tuned for cosmetics/beauty traffic.",
            "Medium",
            "**Expect some work** — Shopify bot protection, Flow rules, or CAPTCHA/checkout apps.",
        ),
        (
            "Tax determination and checkout address validation",
            "Taxes follow the ship‑to jurisdiction; addresses are validated or corrected before fulfillment to cut carrier fees.",
            "High",
            "**Expect some work** — Shopify Tax plus carrier‑grade address validation apps.",
        ),
        (
            "Warehouse and 3PL order lifecycle (export, ship, callback)",
            "Orders are pushed to fulfillment partners; partners send ship, delay, or delivery signals back so statuses and emails stay accurate.",
            "High",
            "**Expect some work** — fulfillment apps and order webhooks; middleware only where ERP rules require it.",
        ),
        (
            "Customer-facing shipment tracking and post‑purchase communications",
            "After purchase, shoppers get tracking pages, proactive delay notices, and branded delivery experiences where configured.",
            "High",
            "**Expect some work** — post‑purchase tracking and delivery‑comms apps on Shopify plus transactional email design.",
        ),
        (
            "ERP or finance system order posting",
            "Accepted orders land in the corporate ERP for allocation, invoicing, or manufacturing—without manual re‑typing.",
            "High",
            "**Expect some work** — middleware or iPaaS posting Shopify orders into your ERP’s APIs.",
        ),
        (
            "Email and SMS automation tied to storefront behavior",
            "Browse, cart, checkout, and post‑purchase events drive segments, flows, and consent-aware messaging.",
            "High",
            "**Easy move / expect some work** — connect your ESP to Shopify; re‑wire events and consent carefully.",
        ),
        (
            "Pop‑ups, banners, and gated lead capture",
            "Campaigns show targeted overlays or forms based on URL, segment, or behavior; leads sync to marketing lists.",
            "Medium",
            "**Expect some work** — embedded capture tools or Shopify‑native forms plus segmentation.",
        ),
        (
            "Behavioral onsite personalization and triggered campaigns",
            "Browse patterns change which creatives, reminders, or incentives a returning visitor sees across sessions.",
            "Medium",
            "**Expect some work** — personalization vendors with Shopify connectors plus first‑party data hygiene.",
        ),
        (
            "Product reviews, ratings, and Q&A surfaces",
            "PDPs and landing blocks show syndicated or first‑party reviews with moderation and schema where needed.",
            "High",
            "**Expect some work** — review platforms on Shopify with import/migration planning.",
        ),
        (
            "Loyalty points, tiers, and promotion codes generated from loyalty events",
            "Customers earn and burn points; the stack can mint or revoke discount codes when loyalty rules fire.",
            "High",
            "**Expect some work** — loyalty suite on Shopify; align coupon policies with finance.",
        ),
        (
            "Embedded third‑party trust and syndicated review portals",
            "Trustpilot or similar widgets appear where marketing wants social proof beyond native reviews.",
            "Medium",
            "**Easy move** — vendor’s Shopify snippet or theme embed.",
        ),
        (
            "Affiliate and partnership attribution",
            "Partner links and conversions are tracked for commission reporting without double‑counting paid channels.",
            "Medium",
            "**Expect some work** — affiliate/partner platforms with Shopify integration plus UTM governance.",
        ),
        (
            "Social and ads catalog feeds (Meta, TikTok, etc.)",
            "Product catalogs stay in sync with social commerce channels for ads and shoppable experiences.",
            "Medium",
            "**Expect some work** — Shopify sales channels and feed QA.",
        ),
        (
            "Tag management and multi‑pixel measurement with server‑side options",
            "GTM plus ad pixels (Meta, GA, etc.) fire consistently; server‑side or CAPI‑style events reduce loss from blockers.",
            "High",
            "**Expect some work** — Shopify Customer Privacy + partner pixels; validate revenue in QA.",
        ),
        (
            "Helpdesk with full order timeline for agents",
            "Support sees orders, tags, and key events beside tickets to answer “where is my order?” quickly.",
            "High",
            "**Expect some work** — helpdesk apps that sync the full order timeline from Shopify.",
        ),
        (
            "Customer issue intake forms routed to support tooling",
            "Shoppers submit structured requests (returns, product questions) that arrive in the ticketing stack.",
            "Medium",
            "**Expect some work** — forms apps or native forms + Flow.",
        ),
        (
            "Structured merchandising and editorial fields (repeatable promos, ingredients, claims)",
            "Merch teams edit rich modules without developers—clinical claims, press logos, bundles, ingredients blocks, etc.",
            "High",
            "**Expect some work** — metafields, metaobjects, and theme sections; optional visual page builder.",
        ),
        (
            "Campaign landing URLs separate from core PDP templates",
            "Long‑form `/lpage/…` style experiences for launches, bundles, or partnerships with their own layout system.",
            "High",
            "**Expect some work** — Shopify Pages + sections; redirect legacy URLs.",
        ),
        (
            "Guided quizzes and recommendation flows",
            "Interactive questionnaires map answers to SKUs or routines (e.g., skincare quiz).",
            "High",
            "**Expect some work** — quiz app or custom theme flow writing to cart or line‑item properties.",
        ),
        (
            "Editorial magazine content alongside commerce",
            "Articles, series, and related reading patterns that cross‑link products without slowing every page.",
            "Medium",
            "**Expect some work** — Online Store blog templates and linking strategy.",
        ),
        (
            "Rich “My account” area (subscriptions, orders, recommendations)",
            "Logged‑in shoppers manage payment methods, subscriptions, reorders, and personalized picks in a branded shell.",
            "High",
            "**Expect some work** — new customer accounts strategy + subscription portal apps.",
        ),
        (
            "Replacement, exchange, and reship workflows",
            "Operations create parallel fulfillment records with reasons, notes, warehouse export, and customer comms like normal orders.",
            "High",
            "**Expect some work** — returns/exchange apps or draft‑order patterns; rebuild staff steps from section 10.",
        ),
        (
            "Region-specific shipping methods and business rules",
            "Certain countries get unique carriers, free‑shipping thresholds, or restrictions driven by policy.",
            "High",
            "**Expect some work** — carrier service configuration, Functions, or shipping apps.",
        ),
        (
            "Carrier rate shopping and label generation where used",
            "Some flows buy labels or show live carrier rates at checkout depending on origin/destination.",
            "Medium",
            "**Expect some work** — Shopify Shipping and/or multi‑carrier apps.",
        ),
        (
            "Pre‑orders and launch windows",
            "Shoppers can buy before inventory arrives with clear ship dates or authorization holds.",
            "Medium",
            "**Expect some work** — preorder apps or selling plan APIs.",
        ),
        (
            "Try‑before‑buy or trial programs (if offered)",
            "Special fulfillment or authorization models for sampling programs.",
            "Medium",
            "**Expect some work** — dedicated trial/tBYB apps; confirm legal and payment capture rules.",
        ),
        (
            "Project‑tool‑driven coupon issuance",
            "When a row in internal planning/ops workflow reaches “approved,” the store receives a ready‑to‑use discount aligned to that campaign.",
            "Medium",
            "**Expect some work** — Shopify Flow, discount API, or middleware listening to the project tool.",
        ),
        (
            "Optional shipping protection upsell at checkout",
            "Shoppers can add parcel insurance or protection for a fee before paying.",
            "Medium",
            "**Expect some work** — shipping protection apps or checkout line‑item.",
        ),
        (
            "Address autocomplete and formatting in checkout",
            "Reduces typos and speeds mobile checkout using a lookup provider.",
            "Medium",
            "**Expect some work** — checkout extension or app providing suggestions.",
        ),
        (
            "Seasonal merchandising toggles",
            "Timed banners, product grids, or promos flip on/off for holidays without code deploys.",
            "Medium",
            "**Expect some work** — theme settings, metaobject flags, or scheduling apps.",
        ),
        (
            "Abandoned checkout and browse recovery messaging",
            "Shoppers who drop receive timed reminders with cart contents and compliance with consent.",
            "Medium",
            "**Expect some work** — ESP‑driven recovery plus Shopify checkout abandonment features.",
        ),
        (
            "No‑code automations between the store and other SaaS",
            "Zapier‑style triggers move orders, tags, or customers into spreadsheets, Slack, or databases.",
            "Medium",
            "**Expect some work** — Shopify Flow plus native Zapier/Make connectors.",
        ),
        (
            "Operations analytics beyond native Shopify reports",
            "Finance and ops export cohorts, LTV views, or custom slices for weekly reviews.",
            "Medium",
            "**Expect some work** — ShopifyQL, BI export, or analytics vendors with Shopify connectors.",
        ),
        (
            "Optional marketplace listing sync",
            "Selected SKUs sync to external marketplaces with inventory guards.",
            "Medium",
            "**Expect some work** — marketplace connector apps per channel.",
        ),
        (
            "WordPress editorial ergonomics (admin columns, duplicating posts, SMTP)",
            "Editors work faster inside WP admin; transactional mail uses a dedicated SMTP provider.",
            "Low",
            "**Not part of Shopify** — replace with Shopify admin patterns and Shopify/email vendor settings.",
        ),
        (
            "Staff login hardening (two‑factor, role granularity)",
            "Extra protection and fine roles for large content/marketing teams.",
            "Low",
            "**Not part of Shopify** — map to Shopify org security and staff permissions.",
        ),
    ]

    lines: list[str] = [
        "---\n\n",
        "## 11. Store capabilities to re‑home on Shopify (no plugin names)\n\n",
        "> [!NOTE]\n",
        "> This section is **only business capabilities**—things shoppers, marketing, finance, or ops need after migration. "
        "It intentionally **does not** name WordPress plugin folders, SEO suites, cache plugins, image optimizers, or translation packages; "
        "those are implementation details. Map each capability to Shopify native features, first‑party channels, or an app category.\n\n",
    ]
    for title, desc, rel, xfer in rows:
        lines.append(f"### {title}\n\n")
        lines.append(f"- **Description:** {desc}\n")
        lines.append(f"- **Relevance:** {rel}\n")
        lines.append(f"- **Transferability:** {xfer}\n\n")
    return "".join(lines)


def main() -> None:
    out = ROOT / "docs" / "shopify-migration-features-inventory.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    blocks = sorted(
        d.parent.name
        for d in (THEME / "app" / "blocks").rglob("block.php")
        if d.is_file()
    )

    woo_tpl = sorted(
        str(p.relative_to(THEME)).replace("\\", "/")
        for p in (THEME / "woocommerce").rglob("*.php")
        if p.is_file()
    )

    theme_libs = [
        "lib/image-sizes.php",
        "lib/custom-post-types.php",
        "lib/remove-trash.php",
        "lib/script-style.php",
        "lib/gutenberg/gutenberg.php",
        "lib/acf/acf.php",
        "lib/ajaxFunctions.php",
        "lib/theme-setup.php",
        "lib/accessibility.php",
        "lib/woocommerce-setup.php",
        "lib/checkout.php",
        "lib/rest-api.php",
        "lib/seo.php",
        "lib/retention.php",
        "lib/request-checker.php",
        "lib/admin-dashboard.php",
        "lib/meta-shop-checkout.php",
        "lib/utils.php",
        "lib/super-editor.php",
        "lib/cart-functions.php",
        "lib/ab-tests.php",
        "lib/class-particle-klaviyo-helper.php",
        "lib/optimization.php",
        "lib/retention-lp-utils.php",
    ]

    body: list[str] = []
    body.append("# Shopify migration — features inventory (Particle For Men)\n\n")
    body.append(
        "> [!NOTE]\n"
        "> This document lists **what the current website and back office can do** so your team can talk to Shopify with fewer surprises. "
        "It was built from a technical review of the store code; this version is written so **non‑technical readers can follow the story**.\n\n"
    )
    body.append("### How to read each row\n\n")
    body.append("| Column | What it means |\n")
    body.append("| --- | --- |\n")
    body.append(
        "| **Description** | In plain words: what customers, support, or the warehouse experience because of this item. |\n"
    )
    body.append(
        "| **Relevance** | **High** — money, legal, shipping, languages, or subscriptions. "
        "**Medium** — marketing, content, or important experience. **Low** — small convenience or mostly internal. |\n"
    )
    body.append(
        "| **Transferability** | **Easy move** — close match in Shopify or a common partner. "
        "**Expect some work** — apps or a short custom project. **Needs a fresh build** — redesign on Shopify. "
        "**Not part of Shopify** — goes away when WordPress is retired. |\n\n"
    )
    body.append(
        "Theme wiring and checkout templates are summarized **once each** (not every PHP filename). "
        "**Section 11** is a **capability checklist** (what the business must still have on Shopify)—not a list of WordPress package names.\n\n"
    )
    body.append("---\n\n")

    body.append("## Legend (quick read)\n\n")
    body.append("| Level | Typical scope |\n")
    body.append("| --- | --- |\n")
    body.append(
        "| **High** | Shoppers, revenue, tax, fraud, shipping, languages/currencies, subscriptions, or day‑to‑day operations. |\n"
    )
    body.append(
        "| **Medium** | Marketing, reviews, email, landing pages, SEO, or noticeable shopper experience. |\n"
    )
    body.append(
        "| **Low** | Editor helpers, host‑specific tools, or things that rarely affect the customer journey. |\n\n"
    )
    body.append("---\n\n")

    body.append("## 0. Big moving parts (several add-ons work together)\n\n")
    body.append(
        "> [!TIP]\n"
        "> These threads describe **whole workflows** that align with the capability checklist in section 11. "
        "Use them in workshops; they do not replace the detailed rows below.\n\n"
    )
    threads = [
        (
            "Many countries, many languages, many currencies",
            "Today the store can show different languages and charge in different currencies depending on where someone shops. "
            "That touches the header language picker, product links, cart, and how prices convert. "
            "On Shopify this becomes **Markets** (and careful planning for links people already bookmarked). "
            "Some wording also comes from **inside** add-ons (see the next thread)—not only from normal page editors.",
            "High",
            "**Expect some work** — Shopify handles the idea well, but the exact setup and redirects need a dedicated project.",
        ),
        (
            "Translating text that comes from inside add-ons (not from normal pages)",
            "Besides translating whole pages, the team can translate **short strings** that originate inside plugins or the theme—"
            "things like a button label baked into an add-on, a checkout message, or a tiny widget line. "
            "On WordPress this is part of the same multilingual story as page translation; on Shopify the same outcome is usually "
            "**theme locale files**, **translation apps**, or Markets-aware copy in apps—planned together with the main language rollout.",
            "High",
            "**Expect some work** — bundle it with Markets and your translation process so no “mystery English” is left in foreign storefronts.",
        ),
        (
            "Subscribe & save (recurring orders)",
            "Customers can put products on a schedule with renewals, price changes over time, and self‑service changes. "
            "Several add‑ons and custom tools support that today—including internal staff screens for fixes and notes.",
            "High",
            "**Expect some work** — Shopify has subscription tools, but every billing rule must be checked one by one.",
        ),
        (
            "Fraud and risky orders",
            "Before an order is accepted, outside services score risk; bots can be blocked and some checkout steps are watched closely.",
            "High",
            "**Expect some work** — Shopify has built‑in fraud signals; reconnect your chosen fraud vendors via apps.",
        ),
        (
            "Getting the box out the door (and telling the customer where it is)",
            "Primary 3PL, tracking communications, warehouse export jobs, and ERP order posting together keep shoppers, warehouse, and finance aligned on fulfillment state.",
            "High",
            "**Expect some work** — Connectors and emails are rebuilt using Shopify’s order updates plus partner apps.",
            True,
        ),
        (
            "Ads, pixels, and “who clicked what”",
            "Google Tag Manager, Meta/TikTok pixels, affiliate tools, pop‑ups, and similar tags feed marketing teams.",
            "High",
            "**Expect some work** — Most partners publish a Shopify‑ready snippet; still needs QA so sales numbers stay trustworthy.",
            False,
        ),
    ]
    for thread in threads:
        title, desc, rel, xfer = thread[0], thread[1], thread[2], thread[3]
        shipstation_caution = thread[4] if len(thread) > 4 else False
        body.append(f"### {title}\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append(f"- **Relevance:** {rel}\n")
        body.append(f"- **Transferability:** {xfer}\n")
        if shipstation_caution:
            body.append(
                "\n> [!CAUTION]\n"
                "> A **ShipStation** add‑on exists in the code folder, but **Particle does not use ShipStation**—"
                "do not budget it for Shopify unless you explicitly adopt that product.\n"
            )
        body.append("\n")

    n_libs = len(theme_libs)
    body.append("## 1. The storefront “glue” (theme code)\n\n")
    body.append("### Custom Particle theme wiring\n\n")
    body.append(
        "- **Description:** "
        f"About **{n_libs}** small code modules load with every page to connect the design to real store behavior—cart, checkout, "
        "languages, coupons, marketing‑automation emails, address checks, SEO, quizzes, A/B tests, and more. "
        "Think of this as the **instruction list behind the scenes**; shoppers never see the filenames. "
        "Engineers use the theme’s `functions.php` file if they need the exact list.\n"
    )
    body.append("- **Relevance:** High\n")
    body.append(
        "- **Transferability:** **Expect some work** — Shopify replaces the whole engine, but each shopper-facing habit must be checked so nothing is lost.\n\n"
    )

    body.append("## 2. Special rules baked into the old checkout & blog\n\n")
    body.append("### Language picks the default currency\n\n")
    body.append(
        "- **Description:** When someone picks a country/language, the store quietly switches which currency prices use "
        "(for example Australia → Australian dollars, Japan → yen, EU countries → euros).\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** **Expect some work** — Shopify Markets handles the same idea with a cleaner setup.\n\n")
    body.append("### Lighter blog reading mode\n\n")
    body.append(
        "- **Description:** Certain magazine-style articles load without heavy shop scripts so they feel faster on slow phones.\n"
    )
    body.append("- **Relevance:** Low\n")
    body.append("- **Transferability:** **Expect some work** — recreate with a simple Shopify blog template if still wanted.\n\n")
    body.append("### Blocked test phone numbers at checkout\n\n")
    body.append(
        "- **Description:** A short internal list of phone numbers is rejected at checkout to stop known bad actors.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** **Expect some work** — rebuild as a Shopify Flow rule or checkout validation app.\n\n")
    body.append("### Extra coupon bookkeeping\n\n")
    body.append(
        "- **Description:** Custom logic changes how some coupon details are stored in the database—usually tied to a promotion partner. "
        "Business stakeholders should confirm **why** it exists before copying anything.\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** **Needs a fresh build** — must be understood before promising the same behavior on Shopify.\n\n")
    body.append("### Magazine helpers & SEO tweaks\n\n")
    body.append(
        "- **Description:** Related articles, breadcrumbs, and legacy SEO/editor settings that change how some URLs and snippets behave.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** **Expect some work** — rebuild redirects and metadata inside Shopify.\n\n")

    tpl_files = sorted(p.name for p in (THEME / "template").glob("*.php"))
    tpl_list = ", ".join(f"`{n}`" for n in tpl_files)
    body.append("## 3. Campaign & landing page layouts\n\n")
    body.append("### Special WordPress page layouts\n\n")
    body.append(
        "- **Description:** "
        f"The merchandising team can attach **{len(tpl_files)}** custom layouts to normal WordPress pages for big campaigns—"
        f"examples include Build‑Your‑Own Bundle, Marsmen‑style product stories, commercials, consultations, Amazon gift flows, "
        f"and thank‑you pages. File names for reference: {tpl_list}.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** **Expect some work** — rebuild as Shopify pages with reusable sections and plan URL redirects.\n\n")

    blocks_preview = ", ".join(f"`{b}`" for b in blocks[:40])
    blocks_suffix = "" if len(blocks) <= 40 else f" …and **{len(blocks) - 40}** more."
    body.append("## 4. Drag‑and‑drop content blocks for editors\n\n")
    body.append("### Custom content blocks (Gutenberg)\n\n")
    body.append(
        "- **Description:** "
        f"Editors have **{len(blocks)}** reusable blocks for rich storytelling—best sellers, bundles, FAQs, reviews, quizzes, "
        f"Gravité‑specific promos, sliders, press logos, Instagram grids, post‑purchase thank‑you snippets, ingredients, clinical claims, "
        f"and more. Sample block names: {blocks_preview}{blocks_suffix}.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** **Expect some work** — rebuild as Shopify sections or metaobject‑driven content.\n\n")

    body.append("## 5. Cart, checkout, and “my account” screens\n\n")
    body.append("### Branded shopping funnel templates\n\n")
    body.append(
        "- **Description:** "
        f"The Particle design replaces **{len(woo_tpl)}** of WooCommerce’s default screens—cart drawer, checkout (including older vs newer versions), "
        "subscription renewals, customer account area, product detail layouts, and galleries. Shoppers experience this as “the Particle checkout,” "
        "not as individual files.\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** **Expect some work** — Shopify checkout + customer accounts look different; plan a UX review, not a copy‑paste.\n\n")

    body.append("## 6. Landing page content type\n\n")
    body.append("### “Landing pages” content bucket\n\n")
    body.append(
        "- **Description:** A dedicated content type powers long‑form campaign URLs that start with `/lpage/…`, separate from normal products.\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** **Expect some work** — map to Shopify pages or landing apps and redirect old links.\n\n")

    body.append("## 7. Behind‑the‑scenes data feeds & webhooks\n\n")
    body.append(
        "> [!TIP]\n"
        "> Shoppers never see these feeds, but **marketing, warehouse, and finance** often depend on them.\n\n"
    )
    rest_items = [
        ("SMS send and verification", "Lets the site send or verify text messages (for example two‑step flows) via a messaging gateway."),
        (
            "Email platform profile sync from forms",
            "Keeps marketing‑database profiles in sync when someone completes special forms or promotions.",
        ),
        ("Email verification for promotions", "Confirms email addresses before certain promotions unlock."),
        (
            "Payment processor dispute signals",
            "When the card processor flags a dispute, the site can attach notes to the matching order for finance.",
        ),
        ("Order and subscription notes for staff tools", "Lets trusted internal tools read or write internal notes on orders or subscriptions."),
        (
            "AI and search crawler visit analytics",
            "Aggregates stored crawler traffic (which URLs were visited and how often over time) for monitoring and SEO-related visibility—shoppers never see this screen.",
        ),
        (
            "Primary warehouse shipment callbacks",
            "The main 3PL tells the site when a parcel ships, is delayed, or is delivered so statuses and emails stay accurate.",
        ),
        ("Secondary warehouse shipment callbacks", "A second logistics partner uses the same style of shipped/delivered signals."),
        (
            "Project‑tool‑driven coupon creation",
            "Creates or updates coupons when an external project or ops workflow reaches the right state.",
        ),
        (
            "Loyalty‑driven coupon automation",
            "Creates or cancels discount codes automatically when loyalty rules fire.",
        ),
        (
            "Miscellaneous staff helper hooks",
            "Small one-off endpoints used by internal dashboards—engineering should confirm which are still called.",
        ),
        ("Chargeback lookup", "Looks up chargeback status for a given order for finance/support."),
        ("Geo privacy gate", "Controls what appears based on privacy / geography rules."),
        ("Partner catalog and coupon export", "Exposes catalog and coupon data for an external partner system."),
        (
            "Behavioral marketing product feed",
            "Sends catalog snapshots to a partner that powers browse‑based onsite campaigns.",
        ),
        ("Order summary widget", "Feeds a small admin widget with order totals."),
        (
            "Lead‑capture campaign mapping",
            "Maps lead‑capture campaigns to the right storefront content when that integration is enabled.",
        ),
        (
            "Email marketing platform maintenance hooks",
            "Server endpoints keep the email platform in sync with forms, lists, and custom events—rarely shopper facing.",
        ),
        (
            "SEO and performance tooling maintenance hooks",
            "Background jobs for search metadata, sitemaps, or HTML/asset cache housekeeping—rarely shopper facing.",
        ),
    ]
    for title, desc in rest_items:
        body.append(f"### {title}\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append(
            "- **Relevance:** Medium to High — only matters if finance, warehouse, marketing, or a partner integration still relies on this feed.\n"
        )
        body.append("- **Transferability:** **Expect some work** — rebuild using Shopify webhooks, partner apps, or a small middleware service.\n\n")

    body.append("## 8. Always‑on WordPress “safety” files\n\n")
    mu_custom = [
        (
            "pfm-braintree-api-access.php",
            "Lets trusted server jobs talk to Braintree with the right credentials.",
            "High",
            "**Expect some work:** move secrets to the new hosting model; reconnect Braintree where still needed.",
        ),
        (
            "redirections.php",
            "Guesses the shopper’s language, fixes URLs, and remembers multilingual `store_switch` choices.",
            "High",
            "**Expect some work:** rebuild with Shopify Markets + redirect import.",
        ),
        (
            "pfm-performance.php",
            "Small performance tweaks specific to this host/theme combo.",
            "Medium",
            "**Not part of Shopify:** Shopify handles performance differently.",
        ),
        (
            "custom_plugin_organizer.php",
            "Controls which heavy plugins load during AJAX, and fixes cart redirects when languages are involved.",
            "High",
            "**Expect some work:** not needed on Shopify, but behaviors (like redirects) must be reproduced if shoppers rely on them.",
        ),
        (
            "woocommerce-additional.php",
            "Extra WooCommerce hooks loaded very early—confirm with engineering what they still do.",
            "Medium",
            "**Expect some work:** validate before cutover.",
        ),
        (
            "om-map-output.php",
            "Optional helper for lead‑capture campaign mapping.",
            "Low",
            "**Expect some work:** only if the same lead‑capture tooling stays in the marketing stack.",
        ),
    ]
    for fname, desc, rel, xfer in mu_custom:
        body.append(f"### Always‑on file: `{fname}`\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append(f"- **Relevance:** {rel}\n")
        body.append(f"- **Transferability:** {xfer}\n\n")

    body.append("### WP Engine hosting bundles\n\n")
    body.append(
        "- **Description:** Caching, forced security patches, login helpers, and other tools injected by the WP Engine host. "
        "They keep WordPress healthy but are invisible to shoppers.\n"
    )
    body.append("- **Relevance:** Low for the Shopify project itself\n")
    body.append("- **Transferability:** **Not part of Shopify:** disappears when WordPress is retired.\n\n")

    body.append("## 9. Saved HTML snapshots (research only)\n\n")
    body.append(
        "- **Description:** A folder of frozen HTML captures from the live site helps double‑check which marketing tags, "
        "languages, and subscription links appear in the real storefront. Path on disk: "
        "`C:\\Users\\denis_particleformen\\Desktop\\Cursor Projects\\particleformen-scrape\\output\\html`.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** **Not part of Shopify:** reference material only.\n\n")

    body.append("---\n\n")

    pfm_section = ROOT / "docs" / "_pfm-panel-section.md"
    if pfm_section.is_file():
        body.append(pfm_section.read_text(encoding="utf-8").rstrip() + "\n\n")
    else:
        body.append(
            "## 10. Internal staff tools (`pfm-panel`)\n\n"
            "_(Missing `docs/_pfm-panel-section.md` — run from repo with snippet present.)_\n\n"
        )

    body.append(emit_capability_inventory())

    body.append(
        "\n---\n\n> [!TIP]\n"
        "> **Regenerate this file** after the theme or integrations change: from the WordPress project folder run "
        "`python docs/generate-shopify-inventory.py`.\n"
    )

    out.write_text("".join(body), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
