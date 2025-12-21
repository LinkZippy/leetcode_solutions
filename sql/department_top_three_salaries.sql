-- A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

-- Write a solution to find the employees who are high earners in each of the departments.

-- Return the result table in any order.

SELECT Department, Employee, Salary
FROM
    (SELECT 
        d.name AS Department, 
        e.name AS Employee, 
        salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON d.id = e.departmentId)
WHERE rnk <= 3
;
