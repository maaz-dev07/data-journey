-- ============================================================
--  SQL practice - exercises
--  Database: practice   (run: USE practice;)
--  Tables:
--    customers(customer_id, first_name, last_name, email, city, country, signup_date)
--    products(product_id, product_name, category, unit_price, unit_cost, is_active)
--    orders(order_id, customer_id, order_date, status, channel)
--    order_items(order_item_id, order_id, product_id, quantity, unit_price, discount)
--    employees(employee_id, first_name, last_name, department, job_title,
--              salary, hire_date, manager_id)
-- ============================================================

-- 1. EASY: List all products in the 'Electronics' category, cheapest first.

-- 2. EASY: How many customers are there per country? Highest count first.

-- 3. EASY: Show orders placed in 2025 that were cancelled.

-- 4. EASY: What is the average product price per category?
--    Round to 2 decimals.

-- 5. MEDIUM: For each order status, show the number of orders and the
--    total quantity of items in those orders.

-- 6. MEDIUM: List the 10 customers who have spent the most money
--    (only 'completed' orders). Show name, country, total spent.

-- 7. MEDIUM: Which product categories have more than 10 active products?
--    Show category and the count.

-- 8. MEDIUM: Find customers who have never placed an order.
--    (Hint: LEFT JOIN ... IS NULL, or NOT IN / NOT EXISTS)

-- 9. HARD: Monthly revenue trend for completed orders.
--    Columns: month (YYYY-MM), revenue, number of orders.

-- 10. HARD: For each category, find the single best-selling product
--     by revenue. (Hint: window function ROW_NUMBER() over a grouped subquery.)

-- 11. HARD: Using a CTE, compute each customer's total spend and bucket them:
--     'High'   >= 2000
--     'Medium' >= 500
--     'Low'    < 500
--     Then count how many customers are in each bucket.

-- 12. HARD: For every employee, show their name, job_title, salary,
--     and the average salary of their department, plus the difference.
--     (Hint: window function AVG() OVER (PARTITION BY department))

-- 13. STRETCH: Which channel has the highest average order value?
--     Average order value = revenue / number of distinct orders.

-- 14. STRETCH: Find the top 3 products by revenue within each category,
--     using a window function, then filter to rank <= 3.

-- 15. STRETCH: Retention-style question - of the customers who signed up
--     in 2025, how many placed at least one completed order within 30 days
--     of signing up?
