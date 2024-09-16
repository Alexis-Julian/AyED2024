#Adrian Carrizo, Alexis Rojas, German Villalba, Lautaro Arnay

import os 
from getpass import getpass
from datetime import datetime
from math import factorial,comb
import random
fecha_actual = str(datetime.today().date())
print(fecha_actual)
input("")
##[indice, email, contra, activo/inactivo, fecha nacimiento, sexo, biografia, hobbies]

"estudiantes:array[1...10,1...8] of strings"
estudiantes=[[""]*10 for i in range (8)]
"moderador:array[1...4,1...4] of strings"
moderador=[[""]*4 for i in range(4)]

"matriz_like:array[1...8,1...8]of interger"
matriz_like=[[0]*8 for i in range(8)]
"reporte:[1...3,1...8,1...8] of strings"
reporte=[[[""]*3 for i in range(8)]for j in range(8)]

"var:uid_logeado,ultima_posicion_estudiantes,ultima_posicion_moderadores=tipo interger"
ultima_posicion_estudiantes = 4
ultima_posicion_moderadores = 1
uid_logeado= -1
"var:role_logeado=tipo string"
role_logeado= ""
#GENERAMOS LA VARIABLE INTENTO <= 3 PARA QUE NO HAYA ERROR
"var:intento_login=tipo interger"
intento_login = 0
"var:fecha_actual=tipo string"
fecha_actual = str(datetime.today().date())

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

"var:fecha=tipo str"
"var:fecha_obj,anio_actual,mes_actual,dia_actual,edad=tipo interger"
def fn_validar_fecha():
    fecha = input("Ingrese nueva fecha en formato YYYY-MM-DD: ").strip()
    try:
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
        anio_actual = datetime.today().year
        mes_actual= datetime.today().month
        dia_actual= datetime.today().day
        if 1900 <= fecha_obj.year <= anio_actual:
            edad=anio_actual-fecha_obj.year
            if (mes_actual<fecha_obj.month) or (mes_actual==fecha_obj.month and fecha_obj>dia_actual):
                edad=edad-1
                estudiantes[uid_logeado][7]=str(edad)
            else:
                estudiantes[uid_logeado][7]=str(edad)
            return fecha
        else:
            print(f"\nEl año debe ser mayor a 1900 y menor o igual a {anio_actual}\n")
            return fn_validar_fecha()
    except ValueError:
        print("\nLa fecha debe tener el formato YYYY-MM-DD\n")
        return fn_validar_fecha()
    
###PROCEDIMIENTOS###
def pr_Cargar_moderadores():
    moderador[0][0]="0"
    moderador[0][1]="lau@gmail.com"
    moderador[0][2]="123"
    moderador[0][3]="a"

def pr_Cargar_estudiantes():
    estudiantes[0][0]="0"
    estudiantes[1][0]="1"
    estudiantes[2][0]="2"
    estudiantes[3][0]="3"
    estudiantes[0][1]="pepe@gmail.com"
    estudiantes[1][1]="pedro@gmail.com"
    estudiantes[2][1]="adri@gmail.com"
    estudiantes[3][1]="lauti@gmail.com"
    estudiantes[0][2]="123"
    estudiantes[1][2]="321"
    estudiantes[2][2]="123"
    estudiantes[3][2]="123"
    estudiantes[0][3]="a"
    estudiantes[1][3]="a"
    estudiantes[2][3]="a"
    estudiantes[3][3]="a"
    estudiantes[0][4]="Pepe"
    estudiantes[1][4]="Pedro"
    estudiantes[2][4]="Adriana"
    estudiantes[3][4]="Lautaro"
    estudiantes[0][5]="1999-03-22"
    estudiantes[1][5]="1989-06-11"
    estudiantes[2][5]="1994-01-08"
    estudiantes[3][5]="2002-09-02"
    estudiantes[0][6]="H"
    estudiantes[1][6]="H"
    estudiantes[2][6]="F"
    estudiantes[3][6]="H"
    estudiantes[0][7]="25"
    estudiantes[1][7]="35"
    estudiantes[2][7]="30"
    estudiantes[3][7]="21"
    estudiantes[0][8]="Estudio"
    estudiantes[1][8]="Estudio"
    estudiantes[2][8]="Estudio"
    estudiantes[3][8]="Estudio"
    estudiantes[0][9]="Toco la guitarra"
    estudiantes[1][9]="Toco la guitarra"
    estudiantes[2][9]="Toco la guitarra"
    estudiantes[3][9]="Toco la guitarra"

"var:i,j=tipo interger"
def pr_setear_matriz():
    for i in range(ultima_posicion_estudiantes):
        for j in range(ultima_posicion_estudiantes):
            matriz_like[i][j]=random.randint(0,1)

def pr_mostrar_opcion_invalida():
    print("Opción o formato no válido. Por favor, intente de nuevo.")

def pr_mostrar_usuario_inexistente():
    print("Usuario inexistente. Por favor, intente de nuevo.")

"var:columnas=tipo string"
"var:cantidadletra,columnatamano,i,copiarcolumnas=tipo interger"
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
    
def pr_limpiar_consola():
    os.system("cls")

def pr_cartel_construccion():
    print("\nOpcion en construccion...\n")

def pr_pausar_consola():
    os.system("pause")

"var:mid=tipo interger"
"var:parte_decimal=tipo float"
#Funcion para emparejar el texto en la pantalla 
def fn_text_center(data,space):
    mid = (space- len(data)) / 2
    parte_decimal = mid - int(mid)
    if(str(parte_decimal) == "0.0"):
        mid=int(mid)
        return (" "*mid)+data+(" "*mid)
    else:
        mid = int(mid)
        return (" "*mid)+" "+data+(" "*mid)  

"var:data,aux=string"
"var:length=tipo interger"
#Funcion para fromatear un texto y dejarlo centrado
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

"Array: array[1...6] of interger"
def pr_Bonus1():
    Array=[0]*6
    def cargar_array_bonus1(a):
        a[0]=21
        a[1]=18
        a[2]=20
        a[3]=19
        a[4]=23
        a[5]=24
    cargar_array_bonus1(Array)

    "A: array[1...6] of interger"
    "var:limite,cont,num=tipo interger"
    def Hallar_numero_faltante(A, limite):
        ordenar(A, limite)
        cont=0
        num=A[0]
        while num==A[cont] and cont<limite:
            cont=cont+1
            num=num+1
        if num!=A[cont]:
            print(f"El numero faltante para que la secuencia sea autoincremental es el {num}, y se encuentra entre las edades {num-1} y {num+1}")
        else:
            print("no falta ningun numero")
            
    "A: array[1...6] of interger"
    "var:i,j,aux,limite=tipo interger"
    def ordenar(A, limite):
        for i in range(limite-1):
            for j in range(i+1, limite):
                if A[i]>A[j]:
                    aux=A[i]
                    A[i]=A[j]
                    A[j]=aux
        print(f"El mismo ordenado es el siguiente {A}\n\n")


    pr_limpiar_consola()
    pr_crear_titulo("Bonus 1")
    print(f"El arreglo con las edades cargadas por un programador anterior a nosotros es: {Array} , nos dejo como tarea ordenarlo y encontrar la edad faltante para que sea autoincremental\n\n")
    Hallar_numero_faltante(Array[:],5)
    pr_pausar_consola()

"var:n,k=tipo interger"
def fn_combinaciones(n, k):
    return int(factorial(n)/(factorial(n-k) * factorial(k)))


###FUNCIONES GENERALES###
"var:encontrado,index,limite=tipo interger"
def fn_busqueda_secuencial_uni(limite:int,condicion) -> bool:
    encontrado = 0
    index = 0
    while  index <  limite and encontrado==0:
        encontrado = condicion(index) 
        index = index + 1 
        
    return [encontrado, (index - 1)]


###FUNCIONES PRINCIPALES###
#Procedure de reportes estadisticos consigna del TP2
"var:match,likes,no_likes,porcentaje_match=tipo interger"
def pr_reporte_estadistico():
    pr_limpiar_consola()
    pr_crear_titulo("REPORTES ESTADISTICOS")

    match = 0
    likes = 0
    no_likes=0

    for i in range(0,ultima_posicion_estudiantes):            
        #RECIBIDOS Y DADOS
        if(matriz_like[uid_logeado][i] == 1 and matriz_like[i][uid_logeado] == 1):
            if i!=uid_logeado:
                match = match + 1
        #RECIBIDOS PERO NO DADOS
        if(matriz_like[i][uid_logeado] == 1 and matriz_like[uid_logeado][i]== 0):
            if estudiantes[i][3]!="i":
                no_likes = no_likes + 1 
        #DADOS PERO NO RECIBIDOS 
        if(matriz_like[i][uid_logeado] == 0 and matriz_like[uid_logeado][i]== 1):
            if estudiantes [i][3]!="i":
                likes = likes + 1 
    porcentaje_match = ((match*100)//(ultima_posicion_estudiantes-1))

    print(f"Matcheados sobre el % de usuarios registrados: {porcentaje_match}% \n\nLikes dados y no recibidos: {likes} \n\nLikes recibidos y no respondidos: {no_likes}")
    print("")
    pr_pausar_consola()

"var:opc=tipo str"
def fn_eliminar_usuario():
    pr_limpiar_consola()
    pr_crear_titulo("Eliminar mi cuenta")
    print("esta seguro de eliminar su usuario?(S/N)\n")
    opc=str(input("introduzca la letra de la opcion correspondiente: ")).upper()
    while opc!="S" and opc!="N":
         opc=str(input("introduzca una opcion valida: ")).upper()
    
    match opc:
        case "S":
            estudiantes[uid_logeado][3]="i"
            return False
        case "N":
            return True

"var:id=tipo interger"
"var:msg,si_no=tipo string"
"var:band=tipo boolean"
def pr_reportar_candidato():    
    id=0
    msg=""
    si_no=""
    
    def pr_mostrar_tabla():
            columnas=[""]*5
            def pr_cargar_contcolumnas():
                columnas[0]="UID"
                columnas[1]="NOMBRE"
                columnas[2]="EDAD"
                columnas[3]="HOBBIES"
                columnas[4]="BIOGRAFIA"

            personas_vista = [[""]*5 for _ in range (8)]
            pr_cargar_contcolumnas()

            for i in range (0,ultima_posicion_estudiantes):
                personas_vista[i][0] = estudiantes[i][0]
                personas_vista[i][1] = estudiantes[i][4]
                personas_vista[i][2] = estudiantes[i][7]
                personas_vista[i][3] = estudiantes[i][8]
                personas_vista[i][4] = estudiantes[i][9]

            pr_tabla(columnas,personas_vista)

    def fn_buscar_usuario_correspondiente(index):
        if id==index:
            return 1
        else:
            return 0

    band=True
    pr_limpiar_consola()
    pr_crear_titulo("Reportar un candidato")
    pr_mostrar_tabla()
    while id !=9 and msg != "*" and band==True:
        try:
            id= int(input ("\nIngrerse el id de quien desea reportar [9]-Salir:  "))
        except ValueError:
            print("solo se permiten numeros")
            pr_pausar_consola()

        if id!=9:
            res=fn_busqueda_secuencial_uni(ultima_posicion_estudiantes,fn_buscar_usuario_correspondiente)
            if res[0]==1:
                msg = input ("\nIngrese el motivo de su reporte [*]-Salir:  ")
                if(id != 9 and msg != "*" ):
                    if(reporte[uid_logeado][id][0] != ""):
                        print("Usted ya tiene un reporte hecho, si desea crear uno nuevo va tener que remplezarlo [S]-SI [N]-NO: ")
                        si_no = input("")

                if(si_no == "" or si_no == "S"):

                    reporte[uid_logeado][id][0] = "0"
                    reporte[uid_logeado][id][1] = msg
                    reporte[uid_logeado][id][2] =str(id)

                    os.system("cls")
                    print(f"\nUsted reporto ha {id}")
                    band=False
                else:
                    band=False
            elif( res[0] == 0):
                    print("El usuario que ingreso no esta disponible o no existe.")
                    pr_pausar_consola()

"band: arrar[1,2] of boolean"
"var:opc=tipo string"
def fn_gestionar_usuario():
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR MI PERFIL")
    
    band=[True, True]
    while band[0]:
        print("\na-Editar datos de usuario\n\nb-Eliminar usuario\n\nc-Salir\n")
        opc = fn_validar_rango_str('a', 'c')
        match opc:
            case "a":
                pr_editar_usuario()
            case "b":
                if not fn_eliminar_usuario():
                    band[0], band[1] = False, False
            case "c":
                pr_limpiar_consola()
                pr_crear_titulo("MENU PRINCIPAL")
                band[0]=False
    
    return band

def validar_none(msg:str,isPass):
    if(isPass):
        data = getpass(msg)

        while data == "":
            data = getpass(f"Error tiene que ingresar algun caracter, {msg.lower()}: ")

        return data 
    else:    
        data = input(msg)

        while data == "":
            data = input(f"Error tiene que ingresar algun caracter, {msg.lower()}: ")

        return data 


"var:band=tipo boolean"
"var:opc=tipo interger"
def pr_gestionar_candidatos():
    band=True
    while band==True:
        pr_limpiar_consola()
        pr_crear_titulo("Gestionar candidatos")
        print("1.Ver candidatos\n\n2.Reportar un candidato\n\n3.Salir\n\n")
        opc=fn_validar_rango(1,3)
        match opc:
            case 1:
                pr_ver_candidatos()
            case 2:
                pr_reportar_candidato()
            case 3:
                band=False

"var:band=tipo boolean"
"var:cont,cont1,opc1=tipo interger"
def ver_reporte_usr(user,index):
    cont=0
    cont1=0
    band=True
    while cont<index and band == True:
        pr_limpiar_consola()
        pr_crear_titulo(f"Reportes del usuario {user}")
        if estudiantes[user][3]=="i":
            print("el usuario se encuentra inactivo")
            band=False
        if reporte[user][cont][0]!="" and estudiantes[cont][3]!="i":
            print(f"El usuario {user} ha reportado al usuario {cont}, por el motivo: {reporte[user][cont][1]}\n\n1.banear al usuario reportado\n\n2.siguiente reporte\n\n3.salir")
            opc1=fn_validar_rango(1,3)
            match opc1:
                case 1:
                    reporte[user][cont][0]="2"
                    estudiantes[cont][3]="i"
                    cont1=cont1+1
                    cont=cont+1
                case 2:
                    reporte[user][cont][0]="1"
                    cont1=cont1+1
                    cont=cont+1
                case 3:
                    band=False
                    cont1=cont+1
        else:
            cont=cont+1
    if cont1==0 and estudiantes[user][3]=="a":
        print("el usuario no hizo reportes")
        pr_pausar_consola()
    elif cont<0 and estudiantes[user][3]=="a":
        print("esos fueron todos los reportes realizados por el usuario")
        pr_pausar_consola()


"var:me_gusta,soy_yo=tipo interger"
"var:match=tipo boolean"
def fn_verificar_match(soy_yo,me_gusta):
    match = False
    if (matriz_like[me_gusta][soy_yo] == "1" ):
        match = True
    return match

"columnas: array[1...6]of strings"
"personas_vista: array[1...6,1...8] of strings"
"var:encontrado,match=tipo boolean"
"var:indice_like=tipo interger"
def pr_ver_candidatos():
    def pr_mostrar_tabla():
        columnas=[""]*6
        def pr_cargar_contcolumnas():
            columnas[0]="UID"
            columnas[1]="NOMBRE"
            columnas[2]="EDAD"
            columnas[3]="HOBBIES"
            columnas[4]="BIOGRAFIA"
            columnas[5]="LIKE"

        personas_vista = [[""]*6 for _ in range (8)]
        pr_cargar_contcolumnas()

        for i in range (0,ultima_posicion_estudiantes):
            personas_vista[i][0] = estudiantes[i][0]
            personas_vista[i][1] = estudiantes[i][4]
            personas_vista[i][2] = estudiantes[i][7]
            personas_vista[i][3] = estudiantes[i][8]
            personas_vista[i][4] = estudiantes[i][9]
            if(matriz_like[uid_logeado][i]==1):
                personas_vista[i][5] = "Otorgado"
            else:
                personas_vista[i][5] = "No otorgado"

        pr_tabla(columnas,personas_vista)

    pr_crear_titulo("Ver candidatos")
    pr_mostrar_tabla()
    encontrado = False
    while not (encontrado): 
        print("ingrese el id de la persona a quien le desea dar like")
        indice_like = fn_validar_rango(0,ultima_posicion_estudiantes-1)
        #[me_gusta_bool,me_gusta_indice] = fn_busqueda_secuencial(personas,4,input ("\n Ingrese el nombre a quien le desea dar like: "),0)
        
        if(uid_logeado == indice_like):
            print("Te estas intentado dar like a vos mismo?cuanto amor propio")
            pr_pausar_consola()

        #print(f"Le has dado me gusta a {personas[indice_like][0]}")
        if(matriz_like[uid_logeado][indice_like] == 1 and estudiantes[indice_like][3]!="i"):
            print("Usted ya propuso el like a esta persona")
            print("\nQuiere usted sacarle el like a esta persona? ")
            print(matriz_like[uid_logeado][indice_like])
            if fn_validar_si_no() == "si":
                matriz_like[uid_logeado][indice_like] = 0
                
        elif estudiantes[indice_like][3]!="i":
            print(f"Usted le ha dado like al usuario numero {indice_like}")
            matriz_like[uid_logeado][indice_like] = 1
        
        else:
            print("El usuario a quien le intentas dar o eliminar el like se encuentra desactivado.")
            pr_pausar_consola()
        

        match = fn_verificar_match(uid_logeado,indice_like)

        if(match):
            print("Se ha generado match")
        
        pr_pausar_consola()
        pr_limpiar_consola()
        pr_crear_titulo("Ver candidatos")
        pr_mostrar_tabla()

        print("Desea seguir dando like? [si] [no]")
        si_no = fn_validar_si_no()
        if (si_no != "si"):
            encontrado= True

"var:band=tipo boolean"
"var:s,opc=tipo interger"
def pr_ver_reportes():
    band=True
    while band==True:
        pr_limpiar_consola()
        pr_crear_titulo("Ver reportes")
        for i in range(ultima_posicion_estudiantes):
            print(f"\n{i}-Ver reportes del usuario {estudiantes[i][1]} {"- Estudiante desactivado" if estudiantes[i][3] == 'i' else ""}")
        s=i+1
        print(f"\n{s}-Salir\n")
        opc=fn_validar_rango(0,s)
        if opc==s:
            band=False
        else:
            ver_reporte_usr(opc,8)
        
"var:band=tipo boolean"
"var:opc=tipo string"    
def pr_editar_usuario():
    band=True
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("EDITAR DATOS DE USUARIO")

        def pr_mostrar_tabla():
            columnas=[""]*5
            def pr_cargar_contcolumnas():
                columnas[0]="NOMBRE"
                columnas[1]="FECHA DE NACIMIENTO"
                columnas[2]="HOBBIES"
                columnas[3]="BIOGRAFIA"
                columnas[4]="SEXO"

            tabla_usuario = [[""]*5]
            pr_cargar_contcolumnas()

            tabla_usuario[0][0] = estudiantes[uid_logeado][4]
            tabla_usuario[0][1] = estudiantes[uid_logeado][5]
            tabla_usuario[0][2] = estudiantes[uid_logeado][9]
            tabla_usuario[0][3] = estudiantes[uid_logeado][8]
            tabla_usuario[0][4] = estudiantes[uid_logeado][6]

            pr_tabla(columnas,tabla_usuario)

        pr_mostrar_tabla()

        print("\na-Editar Fecha de nacimiento\n\nb-Editar sexo\n\nc-Editar biografia\n\nd-Editar hobbies\n\ne-Editar nombre\n\nf-Salir\n")
        opc=fn_validar_rango_str('a', 'g')

        match opc:
            case "a":
                fn_editar_datos(5, 1)
            case "b":
                fn_editar_datos(6, 0)
            case "c":
                fn_editar_datos(8, 0)
            case "d":
                fn_editar_datos(9, 0)
            case "e":
                fn_editar_datos(4, 0)
            case "f":
                pr_limpiar_consola()
                pr_crear_titulo("GESTIONAR MI PERFIL")
                band=False
    
    return band

"var:nuevos_datos=tipo string"
def fn_editar_datos(indice, es_fecha):
    pr_limpiar_consola()
    pr_crear_titulo("EDITAR DATOS DE USUARIO")
    print(f"\nDatos actuales: {estudiantes[uid_logeado][indice]}\n")
    nuevos_datos = ""
    
    if es_fecha==1:
        nuevos_datos = str(fn_validar_fecha())
    else:
        nuevos_datos = input("Ingrese la nueva informacion: ")
    
    print(f"\nCambios guardados con exito\n")
    estudiantes[uid_logeado][indice] = nuevos_datos

"var:band,creado_exitoso=tipo boolean"
"var:email,password=tipo string"
"var:ultima_posicion_moderadores=tipo interger"
def fn_registrar_moderadores():
    global ultima_posicion_moderadores
    creado_exitoso = False
    
    if ultima_posicion_moderadores == 4:
        print("\nNo es posible registrar mas estudiantes. Limite máximo alcanzado.\n")
        return creado_exitoso
    
    pr_limpiar_consola()
    pr_crear_titulo("Registrarse como moderador")
    def fn_buscar_usuario_correspondiente1(indice):
        if email==estudiantes[indice][1]:
            return 1
        else:
            return 0

    def fn_buscar_usuario_correspondiente2(indice):
        if email==moderador[indice][1]:
            return 1
        else:
            return 0

    email = validar_none("Ingrese un email ", False)

    band=True
    while band==True:
        res_est=fn_busqueda_secuencial_uni(ultima_posicion_estudiantes,fn_buscar_usuario_correspondiente1)
        res_mod=fn_busqueda_secuencial_uni(ultima_posicion_moderadores,fn_buscar_usuario_correspondiente2)

        if res_est[0]== 1 and res_mod[0]== 1:
            print("ya existe otro usuario registrado con ese mail\n\n")
            email = validar_none("Ingrese un email ", False)
        else:
            band=False

    password = validar_none("Ingrese una contraseña ", True)

    moderador[ultima_posicion_moderadores][0] = str(ultima_posicion_moderadores)
    moderador[ultima_posicion_moderadores][1] = email
    moderador[ultima_posicion_moderadores][2] = password
    moderador[ultima_posicion_moderadores][3] = 'a'
    
    ultima_posicion_moderadores+=1
    
    creado_exitoso = True
 
    return creado_exitoso

"var:ultima_posicion_estudiantes=tipo interger"
"var:email,password,nombre=tipo string"
"var:band,creado_exitoso=tipo boolean"
def fn_registrar_estudiante():
    global ultima_posicion_estudiantes
    creado_exitoso = False
    email=""
    password=""
    if ultima_posicion_estudiantes == 8:
        print("\nNo es posible registrar mas moderadores. Limite máximo alcanzado.\n")
        return creado_exitoso
    
    def fn_buscar_usuario_correspondiente1(indice):
        if email==estudiantes[indice][1]:
            return 1
        else:
            return 0

    def fn_buscar_usuario_correspondiente2(indice):
        if email==moderador[indice][1]:
            return 1
        else:
            return 0

    pr_limpiar_consola()
    pr_crear_titulo("Registrarse")
    band=True
    nombre=input("introduzca su nombre: ")
    while band==True:
        email = validar_none("Ingrese email ", False)
        res_est=fn_busqueda_secuencial_uni(ultima_posicion_estudiantes,fn_buscar_usuario_correspondiente1)
        res_mod=fn_busqueda_secuencial_uni(ultima_posicion_moderadores,fn_buscar_usuario_correspondiente2)

        if res_est[0]== 1 and res_mod[0]== 1 :
            print("Ya hay otro usuario registrado con ese email")
            pr_pausar_consola()
        else:
            band=False
    password = validar_none("Ingrese una contraseña ", True)

    estudiantes[ultima_posicion_estudiantes][0] = str(ultima_posicion_estudiantes)
    estudiantes[ultima_posicion_estudiantes][1] = email
    estudiantes[ultima_posicion_estudiantes][2] = password
    estudiantes[ultima_posicion_estudiantes][3] = 'a'
    estudiantes[ultima_posicion_estudiantes][4] = nombre

    
    ultima_posicion_estudiantes+=1

    creado_exitoso = True
 
    return creado_exitoso

"res: array[1,2] of interger"
"var:autenticado,desactivado=tipo boolean"
"var:encontrado,uid_logeado,pos,intento_login=tipo interger"
"var:email,contrasena,role_logueado=tipo string"
def fn_iniciar_sesion():
    global intento_login
    
    pr_limpiar_consola()
    pr_crear_titulo("Loguearse")
    
    #LA VARIABLE AUTENTICADO SIRVE COMO BOOLEANO PARA SABER CUANDO EL USUARIO ESTA LOGEADO
    autenticado = False
    
    while intento_login < 3 and not(autenticado): 
        email = input("\nIngrese el email: ")
        contrasena = getpass("\nIngrese una contraseña: ")

        desactivado = False
    
        if not(autenticado):
            # FUNCION INTERNA PARA BUSCAR USUARIOS EN EL ARRAY DE ESTUDIANTES
            def fn_busqueda_usuario(indice): 
                global role_logeado,uid_logeado
                if(estudiantes[indice][1] ==email  and estudiantes[indice][2]==contrasena):
                    role_logeado = "U"
                    uid_logeado = indice
                    return 1
                else:
                    return 0

            #BUSCAR USUARIO EN LA LISTA DE ESTUDIANTES
            res = fn_busqueda_secuencial_uni(8 ,fn_busqueda_usuario)

            encontrado, pos = res[0], res[1]
           # encontrado, pos = res[0], res[1]
            
            if encontrado==1:
                if estudiantes[pos][3] == 'a':
                    autenticado = True
                else:
                    desactivado = True
                    print("\nEl usuario se encuentra desactivado.\n")
            

        if not(autenticado):
            #FUNCION INTERNA PARA BUSCAR MODERADORES EN EL ARRAY DE MODERADORES
            def fn_busquedaModerador(indice):
                if moderador[indice][1] == email and moderador[indice][2] == contrasena:
                    global role_logeado,uid_logeado
                    uid_logeado = indice
                    role_logeado="M"
                    return 1
                else:
                    return 0

            #BUSCAR USUARIO EN LA LISTA DE MODERADORES
            res = fn_busqueda_secuencial_uni(4,fn_busquedaModerador)
            encontrado, pos = res[0], res[1]

            if encontrado==1:
                if moderador[pos][3] == 'a':
                    autenticado = True
                else:
                    desactivado = True
                    print("\nEl usuario se encuentra desactivado.\n")

        if not desactivado:
            print("\nUsuario o contrasena incorrectos. Intente nuevamente")
        
        intento_login = intento_login + 1
            
        print(f"Numero de intentos restantes: {3 - intento_login}")

    #SI EL AUTENTICADO ES TRUE ENTONCES SE TE DIRIGE AL MENU PRINCIPAL Y SI NO SALE DEL PROGRAMA 
    if(autenticado):
        intento_login = 0
        if role_logeado=="U":
            autenticado = fn_menu_usr()
        elif role_logeado=="M":
            autenticado = fn_menu_mod()

    return autenticado

"var:desactivado=tipo boolean"
"var:confirm,pos,encontrado,opc2=tipo interger"
"var:opc=tipo string"
def fn_desactivar_usuario():
    desactivado = False
    def pr_mostrar_tabla():
            columnas=[""]*2
            def pr_cargar_contcolumnas():
                columnas[0]="UID"
                columnas[1]="NOMBRE"

            personas_vista = [[""]*2 for _ in range (ultima_posicion_estudiantes)]
            pr_cargar_contcolumnas()

            for i in range (0,ultima_posicion_estudiantes):
                personas_vista[i][0] = estudiantes[i][0]
                personas_vista[i][1] = estudiantes[i][4]

            pr_tabla(columnas,personas_vista)
    
    while not desactivado:
        pr_limpiar_consola()
        pr_crear_titulo("DESACTIVAR USUARIO")

        pr_mostrar_tabla()

        pos = 100
        encontrado = 0
        
        opc = input("\nIngrese un usuario o ID: ")
        try:
            opc2 = int(opc)
            
            def fn_desactivar_usu_por_id(indice):
                if estudiantes[indice][0] == str(opc2):
                    return 1
                else:
                    return 0
            
            encontrado = fn_busqueda_secuencial_uni(8, fn_desactivar_usu_por_id)[0]
            pos = fn_busqueda_secuencial_uni(8, fn_desactivar_usu_por_id)[1]
                
        except ValueError:
            def fn_buscar_usu_por_email(indice):
                if estudiantes[indice][1] == opc:
                    return 1
                else:
                    return 0
                               
            encontrado = fn_busqueda_secuencial_uni(8, fn_buscar_usu_por_email)[0]
            pos = fn_busqueda_secuencial_uni(8, fn_buscar_usu_por_email)[1]
        
        if encontrado!=1:
            print("\nUsuario no encontrado. Intente nuevamente.\n")

        else:
            print(f"\nEsta seguro que desea desactivar al usuario: {estudiantes[pos][1]} ?\n\n1-Si\n\n2-No\n")
            confirm = fn_validar_rango(1, 2)
            if confirm == 1:
                if estudiantes[pos][3] == 'a':
                    estudiantes[pos][3] = 'i'
                    print('\nUsuario desactivado con exito.\n')
                    desactivado = True
                else:
                    desactivado = True
                    print("\nEl usuario ya se encuentra desactivado.\n")
            
            else:
                desactivado = True
                
    return desactivado

def pr_Bonus2():
    pr_limpiar_consola()
    pr_crear_titulo("Bonus 2")
    print(f"La cantidad posible de matcheos sin repetir son {fn_combinaciones(ultima_posicion_estudiantes, 2)}, teniendo en cuenta que tenemos {ultima_posicion_estudiantes} usuarios cargados y no se pueden repetir")
    pr_pausar_consola()

"var:band=tipo boolean"
"var:opc=tipo string"
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
                pr_limpiar_consola()
                pr_crear_titulo("MENU PRINCIPAL")
                band = False
        
    return band

"var:band=tipo boolean"
"var:opc=tipo interger"
def fn_menu_mod():
    band= True
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("MENU PRINCIPAL")
        print("\n1-Gestionar usuarios\n\n2-Gestionar reportes\n\n3-Reportes estadisticos\n\n4-Salir\n\n")
        opc = fn_validar_rango(1, 6)
        
        match opc:
            case 1:
                 fn_gestionar_usuarios()
            case 2:
                 pr_ver_reportes()
            case 3:
                 pr_cartel_construccion()
                 pr_pausar_consola()
            case 4:
                band=False
            case 5:
                pr_Bonus1()
            case 6:
                pr_Bonus2()

    return band

"var:band=tipo boolean"
"var:opc=tipo interger"
def fn_menu_usr():
    band=True
    while band:
        pr_limpiar_consola()
        pr_crear_titulo("MENU PRINCIPAL")
        print("\n1-Gestionar mi perfil\n\n2-Ver candidatos\n\n3-Ver matcheos\n\n4-Reportes estadisticos\n\n5-Salir\n")
        opc = fn_validar_rango(1,5)
        match opc:
            case 1:
                if not fn_gestionar_usuario()[1]:
                    band = False
            case 2:
                pr_gestionar_candidatos()
            case 3:
                pr_cartel_construccion()
                pr_pausar_consola()
            case 4:
                pr_reporte_estadistico()
            case 5:
                band = False
            
    return band

"var:opc=tipo interger"
def inicializacion():
    global intento_login
    pr_Cargar_moderadores()
    pr_Cargar_estudiantes()
    pr_setear_matriz()
    pr_limpiar_consola()
    pr_crear_titulo("Bienvenido, ¿buscando al compañero ideal?  ")
    print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
    
    opc = fn_validar_rango(0, 4)
    while opc != 0:
        if(opc == 1):
            if not fn_iniciar_sesion():
                pr_limpiar_consola()
                pr_crear_titulo("Bienvenido, ¿buscando al compañero ideal?  ")
                print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        elif (opc == 2):
            if fn_registrar_estudiante():
                pr_limpiar_consola()
                pr_crear_titulo("Cuenta creada con exito")
                print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        elif (opc==3):
            if fn_registrar_moderadores():
                pr_limpiar_consola()
                pr_crear_titulo("Cuenta con poder creada con exito")
                print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        if(intento_login == 3):
            pr_limpiar_consola()
            print('\nSe ha quedado sin intentos.')
            opc = 0
        else:
             opc = fn_validar_rango(0, 3)
    
    print("\nSaliendo del programa.\n")
inicializacion()

