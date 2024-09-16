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
print(datetime.now())
print(diferencia_fechas(str(fecha1), datetime.now()))
print(datetime.now())