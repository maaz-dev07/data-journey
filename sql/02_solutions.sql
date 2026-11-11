-- ============================================================
--  SQL practice - solutions
--  Try the exercise first. Then compare - there are many valid answers.
-- ============================================================

USE practice;

-- 1. Electronics products, cheapest first
SELECT product_id, product_name, unit_price
FROM products
WHERE category = 'Electronics'
ORDER BY unit_price ASC;

-- 2. Customers per country
SELECT country, COUNT(*) AS customers
FROM customers
GROUP BY country
ORDER BY customers DESC;

-- 3. Cancelled orders in 2025
SELECT order_id, customer_id, order_date
FROM orders
WHERE status = 'cancelled'
  AND order_date >= '2025-01-01'
  AND order_date <  '2026-01-01';

-- 4. Average price per category
SELECT category, ROUND(AVG(unit_price), 2) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- 5. Orders and item quantity per status
SELECT o.status,
       COUNT(DISTINCT o.order_id) AS orders,
       SUM(oi.quantity)           AS total_quantity
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.status
ORDER BY orders DESC;

-- 6. Top 10 customers by spend (completed orders only)
SELECT c.customer_id,
       CONCAT(c.first_name, ' ', c.last_name) AS customer,
       c.country,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS total_spent
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, customer, c.country
ORDER BY total_spent DESC
LIMIT 10;

-- 7. Categories with more than 10 active products
SELECT category, COUNT(*) AS active_products
FROM products
WHERE is_active = 1
GROUP BY category
HAVING COUNT(*) > 10
ORDER BY active_products DESC;

-- 8. Customers with no orders
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

-- 9. Monthly revenue trend
SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
       COUNT(DISTINCT o.order_id) AS orders
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY month
ORDER BY month;

-- 10. Best-selling product per category by revenue
WITH product_revenue AS (
    SELECT p.category,
           p.product_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue,
           ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) DESC) AS rn
    FROM order_items oi
    JOIN orders o   ON o.order_id = oi.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_id, p.product_name
)
SELECT category, product_name, ROUND(revenue, 2) AS revenue
FROM product_revenue
WHERE rn = 1
ORDER BY revenue DESC;

-- 11. Customer spend buckets with a CTE
WITH spend AS (
    SELECT c.customer_id,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS total_spent
    FROM customers c
    JOIN orders o       ON o.customer_id = c.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY c.customer_id
),
bucketed AS (
    SELECT customer_id,
           CASE WHEN total_spent >= 2000 THEN 'High'
                WHEN total_spent >= 500  THEN 'Medium'
                ELSE 'Low' END AS bucket
    FROM spend
)
SELECT bucket, COUNT(*) AS customers
FROM bucketed
GROUP BY bucket
ORDER BY FIELD(bucket, 'High', 'Medium', 'Low');

-- 12. Salary vs department average
SELECT employee_id,
       CONCAT(first_name, ' ', last_name) AS employee,
       job_title,
       salary,
       ROUND(AVG(salary) OVER (PARTITION BY department), 2) AS dept_avg,
       ROUND(salary - AVG(salary) OVER (PARTITION BY department), 2) AS diff_from_avg
FROM employees
ORDER BY department, salary DESC;

-- 13. Average order value per channel
SELECT o.channel,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount))
             / COUNT(DISTINCT o.order_id), 2) AS avg_order_value
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY o.channel
ORDER BY avg_order_value DESC;

-- 14. Top 3 products by revenue per category
WITH product_revenue AS (
    SELECT p.category, p.product_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue,
           ROW_NUMBER() OVER (PARTITION BY p.category
                              ORDER BY SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) DESC) AS rn
    FROM order_items oi
    JOIN orders o   ON o.order_id = oi.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_id, p.product_name
)
SELECT category, rn, product_name, ROUND(revenue, 2) AS revenue
FROM product_revenue
WHERE rn <= 3
ORDER BY category, rn;

-- 15. 2025 signups who ordered within 30 days
SELECT COUNT(DISTINCT c.customer_id) AS customers_ordered_within_30d
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
WHERE c.signup_date >= '2025-01-01'
  AND c.signup_date <  '2026-01-01'
  AND o.status = 'completed'
  AND o.order_date >= c.signup_date
  AND o.order_date <  DATE_ADD(c.signup_date, INTERVAL 30 DAY);
