# Isaac/Roudnd_Robin.py (RF 2.1, RF 2.4 Decisión)
# Implementa la logica central del Round Robin.

from Andrew.Procesos import Proceso

class RoundRobinScheduler:
    """
    RF 2.1: Define y aplica las reglas del Quantum.
    RF 2.4: Decide si se requiere Preemption.
    """
    def __init__(self, quantum):
        self.quantum = quantum

    def seleccionar_proceso(self, ready_queue):
        """
        RF 2.2: Selecciona el proceso que esta en el frente de la cola (CA 2.1).
        """
        # Nota: Jeff (P4) llamara a la cola de Joshua para obtener el proceso.
        # Aqui solo nos aseguramos de que el proceso sea valido.
        if ready_queue:
            # En RR, simplemente toma el primero de la cola FIFO (que ya gestiona Joshua)
            return ready_queue[0]
        return None

    def necesita_preemption(self, proceso, tiempo_ejecutado):
        """
        RF 2.4 (Decisión): Determina si el proceso fue interrumpido por tiempo.
        """
        if proceso.remaining_burst_time > 0 and tiempo_ejecutado == self.quantum:
            # Si el proceso no termino (remaining > 0) Y consumio todo el quantum
            return True
        return False

# Instancia global del planificador (ejemplo con Q=2)
# Nota: Jeff (P4) debe inicializar esto en su main
# rr_scheduler = RoundRobinScheduler(quantum=2)