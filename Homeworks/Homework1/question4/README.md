SELECT 
  TO_CHAR(lpep_pickup_datetime, 'YYYY-MM-DD') AS pickup_day, 
  MAX(trip_distance) AS longest_trip_distance
FROM green_tripdata
WHERE lpep_pickup_datetime >= '2019-10-01 00:00:00' 
  AND lpep_pickup_datetime < '2019-11-01 00:00:00'
GROUP BY pickup_day
ORDER BY longest_trip_distance DESC
LIMIT 1;
