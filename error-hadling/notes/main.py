def calcular_promedio_ponderado(notas, pesos):
    """
        Calcula el promedio ponderado de una lista de notas cientificas.
        Maneja errores comunes como longitud desigual, listas vacias o valores no numericos.
    """

    try:
        if not notas or not pesos:
            raise ValueError("La listas no puede estar vacias.")

        if len(notas) != len(pesos):
            raise ValueError(
                "Las listas de notas y pesos debe tener la misma longitud.")

        # ? Verificamos que todos sean numeros
        for n, p in zip(notas, pesos):
            if not isinstance(n, (int, float)) or not isinstance(p, (int, float)):
                raise TypeError("Todas las notas y pesos debe ser numericos.")

        suma_pesos = sum(pesos)
        if suma_pesos == 0:
            raise ZeroDivisionError("La suma de los pesos no puede ser cero.")

        promedio = sum(n * p for n, p in zip(notas, pesos)) / suma_pesos

    except ValueError as ve:
        print(f"Error de valor: {ve}")
        return None
    except TypeError as te:
        print(f"Error de tipo: {te}")
        return None
    except ZeroDivisionError as ze:
        print(f"Error matematico: {ze}")
        return None
    else:
        print("Cálculo exitoso ✅")
        return promedio
    finally:
        print("Ejecución finalizada.\n")


#! ----- PRUEBAS -----
notas_correctas = [4.5, 3.8, 5.0]
pesos_correctas = [0.4, 0.3, 0.3]

print("Resultado:", calcular_promedio_ponderado(
    notas_correctas, pesos_correctas))

# ? Error: listas desiguales
print("Resultado: ", calcular_promedio_ponderado([4.5, 3.8], [0.4, 0.3, 0.3]))

# ? Error: esos suman cero
print("Resultado: ", calcular_promedio_ponderado([4.5, 3.8, 5.0], [0, 0, 0]))

# ? Error: valor numérico
print("Resultado: ", calcular_promedio_ponderado(
    [4.5, "Error", 5.0], [0.4, 0.3, 0.3]))
