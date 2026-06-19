SELECT
op.payment_value,
strftime('%m', oi.order_purchase_timestamp) AS order_month
FROM 'order payments' AS op
INNER JOIN 'orders' AS oi ON op.order_id = oi.order_id
GROUP BY order_month
ORDER BY op.payment_value DESC