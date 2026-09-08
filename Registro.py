def registro_materias_y_actividades():
    M_A = input("Ingrese el nombre de la materia o actividad que desea registrar: ")
    Dia = input("Ingrese el dia de la semana en el que se realiza la materia o actividad: ").capitalize()
    H_inicio = input("Ingrese la hora de inicio de la materia o actividad (formato 24 horas, ej: 14:00): ")
    H_fin = input("Ingrese la hora de finalizacion de la materia o actividad (formato 24 horas, ej: 16:00): ")
    Ubicacion = input("Ingrese la ubicacion de la materia o actividad: ")
    evento = {
        "Materia o actividad": M_A,
        "Dia": Dia,
        "Hora de inicio": H_inicio,
        "Hora de finalizacion": H_fin,
        "Ubicacion": Ubicacion
    }
    return evento