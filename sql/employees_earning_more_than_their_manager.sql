-- Write a solution to find the employees who earn more than their managers.

Return the result table in any order.
SELECT e.name AS 'Employee'
FROM Employee AS e
JOIN Employee AS m ON e.managerId = m.id
WHERE e.salary > m.salary
;
