import random
import os

os.makedirs("textes", exist_ok=True)

vocabulaire = ["chat", "voiture", "maison", "chien", "arbre"]

# 1. Génération du fichier 1 (100 lignes, 1 mot par ligne)
print("Génération de fichier1_100.txt...")
lignes_100 = [random.choice(vocabulaire) + "\n" for _ in range(100)]

with open("./textes/fichier1_100.txt", "w", encoding="utf-8") as f:
    f.writelines(lignes_100)

def dupliquer_fichier(chemin_sortie, nb_blocs):
    print(f"Génération de {chemin_sortie}...")
    with open(chemin_sortie, "w", encoding="utf-8") as f:
        for _ in range(nb_blocs):
            f.writelines(lignes_100)

# 2. 100k lignes (1 000 blocs de 100)
dupliquer_fichier("./textes/fichier2_100k.txt", 1000)

# 3. 5M lignes (50 000 blocs de 100)
dupliquer_fichier("./textes/fichier3_5M.txt", 50000)

# 4. 50M lignes (500 000 blocs de 100)
dupliquer_fichier("./textes/fichier4_50M.txt", 500000)

print("Tous les fichiers ont été générés avec succès !")