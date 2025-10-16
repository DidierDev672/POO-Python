from dataclasses import dataclass, field
from typing import Optional, List, Tuple
import math
import matplotlib.pyplot as plt

# -------------------------
# Constantes físicas
# -------------------------
G = 6.67430e-11            # Constante gravitacional (m^3 kg^-1 s^-2)
AU = 1.495978707e11        # Unidad astronómica (m)
DAY = 86400                # Segundos en un día
YEAR = 365.25 * DAY        # Un año terrestre en segundos

# -------------------------
# Clases base
# -------------------------
@dataclass
class CelestialBody:
    name: str
    mass: float
    radius: float = 0.0
    parent: Optional["CelestialBody"] = None
    semi_major_axis: Optional[float] = None
    _orbital_period: Optional[float] = field(default=None, init=False)

    def __post_init__(self):
        if self.parent and self.semi_major_axis is not None:
            self._orbital_period = self._calc_orbital_period()
        else:
            self._orbital_period = None

    def _calc_orbital_period(self) -> float:
        """Cálculo de periodo orbital usando la tercera ley de Kepler"""
        a = self.semi_major_axis
        M = self.parent.mass if self.parent else 0.0
        return 2 * math.pi * math.sqrt(a**3 / (G * (M + self.mass)))

    def position_at_time(self, t: float) -> Tuple[float, float]:
        """Calcula posición (x,y) en el tiempo t asumiendo órbita circular"""
        if not self.parent or self.semi_major_axis is None or self._orbital_period is None:
            return (0.0, 0.0)

        T = self._orbital_period
        theta = 2 * math.pi * (t % T) / T
        a = self.semi_major_axis

        x_rel = a * math.cos(theta)
        y_rel = a * math.sin(theta)

        px, py = self.parent.position_at_time(t)
        return (px + x_rel, py + y_rel)

class SolarSystem:
    def __init__(self, name="Sistema Solar"):
        self.name = name
        self.bodies: List[CelestialBody] = []
        self.planetas = []

    def add_body(self, body: CelestialBody):
        self.bodies.append(body)

    def simulate_positions(self, t_seconds: float) -> List[Tuple[str, float, float]]:
        return [(b.name, *b.position_at_time(t_seconds)) for b in self.bodies]

    def plot_orbits(self, days_to_simulate: int = 365):
        """Dibuja órbitas y posiciones actuales"""
        plt.figure(figsize=(9, 9))
        plt.title(f"Órbitas del {self.name}")
        plt.xlabel("Distancia X (UA)")
        plt.ylabel("Distancia Y (UA)")
        plt.grid(True)
        plt.axis("equal")

        t_values = [i * DAY for i in range(0, days_to_simulate, 5)]

        for b in self.bodies:
            if not b.parent:
                continue

            xs, ys = [], []
            for t in t_values:
                x, y = b.position_at_time(t)
                xs.append(x / AU)
                ys.append(y / AU)

            plt.plot(xs, ys, label=b.name)
            x_now, y_now = b.position_at_time(t_values[-1])
            plt.scatter(x_now / AU, y_now / AU, s=50)

        plt.scatter(0, 0, color="yellow", s=250, label="Sol")
        plt.legend(loc="upper right")
        plt.show()

    def distance_difference(self, name1, name2):
        """ Busca dos planetas por nombre y caclula la diferencia de distancia """
        p1 = next((p for p in self.planetas if p.name == name1), None)
        p2 = next((p for p in self.planetas if p.name == name2), None)

        if not p1 or not p2:
            print("Error: Uno o ambos planetas no existen en el sistema.")
            return
        diferencia = p1.diferencia_con(p2)
        print(f"La diferencia de distancia entre {p1.nombre} y {p2.nombre} es {diferencia:.2f} km.")

# -------------------------
# Ejemplo: Sistema Solar completo
# -------------------------
if __name__ == "__main__":
    ss = SolarSystem()

    # Sol
    sun = CelestialBody(name="Sol", mass=1.98847e30)
    ss.add_body(sun)

    moon = CelestialBody(name="Luna", mass=7.342e22)
    ss.add_body(moon)



    # Planetas (valores aproximados)
    planet_data = [
        ("Mercurio", 3.3011e23, 0.387 * AU),
        ("Venus",   4.8675e24, 0.723 * AU),
        ("Tierra",  5.9722e24, 1.000 * AU),
        ("Marte",   6.4171e23, 1.524 * AU),
        ("Júpiter", 1.8982e27, 5.204 * AU),
        ("Saturno", 5.6834e26, 9.582 * AU),
        ("Urano",   8.6810e25, 19.201 * AU),
        ("Nptuno", 1.02413e26, 30.047 * AU),
    ]

    for name, mass, dist in planet_data:
        planet = CelestialBody(name=name, mass=mass, parent=sun, semi_major_axis=dist)
        ss.add_body(planet)

    # Graficar las órbitas durante 2 años
    ss.plot_orbits(days_to_simulate=360*2)
