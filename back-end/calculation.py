import numpy as np

def area(diameter):
    return np.pi * diameter**2 / 4


def velocity(flow_rate, diameter):
    A = area(diameter)
    return flow_rate / A


def reynolds_number(rho, velocity, diameter, mu):
    return (rho * velocity * diameter) / mu


def friction_factor(Re):
    if Re < 2300:
        return 64 / Re
    else:
        return 0.3164 / (Re ** 0.25)


def pressure_drop(f, length, diameter, rho, velocity):
    return f * (length / diameter) * (rho * velocity**2 / 2)
