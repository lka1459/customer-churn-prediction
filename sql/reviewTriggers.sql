SELECT
o.order_id,
ore.review_score,
AVG(julianday(o.order_delivered_customer_date) - julianday(o.order_estimated_delivery_date)) AS data_diff
FROM orders AS o
INNER JOIN "order reviews" AS ore ON o.order_id = ore.order_id
GROUP BY o.order_id
ORDER BY ore.review_score ASC