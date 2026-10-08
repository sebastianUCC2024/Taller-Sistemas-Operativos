import psutil
import time
from datetime import datetime

UMBRAL_RAM = 80.0
LOG_FILE = "alertas_memoria.txt"

print("--- Vigilante de Recursos Iniciado (Presiona Ctrl+C para salir) ---")

try:
    while True:
        # psutil.cpu_percent con interval=1 mide el uso real del micro en ese segundo
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        print(f"CPU: {cpu_usage:.1f}% | RAM: {ram_usage:.1f}%")

        if ram_usage > UMBRAL_RAM:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mensaje = f"[{timestamp}] ALERTA! Uso crítico de RAM detectado: {ram_usage:.1f}%\n"
            
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(mensaje)
            
            print(f" -> {mensaje.strip()}")

        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitoreo finalizado.")