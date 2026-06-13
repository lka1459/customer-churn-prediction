SELECT
op.payment_value,
strftime('%m', oi.order_purchase_timestamp) AS order_month,
strftime('%Y', oi.order_purchase_timestamp) AS order_year
FROM 'order payments' AS op
INNER JOIN 'orders' AS oi ON op.order_id = oi.order_id
GROUP BY order_month, order_year
ORDER BY op.payment_value DESC