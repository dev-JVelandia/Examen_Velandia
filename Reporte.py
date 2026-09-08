import json

def generar_reporte():
    try:
        with open("Calendario_Semanal.json", "r") as archivo:
            calendario_semanal = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al generar el reporte: No se encontró el archivo o no hay datos registrados.")
        return

    if not calendario_semanal:
        print("No hay eventos registrados para generar un reporte.")
        return

    with open("Reporte.json", "w") as archivo_reporte:
        json.dump(calendario_semanal, archivo_reporte, indent=4)

    print("Eventos registrados:")
    for actividad in calendario_semanal:
        print(
            actividad["Dia"],
            "|",
            actividad["Materia o actividad"],
            "|",
            actividad["Hora de inicio"],
            "|",
            actividad["Hora de finalizacion"],
            "|",
            actividad["Ubicacion"]
        ) 

    print("Reporte generado exitosamente en 'Reporte.json'")