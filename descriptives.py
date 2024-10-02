from tabulate import tabulate
import numpy as np
from utils import get_data, llm_types

# Affiche les variables descriptifs des modèles :
# Moyenne, écart type, médiane, max, min, 25th, 75th

# ### VARIABLES A MODIFIER
model: llm_types = 'GPT_EN'

data = get_data(model)
notes = np.array(data.Note)

tableau = [
    ["Moyenne", f"{np.mean(notes):.2f}"],
    ["Écart type", f"{np.std(notes):.2f}"],
    ["Médiane", f"{np.median(notes)}"],
    ["Minimum", f"{np.min(notes)}"],
    ["Maximum", f"{np.max(notes)}"],
    ["25e percentile", f"{np.percentile(notes, 25)}"],
    ["75e percentile", f"{np.percentile(notes, 75)}"]
]

print()
print(f"Statistiques de {model} :")
print(tabulate(tableau, headers=["Statistique", "Valeur"], tablefmt="grid"))
