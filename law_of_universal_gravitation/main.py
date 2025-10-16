
import math
import matplotlib.pyplot as plt

#? Constante gravitacional
G = 6.67430e-11 #? N·m²/kg²

#todo ------ Clase Cuerpo Celeste ------
class CuerpoCeleste:
    def __init__(self, name: str, mass: float, x: float, y: float):
        self.name = name
        self.mass = mass #! en kg
        self.x = x #! en metros
        self.y = y #! en metros

    def position(self):
        return (self.x, self.y)

    def distance_a(self, other: "CuerpoCeleste") -> float:
        """ Calcula la distancia entre dos cuerpos  """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def fuerza_gravitacional_a(self, other: "CuerpoCeleste") -> float:
        """ Aplica la ley de gravitación universal para calcular la fuerza entre dos cuerpos """
        distance = self.distance_a(other)
        if distance == 0:
            return 0 #! Evitar división por cero
        force = G * (self.mass * other.mass) / (distance**2)
        return force

#! ------ Clase Sistema Solar ------
class SistemaNewtoniano:
    def __init__(self):
        self.body = []

    def add_body(self, body: CuerpoCeleste):
        self.body.append(body)

    def calculate_force(self):
        """ Muestra las fuerzas entre todos los cuerpos del sistema  """
        print("\n ---- Fuerzas gravitatorias ---")
        for i, body in enumerate(self.body):
            for j, body2 in enumerate(self.body):
                if i < j: #! Evita duplicados
                    force = body.fuerza_gravitacional_a(body2)
                    print(f"Fuerza entre {body.name} y {body2.name}: {force:.2e} N")

    def graphic_system(self):
        """ Dibuja la posición de los cuerpos celestes"""
        plt.figure(figsize=(6, 6))
        plt.title("Sistema Newtoniano (Posición de los cuerpos)")
        plt.xlabel("x")
        plt.ylabel("y")
        for body in self.body:
            plt.scatter(body.x, body.y, label=body.name, s=100)
            plt.text(body.x + 1e10, body.y + 1e10, body.name)
        plt.legend()
        plt.grid(True)
        plt.show()

#todo ---- Ejemplo de uso ----
if __name__ == "__main__":
    system = SistemaNewtoniano()

    #? Crear cuerpos: Sol y Tierra
    sol = CuerpoCeleste("Sol", 1.989e30, 0, 0)
    tierra = CuerpoCeleste("Tierra", 5.972e24, 1.496e11, 0)
    marte = CuerpoCeleste("Marte", 6.39e23, 2.279e11, 0)

    #? Agregar al sistema
    system.add_body(sol)
    system.add_body(tierra)
    system.add_body(marte)

    #? Calcular fuerzas
    system.calculate_force()

    #? Graficar sistema
    system.graphic_system()