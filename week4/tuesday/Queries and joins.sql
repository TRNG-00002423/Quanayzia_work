-- INNER JOIN: List every paid order:
-- customer email, order_id, placed_at, line revenue 
-- sum for that order (SUM(qty * unit_price))
-- use GROUP BY when using aggregate functions 
SELECT 
    c.email, 
    oh.order_id, 
    oh.placed_at, 
    SUM(ol.qty * ol.unit_price) AS order_revenue
FROM 
    customer c 
JOIN 
    order_header oh ON c.customer_id = oh.customer_id 
JOIN 
    order_line ol ON oh.order_id = ol.order_id
GROUP BY 
    c.email, 
    oh.order_id, 
    oh.placed_at;


-- LEFT JOIN: List all customers and their most recent order id (if any). 
-- Include customers with no orders (order_id NULL).

SELECT 
    c.customer_id, 
    MAX(oh.order_id) AS order_id,
    MAX(oh.placed_at) AS recent_date
FROM 
    customer c
LEFT JOIN 
    order_header oh ON c.customer_id = oh.customer_id
GROUP BY 
    c.customer_id;
	
-- RIGHT JOIN: Same logical data as (2) but implement with RIGHT JOIN 
-- (hint: flip table order so you still “start” 
--from customers mentally — comment why you ordered tables that way).
SELECT 
    c.customer_id, 
    MAX(oh.order_id) AS recent_order_id,
    MAX(oh.placed_at) AS recent_date
FROM order_header oh
-- RIGHT JOIN ensures all customers are kept, even if they have no matches in order_header
RIGHT JOIN customer c ON oh.customer_id = c.customer_id
GROUP BY c.customer_id;

-- FULL OUTER JOIN: Produce a report showing all customers 
-- and all orders, pairing where customer_id matches; 
--include unmatched rows on either side with NULLs.
SELECT 
    c.customer_id AS customer_table_id,
    c.email,
    oh.order_id,
    oh.placed_at
FROM customer c
FULL OUTER JOIN order_header oh 
    ON c.customer_id = oh.customer_id;

--CROSS JOIN (controlled): Build a small Cartesian product: 
--each product paired with a literal status dimension you create via an inline VALUES list (e.g. ('STOCK_OK','STOCK_LOW') thresholds are optional). Cap the result: WHERE or small dimension so 
--you do not explode row counts.
SELECT
    p.product_id,
    p.price,
    p.stock_on_hand,
    s.stock_status
FROM products p
CROSS JOIN (
    VALUES
        ('STOCK_OK'),
        ('STOCK_LOW')
) AS s(stock_status)
WHERE p.stock_on_hand <= 100;
