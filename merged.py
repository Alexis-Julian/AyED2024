import os 
import pickle 
import io
import shutil
import time
from datetime import datetime
import random
import locale 
import time 
import string
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
        self.ultima_conexion = ""
        self.clave_recuperacion = ""

class Moderador:
    def __init__(self):
        self.id_moderador=0
        self.email=""
        self.contrasena=""
        self.estado=bool
        self.nombre=""
        self.reportes_ignorados=0
        self.reportes_aceptados=0
        self.reportes_totales=0

class Administrador:
    def __init__(self):
        self.id_admin=0
        self.email=""
        self.contrasena=""

class Like:
    def __init__(self):
        self.remitente=0
        self.destinatario=0
        self.estado = False

class Reporte:
    def __init__(self):
        self.id_reportante=0
        self.id_reportado=0
        self.razon_reporte=""
        self.estado= 0
        
class Usuario:
    def __init__(self):
        self.id = 4
        self.email = ""
        self.nombre= ""
        self.role = ""
        self.estado = True
        
user_sesion = Usuario()
        
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
INIT_MODERADORES = [
    [0, "mod_lautaro@ayed.com", "123", True, "Lautaro"], 
    [1, "mod_alexis@ayed.com", "123", True, "Alexis"],
    [2, "mod_nestor@ayed.com", "123", False, "Nestor"],
    [3, "mod_leonel@ayed.com", "123", False, "Leonel"],] 

INIT_REPORTES = [
    [0, 1, "Me molesta", 0],
    [3, 1, "No me paso la tarea", 0],
    [6, 0, "No me paso su instagram", 0],
    [7, 4, "Jorge trata mal a sus companeros", 0],
    [1, 5, "No quiere participar en el grupo", 0],
    [2, 6, "Habla durante la clase", 0],
    [4, 2, "Se rie en momentos inapropiados", 0],
    [5, 3, "Siempre llega tarde a las reuniones", 0]
]

#--------------------------------------------------------------#
#                                                              #
#                       GLOBALES                               #
#                                                              #
#--------------------------------------------------------------#

MAX_INTENTOS = 3
INTENTO_LOGIN = 0
REG_LOGEADO: io.BufferedRandom
POS_LOGEADA = -1
ROLE_USUARIO="U"
ROLE_MODERADOR="M"
ROLE_ADMINISTRADOR="A"

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

def formatear_estudiantes(x:Estudiante):
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
    x.ultima_conexion=str(x.ultima_conexion).ljust(50)
    x.clave_recuperacion = str(x.ultima_conexion).ljust(80)

def lj_moderadores(x:Moderador):
    x.id_moderador = str(x.id_moderador).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower()
    x.contrasena = str(x.contrasena).ljust(32).lower()
    x.estado = str(x.estado).ljust(10).lower() #Booleano
    x.nombre = str(x.nombre).ljust(32)
    x.reportes_aceptados = str(x.reportes_aceptados).ljust(10).lower()
    x.reportes_totales = str(x.reportes_totales).ljust(10).lower()
    x.reportes_ignorados = str(x.reportes_ignorados).ljust(10).lower()

def lj_administradores(x:Administrador):
    x.id_admin = str(x.id_admin).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower() 
    x.contrasena = str(x.contrasena).ljust(32).lower()

def formatear_likes(x: Like):
    x.destinatario=str(x.destinatario).ljust(10).lower() #Entero
    x.remitente=str(x.remitente).ljust(10).lower() #Entero

def formatear_reportes(x:Reporte):
    x.id_reportante = str(x.id_reportante).ljust(10).lower() #Entero
    x.id_reportado = str(x.id_reportado).ljust(10).lower() #Entero
    x.razon_reporte = str(x.razon_reporte).ljust(255).lower() 
    x.estado = str(x.estado).ljust(10).lower() #Entero
    
#--------------------------------------------------------------#
#                                                              #
#                NORMALIZADORES                                #
#                                                              #
#--------------------------------------------------------------#

def normalizar_estudiante(x:Estudiante):
    x.id_estudiantes=str(x.id_estudiantes).strip() # Entero
    x.email=str(x.email).strip()
    x.nombre=str(x.nombre).strip()
    x.sexo=str(x.sexo).strip()   
    x.contrasena=str(x.contrasena).strip()
    x.estado=str(x.estado).strip() #Booleano
    x.hobbies=str(x.hobbies).strip()
    x.materia_favorita=str(x.materia_favorita).strip()
    x.deporte_favorito=str(x.deporte_favorito).strip()
    x.materia_fuerte=str(x.materia_fuerte).strip()
    x.materia_debil=str(x.materia_debil).strip()
    x.biografia=str(x.biografia).strip()
    x.pais=str(x.pais).strip()
    x.ciudad=str(x.ciudad).strip()
    x.fecha_nacimiento=str(x.fecha_nacimiento).strip()
    x.ultima_conexion=str(x.ultima_conexion).strip()
    x.clave_recuperacion = str(x.ultima_conexion).strip()

def normalizar_likes(x:Like):
    x.destinatario=str(x.destinatario).strip()
    x.remitente=str(x.remitente).strip()
    
#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES DE VALIDACION DE DATOS              #
#                                                              #
#--------------------------------------------------------------#
def pr_verificar_usuario(email:str,contrasena:str) -> bool:
    reg_user:Estudiante
    verificado = False
    
    #VERIFICAR USUARIOS 
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"email",email)
    #Si no lo encuentra devuelve no verificado
    if(pos != -1 ):
        #Logia de lectura de archivo
        LOGICO_ARCHIVO_ESTUDIANTES.seek(pos,0)
        reg_user = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
        normalizar_estudiante(reg_user)

        #Si todo es correcto pone el verificado en verdadero 
        if (reg_user.contrasena == contrasena and reg_user.estado == "True"):
            verificado = True  
            user_sesion.id = reg_user.id_estudiantes
            user_sesion.nombre = reg_user.nombre
            user_sesion.email = reg_user.email
            user_sesion.role= ROLE_USUARIO
            user_sesion.estado = True
        
        return verificado 
        

    #VERIFICAR MODERADORES
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_MODERADORES,FISICO_ARCHIVO_MODERADORES,"email",email)
    #Si no lo encuentra devuelve no verificado
    
    if(pos != -1 ):
        #Logica de lectura de archivo   
        LOGICO_ARCHIVO_MODERADORES.seek(pos,0)
        reg_moderador:Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
        
        if((reg_moderador.contrasena).strip() == contrasena and reg_moderador.estado.strip() == "true"):
            verificado = True
            user_sesion.id=reg_moderador.id_moderador
            user_sesion.email= reg_moderador.email
            user_sesion.role=ROLE_MODERADOR
            user_sesion.nombre = ""
            
    
        return verificado 

    #VERIFICAR ADMINISTRADOR 
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ADMINISTRADORES,FISICO_ARCHIVO_ADMINISTRADORES,"email",email)
    #Si no lo encuentra devuelve no verificado
    if(pos != -1):
        LOGICO_ARCHIVO_ADMINISTRADORES.seek(pos,0)
        reg_administrador:Administrador = pickle.load(LOGICO_ARCHIVO_ADMINISTRADORES)
        if((reg_administrador.contrasena).strip() == contrasena):
            verificado = True
            user_sesion.id = reg_administrador.id_admin
            user_sesion.email= reg_administrador.email
            user_sesion.role=ROLE_ADMINISTRADOR 
            user_sesion.nombre = ""
            return verificado 
    
    return verificado 

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

def validar_none(mensaje:str,longitud:int):
    data = input (mensaje)
    while (len(data) > longitud) or data == "":
        data= input(f"La longitud que ingreso es mayor a la deseada vuelva a ingresar los datos [{longitud} max]: ")
    return data

def fn_validar_fecha():
    band  = True
    while band:
        fecha = input("Ingrese nueva fecha en formato YYYY-MM-DD: ").strip()
        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
            anio_actual = datetime.today().year
            mes_actual= datetime.today().month
            dia_actual= datetime.today().day
            if 1900 >= fecha_obj.year or fecha_obj.year >= anio_actual:
                print(f"\nEl año debe ser mayor a 1900 y menor o igual a {anio_actual}")
            else:
                band= False
        except ValueError:
            print("\nLa fecha debe tener el formato YYYY-MM-DD\n")
    return fecha

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

def fn_traer_registro(archivo_logico:io.BufferedRandom,pos:str,normalizador):
    try:
        archivo_logico.seek(pos)
        reg = pickle.load(archivo_logico)
        normalizador(reg)
        return reg
    except:
        print("Se genero un error en extraccion del archivo")

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
                    user_sesion.email = email_encontrado
            else:
                encontrado = posicion_actual
                user_sesion.email = email_encontrado
                
                    
    return encontrado

def fn_busquedasecuencial(archivo_logico: io.BufferedRandom, archivo_fisico: str, campo:str,data:int | str):
    tam_archivo = os.path.getsize(archivo_fisico)
    archivo_logico.seek(0)
    encontrado = False
    pos = -1

    while archivo_logico.tell() < tam_archivo and encontrado == False :
        pos = archivo_logico.tell()
        regtemporal = pickle.load(archivo_logico)
        if(str(getattr(regtemporal,campo)).strip() == str(data).strip()):
            encontrado = True   

    if(encontrado):
        return pos
    else:
        return -1

def fn_busqueda_secu(archivo_logico: io.BufferedRandom, archivo_fisico: str, nombre: str, id: int, email: str = False):
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

def fn_busquedasecuencial_like(data:int | str):
    tam_archivo = os.path.getsize(FISICO_ARCHIVO_LIKES)
    LOGICO_ARCHIVO_LIKES.seek(0)
    encontrado = False
    pos = -1

    while LOGICO_ARCHIVO_LIKES.tell() < tam_archivo and encontrado == False :
        pos = LOGICO_ARCHIVO_LIKES.tell()
        regtemporal:Like = pickle.load(LOGICO_ARCHIVO_LIKES)
        normalizar_likes(regtemporal)
        if(regtemporal.destinatario == data  and regtemporal.remitente == str(user_sesion.id)) :
            encontrado = True
               

    if(encontrado):
        return pos
    else:
        return -1

#--------------------------------------------------------------#
#                                                              #
#               PROCEDURES/FUNCIONES AUXILIARES                #
#                                                              #
#--------------------------------------------------------------#
def fn_diferencia_fechas(fecha1, fecha2):
    # Asegurarse de que fecha1 y fecha2 sean objetos datetime
    if isinstance(fecha1, str):
        fecha1 = datetime.strptime(fecha1, "%Y-%m-%d %H:%M:%S")
    if isinstance(fecha2, str):
        fecha2 = datetime.strptime(fecha2, "%Y-%m-%d %H:%M:%S")

    # Calcular la diferencia entre las fechas
    diferencia = abs(fecha2 - fecha1)

    # Segundos totales
    segundos_totales = int(diferencia.total_seconds())

    # Calcular días, horas, minutos y segundos
    dias = segundos_totales // 86400  # 86400 segundos en un día
    horas = (segundos_totales % 86400) // 3600  # 3600 segundos en una hora
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60

    # Mostrar resultados
    resultado = ""
    if dias > 0:
        
        resultado = f"{dias} día(s) "
    elif horas > 0:
        resultado = f"{horas} hora(s) "
    elif minutos > 0:
        resultado = f"{minutos} minuto(s) "
    elif segundos > 0:
        resultado = f"{segundos} segundo(s)"
    else:
        resultado ="1 segundo"

    
    return resultado

def fn_verificar_array_vacio(array:list,limite:int):
    vacio = True
    try:
        for i in range(0,limite):
            if(str(array[i]).strip() ==""):
                vacio = not(vacio)
        return vacio
    except:
        print("Se genero un error inesperado")
        return True

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

A = """
 -AAAAA  * BBBBB  *  CCCCC  * DDDDD  * EEEEE  * FFFFF  * GGGGG  * H   H  * IIIII  * JJJJJ  * K   K  * L      * M   M  * N   N  * OOOOO  * PPPPP  * QQQQQ  * RRRRR  * SSSSS  * TTTTT  * U   U  * V   V  * W   W  * X   X  * Y   Y  * ZZZZZ  
A     A * B    B * C       * D    D * E      * F      * G      * H   H  *   I    *     J  * K  K   * L      * MM MM  * NN  N  * O   O  * P    P * Q    Q * R    R * S      *   T    * U   U  * V   V  * W   W  *  X X   *  Y Y   *     Z  
AAAAAAA * BBBBB  * C       * D    D * EEEEE  * FFFFF  * G  GGG * HHHHH  *   I    *     J  * KKK    * L      * M M M  * N N N  * O   O  * PPPPP  * Q  Q Q * RRRRR  * SSSSS  *   T    * U   U  * V   V  * W W W  *   X    *   Y    *  ZZZ  
A     A * B    B * C       * D    D * E      * F      * G    G * H   H  *   I    * J   J  * K  K   * L      * M   M  * N  NN  * O   O  * P      * Q   QQ * R   R  *      S *   T    * U   U  *  V V   * W   W  *  X X   *   Y    * Z    
A     A * BBBBB  *  CCCCC  * DDDDD  * EEEEE  * F      *  GGGGG * H   H  * IIIII  *  JJJ   * K   K  * LLLLL  * M   M  * N   N  * OOOOO  * P      *  QQQ Q * R    R * SSSSS  *   T    *  UUU   *  V V   * W   W  * X   X  *   Y    * ZZZZZ
"""

def obtener_letra_en_grande(letra, arte_ascii):
    # Dividimos el arte ASCII en líneas
    lineas = arte_ascii.strip().split('\n')
    
    # Buscamos la letra en cada línea y extraemos su arte
    for i in range(len(lineas)):
        # Dividimos cada línea por las separaciones de '*'
        lineas[i] = lineas[i].split(' * ')
    
    # Obtenemos la posición de la letra en el alfabeto (A=0, B=1, etc.)
    posicion_letra = ord(letra.upper()) - ord('A')
    
    # Extraemos las líneas correspondientes a la letra
    letra_en_grande = []
    for i in range(5):  # Sabemos que el arte de cada letra tiene 5 líneas
        letra_en_grande.append(lineas[i][posicion_letra])
    
    
    return letra_en_grande

def fn_formatear_array(nuevo) -> list:
    descontar = 0

    # Contar los valores que no son None
    for i in range(len(nuevo)):
        if nuevo[i] != None:
            descontar += 1

    # Crear un nuevo array del tamaño adecuado
    nuevo_array = [None] * descontar
    # Índice para el nuevo array
    j = 0
    # Llenar el nuevo array con los valores que no son None
    for i in range(len(nuevo)):
        if nuevo[i] != None:
            nuevo_array[j] = nuevo[i]
            j += 1

    # Mostrar el nuevo array
    return nuevo_array

def draw_banner(characters, visible_up_to):
    # Obtener las dimensiones de la terminal
    def get_terminal_size():
        size = shutil.get_terminal_size(fallback=(80, 20))  # Valores predeterminados si no se puede obtener el tamaño
        return size.lines, size.columns

    letra=[
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_uppercase)
        ]

    letras =[
        obtener_letra_en_grande(letra[0], A),
        obtener_letra_en_grande(letra[1], A),
        obtener_letra_en_grande(letra[2], A)
        ]



    # Arte ASCII para caracteres grandes 
    ascii_art = {
        '4': letras[0],
        'A': letras[1],
        '2': letras[2]
    }


    # Obtener el tamaño de la terminal
    height, width = get_terminal_size()

    # Definir el alto del cartel como el 20% del alto de la terminal
    banner_height = max(10, int(height * 0.2))  # Mínimo de 10 líneas para acomodar caracteres grandes
    banner_width = width

    # Número de subdivisiones (igual al número de caracteres)
    divisions = len(characters)
    sub_width = banner_width // divisions

    # Crear el banner
    for i in range(banner_height):
        if i == 0 or i == banner_height - 1:
            # Primera y última línea del cartel (bordes superiores e inferiores)
            print('+' + '-' * (banner_width - 2) + '+')
        else:
            # Líneas internas con divisiones
            row = '|'
            for j in range(divisions):
                if j < visible_up_to:
                    char_art = ascii_art.get(characters[j], [' ' * 6] * 5)  # Arte ASCII o espacios si no existe el carácter
                    art_height = len(char_art)
                    art_line_start = (banner_height - 2 - art_height) // 2  # Ajuste vertical
                    art_line = i - 1 - art_line_start  # Línea ajustada para centrar verticalmente

                    if 0 <= art_line < art_height:
                        line = char_art[art_line]
                        padding = (sub_width - len(line) - 1) // 2  # Alinear en el centro de la subdivisión horizontalmente
                        row += ' ' * padding + line + ' ' * (sub_width - len(line) - padding - 1) + '|'
                    else:
                        row += ' ' * (sub_width - 1) + '|'
                else:
                    row += ' ' * (sub_width - 1) + '|'
            print(row)
    return letra

def animate_banner():
    characters =['4', 'A', '2']
    letras =[]
    for k in range(0,3):
        for i in range(1, len(characters) + 1):
            # Limpiar la consola antes de redibujar
            print("\033[H\033[J", end="")  # Limpiar consola (en sistemas compatibles con ANSI)
            letras = draw_banner(characters, i)        
            time.sleep(1 / 5)  # Animar en 1 segundo en total
        time.sleep(1)
    return letras

def pr_tabla(colsDate:list[str],data:list[str], limpiar=True):
    #cols=["CodLocal","Nombre","Estado"]
    # Obtener el tamaño de la terminal
    if(limpiar):
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

def fn_obtener_registros_en_array(ar_logico,ar_fisico,normalizador):
    cantidad_registros = fn_buscar_cantidad_de_registros(ar_logico,ar_fisico)
    registros = [None] * cantidad_registros
    t = os.path.getsize(ar_fisico)

    ar_logico.seek(0)
    i = 0
    while ar_logico.tell() < t and   i <  cantidad_registros:
        reg = pickle.load(ar_logico)
        normalizador(reg)
        registros[i] = reg
        i=i+1
    return registros

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
            
            fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, formatear_estudiantes)

def pr_precarga_de_reportes():
    cant_reportes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES)
    
    if not cant_reportes:
        for i in range(0, len(INIT_REPORTES)):
            reporte:Reporte = Reporte()
            reporte.id_reportante = INIT_REPORTES[i][0]
            reporte.id_reportado = INIT_REPORTES[i][1]
            reporte.razon_reporte = INIT_REPORTES[i][2]
            reporte.estado = INIT_REPORTES[i][3]
            
            fn_guardar_datos(reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, formatear_reportes)
        
#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES/PR PRINCIPALES                      #
#                                                              #
#--------------------------------------------------------------#

def fn_iniciar_sesion():
    global INTENTO_LOGIN
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
                user_sesion.role = 'E'
            elif es_moderador != -1:
                autenticado = True
                user_sesion.role = 'M'
            elif es_admin != -1:
                autenticado = True
                user_sesion.role = 'A'
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
#                  FUNCIONES/PR ESTUDIANTES                    #
#                                                              #
#--------------------------------------------------------------#

def fn_cuadricular_estudiantes(estudiantes:list[Estudiante],mostrar_id=False):
    descontar = 0
    longitud = 5

    if(mostrar_id):
        longitud = 6
    cantidad_registros = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES)

    estudiante_vista = [["" for _ in range(0,longitud)] for _ in range(0,cantidad_registros)]
    for k in range(0,cantidad_registros):
        if(estudiantes[k].estado != "B" and int(estudiantes[k].id_estudiantes) != int(user_sesion.id)):

            estudiante_vista[k][0]=estudiantes[k].nombre

            if(estudiantes[k].fecha_nacimiento != ""):
                estudiante_vista[k][1]=estudiantes[k].fecha_nacimiento
            else:
                estudiante_vista[k][1]="Sin datos"


            if(estudiantes[k].biografia != ""):
                estudiante_vista[k][2]=estudiantes[k].biografia
            else:
                estudiante_vista[k][2]="Sin datos"


            if(estudiantes[k].hobbies) != "":
                estudiante_vista[k][3]=estudiantes[k].hobbies
            else:
                estudiante_vista[k][3]="Sin datos"

            if(estudiantes[k].ultima_conexion) != "":
                ultima_conexion=datetime.strptime(estudiantes[k].ultima_conexion, "%Y-%m-%d %H:%M:%S.%f")
                estudiante_vista[k][4]=fn_diferencia_fechas(ultima_conexion,datetime.now())
            else:
                estudiante_vista[k][4]="Sin datos"

            if(mostrar_id):
                estudiante_vista[k][5]=str(int(estudiantes[k].id_estudiantes) + 1) 

        else:
            descontar = descontar + 1
    
    #* EN ESTE BLOQUE SE LIMPIAN LOS ESTUDIANTES QUE NO CUMPLEN CON EL PROGRAMA LOS DADOS DE BAJA Y SI MISMO 
    #estudiante_limpio = [["" for _ in range(0,longitud)] for _ in range(0,cantidad_registros-descontar)]
   
    estudiante_limpio = []
    for h in range(0,len(estudiante_vista)):
        if(estudiante_vista[h][0] != ""):
            estudiante_limpio.append(estudiante_vista[h])
    
    return estudiante_limpio

def fn_verificar_like():
    all_likess:list[Like] = fn_obtener_registros_en_array(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,normalizar_likes)
    mis_likes =[]
    if(len(all_likess) != 0):
        for i in range(len(all_likess)):
            if(str(all_likess[i].remitente) == str(user_sesion.id)):
                mis_likes.append(all_likess[i])
    return mis_likes

def fn_obtener_informacion_de_likes():
    "[0]: Matcheados [1]:Likes recibidos y no respondidos [2]:Likes dados y no recibidos"
    matchs = 0
    all_likess:list[Like] = fn_obtener_registros_en_array(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,normalizar_likes)

    R:list[Like] = [None]*len(all_likess)
    D:list[Like] = [None]*len(all_likess)
    M:list[Like] = [None]*len(all_likess)
    
    for i in range(0,len(all_likess)):
        if(str(all_likess[i].remitente) == str(user_sesion.id)):
            R[i] =  all_likess[i]
        elif(str(all_likess[i].destinatario) == str(user_sesion.id)):
            D[i] = all_likess[i]

    R=fn_formatear_array(R)
    D=fn_formatear_array(D)
    
    for k in range(0,len(R)):
      for h in range(0,len(all_likess)):
        if(R[k].destinatario == all_likess[h].remitente and R[k].remitente == all_likess[h].destinatario and R[k].remitente != all_likess[h].remitente):
            M[k] = R[k]
            matchs = matchs +1

    M=fn_formatear_array(M)
    
    return [len(M),len(D)-matchs,len(R)-matchs]

def fn_obtener_likes():
    "Te devuelve los likes del usuario logeado"
    cantidad = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES)
    registros = [None]* cantidad
    registro2 = [None]* cantidad



    descontar = 0
    t = os.path.getsize(FISICO_ARCHIVO_LIKES)
    LOGICO_ARCHIVO_LIKES.seek(0)
    index = 0
    while LOGICO_ARCHIVO_LIKES.tell() < t:
        reg_like:Like = pickle.load(LOGICO_ARCHIVO_LIKES)
        normalizar_likes(reg_like) 
        if(str(reg_like.remitente) == str(user_sesion.id)):
            registros[index] = reg_like 
        elif(str(reg_like.destinatario) == str(user_sesion.id)):
            registro2[index] = reg_like 
        else:
            descontar = descontar + 1            
        index= index + 1  
    
    
    registros = fn_formatear_array(registros)
    registro2 = fn_formatear_array(registro2)
    
    return registros

def fn_verificar_si_existe_like(id_destinatario):
    reg_likes:list[Like] = fn_obtener_likes()
    indice = -1
    for i in range(0,len(reg_likes)):
        if(reg_likes[i].destinatario == id_destinatario):
            #SI ESTO EXISTE SE VERA VERIFICAR QUE EL USUARIO DECIDA CAMBIAR A ESTADO DESCATIVADO
            indice = i
    
    if(indice == -1):
        return []

    else:
        return [reg_likes[i]]

def pr_ver_candidatos():
    def fn_insertar_likes(est:list[Estudiante]):        
        nuevo_array = [["" for _ in range(0,7)] for _ in range(0,len(est))]
        likes:list[Like]= fn_verificar_like()

        for i in range(0,len(est)):
            nuevo_array[i][0] = est[i][0]
            nuevo_array[i][1] = est[i][1]
            nuevo_array[i][2] = est[i][2]
            nuevo_array[i][3] = est[i][3]
            nuevo_array[i][4] = est[i][4]
            nuevo_array[i][5] = est[i][5]
            nuevo_array[i][6] = "Sin like"

        for h in range(0,len(nuevo_array)):
            for t in range(0,len(likes)):

                if(int(nuevo_array[h][5])-1 == int(likes[t].destinatario) and likes[t].estado):
                    nuevo_array[h][6] = "Like dado"
        return nuevo_array

    estudiantes = fn_obtener_registros_en_array(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,normalizar_estudiante)
    if(len(estudiantes) ==0):
        pr_crear_titulo("No existen candidatos")
        print("")
        return pr_pausar_consola() 

    
    estudiante_vista = fn_cuadricular_estudiantes(estudiantes,True)
    estudiante_vista= fn_insertar_likes(estudiante_vista)
    

    estudiantes_columnas= ["Nombre","F.Nacimiento","Biografia","Hobbies","Ult.Conexion","ID","Like"]
    pr_crear_titulo("CANDIDATOS")
    print("")
    pr_tabla(estudiantes_columnas,estudiante_vista,False)


    nombre = input("\nIngrese un nombre valido con quien desea hacer match [S-Salir]: ")
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"nombre",nombre)
    while nombre != "S" and pos == -1:
        nombre = input("\nIngrese un nombre valido con quien desea hacer match [S-Salir]: ")
        pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"nombre",nombre)

    if(nombre == "S" ):
        return    


    #TIENE QUE HABER UNA VALIDACION DE LIKE 
    #CON EL REGISTRO PODRIAMOS BUSCAR EL LIKE DEL LIKEADO 

    borro = False
    reg_likeado:Estudiante = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)
    like_repetido = fn_verificar_si_existe_like(reg_likeado.id_estudiantes)
    if(len(like_repetido) > 0):
        #ENCONTRO UN LIKE
        if(like_repetido[0].estado):
            print("Desea quitar su like?")
        else:
            print("Usted antes ya le habia dado like, desea volver activarlo? ")

        si_no_like= fn_validar_si_no()
        if(si_no_like == "si"):
            pos = fn_busquedasecuencial_like(like_repetido[0].destinatario)
            like_repetido[0].estado = not(like_repetido[0].estado) 
            fn_guardar_datos(like_repetido[0],LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,formatear_likes,pos)
            input("Su like se ha actualizado correctamente")
            borro =not(borro)
    
    pr_crear_titulo("CANDIDATOS")
    print("")
    pr_tabla(estudiantes_columnas,estudiante_vista,False)
    
    if(borro):
        return ""

    print("\nSu like esta a punto de ser enviado esta seguro de esta accion? Si-[ACEPTAR] No-[CANCELAR] \n")
    si_no= fn_validar_si_no()
    
    if(si_no == "si"):
        like = Like()
        print("Su like ha sido enviado. ")
        reg_est:Estudiante = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)

        like.destinatario = reg_est.id_estudiantes
        like.remitente = user_sesion.id

        fn_guardar_datos(like,LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,formatear_likes)        
    else:
        print("Su like fue cancelado con exito.")
        
    input("")
    
def pr_crear_estudiantes():
    ver_contraseña = False
    contraseña=""
    estudiante = Estudiante()
    columnas = ["Email","Contraseña","Nombre","Sexo"]
    estudiante_ram = [["","","",""]]
    pr_tabla(columnas,estudiante_ram,True)
    opc = -1
    while opc != 0 and opc != 5:
        print("\n1-Email \n\n2-Contraseña \n\n3-Nombre \n\n4-Sexo \n\n5-Guardar datos \n\n0-Volver\n")
        opc = fn_validar_rango(0,5)
        match(opc):
            case(1):
                pr_tabla(columnas,estudiante_ram)
                email=input("Ingrese su email: ")
                while fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"email",str(email).lower()) != -1:  
                    print("El email ingresado no es valido ya que existe una persona ")
                    email = input("Ingrese su email: ")

                estudiante_ram[0][0] = email
            case(2):
                pr_tabla(columnas,estudiante_ram)                

                contraseña =""
                while len(contraseña) < 8 and contraseña != "S":
                    contraseña = input(f"[0]-{"Ver" if ver_contraseña else "Ocultar" } [S]-Volver || Ingrese su contraseña: ")

                    #SE LE VUELVE A PEDIR LA CONTRASEÑA AL USUARIO YA QUE NO CUMPLE CON LAS CONDICIONES
                    if(len(contraseña) < 8 and contraseña != "0" and contraseña != "S" ):
                        print("\nNecesita ingresar una contraseña mayor a 8 caracteres")
                        pr_pausar_consola()
                        pr_tabla(columnas,estudiante_ram)

                    
                    #SI INGRESA UNA CONTRASEÑA MAYOR A LA LONGITUD REQUERIDA
                    if(len(contraseña) >= 8):
                        estudiante.contrasena = contraseña
                        estudiante_ram[0][1] = estudiante.contrasena
                        pr_tabla(columnas,estudiante_ram)
                    
                     #SI INGRESA 0 SE CAMBIA EL ESTADO DE [VER CONTRASEÑA] PARA QUE REFRESQUE EN MEMORIA LA CONTRASEÑA
                    if(contraseña == "0"):
                        
                        if(ver_contraseña):
                            estudiante_ram[0][1] = estudiante.contrasena

                        if(not(ver_contraseña)):
                            estudiante_ram[0][1] = "*******"

                        ver_contraseña= not(ver_contraseña)
                        pr_tabla(columnas,estudiante_ram)
            case(3):
                pr_tabla(columnas,estudiante_ram)
                nombre = input("Ingrese su nombre: ")
                while fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"nombre",nombre)  != -1 :
                    nombre = input("Este nombre ya existe, ingrese uno nuevo:")
                estudiante_ram[0][2] = nombre
            case(4):
                pr_tabla(columnas,estudiante_ram)
                sexo = input("Ingrese su sexo: ")
                estudiante_ram[0][3] = sexo
            case(5):
                if estudiante_ram[0][0] and estudiante_ram[0][1] and estudiante_ram[0][2] and estudiante_ram[0][3]:
                    pr_tabla(columnas,estudiante_ram)
                    print(f"\n\n¿Desea guardar su datos? Los datos ha guardarse son los indicados arriba 🔼")
                    si_no = fn_validar_si_no()
                    if(si_no == "si"):
                        #AGREGAR UNA CANCELACION POR SI SE ARREPIENTE DE CREAR LA CUENTA
                        estudiante.email = email
                        estudiante.nombre = nombre
                        estudiante.sexo= sexo
                        estudiante.id_estudiantes= fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES)
                        estudiante.ultima_conexion= datetime.now()
                        estudiante.estado=True
                        fn_guardar_datos(estudiante,LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,formatear_estudiantes)
                    else:
                        opc =-1
                else:
                    opc =-1
                    print("Debe rellenar todos los datos")
                    pr_pausar_consola()
            case(0):
                ""
        pr_tabla(columnas,estudiante_ram)

def pr_eliminar_perfil():
    pr_limpiar_consola()
    #VAMOOS A MOSTRAR UNA CUADRILLA CON EL PERFIL
    pr_crear_titulo("Eliminar perfil")
    print("\nDesea eliminar su perfil?\n ")
    si_no = fn_validar_si_no()

    if(si_no =="si"):
        print("\nSe le presentara un captcha en la pantalla porfavor ingrese las letras que corresponden\n")
        pr_pausar_consola()
        letras = animate_banner()
        letras_str = letras[0]+letras[1]+letras[2]
        intento = input("Ingrese las letras mostradas en patanlla (Las mayusculas con las minusuculas son indistinguibles): ").upper()
        if(letras_str == intento):
            print("\nSu perfil se eliminara muchas gracias por estar con nosotros vuelva pronto.\n")
            pr_pausar_consola()

            #TODO: CAMBIAR POR BUSQUEDA DICTOMICA EN VEZ DE SECUENCIAL 
            pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"id_estudiantes",user_sesion.id)
            reg:Estudiante = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)
            reg.estado = "B"
            fn_guardar_datos(reg,LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,formatear_estudiantes,pos)
            user_sesion.estado = False
        else:
            print("\nUsted ingreso mal sus letras mostradas en pantalla, para volver a intentar eliminar su perfil ingrese nuevamente a este menu.\n")
            pr_pausar_consola()

    else:
        print("\nSera devuelto al menu principal, le agradecemos por quedarse con nosotros.\n")
        pr_pausar_consola()

def pr_editar_datos_personales():
    try:
        pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"id_estudiantes",user_sesion.id)
        reg:Estudiante = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)
    except:
        print("Se genero un error en recuperar el usuario, Vuelva a iniciar el programa...")
        return  pr_pausar_consola()
        
    datos_personales:list = [""]*11
    #DATOS PRIMARIOS
    datos_personales[0] = reg.nombre
    datos_personales[1] = reg.sexo
    datos_personales[2] = reg.pais
    datos_personales[3] = reg.ciudad
    datos_personales[4] = reg.fecha_nacimiento

    #DATOS SECUNDARIOS
    if(reg.hobbies!=""):
        datos_personales[5] = reg.hobbies
    else:
        datos_personales[5] = "Sin datos"

    if(reg.materia_favorita!=""):
        datos_personales[6] = reg.materia_favorita
    else:
        datos_personales[6] = "Sin datos"

    if(reg.deporte_favorito != ""):
        datos_personales[7] = reg.deporte_favorito
    else:
        datos_personales[7] = "Sin datos"

    if(reg.materia_fuerte != ""):
        datos_personales[8] = reg.materia_fuerte
    else:
        datos_personales[8] = "Sin datos"

    if(reg.materia_debil != ""):
        datos_personales[9] = reg.materia_debil
    else:
        datos_personales[9] = "Sin datos"

    if(reg.biografia != ""):
        datos_personales[10] = reg.biografia
    else:
        datos_personales[10] = "Sin datos"

    def pr_guardar_datos():
        print("Desea guardar sus datos? ")
        si_no = fn_validar_si_no()
        if(si_no=="si" ):
            reg.nombre =  datos_personales[0] 
            reg.sexo =  datos_personales[1] 
            reg.pais =  datos_personales[2] 
            reg.ciudad =  datos_personales[3] 
            reg.fecha_nacimiento =  datos_personales[4] 
            reg.hobbies =  datos_personales[5] 
            reg.materia_favorita =  datos_personales[6] 
            reg.deporte_favorito =  datos_personales[7] 
            reg.materia_fuerte =  datos_personales[8] 
            reg.materia_debil =  datos_personales[9] 
            reg.biografia  = datos_personales[10]
            fn_guardar_datos(reg,LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,formatear_estudiantes,pos)
            print("Su datos se guardaron correctamente...")
            pr_pausar_consola()
        
        

    def pr_editar_datos_secundarios():
        opc = ""
        while opc != "v":
            pr_crear_titulo("DATOS SECUNDARIOS")
            print("")
            pr_tabla(["Hobbie","Materia Fav","Deporte Fav","Materia 💪","Materia Debil","Biografia"],[datos_personales[-6:]],False)
            print("\n[A].Hobbie \n\n[B].Materia Favorita \n\n[C].Deporte Favorito \n\n[D].Materia Fuerte \n\n[E].Materia Debil \n\n[F].Biografia \n\n[G].Guardar datos \n\n[V].Volver ")
            print("")
            opc = fn_validar_rango_str("a","v")
            match(opc):
                case("a"):
                    hobbie = input ("Ingrese su hobbie: ")
                    datos_personales[5]=hobbie
                case("b"):
                    materia_fav=input("Ingrese materia favorita: ")
                    datos_personales[6]=materia_fav
                case("c"):
                    deporte_fav=input("Ingres deporte favorito: ")
                    datos_personales[7]=deporte_fav
                case("d"):
                    materia_fue=input("Ingrese su materia fuerte: ")
                    datos_personales[8]=materia_fue
                case("e"):
                    materia_deb= input("Ingrese su materia debil: ")
                    datos_personales[9]=materia_deb
                case("f"):
                    biografia=input("Ingrese su biografia: ")
                    datos_personales[10]=biografia
                case ("g"):
                    pr_guardar_datos()
                case _:
                    ""
                
    opc=""
    while opc != "v": 
        pr_crear_titulo("EDITAR DATOS PERSONALES")
        print("")

        pr_tabla(["Nombre","Sexo","Pais","Ciudad","Fecha de nacimiento"],[datos_personales[:-6]],False)
        print("\n[A].Nombre \n\n[B].Sexo \n\n[C].Pais \n\n[D].Ciudad \n\n[E].Fecha de nacimiento \n\n[F].Datos Secundarios \n\n[G].Guardar Datos \n\n[V].Volver\n\n")

        opc=input("Ingrese una opcion: ")
        match(opc):
            case("a"):

                nombre = input("Ingrese su nombre: ")
                while fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"nombre",nombre)  != -1 :
                    nombre = input("Este nombre ya existe, ingrese uno nuevo:")
                
                datos_personales[0] = nombre
            case("b"):
                sexo = input("Ingrese su sexo: ")
                datos_personales[1] = sexo
            case("c"):
                pais = input ("Ingrese su nacionalidad: ")
                datos_personales[2] = pais
            case("d"):
                ciudad = input("Ingrese su ciudad: ")
                datos_personales[3] = ciudad
            case("e"):
                fecha  = ""
                datos_personales[4] = fecha
            case ("f"):
                pr_editar_datos_secundarios()       
            case ("g"):
                pr_guardar_datos()
            case("v"):
                ""
                

def pr_gestionar_perfil():
    opc = ""

    while opc != "c" and user_sesion.estado:
        pr_limpiar_consola()  
        pr_crear_titulo("Gestionar mi perfil")
        print("\na. Editar mi datos personales\n \nb. Eliminar mi perfil\n \nc. Volver\n")
        opc = fn_validar_rango_str("a","c")
        match(opc):
            case("a"):
                pr_editar_datos_personales()
            case("b"):
                pr_eliminar_perfil()
            case _:
                ""

def pr_reportar_candidatos():
    pr_crear_titulo("Reportar Candidato")

    estudiantes = fn_obtener_registros_en_array(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,normalizar_estudiante)
    estudiante_vista = fn_cuadricular_estudiantes(estudiantes,True)
    estudiantes_columnas= ["Nombre","F.Nacimiento","Biografia","Hobbies","Ult.Conexion","ID"]
    print("")

    pr_tabla(estudiantes_columnas,estudiante_vista,False)
    
    print("\nIngrese el id del reportante [0-Salir]\n")
    id = fn_validar_rango(0,fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES))
    while fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"id_estudiantes",id - 1) != -1 and id == 0:
        id = fn_validar_rango(0,fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES))

    if(id == 0):
        return

    motivo =input("\nIngrese el motivo del reporte: ")
    
    print("\n¿Esta seguro de mandar el reporte?\n")
    si_no = fn_validar_si_no()
    if(si_no == "si"):
        reg_reporte = Reporte()
        reg_reporte.id_reportante = user_sesion.id 
        reg_reporte.id_reportado= (id - 1) 
        reg_reporte.razon_reporte = motivo
        fn_guardar_datos(reg_reporte,LOGICO_ARCHIVO_REPORTES,FISICO_ARCHIVO_REPORTES,formatear_reportes)
        print("\nSu reporte ha sido enviado correctamente...\n")
        pr_pausar_consola()

    else:
        pr_crear_titulo("Reportar Candidato")
        print("Su reporte se ha eliminado volviendo al menu principal...")
        pr_pausar_consola()
def pr_gestionar_candidatos():
    opc = ""
    while opc != "c":
        pr_limpiar_consola()  
        pr_crear_titulo("Gestionar Candidatos")
        print("\na. Ver candidatos\n \nb. Reportar candidatos\n \nc. Volver\n")
        opc = fn_validar_rango_str("a","c")
        match(opc):
            case("a"):
                pr_ver_candidatos()            
            case("b"):
                pr_reportar_candidatos()
            case _:
                ""

def pr_reporte_estadisticos():
    pr_limpiar_consola()  
    pr_crear_titulo('REPORTES ESTADISTICOS')
    reportes:list = fn_obtener_informacion_de_likes()
    print("Matcheados sobre el % posible: ",reportes[0])
    print("Likes dados y no recibidos: ",reportes[2])
    print("Likes recibidos y no respondidos: ",reportes[1])
    
    input("c-Salir")
        

def pr_menu_estudiantes():
    opc = -1
    
    while opc != 0 and user_sesion.estado:
        pr_limpiar_consola()         
        pr_crear_titulo("Menu principal")
        print("\n1. Gestionar mi perfil\n \n2. Gestionar candidatos\n \n3. Matcheos\n \n4. Reportes estadísticos\n \n0. Salir\n")
        opc = fn_validar_rango(0, 4)
        match opc:
            case 1:
                pr_gestionar_perfil()
            case 2:
                pr_gestionar_candidatos()
            case 3:
               pr_cartel_construccion()
               
            case 4:
                pr_reporte_estadisticos()
            case _:
                ""

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
                fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, formatear_estudiantes, pos_encontrado)
                
                desactivado = True
            
            else:
                print("No se encontro usuario, intente nuevamente.")
                
        except ValueError:
            pos_encontrado = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, opc, "")
        
            if pos_encontrado != -1:
                LOGICO_ARCHIVO_ESTUDIANTES.seek(pos_encontrado)
                
                estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
                estudiante.estado = False
                fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, formatear_estudiantes, pos_encontrado)
                
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
    fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, formatear_estudiantes, pos_encontrado)
      
def fn_ver_reportes():
    cant_reportes = 0
    tam_reportes = os.path.getsize(FISICO_ARCHIVO_REPORTES)
    
    contador = 1
    
    LOGICO_ARCHIVO_REPORTES.seek(0)
    
    while LOGICO_ARCHIVO_REPORTES.tell() < tam_reportes:
        reporte:Reporte = pickle.load(LOGICO_ARCHIVO_REPORTES)
        
        estado_formateado = reporte.estado.strip()
        
        if estado_formateado == "0":
            cant_reportes+=1
    
    LOGICO_ARCHIVO_REPORTES.seek(0)
    
    while LOGICO_ARCHIVO_REPORTES.tell() < tam_reportes and contador != -1:
        pr_limpiar_consola()
        pr_crear_titulo(f"Reporte {contador}/{cant_reportes}")
        
        posicion_actual = LOGICO_ARCHIVO_REPORTES.tell()
        
        registro_reporte:Reporte = pickle.load(LOGICO_ARCHIVO_REPORTES)
        
        id_reportante = registro_reporte.id_reportante.strip()
        id_reportado = registro_reporte.id_reportado.strip()
              
        #REPORTANTE
        reportante_pos = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", int(id_reportante))
        LOGICO_ARCHIVO_ESTUDIANTES.seek(reportante_pos)
        reportante:Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
        reportante_estado = reportante.estado.strip()
        
        #REPORTADO
        reportado_pos = fn_busqueda_secu(LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, "", int(id_reportado))
        LOGICO_ARCHIVO_ESTUDIANTES.seek(reportado_pos)
        reportado:Estudiante = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
        reportado_estado = reportado.estado.strip()
        
        #MODERADOR
        mod_pos = fn_busqueda_secu(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, "", "", user_sesion.email.strip())
        LOGICO_ARCHIVO_MODERADORES.seek(mod_pos)
        moderador:Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
        
        reportes_totales_formateado = int(moderador.reportes_totales.strip())
        reportes_aceptados_formateado = int(moderador.reportes_aceptados.strip())
        reportes_ignorados_formateado = int(moderador.reportes_ignorados.strip())
        
        if reportado_estado == "True" and reportante_estado == "True":
            if registro_reporte.estado.strip() == "0":
                print(f"\nID_REPORTANTE: {id_reportante}")
                print(f"ID_REPORTADO: {id_reportado}")
                print(f"MOTIVO: {registro_reporte.razon_reporte.strip()}")
                print(f"ESTADO: {registro_reporte.estado.strip()}")                
                print("\nIngrese una accion: ")
                print("\na-Ignorar reporte\n\nb-Bloquear al reportado\n\nc-Salir\n\n")
                opc = fn_validar_rango_str("a", "c")
                
                match opc:
                    case 'a':
                        registro_reporte.estado = 2
                        fn_guardar_datos(registro_reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, formatear_reportes, posicion_actual)
                        moderador.reportes_totales = reportes_totales_formateado + 1
                        moderador.reportes_ignorados = reportes_ignorados_formateado + 1
                        fn_guardar_datos(moderador, LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, lj_moderadores, mod_pos)\
                        
                        contador +=1
                        
                    case 'b':
                        registro_reporte.estado = 1
                        fn_desactivar_usu_reportado(int(id_reportado))
                        fn_guardar_datos(registro_reporte, LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES, formatear_reportes, posicion_actual)
                        moderador.reportes_totales = reportes_totales_formateado + 1
                        moderador.reportes_aceptados = reportes_aceptados_formateado + 1
                        fn_guardar_datos(moderador, LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, lj_moderadores, mod_pos)
                        pr_limpiar_consola()
                        pr_crear_titulo(f"Usuario {reportado.email} bloqueado con exito")
                        
                        print("\na-Continuar\n")
                        opc = fn_validar_rango_str("a", "a")
                        
                        contador +=1
                        
                    case 'c':
                        contador = -1

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
            fn_guardar_datos(estudiante, LOGICO_ARCHIVO_ESTUDIANTES, FISICO_ARCHIVO_ESTUDIANTES, formatear_estudiantes, pos_estudiante)

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

def fn_dar_de_alta_mod():
    cant_moderadores = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES)
    tam_reg = os.path.getsize(FISICO_ARCHIVO_MODERADORES)
    
    activado = False
    
    def fn_mostrar_moderadores():
        columnas = [""]*3
        def pr_cargar_columnas():
            columnas[0] = "UID"
            columnas[1] = "EMAIL"
            columnas[2] = "ESTADO"
        
        personas = [[""]*3 for _ in range (cant_moderadores)]
        pr_cargar_columnas()
        
        LOGICO_ARCHIVO_MODERADORES.seek(0)
        
        contador = 0
        
        while LOGICO_ARCHIVO_MODERADORES.tell() < tam_reg:
            reg: Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
            
            estado_formateado = reg.estado.strip()
            
            if estado_formateado == "false":
                personas[contador][0] = reg.id_moderador
                personas[contador][1] = reg.email
                personas[contador][2] = reg.estado
                
                contador +=1
        
        if contador != 0:
            pr_tabla(columnas, personas)
        
        return contador
    
    while not activado:
        if fn_mostrar_moderadores() == 0:
            pr_crear_titulo("Todos los moderadores estan activados")
            print("\nb-Volver\n\n")
        
            opc = fn_validar_rango_str('b', 'b')

            match opc:
                case 'b':
                    activado = True
                    return activado
        
        opc = input("Ingrese email de moderador a activar: ")
        
        pos_moderador = fn_busqueda_secu(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, "", "", opc)
        
        while pos_moderador == -1:
            print("No se encontro moderador asociado a ese email.")
            opc = input("Ingrese email de usuario a eliminar: ")
            pos_moderador = fn_busqueda_secu(LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, "", "", opc)
        
        LOGICO_ARCHIVO_MODERADORES.seek(pos_moderador)
        
        moderador:Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
        moderador.estado = True
        fn_guardar_datos(moderador, LOGICO_ARCHIVO_MODERADORES, FISICO_ARCHIVO_MODERADORES, lj_moderadores, pos_moderador)
        
        activado = True       
    
    if activado:
        print("Moderador activado con exito.")
        print("\na-Activar otro moderador\n\nb-Volver\n\n")
        
        opc = fn_validar_rango_str('a', 'b')
        
        match opc:
            case 'a':
                fn_dar_de_alta_mod()
            case 'b':
                return activado
    
    return activado

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
                fn_dar_de_alta_mod()
            case 'c':
                band = False
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
    pr_limpiar_consola()
    pr_crear_titulo("REPORTES ESTADISTICOS")
    
    cant_reportes = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_REPORTES, FISICO_ARCHIVO_REPORTES)
    cant_reportes_ignorados = 0
    cant_reportes_aceptados = 0
    
    tam_reg_reportes = os.path.getsize(FISICO_ARCHIVO_REPORTES)
    tam_reg_mod = os.path.getsize(FISICO_ARCHIVO_MODERADORES)
    
    cant_vistos = 0
    cant_aceptados = 0
    cant_ignorados = 0
    
    global mod_mas_vistos
    global mod_mas_aceptados
    global mod_mas_ignorados
    
    LOGICO_ARCHIVO_REPORTES.seek(0)
    
    while LOGICO_ARCHIVO_REPORTES.tell() < tam_reg_reportes:
        reg:Reporte = pickle.load(LOGICO_ARCHIVO_REPORTES)
        
        estado_formateado = reg.estado.strip()
        
        if estado_formateado == '1':
            cant_reportes_aceptados+=1
        
        if estado_formateado == '2':
            cant_reportes_ignorados+=1
    
    
    if cant_reportes_ignorados == 0 and cant_reportes_aceptados == 0:
        print("\nAun no se han revisado reportes")
        print("\nb-Volver\n")
        
        opc = fn_validar_rango_str("b", "b")
        
        if opc == 'b':
            return True
        
    porc_aceptados = f"{(cant_reportes_aceptados * 100) / cant_reportes} %"
    porc_ignorados = f"{(cant_reportes_ignorados * 100) / cant_reportes} %"
    
    LOGICO_ARCHIVO_MODERADORES.seek(0)
    
    while LOGICO_ARCHIVO_MODERADORES.tell() < tam_reg_mod:
        moderador:Moderador = pickle.load(LOGICO_ARCHIVO_MODERADORES)
        
        cant_t = int(moderador.reportes_totales.strip())
        cant_a = int(moderador.reportes_aceptados.strip())
        cant_i = int(moderador.reportes_ignorados.strip())

        email = moderador.email.strip()
        
        if cant_a > cant_aceptados:
            cant_aceptados = cant_a
            mod_mas_aceptados = email
        
        if cant_t > cant_vistos:
            cant_vistos = cant_t
            mod_mas_vistos = email
        
        if cant_i > cant_ignorados:
            cant_ignorados = cant_i
            mod_mas_ignorados = email
    
    print(f"Reportes totales: {cant_reportes}")
    print(f"Reportes aceptados: {porc_aceptados}")
    print(f"Reportes ignorados: {porc_ignorados}")
    print(f"Moderador con mas reportes vistos: {mod_mas_vistos}({cant_vistos})")
    
    if cant_ignorados > 0:
        print(f"Moderador con mas reportes ignorados: {mod_mas_ignorados}({cant_ignorados})")
        
    if cant_aceptados > 0:
        print(f"Moderador con mas reportes aceptados: {mod_mas_aceptados}({cant_aceptados})")
    
    print("\nb-Volver\n")
    opc = fn_validar_rango_str("b", "b")
    
    if opc == 'b':
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
def pr_iniciar_sesion():
    pr_limpiar_consola()
    intento = 1
    
    pr_precarga_de_reportes()
    pr_precarga_de_registros()

    pr_crear_titulo("Iniciar sesion")
    email = input ("\nIngrese su correo electronico: ")
    contrasena = input("\nIngrese su contraseña: ")
    autenticado = pr_verificar_usuario(email,contrasena)
    while (intento < 3 and not (autenticado)):
        pr_limpiar_consola()
        pr_crear_titulo("Iniciar sesion")

        print(f"\nEl email o la contraseña no fueron encontradas. Ingresos restantes: {3 - intento}")
        email = input ("\nIngrese nuevamente su email: ")

        contrasena = input("\nIngrese su contraseña:  ")

        autenticado = pr_verificar_usuario(email,contrasena)
        
        intento = intento + 1 
    
    if(user_sesion.role == ROLE_USUARIO):
        pr_menu_estudiantes()
    elif(user_sesion.role == ROLE_MODERADOR):
        fn_menu_mod()
    elif(user_sesion.role == ROLE_ADMINISTRADOR):
        fn_menu_admin()

def pr_registrarse():
    pr_crear_estudiantes()

def pr_inicializar_programa():
    pr_precarga_de_registros()
    # pr_precarga_de_reportes()
    
    opc = -1
    while opc != 0:
        pr_limpiar_consola()
        pr_crear_titulo("⭐ BIENVENIDO ⭐ ")
        print("\n1 - Loguearse\n \n2 - Registrarse\n \n0 - Salir\n\n\n")
        opc = fn_validar_rango(0,2)
        match opc:
            case(1):
                pr_iniciar_sesion()
            case(2):
                pr_registrarse()
            case _:
                print("Gracias por estar con nosotros finalizando programa...\n")
                pr_pausar_consola()

pr_inicializar_programa()

# def debugger():
#     pr_precarga_de_reportes()
#     pr_precarga_de_registros()
#     fn_reportes_estadisticos()
    
# debugger()