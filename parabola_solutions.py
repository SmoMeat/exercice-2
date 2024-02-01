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

# Transforme un float/int en string et ajoute le signe '+' pour indiquer si le résultat est positif ou négatif
formatted_float = lambda num: str(num) if num < 0 else '+' + str(num)

parabolas = [
    {"a": 2, "b": 5, "c": 2},   # Premier polynome
    {"a": 1, "b": 2, "c": 1},   # Deuxième polynome
    {"a": 2, "b": 2, "c": 2}    # Troisième polynome
]

for parabola in parabolas:
    a = parabola['a']   # coefficient associé à x puissance 2
    b = parabola['b']   # coefficient associé à x puissance 1
    c = parabola['c']   # coefficient associé à x puissance 0

    # Définit un string de l'équation sous la forme ax²+bx+c et prend en considération le signe des coefs b et c pour
    # éviter d'avoir par exemple 2x²+-3x+-2 (peut etre éviter si on n'utilise pas code boot avec f"{a}x²{b:+}x{c:+}")
    parabola_string = str(a) + "x²" + (str(b) if b < 0 else '+' + str(b)) + "x" + (str(c) if c < 0 else '+' + str(c))

    if a == 0:
        print("L'équation", parabola_string, "n'est pas une équation du second degré")
        continue

    # Discriminant (Δ) pour déterminer cmb de solutions existent
    discriminant = b**2 - 4 * a * c

    if discriminant < 0: # Cas avec 0 solution
        print("Il n'existe aucune solution à l'équation", parabola_string)
        continue

    # Solution de la plus grande selon la formule quadratique
    first_solution = (-b + sqrt(discriminant)) / (2 * a)

    if discriminant == 0: # Cas avec 1 solution
        print("La solution à l'équation", parabola_string, "est", first_solution)
        continue
    
    # Solution de la plus petite selon la formule quadratique
    second_solution = (-b - sqrt(discriminant)) / (2 * a)

    print("Les solutions à l'équation", parabola_string, "sont", first_solution, "et", second_solution)