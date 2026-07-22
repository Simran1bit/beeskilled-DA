-- viewing dataset
SELECT* FROM capstone_cleaned
LIMIT 10;

--Total Sales, Profit, Units Sold
SELECT 
sum(Sales) as Total_Sales,
sum(Profit) as Total_Profit,
sum(`Units Sold`) as Total_Units 
from capstone_cleaned;

--Sales by Country
SELECT Country,
sum(Sales) as Total_Sales
from capstone_cleaned
GROUP by Country
order by Total_Sales Desc;

--Profit by Segment
Select Segment,
sum(Profit) as Total_Profit
from capstone_cleaned
GROUP by Segment
ORDER by Total_Profit DESC;

-- Top 5 Products by Sales
SELECT Product,
sum(Sales) as Total_Sales
FROM capstone_cleaned
group by Product
order by Total_Sales DESC
LIMIT 5;

-- Avg Discount by Discount Band
select `Discount Band`,
avg(Discounts) as Avg_Discount
from capstone_cleaned
group by `Discount Band`;

--Monthly Sales trend
select `Month Name`, `Month Number`,
sum(Sales) as Total_Sales
from capstone_cleaned
group by `Month Name`
ORDER by `Month Number`;

--Top 10 Highest Sales Transaction
select Country, Product, Segment, Sales, Profit
from capstone_cleaned
order by Sales DESC
LIMIT 10;

--Country wise Avg Profit
select Country,
avg(profit) as Avg_Profit
from capstone_cleaned
group by Country;

--Sales and Profit by Product
select Product,
sum(Sales) as Total_Sales,
sum(profit) as Total_Profit
from capstone_cleaned
group by Product
order by Total_Sales DESC;