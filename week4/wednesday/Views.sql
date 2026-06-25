--- View 1

CREATE OR REPLACE VIEW v_order_line_detail AS
SELECT
    oh.order_id,
    c.email AS customer_email,
    p.sku,
    ol.qty,
    (ol.qty * ol.unit_price) AS line_total,
    oh.status AS order_status
FROM order_header oh
JOIN customer c 
    ON c.customer_id = oh.customer_id
JOIN order_line ol 
    ON ol.order_id = oh.order_id
JOIN product p 
    ON p.product_id = ol.product_id;


---view 2
CREATE OR REPLACE VIEW v_customer_spend AS
SELECT
    c.email,
    COUNT(DISTINCT oh.order_id) AS order_count,
    COALESCE(SUM(ol.qty * ol.unit_price), 0) AS lifetime_spend
FROM customer c
LEFT JOIN order_header oh 
    ON c.customer_id = oh.customer_id
LEFT JOIN order_line ol 
    ON oh.order_id = ol.order_id
GROUP BY c.email;