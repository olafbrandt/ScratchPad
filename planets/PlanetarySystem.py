import math
import random
import scipy.constants

from Planet import Planet

class PlanetarySystem():

    def __init__(self):
        self.min_order = 1
        self.planets = {}
        self.planetorder = {}

    def AddPlanet(self, p, order=None):
        if order is None:
            order = p.order
        if order is None:
            order = self.min_order
        p.order = order
        self.planets[p.name] = p
        self.planetorder[order] = p.name
        while (self.min_order in self.planetorder):
            self.min_order += 1
        return (p)

    def pretty_print(self):
        for p in sorted(self.planets.values(), key=lambda x: x.order):
            p.set_relative(earth)
            p.pretty_print()
            print()

solar_system = PlanetarySystem()

earth_density = 5.514 / 1000 * 100**3
pluto_density = 1.854 / 1000 * 100**3

earth = Planet('Earth', 5.97237e24, 6371.0, 9.80665, earth_density)
pluto = Planet('Pluto',   1.303e22, 1188, 0.62, pluto_density)

solar_system.AddPlanet(earth, order=3)
solar_system.AddPlanet(Planet('Mercury', 0.055, 0.3829, relative=earth))
solar_system.AddPlanet(Planet('Venus', 0.815, 0.9499, relative=earth))
solar_system.AddPlanet(Planet('Mars', 0.107, 0.531, relative=earth))
solar_system.AddPlanet(Planet('Jupiter', 1.8982e27, 69911, 24.79, 1326))
solar_system.AddPlanet(Planet('Saturn', 95.159, 9.449, relative=earth))
solar_system.AddPlanet(Planet('Uranus', 14.536, 4.007, relative=earth))
solar_system.AddPlanet(Planet('Neptune', 17.147, 3.883, relative=earth))
solar_system.AddPlanet(pluto)

solar_system.pretty_print()

solar_system.AddPlanet(Planet.GenerateDwarfPlanet())
