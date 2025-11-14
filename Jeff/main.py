

# Jeff/main.py - Motor de Ejecucion y Trazabilidad (P4)
# Centraliza la logica. Cubre RF 3.1, RF 2.2, RF 2.3, RF 3.2.

# Importaciones necesarias
from Andrew.Procesos import Proceso, inicializar_procesos 
from Joshua.Scheduler import ReadyQueueManager 
from Isaac.Roudnd_Robin import RoundRobinScheduler 
from Diego.main_analisys import calcular_metricas_finales 

class NanoOSimulator:
    """
    Contiene el estado global y el bucle principal (RF 3.1).
    """
    
    def __init__(self, quantum=2):
        self.global_clock = 0 
        self.quantum = quantum # RF 2.1
        self.all_processes = inicializar_procesos() 
        self.ready_queue_manager = ReadyQueueManager(self.all_processes) # P2/Joshua
        self.rr_scheduler = RoundRobinScheduler(self.quantum) # P3/Isaac
        self.current_process = None 

    def hay_procesos_pendientes(self):
        return any(p.current_state != "TERMINADO" for p in self.all_processes)

    def run_simulation(self):
        """
        Bucle principal de la simulacion (RF 3.1).
        """
        print("\n--- P4: Iniciando Bucle de Simulacion ---")
        
        while self.hay_procesos_pendientes():
            # 1. GESTION DE LA COLA (P2/Joshua): Mueve de NUEVO a LISTO
            self.ready_queue_manager.check_new_arrivals(self.global_clock)
            
            # 2. SELECCION DE PROCESO (P3/Isaac y RF 2.2)
            if self.current_process is None or self.current_process.current_state != "EJECUCION":
                
                # P3 (Isaac) selecciona el proceso de la cola de P2 (RF 2.2)
                proceso_a_ejecutar = self.rr_scheduler.seleccionar_proceso(self.ready_queue_manager.ready_queue)
                
                if proceso_a_ejecutar:
                    # Lo saca de la cola de Joshua para llevarlo a la CPU simulada
                    self.ready_queue_manager.ready_queue.remove(proceso_a_ejecutar)
                    self.current_process = proceso_a_ejecutar
                    
                    # Transicion: LISTO -> EJECUCION (Despachador RF 2.2)
                    self.current_process.current_state = "EJECUCION"

            # ----------------------------------------------------
            
            if self.current_process:
                # --- 3. LOGICA DE EJECUCION (RF 2.3) ---
                
                # Tiempo que realmente ejecutara: minimo entre el Quantum y el tiempo restante
                time_slice = min(self.quantum, self.current_process.remaining_burst_time)
                
                # Consumo de tiempo
                self.current_process.remaining_burst_time -= time_slice
                self.global_clock += time_slice # RF 3.1: El reloj avanza
                
                # --- 4. REGISTRO DE EVENTOS (TRACE) (RF 3.2) ---
                print(f"[TIME: {self.global_clock}] P{self.current_process.id} ejecutado por {time_slice}T. T_Restante: {self.current_process.remaining_burst_time}")
                
                # --- 5. MANEJO DE ESTADOS FINALES Y PREEMPTION (RF 2.4) ---
                
                if self.current_process.remaining_burst_time == 0:
                    # Proceso terminado (CA 3.2)
                    self.current_process.current_state = "TERMINADO"
                    self.current_process.completion_time = self.global_clock # Necesario para P5/Diego
                    print(f"[TIME: {self.global_clock}] P{self.current_process.id} pasa a TERMINADO.")
                    self.current_process = None 
                
                elif self.rr_scheduler.necesita_preemption(self.current_process, time_slice):
                    # P3 (Isaac) decidio preemption, P2 (Joshua) lo reencola
                    self.ready_queue_manager.reencolar_proceso(self.current_process) 
                    print(f"[TIME: {self.global_clock}] P{self.current_process.id} preemptado, reencolado por P2.")
                    self.current_process = None 

            else:
                # CPU inactiva
                self.global_clock += 1
                # print(f"[TIME: {self.global_clock}] CPU Inactiva... Esperando procesos.")
        
        # Al finalizar, se llama al reporte de P5/Diego (RF 3.3)
        print("\n--- SIMULACION FINALIZADA ---")
        calcular_metricas_finales(self.all_processes)

if __name__ == "__main__":
    sim = NanoOSimulator(quantum=2) 
    sim.run_simulation()