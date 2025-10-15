from dataclasses import dataclass, field
from typing import Optional, List, Tuple
import math
import matplotlib.pyplot as plt

# ? Constantes físicas
G = 6.67430e-11  # ? Constante gravitacional (m^3 kg^-1 s^-2)
AU = 1.495978707e11  # ? Unidad astronómica en metros
DAY = 86400  # ? Segundos en un día
YEAR = 365.25 * DAY


@dataclass
class CelestialBody:
    name: str
    mass: float                         # kg
    radius: float = 0.0                 # m (opcional)
    parent: Optional["CelestialBody"] = None
    # ? metros (distancia media al padre)
    semi_major_axis: Optional[float] = None
    eccentricity: float = 0.0           # no usado en este modelo circular
    _orbital_period: Optional[float] = field(
        default=None, init=False)  # segundos, calculado

    def __post_init__(self):
        if self.parent and self.semi_major_axis is not None:
            self._orbital_period = self._calc_orbital_period()
        else:
            self._orbital_period = None

    def _calc_orbital_period(self) -> float:
        # ? T = 2π * sqrt(a^3 / (G*(M_parent + m))) — normalmente m << M_parent
        a = self.semi_major_axis
        M = self.parent.mass if self.parent else 0.0
        return 2 * math.pi * math.sqrt(a**3 / (G * (M + self.mass)))

    def position_at_time(self, t: float) -> Tuple[float, float]:
        if not self.parent or self.semi_major_axis is None or self._orbital_period is None:
            return (0.0, 0.0)

        T = self._orbital_period
        theta = 2 * math.pi * (t % T) / T

        a = self.semi_major_axis
        x_rel = a * math.cos(theta)
        y_rel = a * math.sin(theta)

        px, py = self.parent.position_at_time(t)
        return (px + x_rel, py + y_rel)

    @property
    def orbital_period(self) -> Optional[float]:
        return self._orbital_period

    def position_at_time(self, t: float) -> Tuple[float, float]:
        """
        Devuelve (x, y) en metros en un plano con el padre en su origen.
        - Si no tiene padre (por ejemplo, el Sol), lo ubicamos en (0,0).
        - Asumimos órbitas circulares y movimiento con fase 0 en t=0 (x = a, y = 0).
        """
        if not self.parent or self.semi_major_axis is None or self._orbital_period is None:
            # ? cuerpo central: posición absoluta (0,0)
            return (0.0, 0.0)

        T = self._orbital_period
        # ? Fracción del periodo (ángulo)
        frac = (t % T) / T
        theta = 2 * math.pi * frac  # radianes
        a = self.semi_major_axis

        # ? posición relativa al padre
        x_rel = a * math.cos(theta)
        y_rel = a * math.sin(theta)

        # ? obtener posición absoluta del padre (recursivo)
        px, py = self.parent.position_at_time(t)
        return (px + x_rel, py + y_rel)

    def __str__(self):
        if self.orbital_period:
            days = self.orbital_period / DAY
            return f"{self.name} (masa={self.mass:.2e} kg, a={self.semi_major_axis/AU:.3f} AU, periodo={days:.2f} días)"
        else:
            return f"{self.name} (masa={self.mass:.2e} kg, central)"


class SolarSystem:
    def __init__(self, name="Sistema Solar"):
        self.name = name
        self.bodies: List[CelestialBody] = []

    def add_body(self, body: CelestialBody):
        self.bodies.append(body)

    def get_body(self, name: str) -> Optional[CelestialBody]:
        for b in self.bodies:
            if b.name.lower() == name.lower():
                return b
        return None

    def simulate(self, t_seconds: float) -> List[Tuple[str, float, float]]:
        """
        Devuelve lista de (nombre, x, y) de cada cuerpo en el instante t_seconds.
        """
        result = []
        for b in self.bodies:
            x, y = b.position_at_time(t_seconds)
            result.append((b.name, x, y))
        return result

    def simulate_positions(self, t_seconds: float) -> List[Tuple[str, float, float]]:
        return [(b.name, *b.position_at_time(t_seconds)) for b in self.bodies]

    def plot_orbits(self, days_to_simulate: int = 365):
        """
        Dibuja las órbitas de todos los cuerpos y su posición actual.
        """

        plt.figure(figsize=(8, 8))
        plt.title(f"Orbitas del {self.name}")
        plt.xlabel("Distancia x (UA)")
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
            # ? Posicion actual al final del recorrido
            x_now, y_now = b.position_at_time(t_values[-1])
            plt.scatter(x_now / AU, y_now / AU, s=50)

        plt.scatter(0, 0, color="yellow", s=200, label="Sol")
        plt.legend()
        plt.show()


# -------------------------
#! EJEMPLO DE USO
# -------------------------
if __name__ == "__main__":
    ss = SolarSystem()

    # ? Sol
    sun = CelestialBody(name="Sol", mass=1.98847e30)
    ss.add_body(sun)

    # ? Tierra
    earth = CelestialBody(name="Tierra", mass=5.9722e24,
                          parent=sun, semi_major_axis=1.0 * AU)
    ss.add_body(earth)

    # ? Luna
    moon = CelestialBody(name="Luna", mass=7.342e22,
                         parent=earth, semi_major_axis=384400e3)
    ss.add_body(moon)

    # ? Marte
    mars = CelestialBody(name="Marte", mass=6.4171e23,
                         parent=sun, semi_major_axis=1.523679 * AU)
    ss.add_body(mars)

    # ?Dibujar las órbitas durante un año
    ss.plot_orbits(days_to_simulate=365)

    # # ? Mostrar info de cuerpos
    # for b in ss.bodies:
    #     print(b)

    # print("\nPosiciones en t = 0 (m):")
    # for name, x, y in ss.simulate(0):
    #     print(f"{name:7s} -> x={x:.3e} m, y={y:.3e} m")

    # # ? Simular varias fechas: t = 0, 30, 365 días
    # tiempos_dias = [0, 30, 365]
    # print("\nPosiciones (en AU) en varios tiempos:")
    # for d in tiempos_dias:
    #     t = d * DAY
    #     print(f"\nDía {d}:")
    #     for name, x, y in ss.simulate(t):
    #         print(f"{name:7s} -> x={x/AU:.6f} AU, y={y/AU:.6f} AU")

    # ? Dibujar las orbitas durante un year
    ss.plot_orbits(days_to_simulate=365)
