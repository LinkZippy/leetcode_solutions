-- Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

-- Return the result table ordered by visit_date in ascending order.

SELECT a.id, visit_date, people
FROM 
    (SELECT s1.id
    FROM Stadium s1
    JOIN Stadium s2 ON s1.id = s2.id+1
    JOIN Stadium s3 ON s1.id = s3.id+2
    WHERE s1.people >= 100 AND s2.people >= 100 and s3.people >= 100

    UNION

    SELECT s2.id
    FROM Stadium s1
    JOIN Stadium s2 ON s1.id = s2.id+1
    JOIN Stadium s3 ON s1.id = s3.id+2
    WHERE s1.people >= 100 AND s2.people >= 100 and s3.people >= 100

    UNION 

    SELECT s3.id
    FROM Stadium s1
    JOIN Stadium s2 ON s1.id = s2.id+1
    JOIN Stadium s3 ON s1.id = s3.id+2
    WHERE s1.people >= 100 AND s2.people >= 100 and s3.people >= 100) AS a
JOIN Stadium b ON a.id = b.id
;
