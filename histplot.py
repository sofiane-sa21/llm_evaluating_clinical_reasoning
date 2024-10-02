import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import get_data, llm_types, couleurs

# Dans ce script on trace les diagrammes en barres
# pour évaluer la répartition des notes avec courbe de densité

# ### VARIABLES A MODIFIER
model1: llm_types = 'Llama_FR'
model2: llm_types = 'Llama_EN'

# Quelques paramètres qu'on utilise à travers les graphiques
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 12

# Suppose que 'get_data' est défini et retourne un DataFrame avec une colonne 'Note'
llm1 = get_data(model1)
llm2 = get_data(model2)

notes_llm1 = np.array(llm1.Note)
notes_llm2 = np.array(llm2.Note)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

bins = range(-2, 12)
sns.histplot(notes_llm1, bins=[
             x - 0.5 for x in bins], ax=axs[0], color=couleurs[model1], shrink=1, stat='density')
kde = sns.kdeplot(notes_llm1, ax=axs[0], color='darkred')
kde_data = kde.get_lines()[0].get_data()
x_kde = kde_data[0]
y_kde = kde_data[1]
x_peak = x_kde[np.argmax(y_kde)]
axs[0].axvline(x=x_peak, color='red', linestyle='dotted', alpha=0.5)
axs[0].set_title(f'Distribution des notes pour {model1}')
axs[0].set_xlim(-2, 12)
axs[0].set_ylim(0, 0.40)
axs[0].set_xlabel('Note')
axs[0].set_xticks(bins)
axs[0].set_ylabel('Fréquence')

# Deuxième histogramme pour les notes en anglais
sns.histplot(notes_llm2, bins=[x - 0.5 for x in bins],
             ax=axs[1], color=couleurs[model2], shrink=1, stat='density')
kde = sns.kdeplot(notes_llm2, ax=axs[1], color='darkred')
kde_data = kde.get_lines()[0].get_data()
x_kde = kde_data[0]
y_kde = kde_data[1]
x_peak = x_kde[np.argmax(y_kde)]
axs[1].axvline(x=x_peak, color='red', linestyle='dotted', alpha=0.5)
axs[1].set_title(f'Distribution des notes pour {model2}')
axs[1].set_xlim(-2, 12)
axs[1].set_ylim(0, 0.40)
axs[1].set_xlabel('Note')
axs[1].set_xticks(bins)
axs[1].set_ylabel('Fréquence')

# Ajuster les espaces entre les sous-graphes
plt.tight_layout()
plt.show()
