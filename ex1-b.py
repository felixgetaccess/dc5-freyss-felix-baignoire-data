# Demander à l'utilisateur de saisir une phrase
phrase_utilisateur = input("Veuillez saisir une phrase : ")

# Convertir la phrase en majuscules
phrase_majuscules = ""
for caractere in phrase_utilisateur:
    if 'a' <= caractere <= 'z':
        lettre_majuscule = chr(ord(caractere) - 32)
        phrase_majuscules += lettre_majuscule
    else:
        phrase_majuscules += caractere

# Convertir la phrase en minuscules
phrase_minuscules = ""
for caractere in phrase_utilisateur:
    if 'A' <= caractere <= 'Z':
        lettre_minuscule = chr(ord(caractere) + 32)
        phrase_minuscules += lettre_minuscule
    else:
        phrase_minuscules += caractere

# Compter le nombre de mots
mot = False
nombre_mots = 0

for caractere in phrase_utilisateur:
    if caractere.isalpha() and not mot:
        mot = True
        nombre_mots += 1
    elif not caractere.isalpha():
        mot = False

# Afficher les résultats
print(f"La phrase en majuscules : {phrase_majuscules}")
print(f"La phrase en minuscules : {phrase_minuscules}")
print(f"Le nombre de mots dans la phrase : {nombre_mots}")
