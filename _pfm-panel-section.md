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
