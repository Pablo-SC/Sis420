import random
import math

numero_genes = 9  # La longitud del material genetico de cada individuo
tamano_poblacion = 500  # La cantidad de individuos que habra en la poblacion
precision = 5  # Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
probabilidad_mutacion = 0.4  # La probabilidad de que un individuo mute
valor_minimo_gen = 1
valor_maximo_gen = 9

# Crea un individuo
def crear_individuo(min, max):
    return [random.randint(min, max) for i in range(numero_genes)]


# Crea una poblacion nueva de individuos
def crear_poblacion(numero_individuos):
    return [crear_individuo(valor_minimo_gen, valor_maximo_gen) for i in range(numero_individuos)]

# def calcular_fitness(individuo):
#     # Calcula el fitness de un individuo concreto.
#     # F(x) = 2*x1 + 5*x2^2 - x3 + x4 - 8 * x5 - 10
#     # print(individuo)
#     Fx = abs(2 * individuo[0] + 5 * individuo[1]**2 -
#              individuo[2] + individuo[3] - 8 * individuo[4] - 10)
#     Fx = individuo[0]

#     return Fx

def calcular_fitness(individuo):
    total_distance = 0
    for i in range(1, numero_genes):
        distance = abs(individuo[i] - individuo[i - 1])
        total_distance += distance
    return total_distance 



# funcion empleada para ordenar la poblacion
def ordenar_por_segundo_elemento(elem):
    return elem[1]

poblacion = crear_poblacion(tamano_poblacion)
poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)
poblacion = [i[0] for i in poblacion_ordenada]

for ind in poblacion_ordenada:
    print(f"individuo: {ind[0]} fitness: {ind[1]}")

print("**"*3)
print("**"*3)

for ind in poblacion:
    print(f"individuo: {ind} fitness: {calcular_fitness(ind)}")


def seleccion_y_reproduccion(poblacion):
    # Puntua todos los elementos de la poblacion (population) y se queda con los mejores guardandolos dentro de 'seleccionados'.
    # Despues mezcla el material genetico de los elegidos para crear nuevos individuos y llenar la poblacion
    # (guardando tambien una copia de los individuos seleccionados sin modificar).
    # Por ultimo se aplica la mutacion a los individuos.
    # Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    poblacion_evaluada = [(indiv, calcular_fitness(indiv)) for indiv in poblacion]
    # Ordena los pares ordenados y se queda solo con el array de valores
    poblacion_ordenada = [indiv[0] for indiv in sorted(
        poblacion_evaluada, key=ordenar_por_segundo_elemento)]

    poblacion = poblacion_ordenada
    # poblacion_seleccionada = poblacion_ordenada[(len(poblacion_ordenada) - precision):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
    # Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
    poblacion_seleccionada = poblacion_ordenada[precision:]
    # Se mezcla el material genetico para crear nuevos individuos
    for i in range(precision, len(poblacion)):
        # Se elige un punto para hacer el intercambio
        punto_cruce = random.randint(1, numero_genes - 1)
        padre = random.sample(poblacion_seleccionada,2)  # Se eligen dos padres
        # Se mezcla el material genetico de los padres en cada nuevo individuo
        poblacion[i][:punto_cruce] = padre[0][:punto_cruce]
        poblacion[i][punto_cruce:] = padre[1][punto_cruce:]

    # El array 'poblacion' tiene ahora una nueva poblacion de individuos, que se devuelven
    return poblacion


poblacion = crear_poblacion(tamano_poblacion)
poblacion = seleccion_y_reproduccion(poblacion)
poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion]
poblacion_ordenada = sorted(
poblacion_evaluada, key=ordenar_por_segundo_elemento)
poblacion = [i[0] for i in poblacion_ordenada]

for ind in poblacion_ordenada:
    print(f"individuo: {ind[0]} fitness: {ind[1]}")
