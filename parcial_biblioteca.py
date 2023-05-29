import json
import re

def leer_archivo(nombre_archivo:str) ->list:
    """
    Lee el archivo con el nombre pasado por parametro
    
    :param nombre_archivo: Nombre del archivo
    :return: La lista del archivo
    """
    lista= []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]

    return lista

def imprimir_dato(dato:str):
    """
    Imprime el dato pasado por parametro

    :param dato: Recibe un dato
    :return: No retorna
    """
    print(dato)


"""
1. Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
"""

def mostrar_jugadores(lista_jugadores:list):

    """
    Muestra el nombre y posicion de los jugadores de la lista
    
    :param lista_jugadores: Lista de jugadores
    :return: No retorna
    """

    for jugadores in lista_jugadores:
        print("{0} - {1}".format(jugadores["nombre"],jugadores["posicion"]))


"""
2. Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido,
rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo,
porcentaje de tiros libres y porcentaje de tiros triples.
"""

def mostrar_estadisticas_jugador(lista_jugadores:list, indice_ingresado:int):

    """
    Muestra las estadisticas del jugador con el indice pasado por parametro
    
    :param lista_jugadores: Lista de jugadores
    :param indice_ingresado: Indice ingresado por el usuario
    :return: No retorna
    """

    if indice_ingresado < 0 or indice_ingresado > len(lista_jugadores):
        dato = ("El indice ingresado no está en la lista, elija otro")
    else:   
        dato = ("Estadisticas de {0}: \nTemporadas: {1} \nPuntos_totales: {2} \nPromedio_puntos_por_partido: {3} \nRebotes_totales: {4} \
               \nPromedio_rebotes_por_partido: {5} \nAsistencias_totales: {6} \nPromedio_asistencias_por_partido: {7} \nRobos_totales: {8} \nBloqueos_totales: {9} \
              \nPorcentaje_tiros_de_campo: {10} \nPorcentaje_tiros_libres: {11} \nPorcentaje_tiros_triples: {12}".format(lista_jugadores[indice_ingresado]["nombre"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["temporadas"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["puntos_totales"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["promedio_puntos_por_partido"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["rebotes_totales"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["promedio_rebotes_por_partido"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["asistencias_totales"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["promedio_asistencias_por_partido"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["robos_totales"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["bloqueos_totales"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["porcentaje_tiros_de_campo"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["porcentaje_tiros_libres"],
                                                                                                                        lista_jugadores[indice_ingresado]["estadisticas"]["porcentaje_tiros_triples"]))

    imprimir_dato(dato)

"""
3. Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.
El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, 
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
"""

def guardar_archivo(nombre_archivo:str, contenido_archivo:str):
    
    """
    Guarda un archivo con el nombre y el contenido pasados por parametro

    :param nombre_archivo: Nombre de un archivo
    :param contenido_archivo: Contenido del archivo a escribir
    :return: No retorna
    """
    estadisticas_keys = contenido_archivo["estadisticas"].keys()

    encabezados = "Nombre,\tPosicion,\t" + ",\t".join(estadisticas_keys)
    with open(nombre_archivo, 'w+') as archivo:
        archivo.writelines("{0}\n{1},\t{2},\t{3},\t{4},\t{5},\t{6},\t{7},\t{8},\t{9},\t{10},\t{11},\t{12},\t{13},\t{14} \n".format(encabezados,
                                                                                              contenido_archivo["nombre"], 
                                                                                              contenido_archivo["posicion"], 
                                                                                              contenido_archivo["estadisticas"]["temporadas"],
                                                                                              contenido_archivo["estadisticas"]["puntos_totales"],
                                                                                              contenido_archivo["estadisticas"]["promedio_puntos_por_partido"],
                                                                                              contenido_archivo["estadisticas"]["rebotes_totales"],
                                                                                              contenido_archivo["estadisticas"]["promedio_rebotes_por_partido"],
                                                                                              contenido_archivo["estadisticas"]["asistencias_totales"],
                                                                                              contenido_archivo["estadisticas"]["promedio_asistencias_por_partido"],
                                                                                              contenido_archivo["estadisticas"]["robos_totales"],
                                                                                              contenido_archivo["estadisticas"]["bloqueos_totales"],
                                                                                              contenido_archivo["estadisticas"]["porcentaje_tiros_de_campo"],
                                                                                              contenido_archivo["estadisticas"]["porcentaje_tiros_libres"],
                                                                                              contenido_archivo["estadisticas"]["porcentaje_tiros_triples"]))

"""
4. Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del 
Baloncesto, etc.
"""

def mostrar_logros_por_nombre(lista_jugadores:list,nombre_buscado:str):
    """
    Muestra los logros del nombre del jugador pasado por parametro

    :param lista_jugadores: Lista de jugadores
    :param nombre_buscado: Contenido del archivo a escribir
    :return: No retorna
    """
    for jugador in lista_jugadores:
        if re.search(nombre_buscado, jugador["nombre"]):
                logros = "\n".join(jugador["logros"])
                print("\nLos logros de {0} son:\n{1}".format(jugador["nombre"],logros))
    

"""
5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
"""
def calcular_por_key_ordenado(lista_jugadores:list, key:str):

    """
    Muestra el valor de la clave pasada por parametro ordenada por nombre de manera ascendente

    :param lista_jugadores: Lista de jugadores
    :param key: Clave que se va a mostrar
    :return: No retorna
    """

    lista_ordenada = ordenar_jugadores_por_nombre(lista_jugadores)
    for jugador in lista_ordenada:
        print("{0} - {1}".format(jugador["nombre"],jugador["estadisticas"][key]))


def ordenar_jugadores_por_nombre(lista_jugadores:list) -> list:

    """
    Ordena por nombre de manera ascendente en una copia de la lista

    :param lista_jugadores: Lista de jugadores
    :return: Retorna la copia de la lista ordenada
    """

    lista_copia = lista_jugadores[:]
    rango_a = len(lista_copia)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if lista_copia[indice_A]["nombre"] > lista_copia[indice_A+1]["nombre"]:
                lista_copia[indice_A],lista_copia[indice_A+1] = lista_copia[indice_A+1],lista_copia[indice_A]
                flag_swap = True
    return lista_copia

"""
6. Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la 
Fama del Baloncesto.
"""

def miembro_salon_fama_baloncesto(lista_jugadores:list):

    """
    Muestra si el nombre del jugador ingresado es miembro del Salón de la Fama del Baloncesto

    :param lista_jugadores: Lista de jugadores
    :return: No retorna
    """


    nombre_ingresado = input("Ingrese el nombre del jugador a buscar: ")

    es_miembro = False  

    for jugador in lista_jugadores:
        if re.search(nombre_ingresado, jugador["nombre"]):
            nombre_jugador = jugador["nombre"]
            for logros in jugador["logros"]:

                if logros == "Miembro del Salon de la Fama del Baloncesto":
                    es_miembro = True
        
    if es_miembro:    
        dato = "{0} es miembro del Salón de la Fama del Baloncesto".format(nombre_jugador)
    else:
        dato = "{0} no es miembro del Salón de la Fama del Baloncesto".format(nombre_jugador)

    imprimir_dato(dato)                


"""
7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.

8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.

9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.

13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.

14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.

19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.
"""

def jugador_mayor_cantidad(lista_jugadores:list, key:str):

    """
    Muestra el jugador con mayor cantidad o porcentaje de la key pasada por parametro

    :param lista_jugadores: Lista de jugadores
    :param key: Clave por la que se calculara el jugador
    :return: No retorna
    """

    jugador_mayor = lista_jugadores[0]["estadisticas"][key]
    jugador_mayor_nombre = lista_jugadores[0]["nombre"]

    for jugador in lista_jugadores:
        jugador_key = jugador["estadisticas"][key]
        if jugador_key > jugador_mayor:
            jugador_mayor = jugador_key
            jugador_mayor_nombre = jugador["nombre"]

    key_separada = key.split("_")

    if len(key_separada) == 1:
        dato = "El jugador con mayor cantidad de {0} es {1}".format(key_separada[0],jugador_mayor_nombre)
    elif len(key_separada) == 2:
        dato = "El jugador con mayor cantidad de {0} {1} es {2}".format(key_separada[0],key_separada[1],jugador_mayor_nombre)
    else:
        dato = "El jugador con mayor cantidad de {0} {1} {2} {3} es {4}".format(key_separada[0],key_separada[1],key_separada[2],key_separada[3],jugador_mayor_nombre)

    imprimir_dato(dato)


"""
10. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que 
ese valor.

11. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que 
ese valor.

12. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido 
que ese valor.

15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres 
superior a ese valor.

18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros 
triples superior a ese valor.
"""

def jugador_mayor_valor(lista_jugadores:list, key:str, valor:int):

    """
    Muestra el o los jugadores que promediaron o han tenido mas que el valor que ingresa el usuario segun la key

    :param lista_jugadores: Lista de jugadores
    :param key: Clave por la que se calculara el o los jugadores
    :param valor: Valor que ingresa el usuario
    :return: No retorna
    """

    jugadores_mayor_valor = []

    for jugador in lista_jugadores:
        jugador_key = jugador["estadisticas"][key]
        jugador_nombre = jugador["nombre"]
        if jugador_key > valor:
            jugadores_mayor_valor.append(jugador_nombre)

    if len(jugadores_mayor_valor) > 1:     
        dato = ("Los jugadores con {0} mayor a {1} son: {2}".format(key,valor,jugadores_mayor_valor))
    elif len(jugadores_mayor_valor) == 1:
        dato = ("El jugador con {0} mayor a {1} es: {2}".format(key,valor,jugadores_mayor_valor))
    else:
        dato = ("No hay jugadores con {0} mayor a {1}".format(key,valor,jugadores_mayor_valor))

    imprimir_dato(dato)

"""
16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de 
puntos por partido.
"""

def promedio_puntos_excluyendo_jugador_menor(lista_jugadores:list,key:str):

    """
    Muestra el promedio de puntos por partido excluyendo al jugador con la menor cantidad de puntos por partido

    :param lista_jugadores: Lista de jugadores
    :param key: Clave por la que se calculara el jugador
    :return: No retorna
    """

    lista_copia = lista_jugadores[:]
    jugador_menor = lista_copia[0]["estadisticas"][key]
    acum_puntos = 0


    for jugador in lista_copia:
        jugador_key = jugador["estadisticas"][key]

        if jugador_key < jugador_menor:
            jugador_menor = jugador_key


    for jugador in lista_copia:
        if jugador != jugador_menor:
            acum_puntos += jugador["estadisticas"][key]

    promedio_puntos = acum_puntos / len(lista_copia)

    print("El promedio de puntos por partido del equipo excluyendo al jugador con menor cantidad de puntos es {0}\n".format(promedio_puntos))

"""
17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.
"""

def jugador_mayor_cantidad_logros(lista_jugadores:list, key:str):
    
    """
    Muestra el jugador con la mayor cantidad de logros obtenidos

    :param lista_jugadores: Lista de jugadores
    :param key: Clave por la que se calculara el jugador
    :return: No retorna
    """

    jugador_mayor = len(lista_jugadores[0][key])
    jugador_mayor_nombre = lista_jugadores[0]["nombre"]

    for jugador in lista_jugadores:
        jugador_key = len(jugador[key])
        if jugador_key > jugador_mayor:
            jugador_mayor = jugador_key
            jugador_mayor_nombre = jugador["nombre"]
   
    print("El jugador con mayor cantidad de logros es {0}".format(jugador_mayor_nombre))

"""
20. Permitir al usuario ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que 
hayan tenido un porcentaje de tiros de campo superior a ese valor.
"""
def ordenar_por_posicion(lista_jugadores:list) -> list:

    """
    Ordena una copia de la lista por posicion

    :param lista_jugadores: Lista de jugadores
    :return: Retorna la copia de la lista
    """

    lista_copia = lista_jugadores[:]
    rango_a = len(lista_copia)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if lista_copia[indice_A]["posicion"] > lista_copia[indice_A+1]["posicion"]:
                lista_copia[indice_A],lista_copia[indice_A+1] = lista_copia[indice_A+1],lista_copia[indice_A]
                flag_swap = True
    return lista_copia


def menu():
    """
    Muestra el menú y le pide al usuario una opcion
    
    :param: No se le pasan parametros
    :return: No retorna
    """
    
    flag_case_2 = "No entro al case 2"

    lista_jugadores = leer_archivo("C:/Users/USURIO/OneDrive/Documentos/Programacion_I/dt.json")
    if len(lista_jugadores) > 0:
        while True:
            
            respuesta_str = input("1. Mostrar todos los jugadores del Dream Team\n"
                                  "2. Mostrar estadisticas del jugador del Dream Team segun su indice\n"
                                  "3. Guardar estadisticas del jugador en un archivo\n"
                                  "4. Buscar jugador por nombre y mostrar sus logros\n"
                                  "5. Mostrar el promedio de puntos por partido de todo el equipo ordenado por nombre de manera ascendente\n"
                                  "6. Ingresar nombre de jugador y mostrar si es miembro del Salón de la Fama del Baloncesto\n"
                                  "7. Mostrar jugador con mayor cantidad o porcentaje de...\n"
                                  "8. Mostrar jugadores que han promediado o tenido mas... que el valor ingresado\n"
                                  "9. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad\n")

            respuesta_int = int(respuesta_str)

            match(respuesta_int):
                case 1:
                    mostrar_jugadores(lista_jugadores)
                case 2:
                    indice = input("Ingrese indice del jugador a buscar: ")
                    indice_int = int(indice)
                    mostrar_estadisticas_jugador(lista_jugadores,indice_int)
                    if indice_int < len(lista_jugadores):
                        flag_case_2 = indice_int
                case 3:
                    if flag_case_2 != "No entro al case 2":
                        ruta_final = "estadisticas_de_{0}.csv".format(lista_jugadores[flag_case_2]["nombre"])
                        guardar_archivo(ruta_final, lista_jugadores[flag_case_2])
                    else:
                        print("Primero debe entrar a la 2da opción")
                case 4:
                    nombre_jugador = input("Ingrese nombre del jugador a buscar: ")
                    mostrar_logros_por_nombre(lista_jugadores,nombre_jugador)
                case 5:
                    calcular_por_key_ordenado(lista_jugadores,"promedio_puntos_por_partido")
                case 6:
                    miembro_salon_fama_baloncesto(lista_jugadores)    
                case 7:
                    respuesta_str = input("1. Mostrar jugador con mayor cantidad de rebotes totales\n"
                                          "2. Mostrar el jugador con el mayor porcentaje de tiros de campo\n"
                                          "3. Mostrar el jugador con la mayor cantidad de asistencias totales\n"
                                          "4. Mostrar el jugador con la mayor cantidad de robos totales\n"
                                          "5. Mostrar el jugador con la mayor cantidad de bloqueos totales\n"
                                          "6. Mostrar el jugador con la mayor cantidad de temporadas jugadas\n"
                                          "7. Mostrar el jugador con la mayor cantidad de logros\n")
                    respuesta_int = int(respuesta_str)
                    
                    match(respuesta_int):
                        case 1:
                            jugador_mayor_cantidad(lista_jugadores,"rebotes_totales")
                        case 2:
                            jugador_mayor_cantidad(lista_jugadores,"porcentaje_tiros_de_campo")
                        case 3:
                            jugador_mayor_cantidad(lista_jugadores,"asistencias_totales")
                        case 4:   
                            jugador_mayor_cantidad(lista_jugadores,"robos_totales")
                        case 5:    
                            jugador_mayor_cantidad(lista_jugadores,"bloqueos_totales")
                        case 6:    
                            jugador_mayor_cantidad(lista_jugadores,"temporadas")
                        case 7:
                            jugador_mayor_cantidad_logros(lista_jugadores, "logros")
                            

                case 8:
        
                    respuesta_str = input("1. Mostrar los jugadores que han promediado más puntos por partido que el valor ingresado\n"
                                          "2. Mostrar los jugadores que han promediado más rebotes por partido que el valor ingresado\n"
                                          "3. Mostrar los jugadores que han promediado más asistencias por partido que el valor ingresado\n"
                                          "4. Mostrar los jugadores que han promediado más porcentaje de tiros triples por partido que el valor ingresado\n"
                                          "5. Mostrar los jugadores que han promediado más porcentaje de tiros libres por partido que el valor ingresado\n"
                                          "6. Mostrar los jugadores, ordenados por posición en la cancha, que han tenido más porcentaje de tiros de campo que el valor ingresado\n")
                    respuesta_int = int(respuesta_str)
                    
                    valor_str = input("Ingrese un valor\n")
                    valor_int = int(valor_str)
                    
                    match(respuesta_int):
                        case 1:
                            jugador_mayor_valor(lista_jugadores, "promedio_puntos_por_partido", valor_int)
                        case 2:
                            jugador_mayor_valor(lista_jugadores, "promedio_rebotes_por_partido", valor_int)
                        case 3:
                            jugador_mayor_valor(lista_jugadores, "promedio_asistencias_por_partido", valor_int)
                        case 4:   
                            jugador_mayor_valor(lista_jugadores, "porcentaje_tiros_triples", valor_int)
                        case 5:    
                            jugador_mayor_valor(lista_jugadores, "porcentaje_tiros_libres", valor_int)
                        case 6:
                            lista_ordenada = ordenar_por_posicion(lista_jugadores)
                            jugador_mayor_valor(lista_ordenada,"porcentaje_tiros_de_campo", valor_int)            
                case 9:
                    promedio_puntos_excluyendo_jugador_menor(lista_jugadores, "promedio_puntos_por_partido")
    else:
        print("La lista está vacia")