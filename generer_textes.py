import os
import random

os.makedirs("textes", exist_ok=True)

vocabulaire = ["chat", "voiture", "maison", "chien", "arbre"]

def generer_fichier(nom_fichier, nb_lignes):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for _ in range(nb_lignes):
            mot = random.choice(vocabulaire)
            f.write(mot + "\n")

generer_fichier("./textes/fichier1_1000.txt", 1000)
generer_fichier("./textes/fichier2_100k.txt", 100000)
generer_fichier("./textes/fichier3_5M.txt", 5000000)
generer_fichier("./textes/fichier4_50M.txt", 50000000)