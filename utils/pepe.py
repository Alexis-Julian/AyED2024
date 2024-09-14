import pickle 
import io 
import os 


def lj_moderadores(x):
    x.id_moderador = str(x.id_moderador).ljust(10).lower() #Entero
    x.email = str(x.email).ljust(32).lower()
    x.contrasena = str(x.contrasena).ljust(32).lower()
    x.estado = str(x.estado).ljust(10).lower() #Booleano


def fn_crear_logico(ruta: str):
    archivo_logico = None  # Inicialización explícita
    
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
 
class Moderadores:
    def __init__(self):
        self.id_moderador=0
        self.email=""
        self.contrasena=""
        self.estado=bool

for i in range(0,20):
    moderador = Moderadores()
    moderador.id_moderador = i
    """ fn_guardar_datos(moderador,LOGICO_ARCHIVO_MODERADORES,FISICO_ARCHIVO_MODERADORES,lj_moderadores) """
    




def ver_moderadores():
    t = os.path.getsize(FISICO_ARCHIVO_MODERADORES)
    while LOGICO_ARCHIVO_MODERADORES.tell() < t:
        moderador:Moderadores = pickle.load(LOGICO_ARCHIVO_MODERADORES)
        print(moderador.id_moderador)
    

    

#Funciones de utilidad 
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







def probando(registro:Moderadores):
    return registro.id_moderador

busquedadico(4,LOGICO_ARCHIVO_MODERADORES,FISICO_ARCHIVO_MODERADORES,probando) 
