import os 
import pickle 
import io
import datetime
import random
import locale 
import time 
import getpass

def fn_crear_logico(ruta: str):
    archivo_logico = None  # Inicialización explícita
    
    if os.path.exists(ruta):
        archivo_logico = open(ruta, "r+b")  # Abre para lectura y escritura binaria
    else:
        archivo_logico = open(ruta, "w+b")  # Crea un archivo nuevo y lo abre en modo binario
    
    return archivo_logico


def fn_cerrar_logico():
    ARCHIVO_LOGICO_ESTUDIANTES.close()
    ARCHIVO_LOGICO_MODERADORES.close()
    ARCHIVO_LOGICO_REPORTES.close()
    ARCHIVO_LOGICO_LIKES.close()
    ARCHIVO_LOGICO_ADMINISTRADORES.close()


if(not(os.path.exists("archivos"))):
    os.mkdir(os.getcwd() + "/archivos")
    
if(os.path.exists("archivos")):
    #Archivo fiscos
    ARCHIVO_FISICO_ESTUDIANTES= os.getcwd() + "/archivos/estudiantes.dat" 
    ARCHIVO_FISICO_MODERADORES= os.getcwd() + "/archivos/moderadores.dat" 
    ARCHIVO_FISICO_REPORTES= os.getcwd() + "/archivos/reportes.dat"
    ARCHIVO_FISICO_LIKES= os.getcwd() + "/archivos/likes.dat"
    ARCHIVO_FISICO_ADMINISTRADORES= os.getcwd() + "/archivos/administradores.dat"

    ARCHIVO_LOGICO_ESTUDIANTES= fn_crear_logico(ARCHIVO_FISICO_ESTUDIANTES) 
    ARCHIVO_LOGICO_MODERADORES= fn_crear_logico(ARCHIVO_FISICO_MODERADORES) 
    ARCHIVO_LOGICO_REPORTES= fn_crear_logico(ARCHIVO_FISICO_REPORTES)
    ARCHIVO_LOGICO_LIKES= fn_crear_logico(ARCHIVO_FISICO_LIKES)
    ARCHIVO_LOGICO_ADMINISTRADORES= fn_crear_logico(ARCHIVO_FISICO_ADMINISTRADORES)



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

###FUNCIONES DE VALIDACION DE DATOS###
"var:respuesta=tipo string"
def fn_validar_si_no():
    respuesta=input("Ingrese si o no: ") 
    while (respuesta !="si") and  (respuesta !="no"):
        print("No es un opción valida, ingrese si o no")
        respuesta=input("Ingrese si o no: ")
    return respuesta

"var:numero,inicio,limite=tipo interger"
def fn_validar_rango(inicio:int,limite:int):
    try:
        numero =int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input("Ingrese una opción: "))
        return numero
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio,limite)

"var:inicio,limite,opc=tipo string"
def fn_validar_rango_str(inicio: str, limite:str):
    opc = input("Ingrese una opcion:").lower()
    
    while not (inicio <= opc <= limite):
        print("\nError, ingrese una opcion valida.\n")
        opc = input("Ingrese una opcion:")
    
    return opc

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

def lj_estudiantes(x:Estudiantes):
    x.id_estudiantes=str(x.id_estudiantes).ljust(10).lower() # Entero
    x.email=str(x.email).ljust(32).lower()
    x.nombre=str(x.nombre).ljust(32).lower()
    x.sexo=str(x.sexo).ljust(1).lower()
    x.contrasena=str(x.contrasena).ljust(32).lower()
    x.estado=str(x.estado).ljust(10).lower() #Booleano
    x.hobbies=str(x.hobbies).ljust(255).lower() 
    x.materia_favorita=str(x.materia_favorita).ljust(16).lower()
    x.deporte_favorito=str(x.deporte_favorito).ljust(16).lower()
    x.materia_fuerte=str(x.materia_fuerte).ljust(16).lower()
    x.materia_debil=str(x.materia_debil).ljust(16).lower()
    x.biografia=str(x.biografia).ljust(255).lower()
    x.pais=str(x.pais).ljust(32).lower()
    x.ciudad=str(x.ciudad).ljust(32).lower()
    x.fecha_nacimiento=str(x.fecha_nacimiento).ljust(10).lower()

def lj_moderadores(x:Moderadores):
    x.id_moderador = str(x.id_moderador).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower()
    x.contrasena = str(x.contrasena).ljust(32).lower()
    x.estado = str(x.estado).ljust(10).lower() #Booleano

def lj_administradores(x:Administradores):
    x.id_admin = str(x.id_admin).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower() 
    x.contrasena = str(x.contrasena).ljust(32).lower()

def lj_likes(x:Likes):
    x.destinatario=str(x.destinatario).ljust(10).lower() #Entero
    x.remitente=str(x.remitente).ljust(10).lower() #Entero

def lj_reportes(x:Reportes):
    x.id_reportante = str(x.id_reportante).ljust(10).lower() #Entero
    x.id_reportado = str(x.id_reportado).ljust(10).lower() #Entero
    x.razon_reporte = str(x.razon_reporte).ljust(255).lower() 
    x.estado = str(x.id_reportado).ljust(10).lower() #Entero


