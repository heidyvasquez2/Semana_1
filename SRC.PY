#sistema de registro de calificaciones de estudiantes

#Definir una tupla con los nombres de los cursos del semestre

tup_cursos = (
    "Estructuras","Cálculo Multivariado","Arquitectura de Computadores", "Física","Fundamentos Administrativos", "Inglés"
)
#Cadena de texto con el nombre del estudiante
nombre_estudiante = "Juan Pablo Isaza Piñeros"

#Usar una lista para almacenar las calificaciones de cada curso
calificaciones = []
dic_cursos = {}

# Funciones
def mostrar_cursos():
    print("\nCursos disponibles:")
    for i, curso in enumerate(tup_cursos, start=1):
        if curso in dic_cursos:
            print(f"{i}. {curso} (Nota: {dic_cursos[curso]})")
        else:
            print(f"{i}. {curso} (Sin nota)")

def agregar_calificacion(curso, calificacion):
    dic_cursos[curso] = calificacion
    if curso not in calificaciones:   
        calificaciones.append(calificacion)
    print(f"Se registró la calificación {calificacion} en {curso}")

def modificar_calificacion(curso, calificacion):
    if curso in dic_cursos:
        dic_cursos[curso] = calificacion
        print(f"Se modificó la calificación de {curso} a {calificacion}")
    else:
        print("Ese curso no tiene calificación registrada.")

def eliminar_calificacion(curso):
    if curso in dic_cursos:
        dic_cursos.pop(curso)
        print(f"Se eliminó la calificación de {curso}")
    else:
        print("Ese curso no tiene calificación registrada.")

def prom():
    if len(dic_cursos) == 0:
        return 0
    return sum(dic_cursos.values()) / len(dic_cursos)

# Menú principal
def main():
    while True:
        print("\nSistema de registro de calificaciones")
        print("Estudiante:", nombre_estudiante)
        print("\n1. Agregar calificación")
        print("2. Modificar calificación")
        print("3. Eliminar calificación")
        print("4. Calcular promedio")
        print("5. Ver todas las calificaciones")
        print("6. Salir")

        try:
            seleccion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if seleccion == 1:
            mostrar_cursos()
            try:
                num = int(input("Seleccione el número del curso: "))
                curso = tup_cursos[num - 1]
                nota = float(input(f"Ingrese la calificación para {curso}: "))
                agregar_calificacion(curso, nota)
                
            except (ValueError, IndexError):
                print("Entrada inválida.")

        elif seleccion == 2:
            mostrar_cursos()
            try:
                num = int(input("Seleccione el número del curso: "))
                curso = tup_cursos[num - 1]
                nota = float(input(f"Ingrese la nueva calificación para {curso}: "))
                modificar_calificacion(curso, nota)
            except (ValueError, IndexError):
                print("Entrada inválida.")

        elif seleccion == 3:
            mostrar_cursos()
            try:
                num = int(input("Seleccione el número del curso: "))
                curso = tup_cursos[num - 1]
                eliminar_calificacion(curso)
            except (ValueError, IndexError):
                print("Entrada inválida.")

        elif seleccion == 4:
            print("El promedio actual es:", prom())

        elif seleccion == 5:
            if dic_cursos:
                print("\nCalificaciones registradas:")
                for c, nota in dic_cursos.items():
                    print(f"{c}: {nota}")
            else:
                print("No hay calificaciones registradas.")

        elif seleccion == 6:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
