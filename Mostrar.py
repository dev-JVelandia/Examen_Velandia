import json

def Mostrar_Calendario_Semanal():
    try:
        with open("Calendario_Semanal.json", "r") as archivo:
            Calendario_Semanal = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay eventos registrados para mostrar.")
        Calendario_Semanal = []

    if not Calendario_Semanal:
        print("No hay eventos registrados para mostrar.")
        return

    ANCHO = 20
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    # Encabezado con la palabra fija "Hora"
    encabezado = [f"{'Hora':^{ANCHO}}"] + [f"{dia:^{ANCHO}}" for dia in dias]
    linea_divisoria = "-" * len(" | ".join(encabezado))

    print("\n========================= Calendario Semanal =========================")
    print(" | ".join(encabezado))
    print(linea_divisoria)

    # Recorremos cada evento registrado en la lista
    for evento in Calendario_Semanal:
        # Formateamos el rango usando las horas ingresadas por el usuario
        horario = f"{evento['Hora de inicio']} a {evento['Hora de finalizacion']}"
        fila = [f"{horario:^{ANCHO}}"]

        # Evaluamos el evento contra cada columna de día
        for dia in dias:
            if evento["Dia"] == dia:
                nombre_materia = evento["Materia o actividad"][:ANCHO - 2]
                fila.append(f"{nombre_materia:^{ANCHO}}")
            else:
                fila.append(f"{'Libre':^{ANCHO}}")

        print(" | ".join(fila))

    print(linea_divisoria)