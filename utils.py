import pandas as pd
from typing import Literal, Dict, List

# Chemin vers le fichier d'analyse
file_path = "data/analyse.xlsx"

# Chaines faisant référénce à chaque modèle + sa langue
llm_types = Literal["GPT_EN", "GPT_FR", "Llama_EN",
                    "Llama_FR", "Biomistral_EN", "Biomistral_FR"]

# Cette variable me permet d'exclure les dossiers problématiques
# Elle me permet d'éliminer des variables les réponses nulles
# pour le modèle Biomistral
exclude: Dict[llm_types, List[str]] = {
    'GPT_FR': [],
    'GPT_EN': [],
    'Llama_FR': [],
    'Llama_EN': [],
    'Biomistral_FR': ['S03', 'S21', 'S44', 'S82', 'S89',
                      'J05', 'J10', 'J12', 'J19', 'J20', 'J22', 'J24', 'J27',
                      'J29', 'J36', 'J37', 'J38', 'J39', 'J40', 'J47', 'J49',
                      'J52', 'J56', 'J60', 'J63', 'J65', 'J66', 'J75', 'J76',
                      'J81', 'J89'],
    'Biomistral_EN': ['S06', 'S11', 'S13', 'S22', 'S38', 'S41', 'S45',
                      'S55', 'S57', 'S58', 'S60', 'S69', 'S82', 'S83',
                      'S87', 'S90',
                      'J25', 'J27', 'J28', 'J30', 'J37', 'J47', 'J49', 'J55',
                      'J60', 'J62', 'J63', 'J65', 'J68', 'J75', 'J76', 'J77',
                      'J81', 'J82', 'J86', 'J87', 'J88', 'J89']
}

# Codes couleurs pour chaque LLM :
couleurs: Dict[llm_types, str] = {
    'GPT_FR': '#86A44A',
    'GPT_EN': '#B5CA92',
    'Llama_FR': '#416FA6',
    'Llama_EN': '#8EA5CB',
    'Biomistral_FR': '#DA8137',
    'Biomistral_EN': '#F6B18A'
}

# Liste des spécialités
specialites: Dict[str, str] = {
    'urg': 'Urgence-Réanimation',
    'endoc': 'Endocrinologie-diabétologie-nutrition',
    'gyneco': 'Gynécologie',
    'onco': 'Onco-Hématologie',
    'hepato': 'Hépato-gastro-entérologie',
    'infect': 'Maladies infectieuses et tropicales',
    'cardio': 'Médecine cardio-vasculaire',
    'gen': 'Médecine générale',
    'interne': 'Médecine interne',
    'neuro': 'Neurologie',
    'tete_cou': 'Tête et cou',
    'pediatrie': 'Pédiatrie',
    'pneumo': 'Pneumologie',
    'psy': 'Psychiatrie',
    'rhumato': 'Rhumatologie',
    'uro_nephro': 'Urologie-Néphrologie'
}

# Liste des couleurs pour chaque spécialité
couleurs_specialites: Dict[str, str] = {
    'Urgence-Réanimation': '#4B4B4B',
    'Endocrinologie-diabétologie-nutrition': '#8C6E4F',
    'Gynécologie': '#77628C',
    'Onco-Hématologie': '#8C4B31',
    'Hépato-gastro-entérologie': '#9B9B9B',
    'Maladies infectieuses et tropicales': '#4C6B54',
    'Médecine cardio-vasculaire': '#515A63',
    'Médecine générale': '#79699E',
    'Médecine interne': '#586B7E',
    'Neurologie': '#7CA48A',
    'Tête et cou': '#B07A5C',
    'Pédiatrie': '#D2A04E',
    'Pneumologie': '#5A8B83',
    'Psychiatrie': '#6C8FAE',
    'Rhumatologie': '#AE7B74',
    'Urologie-Néphrologie': '#93779D'
}

# Cette fn lit toutes les données dans un Pd.DataFrame en fonction
# du LLM demandé dans sheet_name
# ex : get_data('Biomistral_EN') récupère toutes les notes de Biomistral en anglais


def get_data(sheet_name: llm_types):
    data = pd.read_excel(file_path, sheet_name)
    return data[~data.ID.isin(exclude[sheet_name])]


# Cette fonction récupère les données mais élimine les notes
# communes à exclure entre deux modèles avant
# Initialement faire pour comparer Biomistral à GPT, obsolète du coup car exclu des analyses
def get_compared_data(model_one: llm_types, model_two: llm_types):
    data_one = pd.read_excel(file_path, model_one)
    data_two = pd.read_excel(file_path, model_two)
    data_one = data_one[~data_one.ID.isin(
        exclude[model_one] + exclude[model_two])]
    data_two = data_two[~data_two.ID.isin(
        exclude[model_one] + exclude[model_two])]

    return data_one, data_two


# Fonction qui récupère les données de tous les modèles et les concat
# dans une variable. Utilisé principalement pour le Spearman je crois
def get_all_data():
    notes_gpt_en = get_data('GPT_EN')
    notes_gpt_fr = get_data('GPT_FR')
    notes_llama_en = get_data('Llama_EN')
    notes_llama_fr = get_data('Llama_FR')
    notes_biomistral_en = get_data('Biomistral_EN')
    notes_biomistral_fr = get_data('Biomistral_FR')
    return pd.concat([notes_gpt_en, notes_gpt_fr, notes_llama_fr,
                      notes_llama_en, notes_biomistral_en, notes_biomistral_fr])


# Permet de récupérer les cas cliniques, utilisé surtout pour les indices de lisibilité
def get_cc_ref():
    return pd.read_excel(file_path, sheet_name="CC_REF")


def get_global_data():
    return pd.read_excel(file_path, sheet_name="GLOBAL")
