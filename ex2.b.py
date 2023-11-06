liste_nombres = [12, 45, 67, 23, 90, 34, 56, 78, 89, 10]

maximum = liste_nombres[0]
minimum = liste_nombres[0]

for nombre in liste_nombres:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre

somme = 0

for nombre in liste_nombres:
    somme += nombre

nombre_elements = len(liste_nombres)
moyenne = somme / nombre_elements

print(f"Le maximum de la liste est : {maximum}")
print(f"Le minimum de la liste est : {minimum}")
print(f"La moyenne de la liste est : {moyenne}")
