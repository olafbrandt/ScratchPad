import math
import random
import scipy.constants

# gravitational_constant = scipy.constants.physical_constants['Newtonian constant of gravitation'][0]
# gravitational_constant = scipy.constants.value('Newtonian constant of gravitation')
gravitational_constant = scipy.constants.gravitational_constant
# gravitational_constant = 6.67408e-11
# print (gravitational_constant)

class Planet:
    def __init__(self, name, mass, radius, surface_gravity=0, density=0, order=None, relative=None):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.surface_gravity = surface_gravity
        self.density = density
        self.order = order
        self.relative = relative
        
        if self.relative is not None:
            self.mass = self.mass * relative.mass
            self.radius = self.radius * relative.radius
            self.surface_gravity = self.surface_gravity * relative.surface_gravity
            self.density = self.density * relative.density
            
        if self.surface_gravity == 0:
            self.surface_gravity = self.calc_surface_gravity()
        if self.density == 0:
            self.density = self.calc_density()
        self.area = self.calc_area()
        self.volume = self.calc_volume()
        self.circumference = self.calc_circumference()  

    def __str__(self):
        return ('Planet {}: Surface Gravity: {} m/(s*s), Mass: {} kg, Density: {} kg/(m*m*m), Radius: {} km'.format(
            self.name, self.surface_gravity, self.mass, self.density, self.radius))
    
    def calc_circumference(self):
        return (2.0 * math.pi * self.radius)
    
    def calc_area(self):
        return (4.0 * math.pi * self.radius * self.radius)

    def calc_volume(self):
        return ((4.0 / 3.0) * math.pi * (self.radius * self.radius * self.radius))

    def calc_density(self):
        return (self.mass / (self.calc_volume() * 1000**3))

    def calc_surface_gravity(self):
        radius_meters = self.radius * 1000
        return (gravitational_constant * self.mass / (radius_meters * radius_meters))

    def set_relative(self, relative_planet = None):
        old_relative = self.relative
        self.relative = relative_planet
        return (old_relative)
    
    def pretty_print(self, order=None, str_only = False):
        pp = ('{}Planet {}:\n'.format('{}. '.format(self.order) if self.order else '', self.name))
        if self.relative is None:
            pp = pp + (
                  '\t{:<20s} {:8.3e} kg\n'
                  '\t{:<20s} {:8.0f} km\n'
                  '\t{:<20s} {:8.3f} m/(s**2)\n'
                  '\t{:<20s} {:8.3f} kg/(m**3)\n'
                  '\t{:<20s} {:8.0f} km\n'
                  '\t{:<20s} {:8.3e} km**2\n'
                  '\t{:<20s} {:8.3e} km**3'.format(
                'Mass:', self.mass,
                'Radius:', self.radius,
                'Surface Gravity:', self.surface_gravity,
                'Density:', self.density,
                'Circumference:', self.circumference,
                'Surface Area:', self.area,
                'Volume:', self.volume))
        else:
            pp = pp + (
                  '\t{:<20s} {:11.3e} kg\t\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.0f} km\t\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.3f} m/(s**2)\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.3f} kg/(m**3)\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.0f} km\t\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.3e} km**2\t\t({:8.3f} {}s)\n'
                  '\t{:<20s} {:11.3e} km**3\t\t({:8.3f} {}s)'.format(
                'Mass:', self.mass, self.mass / self.relative.mass, self.relative.name,
                'Radius:', self.radius, self.radius / self.relative.radius, self.relative.name,
                'Surface Gravity:', self.surface_gravity, self.surface_gravity / self.relative.surface_gravity,
                      self.relative.name,
                'Density:', self.density, self.density / self.relative.density, self.relative.name,
                'Circumference:', self.circumference, self.circumference / self.relative.circumference,
                      self.relative.name,
                'Surface Area:', self.area, self.area / self.relative.area, self.relative.name,
                'Volume:', self.volume, self.volume / self.relative.volume, self.relative.name))
        if not str_only:
            print(pp)
            return None
        return (pp)