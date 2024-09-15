import os 
import pickle 
import io
#from typing import Callable

CARPETA = "pruebas"

class kk_class:
    """_summary_: Clase para pruebas
    """
    def __init__(self):
        self.id_estudiantes= 0  # 10 bytes
        self.email= ""          # 32 bytes
        self.nombre=""          # 32 bytes

def fn_crear_logico(ruta: str):
    archivo_logico = None  # Inicialización explícita
    
    if os.path.exists(ruta):
        archivo_logico = open(ruta, "r+b")  # Abre para lectura y escritura binaria
    else:
        archivo_logico = open(ruta, "w+b")  # Crea un archivo nuevo y lo abre en modo binario
    
    return archivo_logico

def fn_cerrar_logico():
    LOGICO_ARCHIVO_KKS.close()

def fn_formatear_kks(x:kk_class):
    x.id_admin = str(x.id_admin).ljust(10) #Entero
    x.email = str(x.email).ljust(32) 
    x.contrasena = str(x.contrasena).ljust(32)

def fn_buscar_cantidad_de_registros(ARCHIVO_LOGICO:io.BufferedRandom, ARCHIVO_FISICO:str):
    cantidad = 0   
    if os.path.getsize(ARCHIVO_FISICO) != 0:
        ARCHIVO_LOGICO.seek(0)
        pickle.load(ARCHIVO_LOGICO)
        longitud_reg = ARCHIVO_LOGICO.tell()
        t = os.path.getsize(ARCHIVO_FISICO) 
        
        cantidad = t//longitud_reg
    ARCHIVO_LOGICO.seek(0)
    return cantidad

def fn_guardar_datos(registro:object, ARCHIVO_LOGICO:io.BufferedRandom, ARCHIVO_FISICO:str, formateador, posicion:int = -1):
    """ Guarda el registro en su respectivo archivo """
    t = os.path.getsize(ARCHIVO_FISICO)
    try:        
        if (posicion) == -1:
            posicion = t

        ARCHIVO_LOGICO.seek(posicion)
        formateador(registro) 
        pickle.dump(registro,ARCHIVO_LOGICO)
        ARCHIVO_LOGICO.flush()
    except (ValueError, TypeError):
        print("Se genero un error")

def fn_busquedadico(ARCHIVO_LOGICO:io.BufferedRandom, ARCHIVO_FISICO:str, campo:str, data:int):
    dato = int(str(data).strip())
    ARCHIVO_LOGICO.seek(0, 0)
    registro = pickle.load(ARCHIVO_LOGICO)
    tamregi = ARCHIVO_LOGICO.tell()
    cantreg = int(os.path.getsize(ARCHIVO_FISICO) / tamregi)
    inicio = 0
    fin = cantreg - 1
    medio = (inicio + fin) // 2
    ARCHIVO_LOGICO.seek(medio * tamregi,0) 
    registro = pickle.load(ARCHIVO_LOGICO)
    """
    print(f"cantreg = {cantreg}")
    print(f"tamregi = {tamregi}")
    print(f"medio = {medio}")
    print(f"fin = {fin}") """

    while inicio <  fin and int(str(getattr(registro, campo)).strip()) != dato :
        #print(f"id_admin = {int(str(getattr(registro, campo)).strip())} es distinto de dato = {dato}")
        if int(str(getattr(registro, campo)).strip()) > dato:
            fin = medio - 1
        else:
            inicio = medio + 1            
        
        medio = (inicio + fin) // 2
        #print(f"medio = {medio}")
        ARCHIVO_LOGICO.seek(medio * tamregi, 0)
        registro = pickle.load(ARCHIVO_LOGICO)
    if int(str(getattr(registro, campo)).strip()) == dato:
        return medio * tamregi

    return -1

def pr_inicializar_programa():
    kks = [["lorenzo@gmail.com", "pepe"], ["pedro@gmail.com", "pepe"], ["pepe@gmail.com", "pepe"]]

    for i in range(0,len(kks)):
        kk = kk_class()
        kk.email = kks[i][0]
        kk.contrasena = kks[i][1]
        kk.id_admin = fn_buscar_cantidad_de_registros(LOGICO_ARCHIVO_KKS, FISICO_ARCHIVO_KKS)
        fn_guardar_datos(kk, LOGICO_ARCHIVO_KKS, FISICO_ARCHIVO_KKS, fn_formatear_kks)


# Main
if not os.path.exists(CARPETA):
    os.mkdir(os.getcwd() + "/" + CARPETA)

if os.path.exists(CARPETA):
    FISICO_ARCHIVO_KKS= os.getcwd() + "/" + CARPETA + "/kks.dat" 
    LOGICO_ARCHIVO_KKS= fn_crear_logico(FISICO_ARCHIVO_KKS) 

#pr_inicializar_programa()

for i in range(3):
    print(f'La posición en el archivo para id_admin={i} es {fn_busquedadico(LOGICO_ARCHIVO_KKS, FISICO_ARCHIVO_KKS, "id_admin", 2)}')

fn_cerrar_logico()

