# Création d'une liste vide pour stocker les clients
clients = []

# Ajout de clients à la liste
for i in range(50):
    nom_client = f"Client {i+1}"
    email_client = f"client{i+1}@exemple.com"
    montant_depense = i * 10  # Montant factice pour l'exemple
    
    # Création du dictionnaire client
    client = {"nom": nom_client, "email": email_client, "montant_depense": montant_depense}
    
    # Ajout du client à la liste
    clients.append(client)

# Affichage de la liste complète des clients
print(clients)
