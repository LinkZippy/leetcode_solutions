-- Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

-- Return the result table in any order.

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
