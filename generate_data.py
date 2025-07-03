# Importation des bibliothèques nécessaires
import pandas as pd               # Manipulation de données tabulaires
from faker import Faker           # Génération de données fictives (aléatoires mais réalistes)
import random                     # Fonctions aléatoires de base (choix, nombres, etc.)

# Initialisation de l'objet Faker
fake = Faker()

# Définition des listes de catégories, pays, modes de paiement et statuts de commande
categories = ['Électronique', 'Vêtements', 'Maison', 'Beauté', 'Sport']
countries = ['France', 'Allemagne', 'Espagne', 'Italie', 'Belgique']
payment_modes = ['Carte bancaire', 'PayPal', 'Virement', 'Espèces']
statuses = ['Livré', 'En cours', 'Annulé', 'Retourné']

# Initialisation de la liste qui contiendra toutes les lignes de données simulées
data = []

# Génération de 100 000 commandes fictives
for _ in range(100_000):
    date = fake.date_between(start_date='-1y', end_date='today')  # Date aléatoire dans les 12 derniers mois
    category = random.choice(categories)                          # Choix d'une catégorie
    country = random.choice(countries)                            # Choix d'un pays
    product = f"{category} - {fake.word()}"                       # Nom de produit combinant catégorie et mot fictif
    quantity = random.randint(1, 5)                               # Quantité aléatoire entre 1 et 5
    price = round(random.uniform(10, 300), 2)                     # Prix unitaire aléatoire entre 10€ et 300€
    status = random.choice(statuses)                              # Statut de commande
    payment = random.choice(payment_modes)                        # Mode de paiement

    # Ajout de la ligne dans la liste des données
    data.append([
        date, product, category, quantity, price, country, payment, status
    ])

# Création d'un DataFrame pandas à partir de la liste de données
df = pd.DataFrame(data, columns=[
    'Date commande', 'Nom produit', 'Catégorie', 'Quantité', 
    'Prix unitaire (€)', 'Pays', 'Mode de paiement', 'Statut commande'
])

# Export du DataFrame au format CSV
df.to_csv("sales_data.csv", index=False)

# Message de confirmation
print("Données de vente générées et enregistrées dans 'sales_data.csv'.")
