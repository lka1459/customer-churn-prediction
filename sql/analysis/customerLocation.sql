SELECT customer_state, COUNT(*) AS CustomerCount
FROM customers 
GROUP BY customer_state
ORDER BY COUNT(*) DESC