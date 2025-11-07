import time as tm
import random as rm

class Proceso: 
    
    def __init__(self, id, arrival_time, initial_burst_time, remaining_burst_time):
        ESTADOS = ['ESPERA','EN_PROCESO','DETENIDO','COMPLETADO','CANCELADO']
        self.id = id
        self.arrival_time = arrival_time
        self. initial_burst_time = initial_burst_time
        self.remaining_burst_time = remaining_burst_time

        self.estado = ESTADOS[0]

    def asignacion_procesos(self):
        tiempo_inicio = tm.time()
        tm.sleep(rm.randint(0, 5))
        tiempo_terminado = tm.time()
        tiempo_tardado = tiempo_terminado - tiempo_inicio
        return f"id del proceso : {self.id}, tiempo de completacion : {self.arrival_time}, tiempo_tardado : {tiempo_tardado:.2f}"
        pass
        
    

proceso1 = Proceso(3, 40, 30, 10)


print(proceso1.asignacion_procesos())

