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

parabolas = [
    {"a": 2, "b": 5, "c": 2},   # Premier polynome
    {"a": 1, "b": 2, "c": 1},   # Deuxième polynome
    {"a": 2, "b": 2, "c": 2}    # Troisième polynome
]

for parabola in parabolas:
    a = parabola['a']   # coefficient associé à x puissance 2
    b = parabola['b']   # coefficient associé à x puissance 1
    c = parabola['c']   # coefficient associé à x puissance 0

    discriminant = b**2 - 4 * a * c     # Discriminant (Δ) pour déterminer cmb de solutions existent

    if discriminant < 0: # Cas avec 0 solution
        print(f"Il n'existe aucune solution à l'équation {a}x²{b:+}x{c:+}.")
        continue

    first_solution = (-b + sqrt(discriminant)) / (2 * a)    # Solution de la plus grande selon la formule quadratique

    if discriminant == 0: # Cas avec 1 solution
        print(f"La solution à l'équation {a}x²{b:+}x{c:+} est {first_solution}.")
        continue

    second_solution = (-b - sqrt(discriminant)) / (2 * a)   # Solution de la plus petite selon la formule quadratique

    print(f"Les solutions à l'équation {a}x²{b:+}x{c:+} sont {first_solution} et {second_solution}.")