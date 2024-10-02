from utils import get_all_data
from scipy.stats import pearsonr
import numpy as np
import pandas as pd
from tabulate import tabulate

# Dans ce fichier on calcule le coefficient de Pearson global

# Pearson global
full_data = get_all_data()
notes_sofiane = full_data[full_data.Auteur == 'S']
notes_josselin = full_data[full_data.Auteur == 'J']

# Calcul du coefficient de Pearson et de la p-valeur
correlation_pearson, p_value = pearsonr(
    np.array(notes_sofiane.Note), np.array(notes_josselin.Note))

print()
print("Coefficient de Pearson entre les auteurs :")
print(
    tabulate([[correlation_pearson, p_value]], headers=['Coefficient de Pearson', 'p-value'], tablefmt="grid"))
