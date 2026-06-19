SELECT 
c.customer_unique_id,
c.customer_city, 
c.customer_state,
COUNT(DISTINCT o.order_id) AS total_orders,
SUM(oi.price) AS total_spent,
AVG(oi.price) AS average_spent,
 AVG(
        julianday(o.order_delivered_customer_date)
        - julianday(o.order_estimated_delivery_date)
    ) AS avg_delivery_lateness,
MAX(o.order_purchase_timestamp) AS last_order_date,
AVG(ore.review_score) AS avg_review_score,
COUNT(DISTINCT p.product_category_name) AS num_categories
FROM customers AS c
JOIN orders AS o 
ON c.customer_id = o.customer_id
JOIN "order reviews" AS ore 
ON o.order_id = ore.order_id
JOIN "order items" AS oi
ON o.order_id = oi.order_id
JOIN products AS p
ON oi.product_id = p.product_id
GROUP BY c.customer_unique_id, c.customer_city, c.customer_state