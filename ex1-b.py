# Demander à l'utilisateur de saisir une phrase
phrase_utilisateur = input("Veuillez saisir une phrase : ")

# Initialiser le compteur de mots
nombre_mots = 0
mot = False

# Parcourir chaque caractère de la phrase
for caractere in phrase_utilisateur:
    if caractere != ' ':
        # Si le caractère n'est pas un espace, c'est un mot
        if not mot:
            mot = True
            nombre_mots += 1
    else:
        # Si le caractère est un espace, marquer la fin du mot
        mot = False

# Gérer le cas où la phrase se termine par un mot
if phrase_utilisateur and phrase_utilisateur[-1] != ' ':
    nombre_mots += 1

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

# Afficher les résultats
print(f"La phrase en majuscules : {phrase_majuscules}")
print(f"La phrase en minuscules : {phrase_minuscules}")
print(f"Le nombre de mots dans la phrase : {nombre_mots}")
