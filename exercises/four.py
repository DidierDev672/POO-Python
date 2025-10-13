
# todo: Crea una calculadora con metodos estaticos para sumar, restar, multiplicar y dividir

class Calculator():
    def __init__(self, operator):
        self.operator = operator

    def calculate(self, a, b):
        if self.operator == "suma":
            return a + b

        if self.operator == "resta":
            return a - b

        if self.operator == "multiplicar":
            return a * b

        if self.operator == "dividir":
            return a / b


operation = Calculator("suma")
operationRestar = Calculator("resta")
operationMultiplicar = Calculator("multiplicar")
operationDividir = Calculator("dividir")


print(f"Suma: {operation.calculate(5, 3)}")
print(f"Resta: {operationRestar.calculate(5, 3)}")
print(f"Multiplicar: {operationMultiplicar.calculate(5, 3)}")
print(f"Dividir: {operationDividir.calculate(5, 3)}")
