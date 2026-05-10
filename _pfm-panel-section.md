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
