import subprocess

def ejecutar(script):
    print(f"\n Ejecutando: {script}")
    resultado = subprocess.run(["python", script], capture_output=True, text=True)

    if resultado.returncode == 0:
        print(f"Completado: {script}\n")
    else:
        print(f"Error ejecutando {script}")
        print(resultado.stdout)
        print(resultado.stderr)

if __name__ == "__main__":
    print("========== INICIANDO ETL ==========")
    ejecutar("scripts/extract.py")
    ejecutar("scripts/transform.py")
    ejecutar("scripts/load.py")
    print("========== ETL FINALIZADO ==========")