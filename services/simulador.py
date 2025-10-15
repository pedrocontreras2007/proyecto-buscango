import threading
import time
import random

class Simulador:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._thread = None
    
    def iniciar(self, buses, callback):
        with self._lock:
            if self._running:
                return False
            self._running = True
            self._thread = threading.Thread(
                target=self._simular,
                args=(buses, callback),
                daemon=True
            )
            self._thread.start()
            return True
    
    def detener(self):
        with self._lock:
            self._running = False
            if self._thread:
                self._thread.join()
                self._thread = None
    
    def _simular(self, buses, callback):
        while True:
            with self._lock:
                if not self._running:
                    break
            for bus in buses:
                if bus.ruta:
                    bus.pasajeros = random.randint(0, bus.capacidad)
                    bus.mover_siguiente_parada()
                    callback(bus)
            time.sleep(2)