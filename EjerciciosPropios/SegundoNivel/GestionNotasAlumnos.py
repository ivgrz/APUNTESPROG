def notas_alumnos():
    alumnos = []
    while True:
        ingreso_alumno = input(
            "Ingresa notas de alumno, formato 'alumno nota': ")

        if ingreso_alumno == "fin":
            break
        else:
            alumno, nota = ingreso_alumno.split()
            nota = float(nota)
            alumnos.append((alumno, nota))

    # Mostrar resultados despues de recoger todos los datos
    for nombre, nota in alumnos:
        if nota >= 5:
            print(f"Alumno {nombre} esta aprobado")
        elif nota >= 0:
            print(f"Alumno {nombre} suspenso")
        else:
            raise ValueError("Nota no puede ser negativa")


if __name__ == "__main__":
    notas_alumnos()
