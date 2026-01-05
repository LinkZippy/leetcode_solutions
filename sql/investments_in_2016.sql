-- Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

-- have the same tiv_2015 value as one or more other policyholders, and
-- are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
-- Round tiv_2016 to two decimal places.

SELECT ROUND(SUM(tiv_2016)::NUMERIC,2) AS tiv_2016
FROM (
    SELECT tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS c15, 
        COUNT(*) OVER(PARTITION BY lat, lon) AS c_latlon
    FROM Insurance  
) AS temp
WHERE temp.c15 > 1 AND temp.c_latlon = 1
;
