import math
import os
import time


from datetime import datetime

def diferencia_fechas(fecha1, fecha2):
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
        resultado += f"{dias} día(s), "
    if horas > 0:
        resultado += f"{horas} hora(s), "
    if minutos > 0:
        resultado += f"{minutos} minuto(s), "
    resultado += f"{segundos} segundo(s)"

    return resultado

# Ejemplo de uso
fecha1 = "2023-09-15 14:30:00"
fecha2 = "2023-09-16 16:45:30"
print(diferencia_fechas(fecha1, fecha2))


A = B = C = 0

cubeWidth = 20
width, height = 160, 44
zBuffer = [0] * (width * height)
buffer = [' '] * (width * height)
backgroundASCIICode = ' '
distanceFromCam = 100
horizontalOffset = 0
K1 = 40

incrementSpeed = 0.6


def calculateX(i, j, k):
    return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + \
           j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)


def calculateY(i, j, k):
    return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - \
           j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - \
           i * math.cos(B) * math.sin(C)


def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)


def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    global x, y, z, ooz, xp, yp, idx
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_cube():
    global A, B, C
    while True:
        buffer[:] = [backgroundASCIICode] * (width * height)
        zBuffer[:] = [0] * (width * height)

        # first cube
        cubeWidth = 20
        horizontalOffset = -2 * cubeWidth
        for cubeX in frange(-cubeWidth, cubeWidth, incrementSpeed):
            for cubeY in frange(-cubeWidth, cubeWidth, incrementSpeed):
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY, cubeX, '$')
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
                calculateForSurface(cubeX, cubeWidth, cubeY, '+')

        # second cube
        cubeWidth = 10
        horizontalOffset = 1 * cubeWidth
        for cubeX in frange(-cubeWidth, cubeWidth, incrementSpeed):
            for cubeY in frange(-cubeWidth, cubeWidth, incrementSpeed):
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY, cubeX, '$')
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
                calculateForSurface(cubeX, cubeWidth, cubeY, '+')

        # third cube
        cubeWidth = 5
        horizontalOffset = 8 * cubeWidth
        for cubeX in frange(-cubeWidth, cubeWidth, incrementSpeed):
            for cubeY in frange(-cubeWidth, cubeWidth, incrementSpeed):
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
                calculateForSurface(cubeWidth, cubeY, cubeX, '$')
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
                calculateForSurface(cubeX, cubeWidth, cubeY, '+')

        # Print buffer
        clear_console()
        for k in range(width * height):
            if k % width == 0:
                print()
            print(buffer[k], end="")

        A += 0.05
        B += 0.05
        C += 0.01
        time.sleep(0.01667)



def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == "__main__":
    draw_cube()
