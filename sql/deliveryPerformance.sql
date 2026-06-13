SELECT
strftime('%Y', order_purchase_timestamp) AS order_year,
strftime('%m', order_purchase_timestamp) AS order_month,
AVG(julianday(order_estimated_delivery_date) - julianday(order_delivered_customer_date)) AS data_diff
FROM orders
WHERE order_status = 'delivered'
GROUP BY order_year, order_month
