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
