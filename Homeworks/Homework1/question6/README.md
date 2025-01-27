SELECT 
    t2."Zone" AS dropoff_zone,
    MAX(t1.tip_amount) AS max_tip
FROM 
    green_tripdata t1
JOIN 
    taxi_zone_lookup t2
    ON t1."DOLocationID" = t2."LocationID"  
WHERE 
    t1.lpep_pickup_datetime BETWEEN '2019-10-01' AND '2019-10-31'
    AND t1."PULocationID" = (SELECT "LocationID" FROM taxi_zone_lookup WHERE "Zone" = 'East Harlem North')
GROUP BY 
    t2."Zone"
ORDER BY 
    max_tip DESC  
LIMIT 1; 
