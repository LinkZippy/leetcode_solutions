-- Report for every three line segments whether they can form a triangle.

-- Return the result table in any order.



SELECT *,
    CASE
        WHEN x+y>z AND y+z>x AND z+x>y THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM triangle;
