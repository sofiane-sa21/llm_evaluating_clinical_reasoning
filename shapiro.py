from scipy.stats import shapiro
import numpy as np
from utils import get_data, llm_types
from tabulate import tabulate

# Fichier utilisé pour la réalisation des tests de Shapiro
# avant la réalisation des Wilcoxon

# ### VARIABLES A MODIFIER
model1: llm_types = 'GPT_FR'
model2: llm_types = 'Llama_FR'

llm1 = get_data(model1)
llm2 = get_data(model2)

notes_llm1 = np.array(llm1.Note)
notes_llm2 = np.array(llm2.Note)

D = notes_llm1 - notes_llm2

print()
print(f'Shapiro pour comparaison entre {model1} et {model2}')
# Test de Shapiro-Wilk
stat_shapiro, p_value_shapiro = shapiro(D)
alpha = 0.05
# Interpréter les résultats
if p_value_shapiro > alpha:
    interpretation = "Les données suivent une distribution normale (on ne rejette pas H0)."
else:
    interpretation = "Les données ne suivent pas une distribution normale (on rejette H0)."
print(tabulate([[stat_shapiro, p_value_shapiro, interpretation]], headers=[
      'Statistique', 'p-value', 'Interprétation du test de Shapiro'], tablefmt="grid"))
