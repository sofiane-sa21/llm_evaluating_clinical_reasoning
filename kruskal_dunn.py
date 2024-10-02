import scikit_posthocs as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from utils import get_data, get_cc_ref, llm_types, specialites
from tabulate import tabulate

# ### VARIABLES A MODIFIER
model: llm_types = 'Llama_FR'
alpha = 0.05

data = get_data(model)

# On récupère les références pour chaque dossier pour avoir la spécialité avec la note
# et pas uniquement la note dans le pd frame
cc_ref = get_cc_ref()
data = pd.merge(data, cc_ref, on="ID")

# Là on va devoir pour chaque spécialité les séparer dans des tableaux différents
# au sein du tableau groupes_notes
groupes_notes = []
for key, specialite in specialites.items():
    # On récupère les notes associées à la spécialité en question
    specialite_actuelle = data[data.Classification == specialite]

    # On vérifie s'il y a des données
    if len(specialite_actuelle) > 0:
        # On ajoute de la spécialité dans le tableau
        groupes_notes.append(specialite_actuelle.Note)
    else:
        print(f"Pas assez de données pour la spécialité : {specialite}")

# Maintenant on a les notes par spécialité
# On fait un Kruskal Wallis pour voir si différences
# dans les sous groupes
stat, p_value = stats.kruskal(*groupes_notes)

print()
print(f"Kruskal-Wallis pour les sous-groupes de spécialités pour {model} :")
# Interpréter les résultats
if p_value < alpha:
    interpretation = "Il y a une différence significative entre les spécialités."
else:
    interpretation = "Il n'y a pas de différence significative entre les spécialités."
print(tabulate([[stat, p_value, interpretation]], headers=[
      'Statistique', 'p-value', 'Interprétation du test de Kruskal Wallis'], tablefmt="grid"))

# Pas de différence significative entre les groupes, on interrompt l'analyse!
if p_value > alpha:
    exit()

# Il y a une différence significative entre les groupes, on va donc réaliser
# un test de Dunn avec une heatmap des p-values
posthoc_results = sp.posthoc_dunn(
    data, val_col='Note', group_col='Classification', p_adjust='bonferroni')

p_values = posthoc_results

# On crée la heatmap avec Seaborn
plt.figure(figsize=(12, 10))
ax = sns.heatmap(p_values, annot=True, cmap="Reds_r",
                 vmin=0, vmax=1, cbar_kws={'label': 'p-value'}, linewidths=0.5, linecolor='darkgrey')

# Titres
plt.title('Heatmap des p-values ajustées pour la comparaison des spécialités pour Llama en Français',
          fontsize=14, fontname='Arial')
plt.xlabel('Spécialités', fontsize=12, fontname='Arial')
plt.ylabel('Spécialités', fontsize=12, fontname='Arial')

# On ajuste les labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                   ha="right", fontsize=11, fontname='Arial')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0,
                   fontsize=11, fontname='Arial')

# Là on retouche les valeurs dans les cases pour les rendre plus visibles
# et en gras si le résultat est significatif (< 0.05)
for text in ax.texts:
    text.set_fontfamily('Arial')
    text.set_fontsize(12)
    v = text.get_text()
    text.set_text(round(float(v), 2))
    if float(text.get_text()) < 0.05:
        text.set_fontweight(900)

# Ajuster la mise en page pour éviter le chevauchement
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

plt.tight_layout()

# On affiche la heatmap
plt.show()
