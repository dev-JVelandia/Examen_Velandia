import json

def generar_reporte():
    try:
        with open("Calendario_Semanal.json", "r") as archivo:
            calendario_semanal = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al generar el reporte: No se encontró el archivo o no hay datos registrados.")
        return


    dias_orden = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    # Agrupamos los eventos por día
    reporte_por_dia = {}
    for evento in calendario_semanal:
        dia = evento["Dia"]
        if dia not in reporte_por_dia:
            reporte_por_dia[dia] = []
        reporte_por_dia[dia].append(evento)

    # Construimos el reporte final
    reporte_final = []
    for dia in dias_orden:
        if dia in reporte_por_dia:
            eventos = reporte_por_dia[dia]
            eventos_ordenados = sorted(eventos, key=lambda x: x["Hora de inicio"])
            reporte_final.append({
                "dia": dia,
                "eventos": [
                    {
                        "materia": evento["Materia o actividad"],
                        "hora_inicio": evento["Hora de inicio"],
                        "hora_fin": evento["Hora de finalizacion"],
                        "ubicacion": evento["Ubicacion"]
                    }
                    for evento in eventos_ordenados
                ]
            })
        else:
            reporte_final.append({
                "dia": dia,
                "eventos": []
            })
                
            
            

    # Guardamos el archivo con el nombre que pide el enunciado
    with open("reporte_horario.json", "w") as archivo_reporte:
        json.dump(reporte_final, archivo_reporte, indent=4)

    # Mostramos en consola con paginación (un día a la vez)
    print("\n==========================================")
    print("REPORTE DEL HORARIO SEMANAL")
    print("==========================================")
    
    
    for dia_info in reporte_final:
        print(f"\nDía: {dia_info['dia']}")
        if dia_info["eventos"]:
            for evento in dia_info["eventos"]:
                print(dia_info["eventos"])
               
        else:
            print("  No hay eventos registrados para este día.")
    
            
    

    input("Presione ENTER para continuar...")



    print("\nReporte generado exitosamente en 'reporte_horario.json'")