-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.

SELECT name
FROM employee
WHERE id IN
    (SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5)
;
