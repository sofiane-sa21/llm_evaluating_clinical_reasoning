from utils import get_all_data
import scipy.stats as stats
import numpy as np
from tabulate import tabulate

# Calcul de coefficient de Spearman entre les auteurs

full_data = get_all_data()
notes_sofiane = full_data[full_data.Auteur == 'S']
notes_josselin = full_data[full_data.Auteur == 'J']

correlation_spearman, p_value = stats.spearmanr(
    np.array(notes_sofiane.Note), np.array(notes_josselin.Note))

print()
print("Calcul du coefficient de Spearman entre les auteurs :")
print(
    tabulate([[correlation_spearman, p_value]], headers=['Coefficient de Spearman', 'p-value'], tablefmt="grid"))
