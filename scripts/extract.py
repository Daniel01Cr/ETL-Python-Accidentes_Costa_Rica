import requests
import os

# URL del archivo CSV (reemplazar por la real)
url = "https://datosabiertos.csv.go.cr/datasets/193472-consolidado-de-accidentes-de-transito-con-victimas.download/"

# Ruta de guardado local
os.makedirs("data", exist_ok=True)
output_path = "data/accidentes_raw.csv"

def descargar_datos():
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Datos descargados correctamente: {output_path}")
    else:
        print(f"Error al descargar: Código {response.status_code}")

if __name__ == "__main__":
    descargar_datos()