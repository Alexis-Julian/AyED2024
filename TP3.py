import os 
import pickle 
import io
import datetime
import random
import locale 
import time 
import getpass
#from typing import Callable

#--------------------------------------------------------------#
#                                                              #
#              CONSTANTES Y VARIABLES GLOBALES                 #
#                                                              #
#--------------------------------------------------------------#

CARPETA = "pruebas"

#--------------------------------------------------------------#
#                                                              #
#                CLASES                                        #
#                                                              #
#--------------------------------------------------------------#

class Estudiantes:
    def __init__(self):
        self.id_estudiantes= 0
        self.email= ""
        self.nombre=""
        self.sexo =""
        self.contrasena=""
        self.estado = False
        self.hobbies=""
        self.materia_favorita=""
        self.deporte_favorito=""
        self.materia_fuerte=""
        self.materia_debil=""
        self.biografia=""
        self.pais=""
        self.ciudad=""
        self.fecha_nacimiento=""

class Usuario:
    def __init__(self):
        self.id_usuario = 0
        self.email = ""
        self.nombre= ""
        self.sexo= ""
        self.hobbies = ""
        self.materia_favorita=""
        self.deporte_favorito=""
        self.materia_fuerte=""
        self.materia_debil=""
        self.biografia=""
        self.pais=""
        self.ciudad=""
        self.fecha_nacimiento=""

class Moderadores:
    def __init__(self):
        self.id_moderador=0
        self.email=""
        self.contrasena=""
        self.estado=bool

class Administradores:
    def __init__(self):
        self.id_admin=0
        self.email=""
        self.contrasena=""

class Likes:
    def __init__(self):
        self.remitente=0
        self.destinatario=0

class Reportes:
    def __init__(self):
        self.id_reportante=0
        self.id_reportado=0
        self.razon_reporte=""
        self.estado= 0


#--------------------------------------------------------------#
#                                                              #
#                ARCHIVOS                                      #
#                                                              #
#--------------------------------------------------------------#

def fn_crear_logico(ruta: str):
    archivo_logico: io.BufferedRandom  # Inicialización explícita
    
    if os.path.exists(ruta):
        archivo_logico = open(ruta, "r+b")  # Abre para lectura y escritura binaria
    else:
        archivo_logico = open(ruta, "w+b")  # Crea un archivo nuevo y lo abre en modo binario
    
    return archivo_logico


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

def formatear_estudiantes(x: Estudiantes):
    x.id_estudiantes=str(x.id_estudiantes).ljust(10) # Entero
    x.email=str(x.email).ljust(32).lower()
    x.nombre=str(x.nombre).ljust(32)
    x.sexo=str(x.sexo).ljust(1).lower()
    x.contrasena=str(x.contrasena).ljust(32)
    x.estado=str(x.estado).ljust(10) #Booleano
    x.hobbies=str(x.hobbies).ljust(255)
    x.materia_favorita=str(x.materia_favorita).ljust(16)
    x.deporte_favorito=str(x.deporte_favorito).ljust(16)
    x.materia_fuerte=str(x.materia_fuerte).ljust(16)
    x.materia_debil=str(x.materia_debil).ljust(16)
    x.biografia=str(x.biografia).ljust(255)
    x.pais=str(x.pais).ljust(32)
    x.ciudad=str(x.ciudad).ljust(32)
    x.fecha_nacimiento=str(x.fecha_nacimiento).ljust(10)

def formatear_moderadores(x: Moderadores):
    x.id_moderador = str(x.id_moderador).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower()
    x.contrasena = str(x.contrasena).ljust(32).lower()
    x.estado = str(x.estado).ljust(10).lower() #Booleano

def formatear_administradores(x: Administradores):
    x.id_admin = str(x.id_admin).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower() 
    x.contrasena = str(x.contrasena).ljust(32).lower()

def formatear_likes(x: Likes):
    x.destinatario=str(x.destinatario).ljust(10).lower() #Entero
    x.remitente=str(x.remitente).ljust(10).lower() #Entero

def formatear_reportes(x: Reportes):
    x.id_reportante = str(x.id_reportante).ljust(10).lower() #Entero
    x.id_reportado = str(x.id_reportado).ljust(10).lower() #Entero
    x.razon_reporte = str(x.razon_reporte).ljust(255).lower() 
    x.estado = str(x.id_reportado).ljust(10).lower() #Entero

#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES DE VALIDACION DE DATOS              #
#                                                              #
#--------------------------------------------------------------#

"var: respuesta = tipo string"
def fn_validar_si_no():
    respuesta=input("Ingrese si o no: ") 
    while (respuesta != "si") and  (respuesta != "no"):
        print("No es un opción valida, ingrese si o no")
        respuesta=input("Ingrese si o no: ")
    return respuesta

"var: numero, inicio, limite = tipo interger"
def fn_validar_rango(inicio: int, limite: int):
    try:
        numero =int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input("Ingrese una opción: "))
        return numero
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio, limite)

"var: inicio, limite, opc = tipo string"
def fn_validar_rango_str(inicio: str, limite: str):
    opc = input("Ingrese una opcion:").lower()
    
    while not inicio <= opc <= limite:
        print("\nError, ingrese una opcion valida.\n")
        opc = input("Ingrese una opcion: ")
    
    return opc

def fn_guardar_datos(registro: object, archivo_logico: io.BufferedRandom, archivo_fisico: str, formateador, posicion: int = -1):
    """ Guarda el registro en su respectivo archivo """
    t = os.path.getsize(archivo_fisico)
    try:        
        if posicion == -1:
            posicion = t
        archivo_logico.seek(posicion)
        formateador(registro) 
        pickle.dump(registro, archivo_logico)
        archivo_logico.flush()
    except (ValueError, TypeError):
        print("Se genero un error")

def fn_buscar_cantidad_de_registros(archivo_logico: io.BufferedRandom, archivo_fisico: str):
    cantidad = 0   
    if os.path.getsize(archivo_fisico) != 0:
        archivo_logico.seek(0)
        pickle.load(archivo_logico)
        longitud_reg = archivo_logico.tell()
        tam_arch = os.path.getsize(archivo_fisico) 
        cantidad = tam_arch // longitud_reg
        archivo_logico.seek(0)
    return cantidad

def fn_busquedadico(archivo_logico: io.BufferedRandom, archivo_fisico: str, campo: str, data: int):
    dato = int(str(data).strip())
    archivo_logico.seek(0, 0)
    registro = pickle.load(archivo_logico)
    tamregi = archivo_logico.tell()
    if tamregi == 0:
        return -1
    cantreg = int(os.path.getsize(archivo_fisico) / tamregi)
    inicio = 0
    fin = cantreg - 1
    medio = (inicio + fin) // 2
    archivo_logico.seek(medio * tamregi, 0) 
    registro = pickle.load(archivo_logico)

    while inicio <  fin and int(str(getattr(registro, campo)).strip()) != dato:
        if int(str(getattr(registro, campo)).strip()) > dato:
            fin = medio - 1
        else:
            inicio = medio + 1            
        
        medio = (inicio + fin) // 2
        archivo_logico.seek(medio * tamregi, 0)
        registro = pickle.load(archivo_logico)
    if int(str(getattr(registro, campo)).strip()) == dato:
        return medio * tamregi

    return -1

def fn_busquedasecuencial(archivo_logico: io.BufferedRandom, archivo_fisico: str, callback):
    """ def busqueeda_especifica(regtemp, pos):
        if str(regtemp.propiedad).strip() == 'valor':
            localesActivos.append(regtemp)         
            return False """

    tam_archivo = os.path.getsize(archivo_fisico)
    archivo_logico.seek(0)
    encontrado = False

    while archivo_logico.tell() < tam_archivo and encontrado == False:
        posicion = archivo_logico.tell()
        regtemporal = pickle.load(archivo_logico)
        encontrado = callback(regtemporal, posicion)

    return encontrado


#--------------------------------------------------------------#
#                                                              #
#                 FUNCIONES AUXILIARES                         #
#                                                              #
#--------------------------------------------------------------#

def fn_text_center(data, space):
    mid = (space - len(data)) / 2
    parte_decimal = mid - int(mid)
    if str(parte_decimal) == "0.0":
        mid = int(mid)
        return (" " * mid) + data + (" " * mid)
    else:
        mid = int(mid)
        return (" " * mid)+" " + data+(" " * mid)  

def fn_text_format(data: str, length: int):
    aux = ""
    if len(data) > length:
        for i in range(0, length - 3):
            if data[i] == "\n":
                aux += ""
            else:  
                aux += data[i]
    else:
        aux = data
    return aux

"var: numerColsDate, columnas, filas, space = tipo interger"
"var: tamano_termina = tipo float"
"var: techo, pared, header = tipo string"
def pr_tabla(colsDate: list[str], data: list[str]):
    #cols=["CodLocal", "Nombre", "Estado"]
    # Obtener el tamaño de la terminal
    os.system("cls")
    tamano_terminal = os.get_terminal_size()
    
    # Extraer el número de columnas y filas
    columnas, filas = tamano_terminal.columns, tamano_terminal.lines
    #print(columnas, "Columnas")

    numberColsDate= len(colsDate)

    #Espacio para separar los datos
    space = (columnas-numberColsDate) // numberColsDate
    
    #Agregar espacio
    for i in range(0, numberColsDate):
        colsDate[i]= fn_text_center(colsDate[i], space)
    
    techo  = "-"*columnas
    pared= ""
    header= "|"

    for i in range(0, numberColsDate):
        mid = (space - len(colsDate[i])) / 2
        header += colsDate[i] + "|"
        
    print(techo)
    print(header)
    print(techo)
    for i in range(0, len(data)):
        pared += "|"
        for t in range(0, numberColsDate ):
            pared += fn_text_center(fn_text_format(data[i][t], space), space) + "|"
        pared += "\n"
        pared += techo
        
    print(pared)

def pr_cartel_construccion():
    print("\nOpcion en construcción...\n")

def pr_limpiar_consola():
    os.system("cls")

def pr_pausar_consola():
    os.system("pause")

def pr_crear_titulo(titulo: str):
    columnas = "" 
    
    cantidadLetra: int = len(titulo) # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamano: int = os.get_terminal_size().columns

    #for i in range(0, columnaTamano):
    #    columnas = columnas + "_"
    columnas = "_" * columnaTamano
    
    copiarColumnas = (columnaTamano - cantidadLetra ) // 2

    print(columnas)
    print("\n" + " " * copiarColumnas + titulo )
    print(columnas)

def pr_menu_estudiantes():
    opc = -1
    while opc != 0:  
        print("\n1. Gestionar mi perfil \n2. Gestionar candidatos \n3. Matcheos \n4. Reportes estadísticos \n0. Salir")
        opc = fn_validar_rango(0, 4)
        match opc:
            case 1:
                pr_gestionar_perfil()
            case 2:
                pr_gestionar_candidatos()
            case 3:
                pr_matcheos()
            case 4:
                pr_reporte_estadisticos()
            case _:
                ""

def pr_menu_moderador():
    opc = -1
    while opc != 0:
        print("\n1. Gestionar usuarios \n2. Gestionar Reportes \n3. Reportes Estadísticos \n0. Salir")
        opc = fn_validar_rango(0, 3)
        match opc:
            case 1 :
                pr_gestionar_usuarios()
            case 2:
                pr_gestionar_repotes()
            case 3:
                pr_reportes_estadisticos()
            case _:
                ""

def pr_menu_administrador():
    opc = -1
    while opc != 0:
        print("\n1. Gestionar usuarios \n2. Gestionar Reportes \n3. Reportes Estadísticos \n0. Salir")
        opc = fn_validar_rango(0, 3)
        match opc:
            case 1 :
                pr_gestionar_usuarios_admin()
            case 2:
                pr_gestionar_reportes_admin()
            case 3:
                pr_reporte_estadisticos_admin()
            case _:
                ""

def pr_inicializar_programa():
    administradores = [["pepe@gmail.com", "pepe"], ["pedro@gmail.com", "pepe"], ["lorenzo@gmail.com", "pepe"]]

    for i in range(0, len(administradores)):
        admin = Administradores()
        admin.email = administradores[i][0]
        admin.contrasena= administradores[i][1]
        admin.id_admin = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES)
        fn_guardar_datos(admin, LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES, formatear_administradores)


#--------------------------------------------------------------#
#                                                              #
#                PROGRAMA PRINCIPAL                            #
#                                                              #
#--------------------------------------------------------------#

if not os.path.exists(CARPETA):
    os.mkdir(os.getcwd() + "/" + CARPETA)
    
if os.path.exists(CARPETA):
    # Archivo fiscos
    FISICO_ARCHIVO_ADMINISTRADORES = os.getcwd() + "/" + CARPETA + "/administradores.dat"
    FISICO_ARCHIVO_MODERADORES = os.getcwd() + "/" + CARPETA + "/moderadores.dat" 
    FISICO_ARCHIVO_ESTUDIANTES = os.getcwd() + "/" + CARPETA + "/estudiantes.dat" 
    FISICO_ARCHIVO_REPORTES = os.getcwd() + "/" + CARPETA + "/reportes.dat"
    FISICO_ARCHIVO_LIKES = os.getcwd() + "/" + CARPETA + "/likes.dat"

    LOGICO_ARCHIVO_ADMINISTRADORES = fn_crear_logico(FISICO_ARCHIVO_ADMINISTRADORES)
    LOGICO_ARCHIVO_MODERADORES = fn_crear_logico(FISICO_ARCHIVO_MODERADORES) 
    LOGICO_ARCHIVO_ESTUDIANTES = fn_crear_logico(FISICO_ARCHIVO_ESTUDIANTES) 
    LOGICO_ARCHIVO_REPORTES = fn_crear_logico(FISICO_ARCHIVO_REPORTES)
    LOGICO_ARCHIVO_LIKES = fn_crear_logico(FISICO_ARCHIVO_LIKES)

# La lógica inicia acá




# Última línea
fn_cerrar_logico()
