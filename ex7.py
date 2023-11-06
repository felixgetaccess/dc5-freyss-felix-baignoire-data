# Liste des clients (comme générée dans l'exercice précédent)
clients = [
    {"nom": "Client 1", "email": "client1@exemple.com", "montant_depense": 10},
    {"nom": "Client 2", "email": "client2@exemple.com", "montant_depense": 120},
    {"nom": "Client 3", "email": "client3@exemple.com", "montant_depense": 80},
    # ... Ajoutez d'autres clients comme nécessaire
]

# Définition de la fonction qui calcule le montant total dépensé
def montant_total_depense(clients):
    total = 0
    for client in clients:
        total += client["montant_depense"]
    return total

# Appel de la fonction
total_depense = montant_total_depense(clients)

# Affichage du montant total dépensé
print(f"Le montant total dépensé par tous les clients est de : {total_depense}€")
