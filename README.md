# de_zoomcamp

## 01-docker-terraform

### 02-virtual-environment
Creamos un pipeline de prueba y lo ejecutamos en un entorno virtual de python.

### 03-dockerizing-pipeline
Creamos un contenedor para ejecutar el pipeline de prueba.

### 04-postgres-docker
Ejecutamos Postgres en un contenedor, creamos una tabla y un registro.
```
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
```

En otra terminal podemos hacer queries a la BD:
```
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

### 05-data-ingestion
Creamos una jupyter notebook para leer datos desde una csv y cargarlo en postgres.
Instalamos librerías: 
- jupyter, para crear las notebooks.
- sqlalchemy, para conectarnos a postgres desde la notebook.
- psycopg2-binary, 
- tqdm, para ver el progreso de carga de datos.

### 06-ingestion-script
Convertimos la notebook en un script de python.
Convertimos inputs de datos en variables y ordenamos el código.
Parametrizamos la variables.
Intalamos la librería click para permitir el input de parámetros por comando.

### 07-pgadmin
Creamos una red compartida entre los contenedores para que puedan comunicarse entre sí.
Ejecutamos un nuevo contenedor para pgadmin.

### 08-dockerizing-ingestion
Actualizamos el Dockerfile para ejecutar la carga de datos (ingest_data.py).
Para ejecutar el nuevo contenedor de carga, y que pueda conectarse a postgres, agregamos un argumento para especificar la network y cambiamos el nombre del host:
```
docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
```
### 09-docker-compose
Con docker-compose podemos ejecutar varios contenedores a la vez, especificando los parámetros de entrada, desde un archivo .yaml, sin necesidad de utilizar comandos largos ni terminales distintas. Además que también crea y utiliza una network compartida para los contenedores que ejecuta.

Para ejecutar los contenedores utilizamos el comando:
```
docker-compose up
```

Y para detenerlos utilizamos (en otra consola):
```
docker-compose down
```

Con este cambio, los contenedores se estarían ejecutando con nuevos volúmenes de almacenamiento, por lo que es necesario volver a configurar pgadmin y volver a cargar los datos en pgdatabase, esta vez con el contenedor de ingest_data y especificando la network que se 
cree con docker-compose:
```
docker network ls

docker run -it --rm\
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
```
