SELECT
c.customer_id,
SUM(op.payment_installments) AS total_installations, 
SUM(op.payment_value) AS total_spendings
FROM 'order payments' AS op
INNER JOIN orders AS o ON op.order_id = o.order_id
INNER JOIN customers AS c ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spendings DESC