phrase_utilisateur = input("Veuillez saisir une phrase : ")

phrase_majuscules = phrase_utilisateur.upper()
phrase_minuscules = phrase_utilisateur.lower()

print(f"La phrase en majuscules : {phrase_majuscules}")
print(f"La phrase en minuscules : {phrase_minuscules}")

mots = phrase_utilisateur.split()
nombre_mots = len(mots)

print(f"Le nombre de mots dans la phrase : {nombre_mots}")
