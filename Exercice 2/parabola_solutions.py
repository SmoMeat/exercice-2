# Auteur: Mathieu Ducharme
# Date: 27 janvier 2024

from math import sqrt

def get_solutions_of_parabola(a: float, b: float, c: float) -> [float]: # make args float or int
    discriminant = b**2 - 4 * a * c
    solutions = []
    if discriminant < 0:
        return solutions
    
    solutions.append((-b + sqrt(discriminant)) / (2 * a))

    if discriminant == 0:
        return solutions
    
    solutions.append((-b - sqrt(discriminant)) / (2 * a))

    return solutions

def print_solutions_of_parabola(a, b, c):
    solutions = get_solutions_of_parabola(a, b, c)
    if len(solutions) == 0:
        return print(f"Il n'existe aucune solution à l'équation {a}x²+{b}x+{c}")
    if len(solutions) == 1:
        return print(f"La solution à l'équation {a}x²+{b}x+{c} est {solutions[0]}")
    return print(f"Les solutions à l'équation {a}x²+{b}x+{c} sont {solutions[0]} et {solutions[1]}")

if __name__ == '__main__':
    print_solutions_of_parabola(2, 5, 2)
    print_solutions_of_parabola(1, 2, 1)
    print_solutions_of_parabola(2, 2, 2)
