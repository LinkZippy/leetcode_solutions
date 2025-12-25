-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

SELECT a.id
FROM Weather a
JOIN Weather b ON a.recordDate = b.recordDate + INTERVAL '1 day'
WHERE a.temperature > b.temperature
;
