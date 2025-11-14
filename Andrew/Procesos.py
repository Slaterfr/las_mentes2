# Andrew/Procesos.py (RF 1.1, RF 1.2)
# Define la estructura base de datos que usara todo el proyecto.

# Se eliminan los imports time y random, no necesarios para la simulacion conceptual.

class Proceso:
    """
    RF 1.1: Estructura de datos para representar un proceso (PCB simulado).
    Los estados se ajustan a la definicion del proyecto (Nuevo, Listo, Ejecucion, Terminado).
    """
    # Estados requeridos por el proyecto (ej. Nuevo, Listo, Ejecucion, Terminado) 
    ESTADOS = ["NUEVO", "LISTO", "EJECUCION", "TERMINADO"] 
    
    # La firma solo necesita los 3 parametros iniciales. Remaining Burst se calcula dentro.
    def __init__(self, id_proceso, arrival_time, initial_burst_time):
        
        # Atributos esenciales (RF 1.1)
        self.id = id_proceso
        self.arrival_time = arrival_time
        self.initial_burst_time = initial_burst_time
        
        # RF 1.1: El Remaining Burst Time es igual al Initial Burst Time al inicio.
        self.remaining_burst_time = initial_burst_time
        
        # RF 1.1: Estado inicial (empezamos en NUEVO o LISTO segun el diseno de P2/Joshua)
        self.current_state = self.ESTADOS[0] # NUEVO
        
        # RF 3.3: Campos para el calculo de metricas (P5/Diego)
        self.completion_time = 0      
        self.turnaround_time = 0      
        self.waiting_time = 0         
    
    def __str__(self):
        return (f"P{self.id} (Estado: {self.current_state}, T_Restante: {self.remaining_burst_time})")

# Se elimina la funcion 'asignacion_procesos' ya que usa logica de tiempo real, no del simulador.

def inicializar_procesos():
    """
    RF 1.2: Crea y retorna la lista inicial de 5 procesos con datos de prueba (CA 1.1).
    """
    print("\n--- P1/Andrew: Inicializando 5 Procesos ---")
    procesos = [
        # Se usa la firma de 3 argumentos para la creacion
        Proceso(id_proceso=1, arrival_time=0, initial_burst_time=5),
        Proceso(id_proceso=2, arrival_time=1, initial_burst_time=3),
        Proceso(id_proceso=3, arrival_time=2, initial_burst_time=8),
        Proceso(id_proceso=4, arrival_time=3, initial_burst_time=6),
        Proceso(id_proceso=5, arrival_time=4, initial_burst_time=2),
    ]
    return procesos