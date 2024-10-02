import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import get_data, llm_types, couleurs

# Boxplot général comparant les différents modèles

first_llm: llm_types = 'Llama_FR'
second_llm: llm_types = 'Llama_EN'
third_llm: llm_types = 'GPT_FR'
fourth_llm: llm_types = 'GPT_EN'

data_first = get_data(first_llm)
data_second = get_data(second_llm)
data_third = get_data(third_llm)
data_fourth = get_data(fourth_llm)

# On récupère les notes
notes_first = np.array(data_first.Note)
notes_second = np.array(data_second.Note)
notes_third = np.array(data_third.Note)
notes_fourth = np.array(data_fourth.Note)

plt.figure(figsize=(20, 10))
custom_palette = [couleurs[first_llm], couleurs[second_llm],
                  couleurs[third_llm], couleurs[fourth_llm]]

# On trace les boxplots
sns.boxplot(data=[notes_first, notes_second, notes_third, notes_fourth],
            palette=custom_palette)
plt.xticks([0, 1, 2, 3], [first_llm, second_llm,
           third_llm, fourth_llm], fontsize=12)
plt.title(
    'Comparaison des notes entre les modèles sous forme de boxplot', fontsize=16)
plt.ylabel('Notes', fontsize=14)
plt.xlabel('Modèles', fontsize=14)
plt.ylim(-1.5, 11)
plt.yticks(range(-3, 11))
sns.set_theme(style="ticks")
plt.rcParams['font.family'] = 'Arial'

# On ajoute des lignes pour les moyennes de chaque distribution
mean_first = np.mean(notes_first)
mean_second = np.mean(notes_second)
mean_third = np.mean(notes_third)
mean_fourth = np.mean(notes_fourth)

plt.axhline(y=0, color="#000000", linestyle="-")
plt.axhline(mean_first, color=couleurs[first_llm], linestyle='--',
            label=f'Moyenne {first_llm}: {mean_first:.2f}')
plt.axhline(mean_second, color=couleurs[second_llm], linestyle='--',
            label=f'Moyenne {second_llm}: {mean_second:.2f}')
plt.axhline(mean_third, color=couleurs[third_llm], linestyle='--',
            label=f'Moyenne {third_llm}: {mean_third:.2f}')
plt.axhline(mean_fourth, color=couleurs[fourth_llm], linestyle='--',
            label=f'Moyenne {fourth_llm}: {mean_fourth:.2f}')

plt.legend(loc='lower left', ncol=1, fontsize=10, bbox_to_anchor=(0, 0))
plt.show()
