cout_campagne = float(input("Entrez le coût de la campagne : "))
revenu_genere = float(input("Entrez le revenu généré : "))

if revenu_genere > cout_campagne:
    print("La campagne a été rentable.")
elif revenu_genere == cout_campagne:
    print("La campagne a été ni rentable ni non rentable.")
else:
    print("La campagne n'a pas été rentable.")
