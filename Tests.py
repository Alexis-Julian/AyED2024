import shutil
import time 
import random
import string

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


def draw_banner(characters, visible_up_to):
    # Obtener las dimensiones de la terminal
    def get_terminal_size():
        size = shutil.get_terminal_size(fallback=(80, 20))  # Valores predeterminados si no se puede obtener el tamaño
        return size.lines, size.columns

    # Arte ASCII para caracteres grandes
    ascii_art = {
        '4': [
            *obtener_letra_en_grande(random.choice(string.ascii_uppercase), A)
        ],
        'A': [
            *obtener_letra_en_grande(random.choice(string.ascii_uppercase), A)
        ],
        '2': [
           *obtener_letra_en_grande(random.choice(string.ascii_uppercase), A)
        ]
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

# Animar el cartel mostrando los números uno por uno
def animate_banner():
    characters =['4', 'A', '2']
    for k in range(0,3):
        for i in range(1, len(characters) + 1):
            # Limpiar la consola antes de redibujar
            print("\033[H\033[J", end="")  # Limpiar consola (en sistemas compatibles con ANSI)
            draw_banner(characters, i)        
            time.sleep(1 / 5)  # Animar en 1 segundo en total
        time.sleep(1)

animate_banner()

