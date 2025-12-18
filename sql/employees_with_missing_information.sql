-- Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.

SELECT employee_id
FROM Employees
LEFT JOIN Salaries USING (employee_id)
WHERE Salaries.employee_id IS NULL

UNION 

SELECT employee_id
FROM Salaries
LEFT JOIN Employees USING (employee_id)
WHERE Employees.employee_id IS NULL

ORDER BY employee_id
;
