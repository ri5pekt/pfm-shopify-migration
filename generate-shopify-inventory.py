#!/usr/bin/env python3
"""Emit docs/shopify-migration-features-inventory.md (exhaustive plugin + theme inventory)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "wp-content" / "plugins"
THEME = ROOT / "wp-content" / "themes" / "particleformen"

# Folders under wp-content/plugins/ omitted from §11 (still on disk, not inventoried as product rows).
EXCLUDED_PLUGIN_SLUGS: frozenset[str] = frozenset(
    {
        "yith-woocommerce-gift-cards-premium",  # not used; Smart Coupons / Shopify gift cards cover the need
        "wpmudev-updates",  # WPMU DEV license updater client only
        "wpml-string-translation",  # explained as a workflow in §0 — avoids duplicating WPML under a second package name
    }
)

# Overrides: slug -> (description, relevance, transferability)
CUSTOM: dict[str, tuple[str, str, str]] = {
    "sitepress-multilingual-cms": (
        "Runs the store’s multiple languages—translated pages, menus, and the correct links for Google in each country.",
        "High",
        "**Expect some work:** Shopify Markets plus translation tools replace most of this, but bookmarks and URLs need a careful plan.",
    ),
    "woocommerce-multilingual": (
        "Pairs languages with the right currency and exchange rates so visitors see familiar money symbols.",
        "High",
        "**Expect some work:** Shopify Markets covers the same idea with different settings; any special rules must be re‑entered.",
    ),
    "wpml-media-translation": (
        "Lets each language version of the site use its own photos or PDFs when needed.",
        "Medium",
        "**Expect some work:**",
    ),
    "woocommerce-subscriptions": (
        "Powers subscribe‑and‑save: renewals, failed payment retries, and customer self‑service for delivery schedules.",
        "High",
        "**Expect some work:** Shopify’s subscription tools are close, but every price and interval must be checked.",
    ),
    "woocommerce-subscription": (
        "Companion tools that sit next to the main subscription engine—confirm with the web team whether both are active.",
        "High",
        "**Expect some work:**",
    ),
    "subscriptions-utils": (
        "Particle‑specific helpers that tweak how subscriptions behave behind the scenes.",
        "High",
        "**Needs a fresh build:** replan each behavior inside Shopify Flow, a subscription partner, or a small custom service.",
    ),
    "pfm-panel": (
        "The internal “mission control” staff use to search orders, resend emails, push refunds, adjust store credit, export to the warehouse, and similar day‑to‑day jobs.",
        "High",
        "**Needs a fresh build:** Shopify Admin plus Flow/partner apps—or a lightweight custom dashboard—replace this over time.",
    ),
    "particleformen-checkout": (
        "Particle‑specific checkout tweaks layered on top of WooCommerce (together with the theme checkout code).",
        "High",
        "**Expect some work:** Shopify Checkout allows apps and small UI extensions instead of the old PHP approach.",
    ),
    "all-upsells": (
        "Upsell flows: thank-you page, post-purchase, BAS/PPU modules (see `includes/`).",
        "High",
        "**Expect some work:** post-purchase apps, checkout upsell extensions.",
    ),
    "custom-coupon": (
        "Custom coupon logic beyond core Woo coupons.",
        "High",
        "**Expect some work:** Shopify Discount Functions / discount apps.",
    ),
    "pfm-store-credits": (
        "Store credit balance and checkout application (frontend + admin).",
        "High",
        "**Expect some work:** Shopify store credit / gift card primitives differ; likely app or custom.",
    ),
    "pfm-monday-coupons": (
        "REST-driven coupon integration (Monday workflow).",
        "Medium",
        "**Expect some work:** Zapier/Flow + discount APIs.",
    ),
    "woo-discount-rules": (
        "Discount Rules for WooCommerce (conditional cart rules).",
        "High",
        "**Expect some work:** Shopify Functions + discount apps.",
    ),
    "woo-discount-rules-pro": (
        "Pro tier for Discount Rules (extra rule types).",
        "High",
        "**Expect some work:**",
    ),
    "woocommerce-smart-coupons": (
        "Smart Coupons: store credit, gift certificates, bulk coupons, blocks.",
        "High",
        "**Expect some work:** Shopify gift cards / discount combinations via apps.",
    ),
    "cart-sidebar": (
        "Slide-out cart UI; integrates WPML/WCML currency and product ID mapping.",
        "High",
        "**Expect some work:** cart drawer theme + AJAX cart APIs on Shopify.",
    ),
    "cart-sidebar-v2": (
        "Alternate cart sidebar implementation — confirm which is primary in production.",
        "Medium",
        "**Expect some work:**",
    ),
    "pfm-signifyd-integration": (
        "Signifyd fraud scoring / order submission.",
        "High",
        "**Expect some work:** Signifyd Shopify app or custom integration.",
    ),
    "kount-fraud-prevention": (
        "Kount fraud screening on checkout.",
        "High",
        "**Expect some work:** Kount for Shopify or equivalent.",
    ),
    "fermiac-siftscience-for-woocommerce": (
        "Sift Science integration for Woo.",
        "High",
        "**Expect some work:** Shopify Fraud / third-party.",
    ),
    "woocommerce-siftscience-extensions": (
        "Extensions for Sift + Woo.",
        "Medium",
        "**Expect some work:**",
    ),
    "sift-wp": (
        "Sift-related WordPress glue.",
        "Medium",
        "**Expect some work:**",
    ),
    "pfm-checkout-observer": (
        "Observes checkout events (logging / risk / analytics — confirm).",
        "High",
        "**Expect some work:** webhooks + Flow.",
    ),
    "pfm-checkout-bot-block": (
        "Bot blocking on checkout.",
        "Medium",
        "**Expect some work:** Shopify bot protection + CAPTCHA apps.",
    ),
    "orders-pay-verify": (
        "Order pay verification flow.",
        "Medium",
        "**Expect some work:**",
    ),
    "bluesnap-payment-gateway-for-woocommerce": (
        "BlueSnap payment gateway.",
        "High",
        "**Expect some work:** Shopify payment provider availability; may require different PSP.",
    ),
    "braintree-saved-token-gateway": (
        "Braintree vaulted cards / gateway.",
        "High",
        "**Expect some work:** Shopify Payments vs Braintree; token migration project.",
    ),
    "woo-payment-gateway": (
        "Payment gateway package (often card UI / blocks).",
        "High",
        "**Expect some work:**",
    ),
    "afterpay-gateway-for-woocommerce": (
        "Afterpay / Clearpay BNPL.",
        "Medium",
        "**Expect some work:** Shop Pay Installments / Afterpay Shopify.",
    ),
    "woocommerce-gateway-paypal-express-checkout": (
        "PayPal Express checkout.",
        "High",
        "**Easy move:** PayPal on Shopify.",
    ),
    "card-checkout-ms": (
        "Checkout card UI / testimonial carousel (custom).",
        "Medium",
        "**Expect some work:** theme + checkout extensions.",
    ),
    "package_protection_ms": (
        "Package protection upsell on checkout.",
        "Medium",
        "**Expect some work:** shipping protection apps.",
    ),
    "recaptcha-for-woocommerce": (
        "reCAPTCHA on Woo checkout/account.",
        "Medium",
        "**Expect some work:** Shopify bot challenge / apps.",
    ),
    "shipbob-integration": (
        "ShipBob fulfillment integration.",
        "High",
        "**Expect some work:** ShipBob Shopify connector or order webhook app.",
    ),
    "warehouse-export": (
        "Warehouse export + REST webhooks (ShipBob, Green warehouse classes).",
        "High",
        "**Expect some work:** OMS integration via Shopify webhooks + custom middleware.",
    ),
    "woocommerce-shipstation-integration": (
        "WooCommerce ShipStation plugin folder exists in the repo; **Particle does not use ShipStation** operationally—no migration to Shopify ShipStation. Deactivate/uninstall with WordPress.",
        "Low",
        "**Not part of Shopify:** not in scope; remove dead plugin during decommission.",
    ),
    "woocommerce-shipment-tracking": (
        "Woo shipment tracking meta on orders.",
        "High",
        "**Expect some work:** native tracking + carrier apps.",
    ),
    "narvar-tracking-integration": (
        "Narvar post-purchase tracking / comms.",
        "High",
        "**Expect some work:** Narvar Shopify integration.",
    ),
    "aftership-woocommerce-tracking": (
        "AfterShip tracking.",
        "Medium",
        "**Expect some work:** AfterShip app.",
    ),
    "woocommerce-services": (
        "WooCommerce Shipping / tax (USPS etc. depending on config).",
        "Medium",
        "**Expect some work:** Shopify Shipping.",
    ),
    "special-shipping-methods": (
        "Custom shipping methods / rules.",
        "High",
        "**Expect some work:** carrier service + Functions or shipping apps.",
    ),
    "PriorityAPI": (
        "Priority ERP API integration.",
        "High",
        "**Expect some work:** middleware posting Shopify orders to Priority.",
    ),
    "WooCommercePriorityAPI": (
        "Alternate or layered Priority Woo bridge — confirm active.",
        "High",
        "**Expect some work:**",
    ),
    "PriorityApiCustomCode": (
        "Custom code layer on Priority API.",
        "High",
        "**Needs a fresh build:** port to middleware.",
    ),
    "post-orders-to-priority": (
        "Pushes orders to Priority system.",
        "High",
        "**Expect some work:**",
    ),
    "klaviyo": (
        "Klaviyo official Woo plugin: events, lists, forms.",
        "High",
        "**Easy move:** Klaviyo Shopify integration.",
    ),
    "klaviyo-wp": (
        "Additional Klaviyo WordPress integration package.",
        "High",
        "Full",
    ),
    "richpanel-for-woocommerce": (
        "Richpanel helpdesk + customer timeline for Woo orders.",
        "High",
        "**Expect some work:** Richpanel Shopify app.",
    ),
    "yotpo-integration": (
        "Yotpo handles loyalty points, product reviews, SMS messages, and can create or cancel coupon codes from its system.",
        "High",
        "**Expect some work:** Yotpo’s own Shopify apps reconnect most of this.",
    ),
    "stampedio": (
        "Stamped.io reviews widgets / integration.",
        "High",
        "**Expect some work:** Stamped Shopify.",
    ),
    "stampedio-product-reviews": (
        "Stamped product reviews companion.",
        "High",
        "**Expect some work:**",
    ),
    "trustpilot-widget": (
        "Trustpilot widget embed.",
        "Medium",
        "**Easy move:** Trustpilot Shopify app/widget.",
    ),
    "trustpilot-integration": (
        "Trustpilot integration glue.",
        "Medium",
        "Full",
    ),
    "ticket-submissions": (
        "Support ticket submission from site.",
        "Medium",
        "**Expect some work:** forms app / Zendesk / Gorgias.",
    ),
    "duracelltomi-google-tag-manager": (
        "GTM container injection and dataLayer.",
        "High",
        "**Easy move:** GTM in theme or Shopify app.",
    ),
    "pixelyoursite-pro": (
        "PixelYourSite: Meta/CAPI/GA events.",
        "High",
        "**Expect some work:** PYS Shopify or server events.",
    ),
    "pixelyoursite-super-pack": (
        "PYS add-on pack.",
        "Medium",
        "**Expect some work:**",
    ),
    "blotout-edgetag": (
        "Blotout EdgeTag / customer data platform.",
        "Medium",
        "**Expect some work:** Shopify Customer Privacy + server pixels.",
    ),
    "impact-partnership-cloud": (
        "Impact affiliate / partnership tracking.",
        "Medium",
        "**Expect some work:** Impact Shopify integration.",
    ),
    "tiktok-shop-integration": (
        "TikTok Shop / catalog sync.",
        "Medium",
        "**Expect some work:** TikTok for Shopify.",
    ),
    "facebook-store-integration": (
        "Facebook / Meta catalog integration.",
        "Medium",
        "**Expect some work:** Meta sales channel.",
    ),
    "wunderkind-integration": (
        "Wunderkind (BounceX) behavioral marketing.",
        "Medium",
        "**Expect some work:** Wunderkind Shopify.",
    ),
    "optinmonster": (
        "OptinMonster lead capture.",
        "Medium",
        "**Expect some work:** OM Shopify embed.",
    ),
    "woocommerce": (
        "WooCommerce core (cart, checkout, products, orders). Entire commerce layer to be replaced by Shopify.",
        "High",
        "**Needs a fresh build:** platform replacement.",
    ),
    "wordpress-seo": (
        "Yoast SEO Free: meta, schema, sitemaps, redirects UI.",
        "High",
        "**Expect some work:** Shopify SEO fields + redirects JSON.",
    ),
    "wordpress-seo-premium": (
        "Yoast Premium: redirects, internal linking, AI features.",
        "High",
        "**Expect some work:**",
    ),
    "wpseo-woocommerce": (
        "Yoast WooCommerce SEO extension.",
        "High",
        "**Expect some work:**",
    ),
    "redirection": (
        "301/302 redirect manager and logs.",
        "High",
        "**Expect some work:** Shopify URL redirects (import).",
    ),
    "sitemap-custom": (
        "Custom sitemap generation for Particle.",
        "Medium",
        "**Expect some work:** Shopify sitemap + hreflang via Markets.",
    ),
    "wp-sitemap-page": (
        "HTML sitemap page shortcode/plugin.",
        "Low",
        "**Expect some work:** theme page.",
    ),
    "advanced-custom-fields-pro": (
        "ACF Pro fields on pages/products/options.",
        "High",
        "**Expect some work:** metafields + metaobject definitions + admin UI.",
    ),
    "landing-pages": (
        "Landing page plugin with blocks and templates (e.g. Marsmen-like LP).",
        "High",
        "**Expect some work:** Shopify Pages + metaobjects + theme sections.",
    ),
    "gravite-landing-pages": (
        "Gravité-specific landing page templates.",
        "High",
        "**Expect some work:**",
    ),
    "japan-landing-pages": (
        "Japan market landing pages.",
        "Medium",
        "**Expect some work:** Markets + templates.",
    ),
    "product-landing-pages": (
        "Product-scoped landing experiences.",
        "High",
        "**Expect some work:**",
    ),
    "woocommerce-magazine": (
        "Magazine / editorial integration with Woo (see plugin).",
        "Medium",
        "**Expect some work:** Shopify blog Online Store.",
    ),
    "woocommerce-cart-page": (
        "Custom cart page behavior/routing.",
        "High",
        "**Expect some work:** Shopify cart template + apps.",
    ),
    "woocommerce-my-account": (
        "Custom My Account SPA/loader and flows.",
        "High",
        "**Expect some work:** Customer Account API / legacy customer accounts strategy.",
    ),
    "woocommerce-checkout-userdata": (
        "Extra checkout user data capture.",
        "Medium",
        "**Expect some work:** checkout UI extensions + metafields.",
    ),
    "woocommerce-replacement-orders": (
        "Replacement order workflow tied to Woo orders.",
        "High",
        "**Expect some work:** draft orders / exchanges apps / custom.",
    ),
    "woocommerce-reminder-pro": (
        "Abandoned cart or reminder emails.",
        "Medium",
        "**Expect some work:** Klaviyo + Shopify checkout abandonment.",
    ),
    "woocommerce-quiz": (
        "Quiz tied to Woo products.",
        "Medium",
        "**Expect some work:** third-party quiz app or custom theme.",
    ),
    "pfm-skincare-quiz": (
        "Particle skincare quiz templates and flow.",
        "High",
        "**Expect some work:** rebuild as theme section or app.",
    ),
    "quiz": (
        "Generic quiz plugin for Particle.",
        "Medium",
        "**Expect some work:**",
    ),
    "product-guide": (
        "Product guide experience.",
        "Medium",
        "**Expect some work:** content pages + metafields.",
    ),
    "preorder-products": (
        "Preorder selling for products.",
        "Medium",
        "**Expect some work:** preorder apps.",
    ),
    "try-before-you-buy": (
        "Try before you buy program.",
        "Medium",
        "**Expect some work:** TBYB apps.",
    ),
    "force-default-variant-for-woocommerce": (
        "Forces default variation selection when variations exist.",
        "Low",
        "**Expect some work:** rarely needed if SKUs are simple; confirm use.",
    ),
    "woofunnels-order-bump": (
        "FunnelKit / WooFunnels order bumps.",
        "High",
        "**Expect some work:** checkout upsell apps.",
    ),
    "post-purchase-upsell": (
        "Post-purchase one-click upsell.",
        "High",
        "**Expect some work:** post-purchase apps.",
    ),
    "empty-cart-upsells": (
        "Upsells when cart empty.",
        "Medium",
        "**Expect some work:**",
    ),
    "add_upsells_option_ms": (
        "Adds upsell options to subscription/cart flows (custom).",
        "High",
        "**Expect some work:**",
    ),
    "woocommerce-complyt-tax": (
        "Complyt tax calculation.",
        "High",
        "**Expect some work:** Shopify Tax / tax apps.",
    ),
    "complyt-address-validator": (
        "Complyt address validation.",
        "High",
        "**Expect some work:** address validation at checkout.",
    ),
    "woocommerce-avatax": (
        "Avalara AvaTax for Woo.",
        "Medium",
        "**Expect some work:** Avalara Shopify.",
    ),
    "tax-helper": (
        "Tax helper utilities for Woo.",
        "Medium",
        "**Expect some work:**",
    ),
    "woocommerce-google-address": (
        "Google Places autocomplete on address fields.",
        "High",
        "**Expect some work:** Shopify address autocomplete / apps.",
    ),
    "pfm-smarty-address-validator": (
        "Smarty (USPS) address validation.",
        "High",
        "**Expect some work:** Smarty or equivalent on Shopify.",
    ),
    "woocommerce-coupons-utils": (
        "Utilities for coupon management/reporting.",
        "Medium",
        "**Expect some work:**",
    ),
    "woocommerce-legacy-rest-api": (
        "Legacy Woo REST API compatibility.",
        "Low",
        "**Not part of Shopify:** any consumers must move to Shopify Admin API.",
    ),
    "woocommerce-zapier": (
        "Zapier triggers/actions for Woo.",
        "Medium",
        "**Easy move:** Shopify Zapier.",
    ),
    "outersignal-order-export": (
        "Order export to Outersignal.",
        "Medium",
        "**Expect some work:** webhooks.",
    ),
    "sellence-api": (
        "Sellence REST API (`/products`, `/coupons`).",
        "Medium",
        "**Expect some work:** custom app on Shopify.",
    ),
    "walmart-marketplace-integration": (
        "Walmart marketplace listing / orders.",
        "Medium",
        "**Expect some work:** Walmart Shopify channel.",
    ),
    "pfm-geo-privacy": (
        "Geo / privacy gate (REST namespace).",
        "High",
        "**Expect some work:** Markets + consent apps.",
    ),
    "pfm-klaviyo-monitor": (
        "Monitoring / hooks for Klaviyo health.",
        "Low",
        "**Not part of Shopify:** ops tooling; replace with monitoring on new stack.",
    ),
    "pfm-chargebacks-utils": (
        "Chargeback utilities + REST.",
        "Medium",
        "**Expect some work:** payment processor dashboards.",
    ),
    "pfm-csv-uploader": (
        "Admin CSV upload utilities.",
        "Medium",
        "**Not part of Shopify:** Shopify bulk import / Admin API.",
    ),
    "pfm-tools-utils": (
        "Misc internal tools + REST routes.",
        "Medium",
        "**Needs a fresh build:** review with engineering before promising dates.",
    ),
    "pfm-holiday-season": (
        "Seasonal promos / toggles.",
        "Medium",
        "**Expect some work:** Shopify scheduled discounts.",
    ),
    "pfm-kill-injected-ui": (
        "Hides stray admin or storefront UI injected by other tools.",
        "Low",
        "**Not part of Shopify:** WordPress-only housekeeping.",
    ),
    "wc-admin-product-note": (
        "Product notes in admin for ops.",
        "Low",
        "**Expect some work:** Shopify order/product notes pattern.",
    ),
    "wc-remove-oldest-orders": (
        "Housekeeping: remove old orders from DB.",
        "Low",
        "**Not part of Shopify:** WP-only maintenance.",
    ),
    "export-refunds-to-csv": (
        "Export refunds to CSV.",
        "Low",
        "**Expect some work:** reporting export from Shopify.",
    ),
    "export-stats": (
        "Export stats to Google Sheets.",
        "Medium",
        "**Expect some work:** Analytics API / Sheets.",
    ),
    "orderswidget-summary": (
        "Small internal API that shows order summaries inside WordPress admin widgets.",
        "Low",
        "**Not part of Shopify:** rebuild in a staff dashboard or BI tool if still needed.",
    ),
    "purchase-push-notifications": (
        "Push notifications on purchase.",
        "Low",
        "**Expect some work:** mobile app channel if applicable.",
    ),
    "livecart-by-wp-engine": (
        "WP Engine LiveCart integration.",
        "Low",
        "**Not part of Shopify:** host-specific.",
    ),
    "wp-rocket": (
        "Caching and performance (HTML/CSS/JS optimization).",
        "Medium",
        "**Not part of Shopify:** Shopify CDN/hosting; different model.",
    ),
    "webp-express": (
        "WebP image conversion/delivery.",
        "Low",
        "**Expect some work:** Shopify image CDN handles formats.",
    ),
    "wp-smush-pro": (
        "Image compression.",
        "Low",
        "**Not part of Shopify:** Shopify image pipeline.",
    ),
    "scheduled-actions": (
        "Action Scheduler tables (often bundled with Woo).",
        "Medium",
        "**Not part of Shopify:** platform cron/queues differ.",
    ),
    "newrelic-transaction-renamer": (
        "Renames New Relic transactions for WP.",
        "Low",
        "N/A",
    ),
    "log-http-requests": (
        "Logs outbound HTTP for debugging.",
        "Low",
        "N/A",
    ),
    "inspect-http-requests": (
        "Inspect HTTP requests in admin.",
        "Low",
        "N/A",
    ),
    "show-current-template": (
        "Dev: shows current PHP template.",
        "Low",
        "N/A",
    ),
    "post-duplicator": (
        "Duplicate posts/pages for editors.",
        "Low",
        "**Not part of Shopify:** editor workflow.",
    ),
    "post-smtp": (
        "SMTP mailer for WP emails.",
        "Medium",
        "**Not part of Shopify:** Shopify email domain; transactional via apps.",
    ),
    "smtp-mailgun-connector": (
        "Mailgun SMTP connector.",
        "Low",
        "N/A",
    ),
    "advanced-cron-manager": (
        "Cron UI for WP.",
        "Low",
        "**Not part of Shopify:** Shopify scheduled jobs via apps.",
    ),
    "login-visit-counter": (
        "Tracks login visits.",
        "Low",
        "N/A",
    ),
    "alert-system": (
        "Internal alerts.",
        "Medium",
        "**Expect some work:** Slack/email from Flow.",
    ),
    "sticky-cta": (
        "Sticky CTA bar.",
        "Medium",
        "**Expect some work:** theme.",
    ),
    "account-page-recommended-products": (
        "Recommended products on account page.",
        "Medium",
        "**Expect some work:** personalization app or theme.",
    ),
    "metorik-helper": (
        "Metorik analytics helper for Woo.",
        "Medium",
        "**Expect some work:** Metorik Shopify.",
    ),
    "sky-wcs-no-periods": (
        "Cleans subscription product titles (removes periods).",
        "Low",
        "**Expect some work:** naming in Shopify subscriptions.",
    ),
    "kadence-woocommerce-email-designer": (
        "Kadence Woo email template designer.",
        "Medium",
        "**Expect some work:** Shopify Notifications customization.",
    ),
    "user-role-editor": (
        "WP role/capability editor.",
        "Low",
        "**Not part of Shopify:** Shopify staff permissions.",
    ),
    "user-switching": (
        "Switch user for support testing.",
        "Low",
        "**Not part of Shopify:** Shopify staff impersonation patterns differ.",
    ),
    "two-factor-authentication-premium": (
        "2FA for WP admin/logins.",
        "Medium",
        "**Not part of Shopify:** Shopify org security; customer 2FA via apps if needed.",
    ),
    "metronet-profile-picture": (
        "Profile pictures for users.",
        "Low",
        "**Expect some work:** customer account profile apps.",
    ),
    "tinymce-advanced": (
        "Classic editor enhancements.",
        "Low",
        "N/A",
    ),
    "codepress-admin-columns": (
        "Admin list column customization.",
        "Low",
        "N/A",
    ),
    "loco-translate": (
        "Translate theme/plugin strings locally.",
        "Medium",
        "**Expect some work:** locale JSON / Markets.",
    ),
    "force-regenerate-thumbnails": (
        "Regenerate attachment sizes.",
        "Low",
        "N/A",
    ),
    "myscripts": (
        "Custom scripts plugin (site-specific).",
        "Medium",
        "**Needs a fresh build:** ask engineering what this small package actually does.",
    ),
    "myplugin": (
        "Placeholder or small custom plugin — audit contents.",
        "Low",
        "**Needs a fresh build:** ask engineering what this small package actually does.",
    ),
}


def default_row(slug: str) -> tuple[str, str, str]:
    label = slug.replace("-", " ").replace("_", " ")
    desc = (
        f"This add-on (folder name **{slug}**) plugs into today’s WordPress store. "
        f"It may show up for shoppers, staff, or only behind the scenes. "
        "Someone who knows the live admin should confirm whether it is turned on and what it is used for. "
        "On Shopify we will match what it does with either a built‑in Shopify feature, a well‑known app, or a small custom project."
    )
    return (
        desc,
        "Medium",
        "**Expect some work:** Shopify usually covers the need, but not always “out of the box”—often an app or short custom setup.",
    )


def emit_plugin_inventory() -> str:
    all_slugs = sorted(p.name for p in PLUGINS.iterdir() if p.is_dir())
    slugs = [s for s in all_slugs if s not in EXCLUDED_PLUGIN_SLUGS]
    lines: list[str] = []
    lines.append("---\n\n")
    lines.append("## 11. Installed plugins (exhaustive)\n\n")
    lines.append(
        f"_**{len(slugs)}** add-ons below (alphabetical). The bold name is the technical folder name—think of it as the “package label.” "
        "If a line sounds vague, that only means the name does not explain itself; your web partner maps it to the real vendor or feature._\n\n"
    )
    lines.append(
        "> [!IMPORTANT]\n"
        "> **Not listed here on purpose:** unused YITH gift‑card folder, WPMU DEV updater client (licensing only), and the separate WPML “strings” package. "
        "**Translating text inside buttons and add-ons** is covered in **section 0** so stakeholders read it once—not under two technical folder names.\n\n"
    )
    for slug in slugs:
        desc, relevance, xfer = CUSTOM.get(slug, default_row(slug))
        lines.append(f"### `{slug}`\n\n")
        lines.append(f"- **Description:** {desc}\n")
        lines.append(f"- **Relevance:** {relevance}\n")
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
        "Section 11 lists almost every installed plugin folder—even boring ones—with a short note for the few folders **deliberately skipped** "
        "(unused gift‑card package, licensing updater, and WPML “strings” explained in section 0 instead).\n\n"
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
        "> These threads describe **whole workflows** that span many items in section 11. "
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
            "**Expect some work** — Shopify has built‑in fraud signals; some partners (Signifyd, Kount, etc.) are re‑connected via apps.",
        ),
        (
            "Getting the box out the door (and telling the customer where it is)",
            "ShipBob, tracking emails, Narvar, AfterShip, warehouse exports, and the link to the Priority business system all feed this story.",
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
        "languages, coupons, Klaviyo emails, address checks, SEO, quizzes, A/B tests, and more. "
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
        "- **Description:** Related articles, breadcrumbs, and a few Yoast SEO settings that change how old URLs behave.\n"
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
        ("Text messages (Twilio)", "Lets the site send or verify SMS messages (for example two‑step flows)."),
        ("Klaviyo profile updates", "Keeps Klaviyo profiles in sync when someone fills out special forms or promotions."),
        ("Email verification for promotions", "Confirms email addresses before certain promotions unlock."),
        ("Braintree dispute alerts", "When Braintree flags a payment dispute, the site can attach notes to the matching order."),
        ("Order and subscription notes for staff tools", "Lets trusted internal tools read or write internal notes on orders or subscriptions."),
        (
            "AI and search crawler visit analytics",
            "Aggregates stored crawler traffic (which URLs were visited and how often over time) for monitoring and SEO-related visibility—shoppers never see this screen.",
        ),
        ("ShipBob warehouse callbacks", "ShipBob tells WordPress when a parcel ships, is delayed, or is delivered."),
        ("Secondary warehouse feed (“Green”)", "Another warehouse integration speaks the same “shipped” language for a different 3PL."),
        ("Monday.com coupon bridge", "Creates or updates coupons when the Monday.com workflow says so."),
        ("Yotpo coupon automation", "Lets Yotpo loyalty create or cancel coupon codes automatically."),
        (
            "Miscellaneous staff helper APIs",
            "Small one-off hooks used by internal dashboards—engineering should confirm which are still called.",
        ),
        ("Chargeback lookup", "Looks up chargeback status for a given order for finance/support."),
        ("Geo privacy gate", "Controls what appears based on privacy / geography rules."),
        ("Sellence product & coupon feed", "Exposes catalog/coupon data for an external partner system."),
        ("Wunderkind product feed", "Sends catalog data to Wunderkind for onsite personalization."),
        ("Order summary widget", "Feeds a small admin widget with order totals."),
        ("OptinMonster map helper", "Helps OptinMonster campaigns map to WordPress content if enabled."),
        ("Klaviyo plugin APIs", "Official Klaviyo endpoints bundled with their WordPress plugin."),
        ("Yoast / WP Rocket maintenance APIs", "Background housekeeping for SEO cache plugins—rarely shopper facing."),
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
            "Guesses the shopper’s language, fixes URLs, and remembers `store_switch` choices for WPML.",
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
            "Optional helper for OptinMonster mapping.",
            "Low",
            "**Expect some work:** only if OptinMonster stays in the marketing stack.",
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

    body.append(emit_plugin_inventory())

    body.append(
        "\n---\n\n> [!TIP]\n"
        "> **Regenerate this file** after plugins or the theme change: from the WordPress project folder run "
        "`python docs/generate-shopify-inventory.py`.\n"
    )

    out.write_text("".join(body), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
