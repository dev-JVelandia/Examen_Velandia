import json

from Registro import registro_materias_y_actividades
from Mostrar import Mostrar_Calendario_Semanal 
from Reporte import generar_reporte
from validaciones import (
    validacion_eventos_registrados, 
    validacion_materia_actividad, 
    validacion_conflicto_horario, 
    validacion_dia_semana, 
    validacion_horas, 
    validacion_materia_actividadN, 
    validacion_ubicacion
)

def guardar_calendario(calendario):
    """Guarda la lista de eventos en el archivo JSON."""
    with open("Calendario_Semanal.json", "w") as archivo:
        json.dump(calendario, archivo, indent=4)

def menu_principal():
    Calendario_Semanal = []

    while True:
        print("\n========Bienvenido al registro de materias y actividades========")
        print("   1. Registrar materia o actividad")
        print("   2. Modificar materia o actividad")
        print("   3. Eliminar materia o actividad")
        print("   4. Mostrar calendario semanal")
        print("   5. Generar reporte")
        print("   6. Salir")
        print("================================================================")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            Calendario_Semanal = validacion_eventos_registrados()
            evento = registro_materias_y_actividades()

            if (
                validacion_materia_actividad(evento["Materia o actividad"]) and
                validacion_materia_actividadN(evento["Materia o actividad"]) and
                validacion_dia_semana(evento["Dia"]) and
                validacion_horas(evento["Hora de inicio"], evento["Hora de finalizacion"]) and
                validacion_ubicacion(evento["Ubicacion"]) and
                validacion_conflicto_horario(evento["Dia"], evento["Hora de inicio"], evento["Hora de finalizacion"])
            ):
                Calendario_Semanal.append(evento)
                guardar_calendario(Calendario_Semanal)
                print("Materia o actividad registrada exitosamente")
            else:
                print("No se pudo registrar debido a errores de validación.")

        elif opcion == "2":
            Calendario_Semanal = validacion_eventos_registrados()
            
            if not Calendario_Semanal:
                print("No hay eventos registrados para modificar.")
            else:
                print("\nEventos registrados:")
                for i, actividad in enumerate(Calendario_Semanal):
                    print(f"{i + 1}. {actividad['Materia o actividad']} - {actividad['Dia']} - {actividad['Hora de inicio']} a {actividad['Hora de finalizacion']} - {actividad['Ubicacion']}")
                
                try:
                    indice = int(input("\nIngrese el numero del evento que desea modificar: ")) - 1 
                    
                    if 0 <= indice < len(Calendario_Semanal):
                        evento_original = Calendario_Semanal.pop(indice)
                        guardar_calendario(Calendario_Semanal)

                        nuevo_evento = registro_materias_y_actividades()
                        
                        if (
                            validacion_materia_actividad(nuevo_evento["Materia o actividad"]) and
                            validacion_materia_actividadN(nuevo_evento["Materia o actividad"]) and
                            validacion_dia_semana(nuevo_evento["Dia"]) and
                            validacion_horas(nuevo_evento["Hora de inicio"], nuevo_evento["Hora de finalizacion"]) and
                            validacion_ubicacion(nuevo_evento["Ubicacion"]) and
                            validacion_conflicto_horario(nuevo_evento["Dia"], nuevo_evento["Hora de inicio"], nuevo_evento["Hora de finalizacion"])
                        ):
                            Calendario_Semanal.insert(indice, nuevo_evento)
                            guardar_calendario(Calendario_Semanal)
                            print("Evento modificado exitosamente")
                        else:
                            Calendario_Semanal.insert(indice, evento_original)
                            guardar_calendario(Calendario_Semanal)
                            print("No se pudo modificar el evento debido a errores de validación.")
                    else:
                        print("Indice invalido")
                except ValueError:
                    print("Entrada invalida, por favor ingrese un numero")

        elif opcion == "3":
            Calendario_Semanal = validacion_eventos_registrados()
            
            if not Calendario_Semanal:
                print("No hay eventos registrados para eliminar.")
            else:
                print("\nEventos registrados:")
                for i, actividad in enumerate(Calendario_Semanal):
                    print(f"{i + 1}. {actividad['Materia o actividad']} - {actividad['Dia']} - {actividad['Hora de inicio']} a {actividad['Hora de finalizacion']} - {actividad['Ubicacion']}")
                
                try:
                    indice = int(input("\nIngrese el numero del evento que desea eliminar: ")) - 1
                    if 0 <= indice < len(Calendario_Semanal):
                        Calendario_Semanal.pop(indice)
                        guardar_calendario(Calendario_Semanal)
                        print("Evento eliminado exitosamente")
                    else:
                        print("Indice invalido")
                except ValueError:
                    print("Entrada invalida, por favor ingrese un numero")

        elif opcion == "4":
            Mostrar_Calendario_Semanal()

        elif opcion == "5":
            generar_reporte()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida, por favor intente de nuevo")

if __name__ == "__main__":
    menu_principal()