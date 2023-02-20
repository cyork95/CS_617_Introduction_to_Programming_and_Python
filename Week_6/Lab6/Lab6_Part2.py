"""
Write a function KineticEnergy(m, v) that computes and returns the kinetic energy of an object whose mass is
m kilograms and whose velocity is v meters per second.
"""


def KineticEnergy(m, v):
    energy = 0.5 * (m * (v ** 2))
    return energy


mass = float(input("Enter the mass of the object: "))
velocity = float(input("Enter the velocity of the object: "))

kinetic_energy = KineticEnergy(mass, velocity)

print("The kinetic energy is {}!".format(kinetic_energy))
