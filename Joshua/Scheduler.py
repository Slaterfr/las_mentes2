# Joshua/Scheduler.py (RF 1.3, RF 1.4, RF 2.4 Re-queue)
# Maneja la Cola de Listos (Ready Queue) y el reencolado por preemption.

from Andrew.Procesos import Proceso

class ReadyQueueManager:
    """
    RF 1.3: Mantiene la estructura de la Cola de Listos.
    RF 1.4: Gestiona las transiciones a/desde el estado LISTO.
    """
    def __init__(self, all_processes):
        self.all_processes = all_processes
        self.ready_queue = [] # La cola en si

    def check_new_arrivals(self, global_clock):
        """
        RF 1.4: Mueve procesos de NUEVO a LISTO al llegar su arrival_time.
        """
        for proceso in self.all_processes:
            if proceso.current_state == "NUEVO" and proceso.arrival_time <= global_clock:
                proceso.current_state = "LISTO"
                self.ready_queue.append(proceso)
                print(f"[P2/Joshua] P{proceso.id} movido a LISTO (Llego al tiempo {global_clock}).")

    def get_next_ready_process(self):
        """
        Funcion llamada por Isaac (P3) para obtener el siguiente proceso.
        """
        if self.ready_queue:
            # En Round Robin, se saca de la cabeza (FIFO)
            return self.ready_queue.pop(0) 
        return None

    def reencolar_proceso(self, proceso):
        """
        RF 2.4 (Re-queue): Toma un proceso preemptado y lo pone al final de la cola.
        """
        proceso.current_state = "LISTO"
        self.ready_queue.append(proceso)
        # print(f"[P2/Joshua] P{proceso.id} reencolado al final de la Cola de Listos.")