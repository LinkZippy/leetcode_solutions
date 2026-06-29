-- Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

-- The employee has a bonus less than 1000.
-- The employee did not get any bonus.
-- Return the result table in any order.

SELECT 
    name, bonus
FROM Employee as e
LEFT JOIN Bonus as b
ON e.empId = b.empId
WHERE bonus < 1000 OR bonus IS NULL
;
