SELECT t.product_category_name_english,
COUNT(*) AS count_orders
FROM products AS p
INNER JOIN 'order items' AS oi ON p.product_id = oi.product_id
INNER JOIN 'product category name translation' AS t ON p.product_category_name = t.product_category_name
GROUP BY t.product_category_name_english
ORDER BY COUNT(*) DESC