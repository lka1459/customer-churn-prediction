SELECT
o.order_id,
ore.review_score,
julianday(o.order_delivered_customer_date) - julianday(o.order_estimated_delivery_date) AS delivery_lateness
FROM orders AS o
INNER JOIN "order reviews" AS ore 
ON o.order_id = ore.order_id
WHERE o.order_delivered_customer_date IS NOT NULL 
AND o.order_estimated_delivery_date IS NOT NULL
GROUP BY o.order_id 
ORDER BY ore.review_score ASC