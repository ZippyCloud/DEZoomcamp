1. Services inside docker-compose are part of the same network and can communicate with each other using the service name as the hostname. 
   Hence in this case, hostname for the first service is `db`.
2. Since they are inside the same network, and internal port is set to be `5432`
   then this is the port that pgadmin should use.

Answer: `db:5432`
