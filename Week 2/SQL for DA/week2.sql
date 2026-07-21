-- Task 1
-- select all from table
SELECT * FROM beeskilled_sales;

-- Task 2
-- select all electronics from table
SELECT * FROM beeskilled_sales
WHERE category='Electronics';

-- Task 3
-- total revenue
SELECT sum(total_price) as Total_Revenue
FROM beeskilled_sales;

-- Task 4
-- category wise revenue
SELECT category, sum(total_price) as Revenue
FROM beeskilled_sales
GROUP by category;

-- Task 5
-- avg order value
SELECT avg(total_price) 
as Avg_Order_value
FROM beeskilled_sales;

-- Task 6
-- Top customer
SELECT customer_name, 
sum(total_price) as Revenue
FROM beeskilled_sales
GROUP by customer_name 
ORDER by Revenue DESC
LIMIT 10;

-- Task 7
-- units sold each product
SELECT product_name, 
sum(quantity) as units_sold
FROM beeskilled_sales
GROUP by product_name
ORDER by units_sold DESC;

