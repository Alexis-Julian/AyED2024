import os
import pickle

def cargar_likes(archivo_likes):
    """Carga los likes desde un archivo pickle o crea uno nuevo si no existe."""
    if not os.path.exists(archivo_likes):
        print(f"El archivo '{archivo_likes}' no existe. Se creará uno nuevo.")
        return []
    else:
        archivo = open(archivo_likes, 'rb')
        datos_likes = pickle.load(archivo)
        archivo.close()
        return datos_likes

def guardar_likes(archivo_likes, datos_likes):
    """Guarda los likes en un archivo pickle."""
    archivo = open(archivo_likes, 'wb')
    pickle.dump(datos_likes, archivo)
    archivo.close()

def dar_like(datos_likes, usuario_id, otro_usuario_id, tipo_like):
    """Agrega un like con ID generado automáticamente sin usar 'append'."""
    if datos_likes:
        max_id = max(like['id'] for like in datos_likes)
    else:
        max_id = 0
    nuevo_id = max_id + 1

    nuevo_like = {
        'id': nuevo_id,
        'usuario_id': usuario_id,
        'otro_usuario_id': otro_usuario_id,
        'tipo_like': tipo_like
    }
    # Agregar el nuevo like sin usar 'append'
    datos_likes = datos_likes + [nuevo_like]
    return datos_likes

def inicializar_candidatos(datos_likes):
    """Inicializa el diccionario de candidatos sin usar 'append' ni 'set'."""
    candidatos = {}
    for like in datos_likes:
        usuario_id = like['usuario_id']
        otro_usuario_id = like['otro_usuario_id']
        tipo_like = like['tipo_like']

        if usuario_id not in candidatos:
            candidatos[usuario_id] = {
                'likes_dados': [],
                'likes_recibidos': []
            }

        if tipo_like == 'dado':
            # Agregar sin 'append'
            candidatos[usuario_id]['likes_dados'] = candidatos[usuario_id]['likes_dados'] + [otro_usuario_id]
        elif tipo_like == 'recibido':
            # Verificar si no está en la lista y agregar sin 'append'
            if otro_usuario_id not in candidatos[usuario_id]['likes_recibidos']:
                candidatos[usuario_id]['likes_recibidos'] = candidatos[usuario_id]['likes_recibidos'] + [otro_usuario_id]

    return candidatos

def calcular_puntajes(candidatos):
    """Calcula los puntajes y rachas de los candidatos."""
    candidatos_puntuados = []
    for usuario_id, datos in candidatos.items():
        racha = 0
        puntaje = 0

        # Procesamos los likes dados
        for otro_usuario_id in datos['likes_dados']:
            if otro_usuario_id in datos['likes_recibidos']:
                puntaje += 1
                racha += 1
                if racha >= 3:
                    puntaje += 1  # Punto extra por racha mantenida
            else:
                puntaje -= 1
                racha = 0  # Reiniciar racha

        # Agregar los datos sin 'append'
        candidatos_puntuados = candidatos_puntuados + [(usuario_id, {'puntaje': puntaje, 'racha': racha})]

    return candidatos_puntuados

def obtener_puntaje(candidato):
    """Función para obtener el puntaje de un candidato."""
    return candidato[1]['puntaje']

def generar_listado(candidatos_puntuados):
    """Genera el listado de candidatos ordenado por puntaje."""
    # Usamos un algoritmo simple de ordenamiento (burbuja)
    n = len(candidatos_puntuados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if obtener_puntaje(candidatos_puntuados[j]) < obtener_puntaje(candidatos_puntuados[j + 1]):
                # Intercambiar posiciones si no están en el orden correcto
                candidatos_puntuados[j], candidatos_puntuados[j + 1] = candidatos_puntuados[j + 1], candidatos_puntuados[j]
    return candidatos_puntuados

def procesar_likes(archivo_likes):
    """Función principal para procesar los likes y generar el listado de candidatos."""
    datos_likes = cargar_likes(archivo_likes)
    if not datos_likes:
        return []

    candidatos = inicializar_candidatos(datos_likes)
    candidatos_puntuados = calcular_puntajes(candidatos)
    listado_candidatos = generar_listado(candidatos_puntuados)
    return listado_candidatos

def menu():
    archivo_likes = 'likes.pkl'
    datos_likes = cargar_likes(archivo_likes)

    running = True
    while running:
        print("\nMenú:")
        print("1. Dar like")
        print("2. Mostrar listado de candidatos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            input_invalid = True
            while input_invalid:
                try:
                    usuario_id = int(input("Ingrese su ID de usuario: "))
                    otro_usuario_id = int(input("Ingrese el ID del usuario al que quiere dar like: "))
                    input_invalid = False
                except ValueError:
                    print("Por favor, ingrese un número válido para los IDs.")

            tipo_like = 'dado'

            # Agregar el like dado sin 'append'
            datos_likes = dar_like(datos_likes, usuario_id, otro_usuario_id, tipo_like)
            print(f"Like dado de Usuario {usuario_id} a Usuario {otro_usuario_id}")

            # Preguntar si el otro usuario correspondió el like
            correspondido = input(f"¿El Usuario {otro_usuario_id} correspondió el like? (s/n): ")
            if correspondido.lower() == 's':  # Se permite el uso de .lower()
                # Agregar el like recibido sin 'append'
                datos_likes = dar_like(datos_likes, otro_usuario_id, usuario_id, 'recibido')
                print(f"Like recibido de Usuario {otro_usuario_id} a Usuario {usuario_id}")

            # Guardar los likes actualizados
            guardar_likes(archivo_likes, datos_likes)

        elif opcion == '2':
            listado = procesar_likes(archivo_likes)
            if listado:
                print("\nListado de candidatos según su puntaje:")
                for usuario_id, datos in listado:
                    print(f"Usuario ID: {usuario_id}, Puntaje: {datos['puntaje']}, Racha: {datos['racha']}")
            else:
                print("No hay datos para mostrar.")

        elif opcion == '3':
            print("Saliendo del programa.")
            running = False

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    menu()
