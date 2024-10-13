import os 
import pickle 
import io
import shutil
import time
from datetime import datetime
import random
import locale 
import time 
import getpass
import string




#from typing import Callable

#--------------------------------------------------------------#
#                                                              #
#              CONSTANTES Y VARIABLES GLOBALES                 #
#                                                              #
#--------------------------------------------------------------#

CARPETA = "archivos"
fecha_actual = str(datetime.today().date())
ROLE_USUARIO="U"
ROLE_MODERADOR="M"
ROLE_ADMINISTRADOR="A"

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
        self.ultima_conexion = ""
        self.clave_recuperacion = "" 

class Usuario:
    def __init__(self):
        self.id = 1
        self.email = ""
        self.nombre= ""
        self.role = ""
        self.estado = True
       
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

# Crear la instancia del usuario genérico
user_sesion = Usuario()



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
    x.ultima_conexion=str(x.ultima_conexion).ljust(50)
    x.clave_recuperacion = str(x.ultima_conexion).ljust(80)

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
#                NORMALIZADORES                                #
#                                                              #
#--------------------------------------------------------------#


def normalizar_estudiante(x:Estudiantes):
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

def normalizar_likes(x:Likes):
    x.destinatario=str(x.destinatario).strip()
    x.remitente=str(x.remitente).strip()

#--------------------------------------------------------------#
#                                                              #
#                FUNCIONES DE VALIDACION DE DATOS              #
#                                                              #
#--------------------------------------------------------------#

"var: respuesta = tipo string"
def fn_validar_si_no():
    respuesta=input("Ingrese si o no: ").lower() 
    while (respuesta != "si") and  (respuesta.lower() != "no"):
        print("No es un opción valida, ingrese si o no")
        respuesta=input("Ingrese si o no: ").lower()
    return respuesta

"var: numero, inicio, limite = tipo interger"
def fn_validar_rango(inicio: int, limite: int):
    try:
        numero =int(input(f"Ingrese una opción [{inicio}-{limite}]: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input(f"Ingrese una opción [{inicio}-{limite}]: "))
        return numero
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio, limite)

"var: inicio, limite, opc = tipo string"
def fn_validar_rango_str(inicio: str, limite: str):
    opc = input("Ingrese una opcion:").lower()

    while not(opc >= inicio and opc <=limite and len(opc) == 1):
        print("\nError, ingrese una opcion valida.\n")
        opc = input("Ingrese una opcion: ")

    return opc


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
        archivo_logico.seek(0)

    except (ValueError, TypeError):
        print("Se genero un error")

def fn_buscar_cantidad_de_registros(archivo_logico: io.BufferedRandom, archivo_fisico: str):
    cantidad = 0   
    tam_arch = os.path.getsize(archivo_fisico) 
    if tam_arch != 0:
        archivo_logico.seek(0)
        pickle.load(archivo_logico)
        longitud_reg = archivo_logico.tell()
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


#--------------------------------------------------------------#
#                                                              #
#                 FUNCIONES AUXILIARES                         #
#                                                              #
#--------------------------------------------------------------#
def verificar_like(id_remitente,id_destinatario):
    ""

def verificar_match(reg):
    ""


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
# Animar el cartel mostrando los números uno por uno
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




"var: numerColsDate, columnas, filas, space = tipo interger"
"var: tamano_termina = tipo float"
"var: techo, pared, header = tipo string"
def pr_tabla(colsDate: list[str], data: list[str],limpiar=True):
    #cols=["CodLocal", "Nombre", "Estado"]
    # Obtener el tamaño de la terminal
    if(limpiar):
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
    pr_limpiar_consola()
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



def fn_cuadricular_estudiantes(estudiantes:list[Estudiantes],mostrar_id=False):
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
    all_likess:list[Likes] = fn_obtener_registros_en_array(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,normalizar_likes)
    mis_likes =[]
    if(len(all_likess) != 0):
        for i in range(len(all_likess)):
            if(str(all_likess[i].remitente) == str(user_sesion.id)):
                mis_likes.append(all_likess[i])
    return mis_likes

def fn_obtener_informacion_de_likes():
    "[0]: Matcheados [1]:Likes recibidos y no respondidos [2]:Likes dados y no recibidos"
    matchs = 0
    all_likess:list[Likes] = fn_obtener_registros_en_array(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,normalizar_likes)

    R:list[Likes] = [None]*len(all_likess)
    D:list[Likes] = [None]*len(all_likess)
    M:list[Likes] = [None]*len(all_likess)
    
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
        reg_like:Likes = pickle.load(LOGICO_ARCHIVO_LIKES)
        normalizar_likes(reg_like) 
        if(str(reg_like.remitente) == str(user_sesion.id)):
            registros[index] = reg_like 
        elif(str(reg_like.destinatario) == str(user_sesion.id)):
            registro2[index] = reg_like 
        else:
            descontar = descontar + 1            
        index= index + 1  
    
    likes_mio = [None] * (index-descontar-1)
    k=0
    e=0
    while k < descontar:
        if(registros[k]!= None):
            likes_mio[e]=registros[k]
            e=e+1
        k = k + 1  
    return likes_mio




        

def pr_ver_candidatos():
    def fn_insertar_likes(est:list[Estudiantes]):        
        nuevo_array = [["" for _ in range(0,7)] for _ in range(0,len(est))]
        likes:list[Likes]= fn_verificar_like()

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
                if(int(nuevo_array[h][5])-1 == int(likes[t].destinatario)):
                    nuevo_array[h][6] = "Like dado"
        return nuevo_array

    estudiantes = fn_obtener_registros_en_array(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,normalizar_estudiante)
    if(len(estudiantes) ==0):
        pr_crear_titulo("No existen candidatos")
        print("")
        return pr_pausar_consola() 

    
    estudiante_vista = fn_cuadricular_estudiantes(estudiantes,True)
    estudiante_vista= fn_insertar_likes(estudiante_vista)
    #print(estudiante_vista)
    #likes = fn_obtener_registros_en_array(LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,normalizar_likes)

    #print(likes)
    #input("")

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

    pr_crear_titulo("CANDIDATOS")
    print("")
    pr_tabla(estudiantes_columnas,estudiante_vista,False)

    print("\nSu like esta a punto de ser enviado esta seguro de esta accion? Si-[ACEPTAR] No-[CANCELAR] \n")
    si_no= fn_validar_si_no()
    
    if(si_no == "si"):
        like = Likes()
        print("Su like ha sido enviado. ")
        reg_est:Estudiantes = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)

        like.destinatario = reg_est.id_estudiantes
        like.remitente = user_sesion.id

        fn_guardar_datos(like,LOGICO_ARCHIVO_LIKES,FISICO_ARCHIVO_LIKES,formatear_likes)        
    else:
        print("Su like fue cancelado con exito.")
        
    input("")
    
    


def pr_crear_estudiantes():
    ver_contraseña = False
    contraseña=""
    estudiante = Estudiantes()
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
                    if(len(contraseña) >=8):
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
                estudiante_ram[0][2] = nombre
            case(4):
                pr_tabla(columnas,estudiante_ram)
                sexo = input("Ingrese su sexo: ")
                estudiante_ram[0][3] = sexo
            case(5):
                if fn_verificar_array_vacio(estudiante_ram[0],3):
                    pr_tabla(columnas,estudiante_ram)
                    print(f"\n\n¿Desea guardar su datos {nombre}? Los datos ha guardarse son los indicados arriba 🔼")
                    si_no = fn_validar_si_no()
                    if(si_no == "si"):
                        #AGREGAR UNA CANCELACION POR SI SE ARREPIENTE DE CREAR LA CUENTA
                        clave = input("Por seguridad de su cuenta ingrese una clave unica: ")
                        estudiante.email = email
                        estudiante.nombre = nombre
                        estudiante.sexo= sexo
                        estudiante.id_estudiantes= fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES)
                        estudiante.ultima_conexion= datetime.now()
                        estudiante.clave_recuperacion = clave
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


def fn_traer_registro(archivo_logico:io.BufferedRandom,pos:str,normalizador):
    try:
        archivo_logico.seek(pos)
        reg = pickle.load(archivo_logico)
        normalizador(reg)
        return reg
    except:
        print("Se genero un error en extraccion del archivo")

def pr_eliminar_perfil():
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
            reg:Estudiantes = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)
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
        reg:Estudiantes = fn_traer_registro(LOGICO_ARCHIVO_ESTUDIANTES,pos,normalizar_estudiante)
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
        reg_reporte = Reportes()
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
    reportes:list = fn_obtener_informacion_de_likes()
    print("Matcheados sobre el % posible: ",reportes[0])
    print("Likes dados y no recibidos: ",reportes[2])
    print("Likes recibidos y no respondidos: ",reportes[1])
    input("")

def pr_menu_estudiantes():
    opc = -1
    while opc != 0 and user_sesion.estado:          
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

def pr_inicializar_datos():
    administradores = [["pepe@gmail.com", "pepe"], ["pedro@gmail.com", "pepe"], ["lorenzo@gmail.com", "pepe"]]

    for i in range(0, len(administradores)):
        admin = Administradores()
        admin.email = administradores[i][0]
        admin.contrasena= administradores[i][1]
        admin.id_admin = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES)
        fn_guardar_datos(admin, LOGICO_ARCHIVO_ADMINISTRADORES, FISICO_ARCHIVO_ADMINISTRADORES, formatear_administradores)


def pr_olvido_contrasena():
    #PRIMERO HACER PREGUNTAS DE SEGURIDAD EN CREAR ESTUDIANTES 
    #PARA PODER CREAR ESTE MENU Y PREGUNTAR EN BASE A ESO
    ""

def pr_verificar_usuario(email:str,contrasena:str) -> bool:
    reg_user:Estudiantes
    verificado = False
    
    #VERIFICAR USUARIOS 
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ESTUDIANTES,FISICO_ARCHIVO_ESTUDIANTES,"email",email)
    #Si no lo encuentra devuelve no verificado
    if(pos == -1 ):
        return verificado 

    #Logia de lectura de archivo
    LOGICO_ARCHIVO_ESTUDIANTES.seek(pos,0)
    reg_user = pickle.load(LOGICO_ARCHIVO_ESTUDIANTES)
    normalizar_estudiante(reg_user)

    #Si todo es correcto pone el verificado en verdadero 
    if (reg_user.contrasena == contrasena and str(reg_user.estado).upper() != "B"):
        verificado = True  
        user_sesion.id = reg_user.id_estudiantes
        user_sesion.nombre = reg_user.nombre
        user_sesion.email = reg_user.email
        user_sesion.role= ROLE_USUARIO

    #VERIFICAR MODERADORES
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_MODERADORES,FISICO_ARCHIVO_MODERADORES,"email",email)
    #Si no lo encuentra devuelve no verificado
    if(pos == -1 ):
        return verificado 

    #Logica de lectura de archivo   
    LOGICO_ARCHIVO_MODERADORES.seek(pos,0)
    reg_moderador:Moderadores = pickle.load(LOGICO_ARCHIVO_MODERADORES)
    
    if(reg_moderador.contrasena==contrasena):
        verificado = True
        user_sesion.id=reg_moderador.id_moderador
        user_sesion.email= reg_moderador.email
        user_sesion.role=""
        user_sesion.nombre = ROLE_MODERADOR

    #VERIFICAR ADMINISTRADOR 
    pos = fn_busquedasecuencial(LOGICO_ARCHIVO_ADMINISTRADORES,FISICO_ARCHIVO_ADMINISTRADORES,"email",email)
    #Si no lo encuentra devuelve no verificado
    if(pos == -1):
        return verificado

    LOGICO_ARCHIVO_ADMINISTRADORES.seek(pos,0)
    reg_administrador:Administradores = pickle.load(LOGICO_ARCHIVO_ADMINISTRADORES)
    if(reg_administrador.contrasena == contrasena):
        verificado = True
        user_sesion.id = reg_administrador.id_admin
        user_sesion.email= reg_administrador.email
        user_sesion.role=""
        user_sesion.nombre = ROLE_ADMINISTRADOR 
    
    return verificado   

def pr_iniciar_sesion():
    intento = 0

    pr_crear_titulo("Iniciar sesion")
    email = input ("\nIngrese su correo electronico: ")
    contrasena = input("\nIngrese su contraseña: ")
    autenticado = pr_verificar_usuario(email,contrasena)
    while (intento <= 3 and not (autenticado)) and email != "O" and contrasena != "O" :
        pr_crear_titulo("Iniciar sesion")
        print("\nSi ingresa [O] se le redigira a una nueva pestaña si usted olvido su contraseña")
        print("\nEl email o la contraseña no fueron encontradas")
        email = input ("\nIngrese nuevamente su email: ")
        #if(email == "O"):
            #FUNCION EN CONSTRUCCION
           # pr_olvido_contrasena()

        contrasena = input("\nIngrese su contraseña:  ")
        if(contrasena == "O"):
            #FUNCION EN CONSTRUCCION
            pr_olvido_contrasena()

        autenticado = pr_verificar_usuario(email,contrasena)
        intento = intento + 1 

    if(user_sesion.role == ROLE_USUARIO):
        pr_menu_estudiantes()
    elif(user_sesion.role == ROLE_MODERADOR):
        pr_menu_moderador()
    elif(user_sesion.role == ROLE_ADMINISTRADOR):
        pr_menu_administrador()


def pr_registrarse():
    pr_crear_estudiantes()

def pr_inicializar_programa():
    opc = -1
    while opc != 0:
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





print(fn_obtener_informacion_de_likes())
input("")


pr_inicializar_programa()
#pr_ver_candidatos()
# Última línea






fn_cerrar_logico()






