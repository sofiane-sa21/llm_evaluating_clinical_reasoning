from scipy import stats
import numpy as np
from utils import get_data, llm_types
from tabulate import tabulate

# Fichier utilisé pour faire les Wilcoxon
# ### VARIABLES A MODIFIER
model1: llm_types = 'Llama_FR'
model2: llm_types = 'GPT_FR'

data_first = get_data(model1)
data_second = get_data(model2)

notes_first = np.array(data_first.Note)
notes_second = np.array(data_second.Note)

# Test de Wilcoxon
differences = notes_first - notes_second
stat, p_value_w = stats.wilcoxon(differences)

print()
print(f'Comparaison entre {model1} et {model2}')
# On fait 4 tests de Wilcoxon donc on diminue le risque alpha
alpha = 0.0125
# Interpréter les résultats
if p_value_w < alpha:
    interpretation = "Il y a une différence significative entre les notes."
else:
    interpretation = "Il n'y a pas de différence significative entre les notes."
print(tabulate([[stat, p_value_w, interpretation]], headers=[
      'Statistique', 'p-value', 'Interprétation du test de Wilcoxon'], tablefmt="grid"))
