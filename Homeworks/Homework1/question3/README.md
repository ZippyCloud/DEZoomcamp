SELECT
  COUNT(*) FILTER (WHERE trip_distance <= 1) AS "Up_to_1_mile",
  COUNT(*) FILTER (WHERE trip_distance > 1 AND trip_distance <= 3) AS "1_to_3_miles",
  COUNT(*) FILTER (WHERE trip_distance > 3 AND trip_distance <= 7) AS "3_to_7_miles",
  COUNT(*) FILTER (WHERE trip_distance > 7 AND trip_distance <= 10) AS "7_to_10_miles",
  COUNT(*) FILTER (WHERE trip_distance > 10) AS "Over_10_miles"
FROM green_tripdata
WHERE lpep_pickup_datetime >= '2019-10-01 00:00:00'
  AND lpep_pickup_datetime < '2019-11-01 00:00:00';