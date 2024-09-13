import os 
import pickle 
import io
import datetime
import random
import locale 
import time 
import getpass
from typing import Callable


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

def pr_cartel_construccion():
    print("\nOpcion en construccion...\n")

def fn_guardar_datos(registro:object,ARCHIVO_LOGICO:io.BufferedRandom,ARCHIVO_FISICO:str,formateador,posicion:int = -1):
    """ Guarda el registro en su respectivo archivo """
    t = os.path.getsize(ARCHIVO_FISICO)
    try:        
        if (posicion) == -1:
            posicion = t

        ARCHIVO_LOGICO.seek(posicion)
        formateador(registro) 
        pickle.dump(registro,ARCHIVO_LOGICO)
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
        


def busquedadico(data:str, ARCHIVO_LOGICO:io.BufferedRandom, ARCHIVO_FISICO:str,funcion:function):
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









def busquedasecuencial(
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



def pr_inicializar_programa():
    administradores = [["pepe@gmail.com","pepe"],["pedro@gmail.com","pepe"],["lorenzo@gmail.com","pepe"]]

    for i in range(0,len(administradores)):
        admin = Administradores()
        admin.email = administradores[i][0]
        admin.contrasena= administradores[i][1]
        admin.id_admin = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ADMINISTRADORES,FISICO_ARCHIVO_ADMINISTRADORES)
        fn_guardar_datos(admin,LOGICO_ARCHIVO_ADMINISTRADORES,FISICO_ARCHIVO_ADMINISTRADORES,lj_administradores)
    

def ver():
        reg:Administradores
        t = os.path.getsize(FISICO_ARCHIVO_ADMINISTRADORES)
        pos = 0
        LOGICO_ARCHIVO_ADMINISTRADORES.seek(0,0)
        reg = pickle.load(LOGICO_ARCHIVO_ADMINISTRADORES)
        while LOGICO_ARCHIVO_ADMINISTRADORES.tell() < t:
            reg = pickle.load(LOGICO_ARCHIVO_ADMINISTRADORES)
            print(reg.id_admin)
            print(reg.id_admin)
            print(reg.id_admin)


def fn_busqueda_secuencial():
    print("2")

    return False # Elemento no encontrado

def fn_falso_burbuja():
    ""

""" def pr_editar_datos_personales():
    pr_crear_titulo("Gestionar perfil")
    print("Ingrese que desea modificar")
    print("Nombre")
    print("Sexo")
    print("Estado")
    print("Hobbies")
    print("Materia Favorita")
    print("Deporte Favorito")
    print("Materia Fuerte")
    print("Materia Debil")
    print("Biografia")
    print("Pais")
    print("Ciudad")
    print("Fecha de nacimiento")
 """

fn_cerrar_logico()