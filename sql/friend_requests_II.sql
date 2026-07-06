-- Write a solution to find the people who have the most friends and the most friends number.

-- The test cases are generated so that only one person has the most friends.

SELECT accepter_id AS id, SUM(num_req) AS num
FROM
    (SELECT accepter_id, count(requester_id) AS num_req
    FROM RequestAccepted
    GROUP BY accepter_id

    UNION ALL

    SELECT requester_id, count(accepter_id) as num_acc
    FROM RequestAccepted
    GROUP BY requester_id) AS a
GROUP BY id
ORDER BY num DESC
LIMIT 1
;
