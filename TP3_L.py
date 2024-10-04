import os
import pickle
import io
from getpass import getpass

#--------------------------------------------------------------#
#                                                              #
#                CLASES                                        #
#                                                              #
#--------------------------------------------------------------#

class Estudiante:
    def __init__(self):
        self.id_estudiantes= 0
        self.email= ""
        self.nombre=""
        self.sexo =""
        self.contrasena=""
        self.hobbies=""
        self.biografia=""
        self.fecha_nacimiento=""
        self.estado = False

class Moderador:
    def __init__(self):
        self.id_moderador=0
        self.email=""
        self.contrasena=""
        self.estado=bool
        self.nombre=""

class Administrador:
    def __init__(self):
        self.id_admin=0
        self.email=""
        self.contrasena=""

class Like:
    def __init__(self):
        self.remitente=0
        self.destinatario=0

class Reporte:
    def __init__(self):
        self.id_reportante=0
        self.id_reportado=0
        self.razon_reporte=""
        self.estado= 0
        
#--------------------------------------------------------------#
#                                                              #
#                       DATOS PRECARGA                         #
#                                                              #
#--------------------------------------------------------------#

INIT_ADMINISTRADORES = [[0, "admin@ayed.com", "123"]]
INIT_ESTUDIANTES = [
    [0, "lautaro@ayed.com", "Lautaro", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True], 
    [1, "alexis@ayed.com", "Alexis", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True], 
    [2, "nestor@ayed.com", "Nestor", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True], 
    [3, "leonel@ayed.com", "Leonel", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True],
    [4, "jorge@ayed.com", "Jorge", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True],
    [5, "matias@ayed.com", "Matias", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True],
    [6, "micaela@ayed.com", "Micaela", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True],
    [7, "agustin@ayed.com", "Agustin", "M", "123", "Futbol", "Futuro ingeniero", "11/06/1999", True]]
INIT_MODERADORES = [[0, "mod_lautaro@ayed.com", "123", True, "Lautaro"], [1, "mod_alexis@ayed.com", "123", True, "Alexis"]] 

INIT_REPORTES = [
    [0, 1, "Me molesta", 0],
    [3, 1, "No me paso la tarea", 0],
    [6, 0, "No me paso su instagram", 0],
    [7, 4, "Jorge trata mal a sus companeros", 0],
    ]

#--------------------------------------------------------------#
#                                                              #
#                       GLOBALES                               #
#                                                              #
#--------------------------------------------------------------#

MAX_INTENTOS = 3
INTENTO_LOGIN = 0
TIPO_LOGEADO = ""
REG_LOGEADO: io.BufferedRandom
POS_LOGEADA = -1

#--------------------------------------------------------------#
#                                                              #
#                ARCHIVOS                                      #
#                                                              #
#--------------------------------------------------------------#

def fn_crear_logico(ruta: str):
    archivo_logico:io.BufferedRandom  # Inicialización explícita
    
    if os.path.exists(ruta):
        archivo_logico = open(ruta, "r+b")  # Abre para lectura y escritura binaria
    else:
        archivo_logico = open(ruta, "w+b")  # Crea un archivo nuevo y lo abre en modo binario
    
    return archivo_logico

if(not(os.path.exists("archivos"))):
    os.mkdir(os.getcwd() + "/archivos")
    
if(os.path.exists("archivos")):
    #Archivo fiscos
    FISICO_ARCHIVO_ESTUDIANTES= os.getcwd() + "/archivos/estudiantes.dat" 
    FISICO_ARCHIVO_MODERADORES= os.getcwd() + "/archivos/moderadores.dat" 
    FISICO_ARCHIVO_REPORTES= os.getcwd() + "/archivos/reportes.dat"
    FISICO_ARCHIVO_LIKES= os.getcwd() + "/archivos/likes.dat"
    FISICO_ARCHIVO_ADMINISTRADORES= os.getcwd() + "/archivos/administradores.dat"

    LOGICO_ARCHIVO_ESTUDIANTES= fn_crear_logico(FISICO_ARCHIVO_ESTUDIANTES) 
    LOGICO_ARCHIVO_MODERADORES= fn_crear_logico(FISICO_ARCHIVO_MODERADORES) 
    LOGICO_ARCHIVO_REPORTES= fn_crear_logico(FISICO_ARCHIVO_REPORTES)
    LOGICO_ARCHIVO_LIKES= fn_crear_logico(FISICO_ARCHIVO_LIKES)
    LOGICO_ARCHIVO_ADMINISTRADORES= fn_crear_logico(FISICO_ARCHIVO_ADMINISTRADORES)

def fn_cerrar_logico():
    LOGICO_ARCHIVO_ESTUDIANTES.close()
    LOGICO_ARCHIVO_MODERADORES.close()
    LOGICO_ARCHIVO_REPORTES.close()
    LOGICO_ARCHIVO_LIKES.close()
    LOGICO_ARCHIVO_ADMINISTRADORES.close()
    
#--------------------------------------------------------------#
#                                                              #
#                FORMATEADORES                                 #
#                                                              #
#--------------------------------------------------------------#

def lj_estudiantes(x:Estudiante):
    x.id_estudiantes=str(x.id_estudiantes).ljust(10) # Entero
    x.email=str(x.email).ljust(32).lower()
    x.nombre=str(x.nombre).ljust(32)
    x.sexo=str(x.sexo).ljust(1).lower()
    x.contrasena=str(x.contrasena).ljust(32)
    x.estado=str(x.estado).ljust(10) #Booleano
    x.hobbies=str(x.hobbies).ljust(255)
    x.biografia=str(x.biografia).ljust(255)
    x.fecha_nacimiento=str(x.fecha_nacimiento).ljust(10)

def lj_moderadores(x:Moderador):
    x.id_moderador = str(x.id_moderador).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower()
    x.contrasena = str(x.contrasena).ljust(32).lower()
    x.estado = str(x.estado).ljust(10).lower() #Booleano
    x.nombre = str(x.nombre).ljust(32)

def lj_administradores(x:Administrador):
    x.id_admin = str(x.id_admin).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower() 
    x.contrasena = str(x.contrasena).ljust(32).lower()

def lj_likes(x:Like):
    x.destinatario=str(x.destinatario).ljust(10).lower() #Entero
    x.remitente=str(x.remitente).ljust(10).lower() #Entero

def lj_reportes(x:Reporte):
    x.id_reportante = str(x.id_reportante).ljust(10).lower() #Entero
    x.id_reportado = str(x.id_reportado).ljust(10).lower() #Entero
    x.razon_reporte = str(x.razon_reporte).ljust(255).lower() 
    x.estado = str(x.estado).ljust(10).lower() #Entero
    
#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES DE VALIDACION DE DATOS              #
#                                                              #
#--------------------------------------------------------------#
def fn_validar_si_int(text: str):
    opc = input(text)
    
    try:
        parsed = int(opc)
        return parsed
    
    except ValueError:
        print("Error. Solo se pueden seleccionar numeros.")
        fn_validar_si_int(text)

def fn_validar_si_no():
    respuesta=input("Ingrese si o no: ") 
    while (respuesta !="si") and  (respuesta !="no"):
        print("No es un opción valida, ingrese si o no")
        respuesta=input("Ingrese si o no: ")
    return respuesta #string

def fn_validar_rango(inicio:int, limite:int):
    try:
        numero =int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input("Ingrese una opción: "))
        return numero #int
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio, limite)

def fn_validar_rango_str(inicio: str, limite:str):
    opc = input("Ingrese una opcion:").lower()
    
    while not (inicio <= opc <= limite):
        print("\nError, ingrese una opcion valida.\n")
        opc = input("Ingrese una opcion:")
    
    return opc #str

def fn_validar_archivo_fisico(archivo_fisico: str):
    while not os.path.exists(archivo_fisico):
        print(f"El archivo '{archivo_fisico}' no existe.")
        archivo_fisico = input("Por favor, ingrese una nueva ruta de archivo: ")
    
    return archivo_fisico

#--------------------------------------------------------------#
#                                                              #
#               FUNCIONES GENERALES                            #
#                                                              #
#--------------------------------------------------------------#

def fn_guardar_datos(registro:object, ARCHIVO_LOGICO:io.BufferedRandom ,ARCHIVO_FISICO:str, formateador, posicion:int = -1):
    tam_archivo = os.path.getsize(fn_validar_archivo_fisico(ARCHIVO_FISICO))
    
    try:        
        if (posicion) == -1:
            posicion = tam_archivo

        ARCHIVO_LOGICO.seek(posicion, 0)
        formateador(registro) 
        pickle.dump(registro, ARCHIVO_LOGICO)
        ARCHIVO_LOGICO.flush()

    except:
        print("Se genero un error")

def fn_buscar_cantidad_de_registros(ARCHIVO_LOGICO:io.BufferedRandom,ARCHIVO_FISICO:str):
    cantidad = 0   
    if(os.path.getsize(ARCHIVO_FISICO) != 0):
        ARCHIVO_LOGICO.seek(0)
        pickle.load(ARCHIVO_LOGICO)
        longitud_reg = ARCHIVO_LOGICO.tell()
        t = os.path.getsize(ARCHIVO_FISICO) 
        
        cantidad = t//longitud_reg
    ARCHIVO_LOGICO.seek(0)
    return cantidad
        
def fn_busqueda_dicotomica(data:str, ARCHIVO_LOGICO:io.BufferedRandom, ARCHIVO_FISICO:str,funcion):
    ARCHIVO_LOGICO.seek(0, 0)
    registro = pickle.load(ARCHIVO_LOGICO)
    tamregi = ARCHIVO_LOGICO.tell()
    cantreg = int(os.path.getsize(ARCHIVO_FISICO) / tamregi)
    inicio = 0                 
    fin = cantreg-1
    medio = (inicio + fin) // 2
    ARCHIVO_LOGICO.seek(medio * tamregi,0) 
    registro = pickle.load(ARCHIVO_LOGICO)

    while inicio <  fin and str(funcion(registro)).strip() != str(data).strip() :

        if str((funcion(registro))).strip()  < str(data).strip():
            fin = medio - 1
        else:
            inicio = medio + 1            
        
        medio = (inicio + fin) // 2
        ARCHIVO_LOGICO.seek(medio * tamregi,0)  #tamregi   
        registro = pickle.load(ARCHIVO_LOGICO)
    if(int(funcion(registro) == data)):
        return medio*tamregi
    else:
        return -1

def fn_busqueda_secuencial(
    ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str, callback
) :
    """ def busqueeda_especifica(regtemp,pos):
        if str(regtemp.propiedad).strip() == 'valor':
            localesActivos.append(regtemp)         
            return False """

    tamañoarchivo = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    encontrado = False

    while ARCHIVO_LOGICO.tell() < tamañoarchivo and encontrado == False:
        posicion = ARCHIVO_LOGICO.tell()
        regtemporal = pickle.load(ARCHIVO_LOGICO)
        encontrado = callback(regtemporal, posicion)

    return encontrado

def fn_validar_usuario(archivo_logico: io.BufferedRandom, archivo_fisico: str, email: str, password: str):
    tam_registro = os.path.getsize(archivo_fisico)
    
    archivo_logico.seek(0)
    
    encontrado = -1
    
    while archivo_logico.tell() < tam_registro and encontrado == -1:
        posicion_actual = archivo_logico.tell()
        registro:Estudiante | Administrador | Moderador = pickle.load(archivo_logico)
        
        email_encontrado = registro.email.strip()
        password_encontrada = registro.contrasena.strip()
        
        if email_encontrado == email and password_encontrada == password:
            if hasattr(registro, 'estado'):
                estado_normalizado = registro.estado.strip()
                
                if estado_normalizado == "true":
                    encontrado = posicion_actual
            else:
                encontrado = posicion_actual
                    
    return encontrado

def fn_busqueda_secu(archivo_logico: io.BufferedRandom, archivo_fisico: str, nombre: str, id: int, email: str):
    tam_archivo = os.path.getsize(archivo_fisico)
    archivo_logico.seek(0)
    
    encontrado = -1
    
    while archivo_logico.tell() < tam_archivo and encontrado == -1:
        posicion_actual = archivo_logico.tell()
        registro: Estudiante | Moderador = pickle.load(archivo_logico)
        
        nombre_formateado = registro.nombre.strip()
        email_formateado = registro.email.strip()
        id_formateado = ""
        
        if hasattr(registro, "id_estudiantes"):
            id_formateado = registro.id_estudiantes.strip()
        else:
            id_formateado = registro.id_moderador.strip()
        
        if nombre_formateado.lower() == nombre.lower() or int(id_formateado) == id or email_formateado == email:
            encontrado = posicion_actual
    
    return encontrado
        
    
#--------------------------------------------------------------#
#                                                              #
#               PROCEDURES/FUNCIONES AUXILIARES                #
#                                                              #
#--------------------------------------------------------------#

def fn_text_center(data,space):
    mid = (space- len(data)) / 2
    parte_decimal = mid - int(mid)
    if(str(parte_decimal) == "0.0"):
        mid=int(mid)
        return (" "*mid)+data+(" "*mid)
    else:
        mid = int(mid)
        return (" "*mid)+" "+data+(" "*mid)  

def fn_text_format(data:str,length:int):
    aux = ""
    if(len(data) > length):
        for i in range(0,length-3):
            if(data[i]=="\n"):
                aux+=""
            else:  
                aux+=data[i]
    else:
        aux=data
    return aux

"var:numerColsDate,columnas,filas,space=tipo interger"
"var:tamano_termina=tipo float"
"var:techo,pared,header=tipo string"
def pr_tabla(colsDate:list[str],data:list[str]):
    #cols=["CodLocal","Nombre","Estado"]
    # Obtener el tamaño de la terminal
    os.system("cls")
    tamano_terminal = os.get_terminal_size()
    
    # Extraer el número de columnas y filas
    columnas, filas = tamano_terminal.columns, tamano_terminal.lines
    #print(columnas,"Columnas")

    numberColsDate= len(colsDate)

    #Espacio para separar los datos
    space = ((columnas-numberColsDate) // numberColsDate)
    
    #Agregar espacio
    for i in range(0,numberColsDate):
        colsDate[i]= fn_text_center(colsDate[i],space)
    
    techo  = "-"*columnas
    pared= ""
    header= "|"

    for i in range(0,numberColsDate):
        mid = (space-len(colsDate[i]))/2
        header += colsDate[i] + "|"
        
    print(techo)
    print(header)
    print(techo)
    for i in range(0,len(data)):
        pared+="|"
        for t  in range(0,numberColsDate ):
            pared+=fn_text_center(fn_text_format(data[i][t],space),space) +"|"
        pared+="\n"
        pared+=techo
        
    print(pared)

def pr_cartel_construccion():
    print("\nOpcion en construccion...\n")

def pr_limpiar_consola():
    os.system("cls")

def pr_pausar_consola():
    os.system("pause")

def pr_crear_titulo(titulo:str):
    columnas="" 
    
    cantidadLetra:int = len(titulo) # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamano:int = os.get_terminal_size().columns

    for i in range(0,columnaTamano):
        columnas= columnas + "_"
    
    copiarColumnas = (columnaTamano - cantidadLetra )//2

    print(columnas)
    print("\n" + " " * copiarColumnas + titulo )
    print(columnas)
#--------------------------------------------------------------#
#                                                              #
#                PRECARGA DE DATOS                             #
#                                                              #
#--------------------------------------------------------------#

def pr_precarga_de_registros():
    cant_registros_mod = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES)
    cant_registros_admin = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES)
    cant_registros_estudiantes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES)
    
    if not cant_registros_admin:
        for i in range(0,len(INIT_ADMINISTRADORES)):
            admin = Administrador()
            admin.id_admin = INIT_ADMINISTRADORES[i][0]
            admin.email = INIT_ADMINISTRADORES[i][1]
            admin.contrasena= INIT_ADMINISTRADORES[i][2]
           
            fn_guardar_datos(admin,LOGICO_ARCHIVO_ADMINISTRADORES,FISICO_ARCHIVO_ADMINISTRADORES,lj_administradores)

    if not cant_registros_mod:
        for i in range(0, len(INIT_MODERADORES)):
            moderador = Moderador()
            moderador.id_moderador = INIT_MODERADORES[i][0]
            moderador.email = INIT_MODERADORES[i][1]
            moderador.contrasena = INIT_MODERADORES[i][2]
            moderador.estado = INIT_MODERADORES[i][3]
            moderador.nombre = INIT_MODERADORES[i][4]
            
            fn_guardar_datos(moderador, LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, lj_moderadores)
    
    if not cant_registros_estudiantes:
        for i in range(0, len(INIT_ESTUDIANTES)):
            estudiante = Estudiante()
            estudiante.id_estudiantes = INIT_ESTUDIANTES[i][0]
            estudiante.email = INIT_ESTUDIANTES[i][1]
            estudiante.nombre = INIT_ESTUDIANTES[i][2]
            estudiante.sexo = INIT_ESTUDIANTES[i][3]
            estudiante.contrasena = INIT_ESTUDIANTES[i][4]
            estudiante.hobbies = INIT_ESTUDIANTES[i][5]
            estudiante.biografia = INIT_ESTUDIANTES[i][6]
            estudiante.fecha_nacimiento = INIT_ESTUDIANTES[i][7]
            estudiante.estado = INIT_ESTUDIANTES[i][8]
            
            fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, lj_estudiantes)

def pr_precarga_de_reportes():
    cant_reportes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES)
    
    if not cant_reportes:
        for i in range(0, len(INIT_REPORTES)):
            reporte:Reporte = Reporte()
            reporte.id_reportante = INIT_REPORTES[i][0]
            reporte.id_reportado = INIT_REPORTES[i][1]
            reporte.razon_reporte = INIT_REPORTES[i][2]
            reporte.estado = INIT_REPORTES[i][3]
            
            fn_guardar_datos(reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, lj_reportes)
        
#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES/PR PRINCIPALES                      #
#                                                              #
#--------------------------------------------------------------#

def fn_iniciar_sesion():
    global INTENTO_LOGIN
    global TIPO_LOGEADO
    pr_limpiar_consola()
    pr_crear_titulo("Loguearse")
    
    autenticado = False
    INTENTO_LOGIN = 0
    
    while INTENTO_LOGIN < MAX_INTENTOS and not autenticado:
        email = input("\nIngrese el email: ")
        password = getpass("\nIngrese una contraseña: ") 
        
        if not autenticado:
            es_estudiante = fn_validar_usuario(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ADMINISTRADORES, email, password)
            es_moderador = fn_validar_usuario(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, email, password)
            es_admin = fn_validar_usuario(LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES, email, password)

            if es_estudiante != -1:
                autenticado = True
                TIPO_LOGEADO = 'E'
            elif es_moderador != -1:
                autenticado = True
                TIPO_LOGEADO = 'M'
            elif es_admin != -1:
                autenticado = True
                TIPO_LOGEADO = 'A'
            else:
                INTENTO_LOGIN += 1   
                                
                if MAX_INTENTOS > INTENTO_LOGIN:
                    print("Mail o contraseña incorrectos. Intente nuevamente.")
                    print(f"Intentos restantes: {MAX_INTENTOS - INTENTO_LOGIN}")
                else:
                    print("Intentos agotados.")
    
    return autenticado             

#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES/PR MODERADOR                        #
#                                                              #
#--------------------------------------------------------------#

def fn_desactivar_usuario():
    cant_usuarios = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES)
    tam_usuarios = os.path.getsize(FISICO_ARCHIVO_ESTUDIANTES)
    
    desactivado = False
    
    def pr_mostrar_tabla():
        columnas = [""]*2
        def pr_cargar_columnas():
            columnas[0] = "UID"
            columnas[1] = "NOMBRE"
        
        personas = [[""]*2 for _ in range(cant_usuarios)]
        pr_cargar_columnas()
        
        LOGICO_ARCHIVO_ESTUDIANTES.seek(0)
        contador = 0
        
        while LOGICO_ARCHIVO_ESTUDIANTES.tell() < tam_usuarios:
            registro: Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
            if registro.estado.strip() == "True":
                personas[contador][0] = registro.id_estudiantes
                personas[contador][1] = registro.nombre
                contador +=1
        
        pr_tabla(columnas, personas)   
    
    while not desactivado:
        pr_mostrar_tabla()
        
        opc = input("\nIngrese un usuario o ID: ")
        
        try:
            int_opc = int(opc)
            pos_encontrado = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", int_opc)
            
            if pos_encontrado != -1:
                LOGICO_ARCHIVO_ESTUDIANTES.seek(pos_encontrado)
                
                estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
                estudiante.estado = False
                fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, lj_estudiantes, pos_encontrado)
                
                desactivado = True
            
            else:
                print("No se encontro usuario, intente nuevamente.")
                
        except ValueError:
            pos_encontrado = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, opc, "")
        
            if pos_encontrado != -1:
                LOGICO_ARCHIVO_ESTUDIANTES.seek(pos_encontrado)
                
                estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
                estudiante.estado = False
                fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, lj_estudiantes, pos_encontrado)
                
                desactivado = True
            
            else:
                print("No se encontro usuario, intente nuevamente.")
    
    if desactivado:
        print(f"El usuario fue desactivado con exito")
        print("\na-Desactivar otro usuario\n\nb-Volver\n\n")
        
        opc = fn_validar_rango_str('a', 'b')
        
        match opc:
            case 'a':
                fn_desactivar_usuario()
            case 'b':
                return desactivado
    
    return desactivado

def fn_gestionar_usuarios():
    band = True
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR USUARIOS")
        print("\na-Desactivar usuario\n\nb-Volver\n\n")
        opc = fn_validar_rango_str('a', 'b')
        
        match opc:
            case 'a':
                fn_desactivar_usuario()
            case 'b':
                band = False
    
    return band

def fn_desactivar_usu_reportado(id:int):
    pos_encontrado = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", id)
    
    LOGICO_ARCHIVO_ESTUDIANTES.seek(pos_encontrado)
    estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
    estudiante.estado = False
    fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, lj_estudiantes, pos_encontrado)
      
def fn_ver_reportes():
    cant_reportes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES)
    tam_reportes = os.path.getsize(FISICO_ARCHIVO_REPORTES)
    
    contador = 1
    
    while LOGICO_ARCHIVO_REPORTES.tell() < tam_reportes:
        pr_limpiar_consola()
        pr_crear_titulo(f"Reporte {contador}/{cant_reportes}")
        
        posicion_actual = LOGICO_ARCHIVO_REPORTES.tell()
        
        registro_reporte:Reporte = pickle.load(LOGICO_ARCHIVO_REPORTES)
        
        id_reportante = registro_reporte.id_reportante.strip()
        id_reportado = registro_reporte.id_reportado.strip()
              
        reportante_pos = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", int(id_reportante))
        LOGICO_ARCHIVO_ESTUDIANTES.seek(reportante_pos)
        reportante:Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
        reportante_estado = reportante.estado.strip()
        
        reportado_pos = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", int(id_reportado))
        LOGICO_ARCHIVO_ESTUDIANTES.seek(reportado_pos)
        reportado:Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
        reportado_estado = reportado.estado.strip()
        
        if reportado_estado == "True" and reportante_estado == "True":
            if registro_reporte.estado.strip() == "0":
                print(f"\nID_REPORTANTE: {id_reportante}")
                print(f"ID_REPORTADO: {id_reportado}")
                print(f"MOTIVO: {registro_reporte.razon_reporte.strip()}")
                print(f"ESTADO: {registro_reporte.estado.strip()}")                
                print("\nIngrese una accion: ")
                print("\na-Ignorar reporte\n\nb-Bloquear al reportado\n\n")
                opc = fn_validar_rango_str("a", "b")
                
                match opc:
                    case 'a':
                        registro_reporte.estado = 2
                        fn_guardar_datos(registro_reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, lj_reportes, posicion_actual)
                    case 'b':
                        registro_reporte.estado = 1
                        fn_desactivar_usu_reportado(int(id_reportado))
                        fn_guardar_datos(registro_reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, lj_reportes, posicion_actual)
                        pr_limpiar_consola()
                        pr_crear_titulo(f"Usuario {reportado.email} bloqueado con exito")
                        
                        print("\na-Continuar\n")
                        opc = fn_validar_rango_str("a", "a")
                        
                contador +=1
    
    return contador

def fn_gestionar_reportes():
    band = True
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR REPORTES")
        print("\na-Ver reportes\n\nb-Volver\n\n")
        opc = fn_validar_rango_str('a', 'b')
        
        match opc:
           
            case 'a':
                if fn_ver_reportes() == 1:
                    pr_limpiar_consola()
                    pr_crear_titulo("GESTIONAR REPORTES")
                    print("\nNo hay reportes para ver")
                    print("\nb-Volver\n\n")
                    opc = fn_validar_rango_str('b', 'b')
            
            case 'b':
                band = False
    return band
    
def fn_menu_mod():
    band= True
    
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("MENU PRINCIPAL")
        print("\n1-Gestionar usuarios\n\n2-Gestionar reportes\n\n3-Salir\n\n")
        opc = fn_validar_rango(1, 3)
        
        match opc:
            case 1:
                fn_gestionar_usuarios()
            case 2:
                fn_gestionar_reportes()
            case 3:
                band=False
        
    return band

#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES/PR ADMINISTRADOR                    #
#                                                              #
#--------------------------------------------------------------#

#-----------#
#Gestionar usuarios
#-----------#
def fn_eliminar_usuario():
    cant_estudiantes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES)
    tam_reg_estudiantes = os.path.getsize(FISICO_ARCHIVO_ESTUDIANTES)
    
    cant_moderadores = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES)
    tam_reg_moderadores = os.path.getsize(FISICO_ARCHIVO_MODERADORES)
    
    desactivado = False
    
    def pr_mostrar_usuarios():
        columnas = [""]*3
        def pr_cargar_columnas():
            columnas[0] = "UID"
            columnas[1] = "EMAIL"
            columnas[2] = "TIPO"
        
        personas = [[""]*3 for _ in range(cant_estudiantes + cant_moderadores)]
        pr_cargar_columnas()
        
        LOGICO_ARCHIVO_ESTUDIANTES.seek(0)
        contador = 0
        
        while LOGICO_ARCHIVO_ESTUDIANTES.tell() < tam_reg_estudiantes:
            reg_est: Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
            
            if reg_est.estado.strip() == "True":
                personas[contador][0] = reg_est.id_estudiantes
                personas[contador][1] = reg_est.email
                personas[contador][2] = "Estudiante"
                contador +=1
        
        LOGICO_ARCHIVO_MODERADORES.seek(0)
    
        while LOGICO_ARCHIVO_MODERADORES.tell() < tam_reg_moderadores:
            reg_mod: Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
            
            if reg_mod.estado.strip() == "true":
                personas[contador][0] = reg_mod.id_moderador
                personas[contador][1] = reg_mod.email
                personas[contador][2] = "Moderador"
                contador +=1
        
        pr_tabla(columnas, personas)
    
    while not desactivado:
        pr_mostrar_usuarios()
        
        opc = input("Ingrese email de usuario a eliminar: ")
        
        pos_estudiante = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", "", opc)
        pos_moderador = fn_busqueda_secu(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, "", "", opc)
        
        if pos_estudiante == -1 and pos_moderador == -1:
            print("No se encuentra usuario con ese email. Intente nuevamente.")
        
        if pos_estudiante != -1:
            LOGICO_ARCHIVO_ESTUDIANTES.seek(pos_estudiante)
            
            estudiante:Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
            estudiante.estado = False
            fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, lj_estudiantes, pos_estudiante)

            desactivado = True
        
        if pos_moderador != -1:
            LOGICO_ARCHIVO_MODERADORES.seek(pos_moderador)
            
            moderador:Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
            moderador.estado = False
            fn_guardar_datos(moderador, LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, lj_moderadores, pos_moderador)

            desactivado = True
    
    if desactivado:
        print(f"El usuario fue desactivado con exito")
        print("\na-Desactivar otro usuario\n\nb-Volver\n\n")
        
        opc = fn_validar_rango_str('a', 'b')
        
        match opc:
            case 'a':
                fn_eliminar_usuario()
            case 'b':
                return desactivado
    
    return desactivado

def fn_gestionar_usuarios_admin():
    band = False
    while not band:
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR USUARIOS")
        print("\na-Eliminar un usuario\n\nb-Dar de alta un moderador\n\nc-Desactivar usuario\n\nd-Salir\n\n")
        opc = fn_validar_rango_str("a", "d")
        
        match opc:
            case 'a':
                fn_eliminar_usuario()
            case 'b':
                band = True
            case 'c':
                band = True
            case 'd':
                band = True
    return band

#-----------#
#Gestionar reportes
#-----------#
def fn_gestionar_reportes_admin():
    return True

#-----------#
#Reportes estadisticos
#-----------#
def fn_reportes_estadisticos():
    return True

def fn_menu_admin():
    band= True
    
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("MENU PRINCIPAL")
        print("\n1-Gestionar usuarios\n\n2-Gestionar reportes\n\n3-Reportes estadisticos\n\n4-Salir\n\n")
        opc = fn_validar_rango(1, 4)
        
        match opc:
            case 1:
                fn_gestionar_usuarios_admin()
            case 2:
                fn_gestionar_reportes_admin()
            case 3:
                fn_reportes_estadisticos()
            case 4:
                band=False
        
    return band

#--------------------------------------------------------------#
#                                                              #
#                PROGRAMA PRINCIPAL                            #
#                                                              #
#--------------------------------------------------------------#

def inicializar():
    global INTENTO_LOGIN
    global TIPO_LOGEADO
    
    pr_precarga_de_reportes()
    pr_precarga_de_registros()

    band = True

    while band:
        pr_limpiar_consola()
        pr_crear_titulo("Bienvenido, ¿buscando al compañero ideal?  ")
        print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        opc = fn_validar_rango(0, 2)
        
        match opc:
            case 1:
                if not fn_iniciar_sesion():
                    band = False
                match TIPO_LOGEADO:
                    case 'M':
                        fn_menu_mod()
                    case 'A':
                        fn_menu_admin()
                    case 'E':
                        autenticado = autenticado
            case 2:
                print("opc 2")
            case 0:
                band = False
    
    print("\nSaliendo del programa.\n")

# inicializar()

def debugger():
    pr_precarga_de_reportes()
    pr_precarga_de_registros()
    fn_eliminar_usuario()
    
debugger()