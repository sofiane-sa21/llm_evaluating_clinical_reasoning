import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import get_data, specialites, couleurs_specialites, llm_types

# Création des barplots pour les spécialités par modèle
# ### VARIABLES A MODIFIER
model: llm_types = 'Llama_FR'

llm = get_data(model)
# On récupère les spécialités pour chaque cas
cc_ref = pd.read_excel('data/analyse.xlsx', sheet_name="CC_REF")
data = pd.merge(llm, cc_ref, on='ID')

noms_specialites = []
moyennes = []

# On calcule les moyennes pour chaque spécialité
for code, nom_specialite in specialites.items():
    data_specialite = data[data.Classification == nom_specialite]
    # Si on a bien une note pour la spécialité
    if not data_specialite.empty:
        moyenne_notes = np.mean(data_specialite.Note)
        # On range dans l'ordre, nom de la spécialité et moyenne associée
        noms_specialites.append(nom_specialite)
        moyennes.append(moyenne_notes)

plt.rcParams['font.family'] = 'Arial'
# On crée le graphique en barres
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x=moyennes, y=noms_specialites, palette=[
                       couleurs_specialites[nom] for nom in noms_specialites])

# On ajoute les annotations pour afficher les valeurs moyennes sur chaque barre
for i in range(len(moyennes)):
    bar_plot.text(
        moyennes[i] + 0.05, i, f'{moyennes[i]:.2f}', color='black', va='center', fontsize=10)

# On ajoute les titres
plt.title(f'Moyennes des notes par spécialité pour {model}', fontsize=16)
plt.xlabel('Moyenne des notes', fontsize=12)
plt.xlim(0, 10)
plt.ylabel('Spécialités', fontsize=12)

# Ajuster la mise en page pour éviter les chevauchements
plt.tight_layout()

# Afficher le graphique
plt.show()
