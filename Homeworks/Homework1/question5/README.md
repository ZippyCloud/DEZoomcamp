SELECT 
  t1."Zone" AS pickup_zone,
  SUM(t2.total_amount) AS total_amount_sum
FROM green_tripdata t2
JOIN taxi_zone_lookup t1
  ON t2."PULocationID" = t1."LocationID"
WHERE t2.lpep_pickup_datetime >= '2019-10-18 00:00:00' 
  AND t2.lpep_pickup_datetime < '2019-10-19 00:00:00'
GROUP BY t1."Zone"
HAVING SUM(t2.total_amount) > 13000
ORDER BY total_amount_sum DESC;
