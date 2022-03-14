#Copyright (C), 2022-2023, bl33h
#FileName: CPU (unico archivo)
#Author: Sara Echeverria
#Date: 11/03/2022
#Version:
    #Creacion: 09/03/2022
    #Ultima modificacion: 13/03/2022

# --- Librerias ---
import random as random;
import simpy as simp;

# --- Semilla ---
RandomSeed = 50; # Valor random de la semilla
Interval = 10; # Intervalo

# --- Proceso --- 
def process (name, env, memory, cpu, arrival, instructionsq, ramq): # Elementos que conforman a un proceso.
    # Simula la espera de llegada del proceso.
    yield env.timeout(arrival)

    # Graba el tiempo de llegada.
    arrivalTime = env.now

    print('%s Proceso en cola [NEW llegada] -> %d cantidad ram requerida %d, disponible %d' % (name, env.now, ramq, memory.level))
    yield memory.get(ramq)  # Solicita la memoria que necesita o espera automaticamente hasta que haya suficiente.

    while instructionsq > 0:  # Loop hasta que se acabe la cantidad de instrucciones pendientes.
        # Memoria inicial disponible
        print('%s proceso en cola READY tiempo -> %d cantidad instrucciones pendientes %d' % (name, env.now, instructionsq))

        with cpu.request() as req:  # Solicitud al procesador.
            yield req

            instructionsq = instructionsq - 3
            yield env.timeout(1) # Simulacion de un ciclo de reloj del procesador.

            # Existencia de un procesador.
            print('%s proceso en estado RUNNING fue atendido en tiempo -> %d cantidad ram %d, Instrucciones pendientes %d ram disponible %d' % (name, env.now, ramq, instructionsq, memory.level))

    # Retorna la memoria utilizada.
    yield memory.put(ramq)
    print('%s proceso TERMINATED salida -> %d cantidad ram devuelta %d, nueva cantidad de memoria disponible %d' % (name, env.now, ramq, memory.level))
    global totalTime
    totalTime += env.now - arrivalTime
    print('Tiempo total %d' % (env.now - arrivalTime)) # Tiempo total en base al arrivalTime.

    # --- Implementacion de la semilla ---
    random.seed(RandomSeed)
    env = simp.Environment()  # Se crea el ambiente de simulacion.
    initialRam = simp.Container(env, 30, init=30)  # Crea el contenedor de la ram.
    initialCpu = simp.Resource(env, capacity=1)  # Se crea el procesador con capacidad establecida.
    initialProcess = 50  # Cantidad de procesos a generar.
    totalTime = 0

    # --- Parametros de los procesos, instrucciones y el uso de la ram ---
    for i in range(initialProcess):
        arrival = 0 # Todos los procesos llegan al mismo tiempo.
        instructionsq = random.randint(1, 10)  # Cantidad de operaciones por proceso.
        ramUse = random.randint(1, 10)  # Cantidad de ram que requiere cada proceso.
        env.process(process('proceso %d' % i, env, initialRam, initialCpu, arrival, instructionsq, ramUse))

    # Se corre la simulacion.
    env.run()
    print('Tiempo promedio %d ' % (totalTime / initialProcess))


