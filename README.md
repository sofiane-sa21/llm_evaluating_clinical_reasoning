# Evaluation du raisonnement diagnostique médical de grands modèles de langue

This project contains Python scripts allowing you to perform statistical tests to compare the performance in diagnostic reasoning of different language models in clinical cases, in English and French, as part of a medical thesis.

Ce projet contient les scripts Python permettant d'effectuer des tests statistiques pour comparer les performances dans le raisonnement diagnostique de différents modèles de langage dans des cas cliniques, en anglais et français, dans le cadre d'une thèse de médecine.

Thèse réalisée par les doctorants Corvellec Josselin et Sid-Ahmed Sofiane.\
Dirigée par le Professeur Gourraud Pierre-Antoine.\ 
Co-dirigée par le Docteur Bazoge Adrien.\ 
Présidée par le Professeur Fournier Jean-Pascal.\ 
Membre du jury : le Docteur Hinzelin Grégoire.

## Structure du projet

- `data/`: Contient les tableurs avec les descriptions des cas cliniques, les notes des auteurs de la thèse.
- `boxplot.py`: Graphique de comparaison des modèles en diagrammes à moustaches.
- `descriptives.py`: Variables descriptives par modèle et par langue (moyenne, médiane, écart type)
- `histplot.py` : Graphique de distribution des notes par modèle.
- `kruskal_heatmaps.py` : Réalisation du test de Kruskal-Wallis par modèle et test de Dunn si significatif avec heatmap.
- `mannwhitney_spec.py` : Réalisation d'un test de Mannwhitney pour une spécialité versus le reste des spécialités.
- `mean_per_spec.py`: Observation des moyennes par spécialité par modèle et réalisation d'un graphique en barres.
- `pearson.py`: Réalisation d'un test de Pearson entre les notes des auteurs.
- `shapiro.py`: Tests diagnostiques évaluant la distribution normale de séries.
- `spearman.py`: Réalisation d'un test de Spearman entre les notes des auteurs.
- `utils.py`: Variables et fonctions utiles à l'ensemble des scripts.
- `requirements.txt`: Liste des dépendances Python nécessaires à l'exécution des scripts.
- `README.md`: Ce fichier expliquant le projet.

## Prérequis

Avant d'exécuter les scripts Python, assurez-vous d'avoir Python 3 installé sur votre machine. Il est également recommandé d'utiliser un **environnement virtuel** pour installer les dépendances du projet.

## Installation

### 1. Cloner le dépôt GitHub

Clonez ce dépôt sur votre machine locale.

### 2. Créer et activer votre environnement virtuel

Sous Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Sous MacOS/Linux :

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installation des dépendances

Installez les dépendances nécessaires avec le code suivant :

```bash
pip install -r requirements.txt
```

## Utilisation

Vous pouvez tester vous-même les scripts en vous rendant dans le dépôt via le terminal et en exécutant le script suivant :

```bash
python boxplot.py
```

Les scripts génèrent les résultats des tests statistiques qui sont visibles dans le terminal.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l’utiliser, de le modifier et de le distribuer.
