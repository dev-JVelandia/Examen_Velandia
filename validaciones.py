import json

# Valida si el nombre de la materia o actividad está vacío
def validacion_materia_actividad(materia_actividad):
    if not materia_actividad:
        print("El nombre de la materia o actividad no puede estar vacío.")
        return False
    return True

# Valida si el nombre de la materia o actividad es puramente numérico
def validacion_materia_actividadN(materia_actividad):   
    if materia_actividad.isdigit():
        print("El nombre de la materia o actividad no puede ser un número.")
        return False
    return True

# Valida si hay eventos registrados en el calendario semanal
def validacion_eventos_registrados():
    try:
        with open("Calendario_Semanal.json", "r") as archivo:
            registro_materias_actividades = json.load(archivo)
            return registro_materias_actividades 
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Valida si ya hay una materia o actividad registrada en el mismo día y hora
def validacion_conflicto_horario(dia, hora_inicio, hora_fin):
    registro_materias_actividades = validacion_eventos_registrados()

    for evento in registro_materias_actividades:
        if evento["Dia"] == dia:
            hora_inicio_evento = int(evento["Hora de inicio"].split(":")[0]) * 60 + int(evento["Hora de inicio"].split(":")[1])
            hora_fin_evento = int(evento["Hora de finalizacion"].split(":")[0]) * 60 + int(evento["Hora de finalizacion"].split(":")[1])
            hora_inicio_nuevo = int(hora_inicio.split(":")[0]) * 60 + int(hora_inicio.split(":")[1])
            hora_fin_nuevo = int(hora_fin.split(":")[0]) * 60 + int(hora_fin.split(":")[1])
            
            if (hora_inicio_nuevo < hora_fin_evento and hora_fin_nuevo > hora_inicio_evento):
                print("Ya hay una materia o actividad registrada en el mismo día y hora.")
                return False
    return True

# Valida si el día de la semana es válido
def validacion_dia_semana(dia):
    dias_validos = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
    if dia not in dias_validos:
        print("El día de la semana no es válido. Debe ser uno de los siguientes: Lunes, Martes, Miercoles, Jueves, Viernes, Sabado.")
        return False
    return True

# Valida si la hora de inicio y finalización están en formato correcto (HH:MM) y si la hora de inicio es menor que la hora de finalización
def validacion_horas(hora_inicio: str, hora_fin: str) -> bool:
    try:
        partes_hora_inicio = hora_inicio.split(":")
        partes_hora_fin = hora_fin.split(":")

        h_inicio, m_inicio = int(partes_hora_inicio[0]), int(partes_hora_inicio[1])
        h_fin, m_fin = int(partes_hora_fin[0]), int(partes_hora_fin[1])
        
        if not (0 <= h_inicio < 24 and 0 <= m_inicio < 60 and 0 <= h_fin < 24 and 0 <= m_fin < 60):
            print("El formato de la hora debe ser HH:MM, donde HH está entre 00 y 23 y MM entre 00 y 59.")
            return False
    except (ValueError, IndexError):
        print("El formato de la hora debe ser un número en formato HH:MM.")
        return False
    
    minutos_inicio_total = h_inicio * 60 + m_inicio
    minutos_fin_total = h_fin * 60 + m_fin
    if minutos_inicio_total >= minutos_fin_total:
        print("La hora de inicio debe ser menor que la hora de finalización.")
        return False
    return True 

# Valida si la ubicación está vacía
def validacion_ubicacion(ubicacion):
    if not ubicacion:
        print("La ubicación no puede estar vacía.")
        return False
    return True