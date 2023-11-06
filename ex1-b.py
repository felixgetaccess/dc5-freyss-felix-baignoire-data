phrase_utilisateur = input("Veuillez saisir une phrase : ")

phrase_majuscules = ""
phrase_minuscules = ""

for caractere in phrase_utilisateur:
    if caractere.isalpha():
        phrase_majuscules += caractere.upper()
        phrase_minuscules += caractere.lower()
    else:
        phrase_majuscules += caractere
        phrase_minuscules += caractere

mot = False
nombre_mots = 0

for caractere in phrase_utilisateur:
    if caractere.isalpha() and not mot:
        mot = True
        nombre_mots += 1
    elif not caractere.isalpha():
        mot = False

print(f"La phrase en majuscules : {phrase_majuscules}")
print(f"La phrase en minuscules : {phrase_minuscules}")
print(f"Le nombre de mots dans la phrase : {nombre_mots}")
