from Andrew.Procesos import Proceso

class ReadyQueueManager:
    """
    Joshua (P2) - Controlador de Tráfico y Azafata de la Sala de Espera.
    RF 1.3: Mantiene la estructura de la Cola de Listos.
    RF 1.4: Gestiona transiciones a/desde LISTO.
    """

    def __init__(self, all_processes):
        self.all_processes = all_processes
        
        # Cola inicial VACÍA — los procesos entran cuando llegue su tiempo.
        self.ready_queue = []

        # Ordenar la lista completa por tiempo de llegada (solo referencia)
        self.all_processes.sort(key=lambda p: p.arrival_time)

        print("[P2/Joshua] Procesos ordenados por arrival_time.")


    def check_new_arrivals(self, global_clock):
        """
        RF 1.4: Mueve procesos de NUEVO a LISTO cuando llegan.
        Y los inserta en la Cola de Listos ordenadamente (FIFO).
        """
        for proceso in self.all_processes:
            if proceso.current_state == "NUEVO" and proceso.arrival_time <= global_clock:
                proceso.current_state = "LISTO"
                self.ready_queue.append(proceso)

                print(f"[P2/Joshua] P{proceso.id} movido a LISTO "
                      f"(Llegó al tiempo {global_clock}).")



    def get_next_ready_process(self):
        """
        RF 2.x: Isaac me pide el siguiente proceso en LISTO.
        Uso FIFO, así que entrego y elimino el primero.
        """
        if self.ready_queue:
            proceso = self.ready_queue.pop(0)
            print(f"[P2/Joshua] Entregado P{proceso.id} a Isaac (CPU).")
            return proceso

        print("[P2/Joshua] No hay procesos en LISTO.")
        return None



    def reencolar_proceso(self, proceso):
        """
        RF 2.4: Isaac interrumpió el proceso por quantum agotado.
        Joshua debe reencolarlo al FINAL.
        """
        proceso.current_state = "LISTO"
        self.ready_queue.append(proceso)

        print(f"[P2/Joshua] P{proceso.id} REENCOLADO al final de la Cola "
              "(Preempted por quantum).")