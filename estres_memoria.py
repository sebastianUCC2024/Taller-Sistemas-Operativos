import psutil
import time

LIMITE_SEGURIDAD_RAM = 88.0
bloques_memoria = []

print(f"RAM Física Inicial Usada: {psutil.virtual_memory().percent}%")
print("Iniciando asignación real de memoria... Observa el Administrador de Tareas.\n")

bloque = 1
try:
    while True:
        ram_info = psutil.virtual_memory()
        swap_info = psutil.swap_memory()

        if ram_info.percent >= LIMITE_SEGURIDAD_RAM:
            print(f"\n[!] Límite de seguridad alcanzado ({ram_info.percent}% RAM). Deteniendo asignación.")
            break

        # Asignación real de ~200 MB por bloque en la RAM del sistema
        bloques_memoria.append(bytearray(200 * 1024 * 1024))
        
        print(f"Bloque {bloque:2d} | RAM Física: {ram_info.percent:.1f}% | Swap/Virtual: {swap_info.percent:.1f}%")
        bloque += 1
        time.sleep(0.5)

except MemoryError:
    print("\n[!] Excepción MemoryError capturada: Memoria exhausta.")

input("\nPresiona Enter para liberar la memoria y finalizar...")