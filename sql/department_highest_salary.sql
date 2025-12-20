-- Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.
SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.name AS Department,  
        e.name AS Employee, 
        salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY salary DESC) AS rnk
    FROM Employee e
    LEFT JOIN Department d ON e.departmentId = d.id)
WHERE rnk = 1
;
