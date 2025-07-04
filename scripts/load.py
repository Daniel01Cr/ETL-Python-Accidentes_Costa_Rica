import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión
usuario = "postgres"
contraseña = "postgres"
host = "localhost"
puerto = "5432"
base_de_datos = "accidentes_cr"

# Cargar los datos limpios
df = pd.read_csv("data/accidentes_clean.csv")

# Crear conexión a PostgreSQL
conexion = create_engine(f"postgresql://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}")

# Cargar datos en una tabla llamada 'accidentes'
df.to_sql("accidentes", conexion, if_exists="replace", index=False)

print("Datos cargados exitosamente en la base de datos.")