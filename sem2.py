import pandas as pd

def cargar_dataset(ruta):
    try:
        # Carga el archivo CSV en un DataFrame de pandas
        df = pd.read_csv(ruta)
        # Muestra las primeras filas del DataFrame
        print(df.head())
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")

# Especifica la ruta del archivo CSV

ruta_archivo = r"D:\DATOS RECUPERADOS\UNIVERSIDAD DE LIMA\10. Decimo Ciclo\Seminario 1\BankSim.csv"
# Llama a la función para cargar el dataset
cargar_dataset(ruta_archivo)