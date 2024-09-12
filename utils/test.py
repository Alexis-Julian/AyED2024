def pr_crear_menu(titulo:str,x:list):
    os.system("cls")


    def fn_creador_devolucion(x):
        nuevo_array = [[None]*2 for _ in range(len(x))]
        for i in range(0,len(x)):
            nuevo_array[i][0] = x[i][0]
        return nuevo_array

    def fn_formateador_menu():
        nuevo_array = [[None]*2 for _ in range(len(x)+1)]
        for i in range(0,len(x)):  
            for k in range(0,2): 
                try:
                    nuevo_array[i][k]=x[i][k]
                except:
                    nuevo_array[i][k] = pr_cartel_construccion
        nuevo_array[-1][0] = "Salir"
        nuevo_array[-1][1] = print

        return nuevo_array

    x = fn_formateador_menu()
    e = fn_creador_devolucion(x)


    #NUNCA PUSE 4 
    a = -1
    while  a != len(x):  
        os.system("cls")
        pr_crear_titulo(titulo)
        for i in range(0,len(x)):
            print(f"\n{i+1}-{x[i][0]}")
        a = int(input("\nIngrese su opcion: "))
        e[a-1][1] = x[a-1][1]()     
        os.system("pause")
    return e

def pr_registrarse():
    opc = "2"

    while opc  != "5":
        prenda = input("vestirse: ")
        opc = input("Ingrese 5 para salir: ")

    return prenda

def pr_logearse():
  
    return "LEO"
# Crear un estudiante de prueba
estudiante_prueba = Estudiantes()

# Asignar valores a los atributos
estudiante_prueba.id_estudiantes = 1
estudiante_prueba.email = "estudiante.prueba@example.com"
estudiante_prueba.nombre = "Juan Pérez"
estudiante_prueba.sexo = "M"
estudiante_prueba.contrasena = "123456"
estudiante_prueba.estado = True
estudiante_prueba.hobbies = "Leer, programar, jugar fútbol"
estudiante_prueba.materia_favorita = "Matemáticas"
estudiante_prueba.deporte_favorito = "Fútbol"
estudiante_prueba.materia_fuerte = "Física"
estudiante_prueba.materia_debil = "Literatura"
estudiante_prueba.biografia = "Estudiante apasionado por la tecnología y los deportes."
estudiante_prueba.pais = "España"
estudiante_prueba.ciudad = "Madrid"
estudiante_prueba.fecha_nacimiento = "2002-01-15"

#fn_guardar_estudiante(estudiante_prueba)

