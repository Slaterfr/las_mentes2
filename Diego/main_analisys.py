# Diego/main_analisys.py (RF 3.3, HU Opcional 5)
# Se encarga del calculo de metricas y el reporte final.

from Andrew.Procesos import Proceso

def calcular_metricas_finales(all_processes):
    """
    RF 3.3: Calcula y presenta el Tiempo de Espera y Retorno para todos los procesos.
    """
    total_turnaround = 0
    total_waiting = 0
    
    print("\n--- P5: Calculo de Metricas Finales (RF 3.3) ---")
    print("ID | T_Llegada | T_Rafaga | T_Finalizacion | T_Retorno | T_Espera")
    print("-" * 75)
    
    for p in all_processes:
        # Calcular T_Retorno (Turnaround Time)
        p.turnaround_time = p.completion_time - p.arrival_time
        
        # Calcular T_Espera (Waiting Time)
        p.waiting_time = p.turnaround_time - p.initial_burst_time
        
        total_turnaround += p.turnaround_time
        total_waiting += p.waiting_time
        
        print(f"P{p.id:2} | {p.arrival_time:9} | {p.initial_burst_time:8} | {p.completion_time:14} | {p.turnaround_time:9} | {p.waiting_time:8}")

    num_procesos = len(all_processes)
    avg_turnaround = total_turnaround / num_procesos
    avg_waiting = total_waiting / num_procesos
    
    print("\n--- PROMEDIOS ---")
    print(f"Tiempo Promedio de Retorno (Average Turnaround Time): {avg_turnaround:.2f}")
    print(f"Tiempo Promedio de Espera (Average Waiting Time): {avg_waiting:.2f}")


# Placeholder para el Bono (HU Opcional 5)
def simular_sincronizacion_basica():
    """
    Implementar la logica opcional de un mutex simulado.
    """
    pass # Logica a implementar por Diego si se busca el bono.