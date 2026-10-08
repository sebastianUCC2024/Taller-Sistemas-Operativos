import psutil
import os
import sys
import time

def aplicar_prioridad_real(prioridad):
    proceso = psutil.Process(os.getpid())
    if sys.platform == "win32":
        if prioridad == "baja":
            proceso.nice(psutil.IDLE_PRIORITY_CLASS)
        elif prioridad == "alta":
            proceso.nice(psutil.HIGH_PRIORITY_CLASS)

def calculo_matematico_intensivo():
    total = 0
    # Iteraciones ajustadas para el procesador AMD Ryzen 5 5500U
    for i in range(35_000_000):
        total += (i * 3) % 7
    return total

if __name__ == "__main__":
    prioridad = sys.argv[1].lower() if len(sys.argv) > 1 else "baja"
    
    aplicar_prioridad_real(prioridad)
    print(f"Proceso PID {os.getpid()} asignado con prioridad: {prioridad.upper()}")
    print(f"Iniciando cálculo pesado ({prioridad.capitalize()})...")
    
    inicio = time.time()
    calculo_matematico_intensivo()
    fin = time.time()
    
    tiempo_total = fin - inicio
    print(f"¡Terminó {prioridad.upper()}! Tiempo real: {tiempo_total:.4f} segundos")