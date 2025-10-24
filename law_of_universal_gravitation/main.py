import numpy as np
import matplotlib.pyplot as plt

#? Constante gravitacional
G = 6.67430e-11 #? N·m²/kg²

#todo ------ Clase Cuerpo Celeste ------
class CuerpoCeleste:
    def __init__(self, name: str, mass: float, position: np.ndarray):
        self.name = name
        self.mass = mass #! en kg
        self.position = np.array(position, dtype=float) #! Vector [x, y]


    def distance_a(self, other: "CuerpoCeleste") -> float:
        """ Calcula la distancia entre dos cuerpos usando norma de Numpy"""
        return np.linalg.norm(self.position - other.position)

    def fuerza_gravitacional_a(self, other: "CuerpoCeleste") -> float:
        """ Devuelve el vector fuerza gravitacional que ejerce otro cuerpo """

        address = other.position - self.position
        distance = np.linalg.norm(address)
        if distance == 0:
            return np.zeros(2)
        force_magnitude = G * (self.mass * other.mass) / distance**2
        force_direction = address / distance
        return force_magnitude *  force_direction

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
                    print(f"Fuerza entre {body.name} y {body2.name}: {force} N")

    def graphic_system(self):
        """ Dibuja la posición de los cuerpos celestes"""
        plt.figure(figsize=(6, 6))
        plt.title("Sistema Newtoniano (coordenadas vectoriales)")
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        for body in self.body:
            plt.scatter(*body.position, label=body.name, s=100)
            plt.text(body.position[0] + 1e10, body.position[1] + 1e10, body.name)
        plt.legend()
        plt.grid(True)
        plt.show()

#todo ---- Ejemplo de uso ----
if __name__ == "__main__":
    system = SistemaNewtoniano()

    #? Crear cuerpos: Sol y Tierra
    sol = CuerpoCeleste("Sol", 1.989e30, [0, 0])
    tierra = CuerpoCeleste("Tierra", 5.972e24, [1.496e11, 0])
    marte = CuerpoCeleste("Marte", 6.39e23, [2.279e11, 1.5e10])

    #? Agregar al sistema
    system.add_body(sol)
    system.add_body(tierra)
    system.add_body(marte)

    #? Calcular fuerzas
    system.calculate_force()

    #? Graficar sistema
    system.graphic_system()