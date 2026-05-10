#!/usr/bin/env python3
"""Emit docs/shopify-migration-features-inventory.md (exhaustive plugin + theme inventory)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "wp-content" / "plugins"
THEME = ROOT / "wp-content" / "themes" / "particleformen"

# Overrides: slug -> (description, relevance, transferability)
CUSTOM: dict[str, tuple[str, str, str]] = {
    "sitepress-multilingual-cms": (
        "WPML core: multilingual posts, menus, hreflang, translation workflow. Deep integration in theme (`wpml_*` filters), cart, optimization.",
        "High",
        "Partial — Shopify Markets + Translate & Adapt (or third-party); URL/hreflang rules must be redesigned.",
    ),
    "woocommerce-multilingual": (
        "WCML: multi-currency with WPML, exchange rates, client currency. Theme `wcml_custom_currency` maps language codes to ISO currencies.",
        "High",
        "Partial — Shopify Markets handles currency/locale differently; custom language→currency matrix must be reimplemented or dropped.",
    ),
    "wpml-string-translation": (
        "WPML String Translation for UI strings and plugin strings.",
        "High",
        "Partial — theme locale files / Markets; no direct port.",
    ),
    "wpml-media-translation": (
        "WPML Media Translation for translated attachments.",
        "Medium",
        "Partial",
    ),
    "woocommerce-subscriptions": (
        "WooCommerce Subscriptions: recurring orders, renewal payments, subscription products, customer portal hooks. Theme has recurring checkout templates.",
        "High",
        "Partial — Shopify Subscriptions / selling plans; plan matrix and dunning must be mapped.",
    ),
    "woocommerce-subscription": (
        "Additional subscription-related plugin (custom or companion) alongside WCS — verify relationship in admin.",
        "High",
        "Partial",
    ),
    "subscriptions-utils": (
        "Custom utilities around Woo subscriptions (see plugin code for hooks).",
        "High",
        "Not transferable — rebuild in Shopify Flow / subscription app / custom app as needed.",
    ),
    "pfm-panel": (
        "Internal operations REST API (`pfm-panel/v1`): orders, subscriptions, refunds, customers, coupons, replacements, reports, warehouse export, Narvar, Braintree info, stats, admin actions.",
        "High",
        "Not transferable — replace with Shopify Admin API + custom internal app or Retool.",
    ),
    "particleformen-checkout": (
        "Custom checkout behaviors for Particle (see plugin + theme `lib/checkout.php`).",
        "High",
        "Partial — Shopify Checkout extensibility (UI extensions, Functions) + apps.",
    ),
    "all-upsells": (
        "Upsell flows: thank-you page, post-purchase, BAS/PPU modules (see `includes/`).",
        "High",
        "Partial — post-purchase apps, checkout upsell extensions.",
    ),
    "custom-coupon": (
        "Custom coupon logic beyond core Woo coupons.",
        "High",
        "Partial — Shopify Discount Functions / discount apps.",
    ),
    "pfm-store-credits": (
        "Store credit balance and checkout application (frontend + admin).",
        "High",
        "Partial — Shopify store credit / gift card primitives differ; likely app or custom.",
    ),
    "pfm-monday-coupons": (
        "REST-driven coupon integration (Monday workflow).",
        "Medium",
        "Partial — Zapier/Flow + discount APIs.",
    ),
    "woo-discount-rules": (
        "Discount Rules for WooCommerce (conditional cart rules).",
        "High",
        "Partial — Shopify Functions + discount apps.",
    ),
    "woo-discount-rules-pro": (
        "Pro tier for Discount Rules (extra rule types).",
        "High",
        "Partial",
    ),
    "woocommerce-smart-coupons": (
        "Smart Coupons: store credit, gift certificates, bulk coupons, blocks.",
        "High",
        "Partial — Shopify gift cards / discount combinations via apps.",
    ),
    "yith-woocommerce-gift-cards-premium": (
        "YITH gift cards premium.",
        "Medium",
        "Partial — Shopify gift cards.",
    ),
    "cart-sidebar": (
        "Slide-out cart UI; integrates WPML/WCML currency and product ID mapping.",
        "High",
        "Partial — cart drawer theme + AJAX cart APIs on Shopify.",
    ),
    "cart-sidebar-v2": (
        "Alternate cart sidebar implementation — confirm which is primary in production.",
        "Medium",
        "Partial",
    ),
    "pfm-signifyd-integration": (
        "Signifyd fraud scoring / order submission.",
        "High",
        "Partial — Signifyd Shopify app or custom integration.",
    ),
    "kount-fraud-prevention": (
        "Kount fraud screening on checkout.",
        "High",
        "Partial — Kount for Shopify or equivalent.",
    ),
    "fermiac-siftscience-for-woocommerce": (
        "Sift Science integration for Woo.",
        "High",
        "Partial — Shopify Fraud / third-party.",
    ),
    "woocommerce-siftscience-extensions": (
        "Extensions for Sift + Woo.",
        "Medium",
        "Partial",
    ),
    "sift-wp": (
        "Sift-related WordPress glue.",
        "Medium",
        "Partial",
    ),
    "pfm-checkout-observer": (
        "Observes checkout events (logging / risk / analytics — confirm).",
        "High",
        "Partial — webhooks + Flow.",
    ),
    "pfm-checkout-bot-block": (
        "Bot blocking on checkout.",
        "Medium",
        "Partial — Shopify bot protection + CAPTCHA apps.",
    ),
    "orders-pay-verify": (
        "Order pay verification flow.",
        "Medium",
        "Partial",
    ),
    "bluesnap-payment-gateway-for-woocommerce": (
        "BlueSnap payment gateway.",
        "High",
        "Partial — Shopify payment provider availability; may require different PSP.",
    ),
    "braintree-saved-token-gateway": (
        "Braintree vaulted cards / gateway.",
        "High",
        "Partial — Shopify Payments vs Braintree; token migration project.",
    ),
    "woo-payment-gateway": (
        "Payment gateway package (often card UI / blocks).",
        "High",
        "Partial",
    ),
    "afterpay-gateway-for-woocommerce": (
        "Afterpay / Clearpay BNPL.",
        "Medium",
        "Partial — Shop Pay Installments / Afterpay Shopify.",
    ),
    "woocommerce-gateway-paypal-express-checkout": (
        "PayPal Express checkout.",
        "High",
        "Full — PayPal on Shopify.",
    ),
    "card-checkout-ms": (
        "Checkout card UI / testimonial carousel (custom).",
        "Medium",
        "Partial — theme + checkout extensions.",
    ),
    "package_protection_ms": (
        "Package protection upsell on checkout.",
        "Medium",
        "Partial — shipping protection apps.",
    ),
    "recaptcha-for-woocommerce": (
        "reCAPTCHA on Woo checkout/account.",
        "Medium",
        "Partial — Shopify bot challenge / apps.",
    ),
    "shipbob-integration": (
        "ShipBob fulfillment integration.",
        "High",
        "Partial — ShipBob Shopify connector or order webhook app.",
    ),
    "warehouse-export": (
        "Warehouse export + REST webhooks (ShipBob, Green warehouse classes).",
        "High",
        "Partial — OMS integration via Shopify webhooks + custom middleware.",
    ),
    "woocommerce-shipstation-integration": (
        "ShipStation labels and tracking.",
        "High",
        "Partial — ShipStation Shopify app.",
    ),
    "woocommerce-shipment-tracking": (
        "Woo shipment tracking meta on orders.",
        "High",
        "Partial — native tracking + carrier apps.",
    ),
    "narvar-tracking-integration": (
        "Narvar post-purchase tracking / comms.",
        "High",
        "Partial — Narvar Shopify integration.",
    ),
    "aftership-woocommerce-tracking": (
        "AfterShip tracking.",
        "Medium",
        "Partial — AfterShip app.",
    ),
    "woocommerce-services": (
        "WooCommerce Shipping / tax (USPS etc. depending on config).",
        "Medium",
        "Partial — Shopify Shipping.",
    ),
    "special-shipping-methods": (
        "Custom shipping methods / rules.",
        "High",
        "Partial — carrier service + Functions or shipping apps.",
    ),
    "PriorityAPI": (
        "Priority ERP API integration.",
        "High",
        "Partial — middleware posting Shopify orders to Priority.",
    ),
    "WooCommercePriorityAPI": (
        "Alternate or layered Priority Woo bridge — confirm active.",
        "High",
        "Partial",
    ),
    "PriorityApiCustomCode": (
        "Custom code layer on Priority API.",
        "High",
        "Not transferable — port to middleware.",
    ),
    "post-orders-to-priority": (
        "Pushes orders to Priority system.",
        "High",
        "Partial",
    ),
    "klaviyo": (
        "Klaviyo official Woo plugin: events, lists, forms.",
        "High",
        "Full — Klaviyo Shopify integration.",
    ),
    "klaviyo-wp": (
        "Additional Klaviyo WordPress integration package.",
        "High",
        "Full",
    ),
    "richpanel-for-woocommerce": (
        "Richpanel helpdesk + customer timeline for Woo orders.",
        "High",
        "Partial — Richpanel Shopify app.",
    ),
    "yotpo-integration": (
        "Yotpo loyalty/reviews/SMS hooks; includes REST coupon routes.",
        "High",
        "Partial — Yotpo Shopify stack.",
    ),
    "stampedio": (
        "Stamped.io reviews widgets / integration.",
        "High",
        "Partial — Stamped Shopify.",
    ),
    "stampedio-product-reviews": (
        "Stamped product reviews companion.",
        "High",
        "Partial",
    ),
    "trustpilot-widget": (
        "Trustpilot widget embed.",
        "Medium",
        "Full — Trustpilot Shopify app/widget.",
    ),
    "trustpilot-integration": (
        "Trustpilot integration glue.",
        "Medium",
        "Full",
    ),
    "ticket-submissions": (
        "Support ticket submission from site.",
        "Medium",
        "Partial — forms app / Zendesk / Gorgias.",
    ),
    "duracelltomi-google-tag-manager": (
        "GTM container injection and dataLayer.",
        "High",
        "Full — GTM in theme or Shopify app.",
    ),
    "pixelyoursite-pro": (
        "PixelYourSite: Meta/CAPI/GA events.",
        "High",
        "Partial — PYS Shopify or server events.",
    ),
    "pixelyoursite-super-pack": (
        "PYS add-on pack.",
        "Medium",
        "Partial",
    ),
    "blotout-edgetag": (
        "Blotout EdgeTag / customer data platform.",
        "Medium",
        "Partial — Shopify Customer Privacy + server pixels.",
    ),
    "impact-partnership-cloud": (
        "Impact affiliate / partnership tracking.",
        "Medium",
        "Partial — Impact Shopify integration.",
    ),
    "tiktok-shop-integration": (
        "TikTok Shop / catalog sync.",
        "Medium",
        "Partial — TikTok for Shopify.",
    ),
    "facebook-store-integration": (
        "Facebook / Meta catalog integration.",
        "Medium",
        "Partial — Meta sales channel.",
    ),
    "wunderkind-integration": (
        "Wunderkind (BounceX) behavioral marketing.",
        "Medium",
        "Partial — Wunderkind Shopify.",
    ),
    "optinmonster": (
        "OptinMonster lead capture.",
        "Medium",
        "Partial — OM Shopify embed.",
    ),
    "woocommerce": (
        "WooCommerce core (cart, checkout, products, orders). Entire commerce layer to be replaced by Shopify.",
        "High",
        "Not transferable — platform replacement.",
    ),
    "wordpress-seo": (
        "Yoast SEO Free: meta, schema, sitemaps, redirects UI.",
        "High",
        "Partial — Shopify SEO fields + redirects JSON.",
    ),
    "wordpress-seo-premium": (
        "Yoast Premium: redirects, internal linking, AI features.",
        "High",
        "Partial",
    ),
    "wpseo-woocommerce": (
        "Yoast WooCommerce SEO extension.",
        "High",
        "Partial",
    ),
    "redirection": (
        "301/302 redirect manager and logs.",
        "High",
        "Partial — Shopify URL redirects (import).",
    ),
    "sitemap-custom": (
        "Custom sitemap generation for Particle.",
        "Medium",
        "Partial — Shopify sitemap + hreflang via Markets.",
    ),
    "wp-sitemap-page": (
        "HTML sitemap page shortcode/plugin.",
        "Low",
        "Partial — theme page.",
    ),
    "advanced-custom-fields-pro": (
        "ACF Pro fields on pages/products/options.",
        "High",
        "Partial — metafields + metaobject definitions + admin UI.",
    ),
    "landing-pages": (
        "Landing page plugin with blocks and templates (e.g. Marsmen-like LP).",
        "High",
        "Partial — Shopify Pages + metaobjects + theme sections.",
    ),
    "gravite-landing-pages": (
        "Gravité-specific landing page templates.",
        "High",
        "Partial",
    ),
    "japan-landing-pages": (
        "Japan market landing pages.",
        "Medium",
        "Partial — Markets + templates.",
    ),
    "product-landing-pages": (
        "Product-scoped landing experiences.",
        "High",
        "Partial",
    ),
    "woocommerce-magazine": (
        "Magazine / editorial integration with Woo (see plugin).",
        "Medium",
        "Partial — Shopify blog Online Store.",
    ),
    "woocommerce-cart-page": (
        "Custom cart page behavior/routing.",
        "High",
        "Partial — Shopify cart template + apps.",
    ),
    "woocommerce-my-account": (
        "Custom My Account SPA/loader and flows.",
        "High",
        "Partial — Customer Account API / legacy customer accounts strategy.",
    ),
    "woocommerce-checkout-userdata": (
        "Extra checkout user data capture.",
        "Medium",
        "Partial — checkout UI extensions + metafields.",
    ),
    "woocommerce-replacement-orders": (
        "Replacement order workflow tied to Woo orders.",
        "High",
        "Partial — draft orders / exchanges apps / custom.",
    ),
    "woocommerce-reminder-pro": (
        "Abandoned cart or reminder emails.",
        "Medium",
        "Partial — Klaviyo + Shopify checkout abandonment.",
    ),
    "woocommerce-quiz": (
        "Quiz tied to Woo products.",
        "Medium",
        "Partial — third-party quiz app or custom theme.",
    ),
    "pfm-skincare-quiz": (
        "Particle skincare quiz templates and flow.",
        "High",
        "Partial — rebuild as theme section or app.",
    ),
    "quiz": (
        "Generic quiz plugin for Particle.",
        "Medium",
        "Partial",
    ),
    "product-guide": (
        "Product guide experience.",
        "Medium",
        "Partial — content pages + metafields.",
    ),
    "preorder-products": (
        "Preorder selling for products.",
        "Medium",
        "Partial — preorder apps.",
    ),
    "try-before-you-buy": (
        "Try before you buy program.",
        "Medium",
        "Partial — TBYB apps.",
    ),
    "force-default-variant-for-woocommerce": (
        "Forces default variation selection when variations exist.",
        "Low",
        "Partial — rarely needed if SKUs are simple; confirm use.",
    ),
    "woofunnels-order-bump": (
        "FunnelKit / WooFunnels order bumps.",
        "High",
        "Partial — checkout upsell apps.",
    ),
    "post-purchase-upsell": (
        "Post-purchase one-click upsell.",
        "High",
        "Partial — post-purchase apps.",
    ),
    "empty-cart-upsells": (
        "Upsells when cart empty.",
        "Medium",
        "Partial",
    ),
    "add_upsells_option_ms": (
        "Adds upsell options to subscription/cart flows (custom).",
        "High",
        "Partial",
    ),
    "woocommerce-complyt-tax": (
        "Complyt tax calculation.",
        "High",
        "Partial — Shopify Tax / tax apps.",
    ),
    "complyt-address-validator": (
        "Complyt address validation.",
        "High",
        "Partial — address validation at checkout.",
    ),
    "woocommerce-avatax": (
        "Avalara AvaTax for Woo.",
        "Medium",
        "Partial — Avalara Shopify.",
    ),
    "tax-helper": (
        "Tax helper utilities for Woo.",
        "Medium",
        "Partial",
    ),
    "woocommerce-google-address": (
        "Google Places autocomplete on address fields.",
        "High",
        "Partial — Shopify address autocomplete / apps.",
    ),
    "pfm-smarty-address-validator": (
        "Smarty (USPS) address validation.",
        "High",
        "Partial — Smarty or equivalent on Shopify.",
    ),
    "woocommerce-coupons-utils": (
        "Utilities for coupon management/reporting.",
        "Medium",
        "Partial",
    ),
    "woocommerce-legacy-rest-api": (
        "Legacy Woo REST API compatibility.",
        "Low",
        "N/A — any consumers must move to Shopify Admin API.",
    ),
    "woocommerce-zapier": (
        "Zapier triggers/actions for Woo.",
        "Medium",
        "Full — Shopify Zapier.",
    ),
    "outersignal-order-export": (
        "Order export to Outersignal.",
        "Medium",
        "Partial — webhooks.",
    ),
    "sellence-api": (
        "Sellence REST API (`/products`, `/coupons`).",
        "Medium",
        "Partial — custom app on Shopify.",
    ),
    "walmart-marketplace-integration": (
        "Walmart marketplace listing / orders.",
        "Medium",
        "Partial — Walmart Shopify channel.",
    ),
    "pfm-geo-privacy": (
        "Geo / privacy gate (REST namespace).",
        "High",
        "Partial — Markets + consent apps.",
    ),
    "pfm-klaviyo-monitor": (
        "Monitoring / hooks for Klaviyo health.",
        "Low",
        "N/A — ops tooling; replace with monitoring on new stack.",
    ),
    "pfm-chargebacks-utils": (
        "Chargeback utilities + REST.",
        "Medium",
        "Partial — payment processor dashboards.",
    ),
    "pfm-csv-uploader": (
        "Admin CSV upload utilities.",
        "Medium",
        "N/A — Shopify bulk import / Admin API.",
    ),
    "pfm-tools-utils": (
        "Misc internal tools + REST routes.",
        "Medium",
        "Not transferable",
    ),
    "pfm-holiday-season": (
        "Seasonal promos / toggles.",
        "Medium",
        "Partial — Shopify scheduled discounts.",
    ),
    "pfm-kill-injected-ui": (
        "Removes unwanted injected admin or frontend UI.",
        "Low",
        "N/A",
    ),
    "wc-admin-product-note": (
        "Product notes in admin for ops.",
        "Low",
        "Partial — Shopify order/product notes pattern.",
    ),
    "wc-remove-oldest-orders": (
        "Housekeeping: remove old orders from DB.",
        "Low",
        "N/A — WP-only maintenance.",
    ),
    "export-refunds-to-csv": (
        "Export refunds to CSV.",
        "Low",
        "Partial — reporting export from Shopify.",
    ),
    "export-stats": (
        "Export stats to Google Sheets.",
        "Medium",
        "Partial — Analytics API / Sheets.",
    ),
    "orderswidget-summary": (
        "REST `orderswidget/v1/summary` for order summaries.",
        "Low",
        "Not transferable",
    ),
    "purchase-push-notifications": (
        "Push notifications on purchase.",
        "Low",
        "Partial — mobile app channel if applicable.",
    ),
    "livecart-by-wp-engine": (
        "WP Engine LiveCart integration.",
        "Low",
        "N/A — host-specific.",
    ),
    "wp-rocket": (
        "Caching and performance (HTML/CSS/JS optimization).",
        "Medium",
        "N/A — Shopify CDN/hosting; different model.",
    ),
    "webp-express": (
        "WebP image conversion/delivery.",
        "Low",
        "Partial — Shopify image CDN handles formats.",
    ),
    "wp-smush-pro": (
        "Image compression.",
        "Low",
        "N/A — Shopify image pipeline.",
    ),
    "wpmudev-updates": (
        "WPMU DEV update client.",
        "Low",
        "N/A",
    ),
    "scheduled-actions": (
        "Action Scheduler tables (often bundled with Woo).",
        "Medium",
        "N/A — platform cron/queues differ.",
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
        "N/A — editor workflow.",
    ),
    "post-smtp": (
        "SMTP mailer for WP emails.",
        "Medium",
        "N/A — Shopify email domain; transactional via apps.",
    ),
    "smtp-mailgun-connector": (
        "Mailgun SMTP connector.",
        "Low",
        "N/A",
    ),
    "advanced-cron-manager": (
        "Cron UI for WP.",
        "Low",
        "N/A — Shopify scheduled jobs via apps.",
    ),
    "login-visit-counter": (
        "Tracks login visits.",
        "Low",
        "N/A",
    ),
    "alert-system": (
        "Internal alerts.",
        "Medium",
        "Partial — Slack/email from Flow.",
    ),
    "sticky-cta": (
        "Sticky CTA bar.",
        "Medium",
        "Partial — theme.",
    ),
    "account-page-recommended-products": (
        "Recommended products on account page.",
        "Medium",
        "Partial — personalization app or theme.",
    ),
    "metorik-helper": (
        "Metorik analytics helper for Woo.",
        "Medium",
        "Partial — Metorik Shopify.",
    ),
    "sky-wcs-no-periods": (
        "Cleans subscription product titles (removes periods).",
        "Low",
        "Partial — naming in Shopify subscriptions.",
    ),
    "kadence-woocommerce-email-designer": (
        "Kadence Woo email template designer.",
        "Medium",
        "Partial — Shopify Notifications customization.",
    ),
    "user-role-editor": (
        "WP role/capability editor.",
        "Low",
        "N/A — Shopify staff permissions.",
    ),
    "user-switching": (
        "Switch user for support testing.",
        "Low",
        "N/A — Shopify staff impersonation patterns differ.",
    ),
    "two-factor-authentication-premium": (
        "2FA for WP admin/logins.",
        "Medium",
        "N/A — Shopify org security; customer 2FA via apps if needed.",
    ),
    "metronet-profile-picture": (
        "Profile pictures for users.",
        "Low",
        "Partial — customer account profile apps.",
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
        "Partial — locale JSON / Markets.",
    ),
    "force-regenerate-thumbnails": (
        "Regenerate attachment sizes.",
        "Low",
        "N/A",
    ),
    "myscripts": (
        "Custom scripts plugin (site-specific).",
        "Medium",
        "Not transferable — audit contents.",
    ),
    "myplugin": (
        "Placeholder or small custom plugin — audit contents.",
        "Low",
        "Not transferable — audit contents.",
    ),
}


def default_row(slug: str) -> tuple[str, str, str]:
    desc = (
        f"Third-party or vendor extension present in `wp-content/plugins/{slug}/`. "
        "Confirm active modules, license, and any customizations in production."
    )
    return desc, "Medium", "Partial — map to Shopify native feature, first-party channel, or app; validate data migration."


def emit_plugin_inventory() -> str:
    slugs = sorted(p.name for p in PLUGINS.iterdir() if p.is_dir())
    lines: list[str] = []
    lines.append("## 11. Installed plugins (exhaustive)\n")
    lines.append(
        f"_Total folders: **{len(slugs)}** (alphabetical). Each row is one installable component._\n"
    )
    for slug in slugs:
        desc, rel, xfer = CUSTOM.get(slug, default_row(slug))
        lines.append(f"### `{slug}`\n")
        lines.append(f"- **Description:** {desc}\n")
        lines.append(f"- **Relevance:** {rel}\n")
        lines.append(f"- **Transferability:** {xfer}\n")
        rel = (PLUGINS.relative_to(ROOT) / slug).as_posix()
        lines.append(f"- **Evidence:** `{rel}`\n")
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

    page_tpl = sorted(
        str(p.relative_to(THEME)).replace("\\", "/")
        for p in (THEME / "template").glob("*.php")
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
        "_Generated from repository scan. "
        "Schema per item: **Title**, **Description**, **Relevance** (High / Medium / Low), **Transferability** "
        "(Full / Partial / Not transferable / N/A). "
        "Low relevance or N/A does **not** mean omit from migration planning — it marks Shopify non-parity or decommission work._\n\n"
    )

    body.append("## Legend\n\n")
    body.append("- **High** — revenue, checkout, subscriptions, fraud, tax, fulfillment, i18n/currency, or ops-critical.\n")
    body.append("- **Medium** — marketing, CRM, merchandising, SEO, or important UX.\n")
    body.append("- **Low** — admin convenience, dev-only, host-only, or minor UX.\n\n")

    body.append("## 0. Cross-cutting thread index (additive)\n\n")
    body.append(
        "These rows summarize behaviors implemented by **multiple** components listed later. "
        "**Do not remove** the underlying rows.\n\n"
    )
    threads = [
        (
            "WPML + WCML + language/currency + redirects",
            "Multilingual URLs, `hreflang`, `?store_switch=`, cookie `wp-wpml_current_language`, "
            "`wcml_custom_currency` in theme `functions.php`, `mu-plugins/redirections.php`, cart redirect in "
            "`mu-plugins/custom_plugin_organizer.php`, WPML product ID memoization in `lib/optimization.php`, "
            "multi-currency reads in `lib/utils.php` and plugins such as `cart-sidebar`.",
            "High",
            "Partial — Shopify Markets + redirects import + theme locale strategy.",
        ),
        (
            "Subscription commerce stack",
            "`woocommerce-subscriptions`, `woocommerce-subscription`, `subscriptions-utils`, theme recurring checkout templates under "
            "`woocommerce/checkout/`, `pfm-panel` subscription REST, upsell plugins touching subscription options (`add_upsells_option_ms`).",
            "High",
            "Partial — Shopify Subscriptions; full plan matrix workshop required.",
        ),
        (
            "Fraud and risk stack",
            "Signifyd, Kount, Sift (multiple plugins), checkout observer/bot block, package protection.",
            "High",
            "Partial — combine Shopify Fraud with third-party apps and payment rules.",
        ),
        (
            "Fulfillment and post-purchase visibility",
            "ShipBob, ShipStation, shipment tracking, Narvar, AfterShip, warehouse-export webhooks, ERP Priority integrations.",
            "High",
            "Partial — OMS connectors and Shopify webhooks.",
        ),
        (
            "Marketing and attribution pixels",
            "GTM, PixelYourSite, Blotout, Impact, TikTok, Facebook channel, Wunderkind, OptinMonster, theme purchase events in `lib/utils.php`.",
            "High",
            "Partial — pixels in Customer Events / server-side partners.",
        ),
    ]
    for title, desc, rel, xfer in threads:
        body.append(f"### Thread: {title}\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append(f"- **Relevance:** {rel}\n")
        body.append(f"- **Transferability:** {xfer}\n\n")

    body.append("## 1. Theme — PHP modules (`functions.php` includes)\n\n")
    for rel in theme_libs:
        body.append(f"### `{rel}`\n\n")
        body.append(
            f"- **Description:** Theme logic loaded on every request (or as gated by internal includes). "
            f"Review file for Woo hooks, REST, WPML, Klaviyo, checkout, cart, SEO, A/B tests, optimization.\n"
        )
        body.append("- **Relevance:** High (commerce + i18n surface area)\n")
        body.append("- **Transferability:** Not transferable — reimplement behaviors in Shopify theme app extensions, Functions, and apps.\n")
        body.append(f"- **Evidence:** `wp-content/themes/particleformen/{rel}`\n\n")

    body.append("## 2. Theme — `functions.php` root-level behaviors\n\n")
    body.append("### `wcml_custom_currency` filter\n\n")
    body.append(
        "- **Description:** Maps `wpml_current_language` codes (`au`,`gb`,`br`,`ca`,`he`,`la`,`ja`,`fr`,`de`,`it`,`es`) to ISO currencies (AUD, GBP, BRL, CAD, ILS, MXN, JPY, EUR).\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** Partial — Shopify Markets pricing.\n\n")
    body.append("### Category `list` asset dequeue\n\n")
    body.append(
        "- **Description:** On posts in category `list`, dequeues Woo + font + cookie scripts for lightweight reading experience.\n"
    )
    body.append("- **Relevance:** Low\n")
    body.append("- **Transferability:** Partial — theme blog templates.\n\n")
    body.append("### Checkout phone blocklist (`njengah_custom_checkout_field_process`)\n\n")
    body.append(
        "- **Description:** Blocks specific hard-coded `billing_phone` values at checkout validation.\n"
    )
    body.append("- **Relevance:** Medium (fraud / abuse)\n")
    body.append("- **Transferability:** Partial — Flow or checkout validation app.\n\n")
    body.append("### `custom_coupon_query` SQL filter\n\n")
    body.append(
        "- **Description:** Intercepts SQL containing INSERT into `woocommerce_order_itemmeta` for `coupon_data` and blanks query (custom coupon persistence behavior).\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** Not transferable — must understand business rule before replicating on Shopify.\n\n")
    body.append("### Magazine related posts + breadcrumbs + Yoast redirect slug + `remove_action` canonical\n\n")
    body.append(
        "- **Description:** Editorial helpers, Yoast filter, disables old slug redirect and `redirect_canonical` on `init` priority 100.\n"
    )
    body.append("- **Relevance:** Medium\n")
    body.append("- **Transferability:** Partial — SEO/redirect strategy on Shopify.\n\n")

    body.append("## 3. Theme — page templates (`template/*.php`)\n\n")
    for p in sorted((THEME / "template").glob("*.php")):
        body.append(f"### Page template file `{p.name}`\n\n")
        body.append(
            "- **Description:** Assignable WordPress page template in Particle theme. Open file for `Template Name` and marketing use case.\n"
        )
        body.append("- **Relevance:** Medium\n")
        body.append("- **Transferability:** Partial — Shopify page template or section set.\n")
        body.append(f"- **Evidence:** `wp-content/themes/particleformen/template/{p.name}`\n\n")

    body.append("## 4. Theme — Gutenberg blocks (`app/blocks/*/block.php`)\n\n")
    body.append(f"_Block count: **{len(blocks)}**._\n\n")
    for name in blocks:
        body.append(f"### Block `{name}`\n\n")
        body.append(
            "- **Description:** Registered block under Particle theme; defines editor + front markup for a reusable section.\n"
        )
        body.append("- **Relevance:** Medium\n")
        body.append("- **Transferability:** Partial — Shopify theme sections or metaobject-driven sections.\n")
        body.append(f"- **Evidence:** `wp-content/themes/particleformen/app/blocks/{name}/`\n\n")

    body.append("## 5. Theme — WooCommerce template overrides\n\n")
    body.append(f"_PHP files under `woocommerce/`: **{len(woo_tpl)}**._\n\n")
    for rel in woo_tpl:
        body.append(f"### Override `{rel}`\n\n")
        body.append("- **Description:** Overrides WooCommerce default template path for storefront/checkout/account behavior.\n")
        body.append("- **Relevance:** High\n")
        body.append("- **Transferability:** Partial — Liquid / Checkout Extensibility.\n")
        body.append(f"- **Evidence:** `wp-content/themes/particleformen/{rel}`\n\n")

    body.append("## 6. Custom post type (theme)\n\n")
    body.append("### CPT `landing_pages`\n\n")
    body.append(
        "- **Description:** Registered in `lib/custom-post-types.php` with `rewrite.slug = lpage`. Public REST-enabled landing content type.\n"
    )
    body.append("- **Relevance:** High\n")
    body.append("- **Transferability:** Partial — Shopify Pages or metaobject landing model + URL redirects.\n\n")

    body.append("## 7. REST and webhooks (non–pfm-panel highlights)\n\n")
    rest_items = [
        ("`twilio-api/v1` verify & send", "Theme `lib/rest-api.php` — SMS / verification flows."),
        ("`klaviyo-api/v1` profile, amazon, consultation, sweepstakes-webhook", "Theme `lib/rest-api.php` — server-side Klaviyo profile updates."),
        ("`email/v1` verify_email", "Theme `lib/rest-api.php`."),
        ("`braintree/v1` dispute-webhook", "Theme `lib/rest-api.php` — Braintree disputes to orders."),
        ("`woo/v1` order-notes & subscription-notes", "Theme `lib/rest-api.php`."),
        ("`get-data/v1` openai-crawlers/overview", "Theme `lib/rest-api.php`."),
        ("`shipbob/v1` order_shipped, shipment_exception, shipment_delivered", "`warehouse-export` plugin ShipBob class."),
        ("`v1` order-shipped/green", "`warehouse-export` Green warehouse webhook."),
        ("`pfm-monday-coupons` REST", "`pfm-monday-coupons` — coupon API for external automation."),
        ("`yotpo-integration/v1` create-coupon & cancel-coupon", "Yotpo loyalty coupon lifecycle."),
        ("`pfm-tools-utils` REST", "Multiple utility endpoints — read `pfm-tools-utils.php`."),
        ("`pfm-chargebacks-utils` REST", "Chargeback lookup by order."),
        ("`pfm-geo-privacy` REST", "Geo privacy endpoint."),
        ("`sellence-api` /products & /coupons", "External catalog/coupon feed."),
        ("`wunderkind/v1` feed", "Wunderkind product feed."),
        ("`orderswidget/v1` summary", "Order summary widget API."),
        ("`om-map/v1` map, bulk-map, nonce", "mu-plugin OptinMonster map output if present."),
        ("Klaviyo `class-wck-api.php` REST", "Official Klaviyo plugin endpoints."),
        ("Yoast / WP Rocket REST", "Admin-only REST for SEO/cache — low migration priority."),
    ]
    for title, desc in rest_items:
        body.append(f"### {title}\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append("- **Relevance:** Medium to High depending on consumer systems.\n")
        body.append("- **Transferability:** Partial — replicate with Shopify webhooks, app proxies, or middleware.\n\n")

    body.append("## 8. MU-plugins and host (custom subset)\n\n")
    mu_custom = [
        ("pfm-braintree-api-access.php", "Braintree API access helper for server-side operations.", "High", "Partial"),
        ("redirections.php", "WPML Redirect: language detection, `store_switch` cookie, URL fixes.", "High", "Partial"),
        ("pfm-performance.php", "Performance-related mu-plugin (theme-adjacent).", "Medium", "N/A"),
        ("custom_plugin_organizer.php", "Plugin load order, dashboard tweaks, cart removed_item redirect with WPML prefix.", "High", "Partial"),
        ("woocommerce-additional.php", "Additional Woo hooks at mu level — audit contents.", "Medium", "Partial"),
        ("om-map-output.php", "OptinMonster map REST if loaded.", "Low", "Partial"),
    ]
    for fname, desc, rel, xfer in mu_custom:
        body.append(f"### MU-plugin `{fname}`\n\n")
        body.append(f"- **Description:** {desc}\n")
        body.append(f"- **Relevance:** {rel}\n")
        body.append(f"- **Transferability:** {xfer}\n")
        body.append(f"- **Evidence:** `wp-content/mu-plugins/{fname}`\n\n")

    body.append("### WP Engine mu-plugins (`wpengine-*`, `wpe-*`, `slt-force-strong-passwords`, etc.)\n\n")
    body.append(
        "- **Description:** Hosting vendor auto-loaded plugins: caching, SSO, security auditor, update source, etc.\n"
    )
    body.append("- **Relevance:** Low for Shopify storefront parity\n")
    body.append("- **Transferability:** N/A — not part of Shopify; decommission with WP.\n\n")

    body.append("## 9. Static scrape inputs (reference)\n\n")
    body.append(
        "- **Description:** Local HTML snapshots under "
        "`C:\\Users\\denis_particleformen\\Desktop\\Cursor Projects\\particleformen-scrape\\output\\html` "
        "validate enqueued plugins, `hreflang` URL patterns, `?purchase-type=subscription`, `?store_switch=`.\n"
    )
    body.append("- **Relevance:** Medium (evidence for Phase G validation)\n")
    body.append("- **Transferability:** N/A — research artifact.\n\n")

    pfm_section = ROOT / "docs" / "_pfm-panel-section.md"
    if pfm_section.is_file():
        body.append(pfm_section.read_text(encoding="utf-8").rstrip() + "\n\n")
    else:
        body.append("## 10. `pfm-panel` REST API\n\n_(Missing `docs/_pfm-panel-section.md` — run from repo with snippet present.)_\n\n")

    body.append(emit_plugin_inventory())

    body.append("\n---\n\n_End of inventory. Re-run `python docs/generate-shopify-inventory.py` after plugin/theme changes._\n")

    out.write_text("".join(body), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
