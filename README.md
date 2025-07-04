# ETL de Datos de Accidentes de Tránsito en Costa Rica

Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) para procesar datos públicos de accidentes de tránsito en Costa Rica, con el objetivo de almacenarlos en una base de datos estructurada para análisis posteriores.

## Objetivo

- Extraer datos del INEC o MOPT.
- Limpiar y normalizar los datos utilizando Python.
- Cargar los datos en una base de datos PostgreSQL.
- Estructurar el modelo en un esquema dimensional tipo estrella para facilitar el análisis.

## Tecnologías Utilizadas

- **Python**: scripts ETL con `pandas`, `sqlalchemy`, `requests`.
- **PostgreSQL**: base de datos relacional para almacenamiento estructurado.
- **SQLAlchemy**: conexión Python ↔ PostgreSQL.

## Cómo ejecutar

1. Instala dependencias:

   ```bash
   pip install -r requirements.txt