# Liste des clients (comme générée dans l'exercice précédent)
clients = [
    {"nom": "Client 1", "email": "client1@exemple.com", "montant_depense": 10},
    {"nom": "Client 2", "email": "client2@exemple.com", "montant_depense": 120},
    {"nom": "Client 3", "email": "client3@exemple.com", "montant_depense": 80},
    # ... Ajoutez d'autres clients comme nécessaire
]

# Parcourir la liste des clients
for client in clients:
    if client["montant_depense"] > 100:
        print(f"{client['nom']} a dépensé plus de 100€.")