import pandas as pd
from scipy import stats
import numpy as np
from utils import get_data, get_cc_ref, llm_types
from tabulate import tabulate

# Réalisation d'un test de Mann-Whitney d'une spécialité VS les autres
# non inclue dans l'étude finale mais intéressante

# ### VARIABLES MODIFIABLES
# Pour information, toutes les spécialités sont visibles dans le fichier utils.py
specialite_choisie = 'Médecine générale'
model: llm_types = 'Llama_EN'
alpha = 0.05

data = get_data(model)
cc_ref = get_cc_ref()
data = pd.merge(data, cc_ref, on="ID")

specialite_etudiee = data[data.Classification == specialite_choisie]
autres_specialites = data[data.Classification != specialite_choisie]

# On extrait les notes pour la spécialité actuelle et les autres spécialités
notes_specialite_etudiee = np.array(specialite_etudiee.Note)
notes_autres_specialites = np.array(autres_specialites.Note)

# Test de Mann-Whitney U
stat, p_value = stats.mannwhitneyu(
    notes_specialite_etudiee, notes_autres_specialites, alternative='two-sided')
# Interprétation des résultats
if p_value < alpha:
    interpretation = f"Différence significative entre {specialite_choisie} et toutes les autres spécialités."
else:
    interpretation = f"Pas de différence significative entre {specialite_choisie} et toutes les autres spécialités."

print()
print(f'Comparaison de la spécialité {specialite_choisie} versus le reste :')
print(tabulate([[stat, p_value, interpretation]],
      headers=["Statistique", "Valeur", "Interprétation"], tablefmt="grid"))
