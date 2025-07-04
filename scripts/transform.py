import pandas as pd
import os
import unidecode  

input_path = "data/accidentes_raw.csv"
output_path = "data/accidentes_clean.csv"


def limpiar_datos():

    df = pd.read_csv(input_path)

    # Limpieza de columnas
    df.columns = [unidecode.unidecode(col.strip().lower().replace(" ", "_")) for col in df.columns]

    # Ejemplo de conversión de fecha si hay una columna llamada 'fecha'
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')

    # Eliminar filas sin fecha o tipo de accidente
    columnas_requeridas = [col for col in ["fecha", "tipo_accidente"] if col in df.columns]
    if columnas_requeridas:
        df = df.dropna(subset=columnas_requeridas)

    # Eliminar duplicados si los hay
    df = df.drop_duplicates()

    # Guardar la versión limpia
    os.makedirs("data", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Archivo limpio guardado en: {output_path}")

if __name__ == "__main__":
    limpiar_datos()