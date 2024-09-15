import shutil
import time

# Obtener las dimensiones de la terminal
def get_terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 20))  # Valores predeterminados si no se puede obtener el tamaño
    return size.lines, size.columns

# Arte ASCII para caracteres grandes
ascii_art = {
    '4': [
        "   4  ",
        "  44  ",
        " 4 4  ",
        "444444",
        "   4  ",
    ],
    'A': [
        "  AA  ",
        " A  A ",
        "AAAAA ",
        "A   A ",
        "A   A ",
    ],
    '2': [
        " 2222 ",
        "2    2",
        "   22 ",
        "  2   ",
        "222222",
    ]
}

# Crear el cartel
def draw_banner(characters, visible_up_to):
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
def animate_banner(characters):
    for i in range(1, len(characters) + 1):
        # Limpiar la consola antes de redibujar
        print("\033[H\033[J", end="")  # Limpiar consola (en sistemas compatibles con ANSI)
        draw_banner(characters, i)
        time.sleep(1 / len(characters))  # Animar en 1 segundo en total

# Personajes a mostrar en cada subdivisión
characters = ['4', 'A', '2']

# Animar el cartel
animate_banner(characters)
