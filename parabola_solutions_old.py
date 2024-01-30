"""parabola_solutions.py : Imprime les solutions d'une parabole

Ce fichier permet d'imprimer à la console les solutions réelles d'une équation du second dégré de
la forme ax²+bx+c et ce, meme s'il n'existe qu'une seule ou tout simplement pas de solutions, en
utilisant la fameuse formule quadratique x = (-b ± sqrt(b²-4ac)) / 2a. Pour plus d'informations,
consultez 'https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-formule-quadratique-m1134'.

@Date: 27 janvier 2024
@Author: Mathieu Ducharme
@Contact: mathieu.ducharme@umontreal.ca
@Matricule: 20297456
"""

from math import sqrt

def get_solutions_of_parabola(a: int | float, b: int | float, c: int | float) -> [float]:
    """
    Cette fonction retourne une liste contenant toutes les solutions réelles d'une équation du second degré de la forme ax²+bx+c où a≠0.
    Args:
        a (int ou float): coefficient associé à x puissance 2
        b (int ou float): coefficient associé à x puissance 1
        c (int ou float): coefficient associé à x puissance 0
    Returns:
        liste de float: une liste contenant des floats représentant les solutions (si aucune solution réelle n'existe, la liste est vide)
    """

    discriminant = b**2 - 4 * a * c
    solutions = []

    if discriminant < 0:
        return solutions
    
    solutions.append((-b + sqrt(discriminant)) / (2 * a))

    if discriminant == 0:
        return solutions
    
    solutions.append((-b - sqrt(discriminant)) / (2 * a))

    return solutions

def print_solutions_of_parabola(a: int | float, b: int | float, c: int | float) -> None:
    """
    Cette fonction imprime à la console toutes les solutions réelles d'une équation du second degré de la forme ax²+bx+c où a≠0.
    Args:
        a (int ou float): coefficient associé à x puissance 2
        b (int ou float): coefficient associé à x puissance 1
        c (int ou float): coefficient associé à x puissance 0
    """

    solutions = get_solutions_of_parabola(a, b, c)

    if len(solutions) == 0:
        print(f"Il n'existe aucune solution à l'équation {a}x²+{b}x+{c}")
        return
    if len(solutions) == 1:
        print(f"La solution à l'équation {a}x²+{b}x+{c} est {solutions[0]}")
        return
    
    print(f"Les solutions à l'équation {a}x²+{b}x+{c} sont {solutions[0]} et {solutions[1]}")

if __name__ == '__main__':
    print_solutions_of_parabola(2, 5, 2)
    print_solutions_of_parabola(1, 2, 1)
    print_solutions_of_parabola(2, 2, 2)