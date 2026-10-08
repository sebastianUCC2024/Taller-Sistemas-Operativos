import time
import os

# Caché en memoria RAM (usando un Diccionario)
cache_memoria = {}
NOMBRE_ARCHIVO = "archivo_prueba_cache.txt"

def preparar_archivo_disco():
    """Crea un archivo de texto real en el disco si no existe para la prueba."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Generando archivo real en disco: '{NOMBRE_ARCHIVO}'...")
        # Generamos un archivo de ~20 MB de texto real en disco
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            for i in range(500_000):
                f.write(f"Linea {i}: Sistemas Operativos - Prueba Real de Cache en RAM\n")

def leer_archivo(nombre_archivo):
    """
    Lee el archivo. La primera vez va al disco físico.
    Las siguientes veces lo lee desde el objeto en RAM.
    """
    inicio = time.time()
    
    # 1. VERIFICACIÓN EN CACHÉ (RAM) -> HIT
    if nombre_archivo in cache_memoria:
        contenido = cache_memoria[nombre_archivo]
        fin = time.time()
        tiempo_total = fin - inicio
        print("\n--- LECTURA DESDE CACHÉ (MEMORIA RAM) ---")
        print(f"-> ¡HIT DE CACHÉ! '{nombre_archivo}' encontrado en RAM.")
        print(f"-> Tamaño leído: {len(contenido) / (1024*1024):.2f} MB")
        print(f"-> Tiempo de ejecución: {tiempo_total:.6f} segundos")
        return contenido

    # 2. LECTURA DESDE DISCO (ALMACENAMIENTO SECUNDARIO) -> MISS
    print("\n--- LECTURA DESDE DISCO (MEMORIA SECUNDARIA) ---")
    print(f"-> MISS DE CACHÉ. '{nombre_archivo}' no está en RAM. Leyendo del disco físico...")
    
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()  # Operación de E/S real sobre el disco
    
    # Guardar en la estructura en RAM para futuras lecturas
    cache_memoria[nombre_archivo] = contenido
    
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"-> Archivo cargado en la caché de RAM.")
    print(f"-> Tiempo de ejecución: {tiempo_total:.6f} segundos")
    return contenido

if __name__ == "__main__":
    # Asegurar la existencia del archivo en el disco local
    preparar_archivo_disco()
    
    # Primera Lectura: Directo desde el disco rígido/SSD
    leer_archivo(NOMBRE_ARCHIVO)
    
    # Segunda Lectura: Directo desde la memoria RAM
    leer_archivo(NOMBRE_ARCHIVO)
    
    # Opcional: Limpiar el archivo de prueba al finalizar
    if os.path.exists(NOMBRE_ARCHIVO):
        os.remove(NOMBRE_ARCHIVO)