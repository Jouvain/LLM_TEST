# Plan : coder un mini-GPT pas à pas

Ce plan mène à un GPT minuscule (environ 1 à 10 millions de paramètres), niveau caractère, entraîné sur un petit texte, en environ 8 heures réparties sur 6 séances.

## Objectif et prérequis

- **Résultat** : un modèle qui génère du texte « à la manière » du corpus, codé par toi, ligne par ligne.
- **Langage** : Python + PyTorch. Aucun GPU requis : un laptop suffit (quelques minutes d'entraînement).
- **Installation** : Python 3.10+, `pip install torch`, un éditeur ou un notebook Jupyter.
- **Corpus** : un fichier texte de 1 Mo environ (Shakespeare ou un texte en français libre de droits).
- **Référence** : la vidéo « Let's build GPT » d'Andrej Karpathy, à regarder en complément, pas obligatoire.

## Vue d'ensemble

Le cœur du projet (étapes 0 à 6) demande environ 8 h ; l'étape 7 est optionnelle.

| # | Étape | Concept à comprendre | Durée | Séance |
| --- | --- | --- | --- | --- |
| 0 | Mise en place | Environnement, tenseurs PyTorch | 30 min | 1 |
| 1 | Données et tokenisation | Texte → entiers, découpage train/val | 45 min | 1 |
| 2 | Modèle de base (bigramme) | Logits, perte cross-entropy | 1 h | 2 |
| 3 | Self-attention | Query, Key, Value, masque causal | 1 h 30 | 3 |
| 4 | Bloc Transformer | Multi-têtes, résiduelles, LayerNorm, MLP | 1 h 30 | 4 |
| 5 | Entraînement | AdamW, batchs, évaluation | 1 h | 5 |
| 6 | Génération et expériences | Température, taille du contexte, sur-apprentissage | 1 h | 6 |
| 7 | Optionnel : aller plus loin | Tokenisation BPE, dropout, comparaison avec nanoGPT | 2 à 3 h | 7+ |

Ces durées supposent que tu prends le temps de comprendre chaque ligne ; compte 30 % de plus si tu veux expérimenter à chaque étape.

## Détail des étapes

Chaque étape suit le même schéma : un concept en quelques phrases, le code écrit ensemble, puis un critère de réussite pour savoir qu'on peut passer à la suite.

### Étape 0 · Mise en place

On installe PyTorch et on manipule des tenseurs (création, forme, indexation). **Réussite** : `torch.__version__` s'affiche et tu sais lire la forme `(B, T, C)` d'un tenseur.

### Étape 1 · Données et tokenisation

Un modèle ne lit que des nombres : on associe un entier à chaque caractère distinct, puis on réserve 90 % du texte à l'entraînement et 10 % à la validation. **Réussite** : `decode(encode(texte)) == texte`.

### Étape 2 · Modèle bigramme

Le plus petit modèle possible : chaque caractère prédit directement le suivant via une table d'embeddings. On y découvre les logits et la perte cross-entropy. **Réussite** : la perte initiale est proche de ln(taille du vocabulaire) et le modèle génère du bruit.

### Étape 3 · Self-attention

Le cœur du Transformer : chaque position pondère les positions précédentes grâce aux vecteurs Query, Key et Value, avec un masque pour interdire de regarder le futur. On part d'une simple moyenne, puis on la rend apprenable. **Réussite** : tu expliques à voix haute pourquoi on divise par √d et pourquoi le masque est triangulaire.

### Étape 4 · Bloc Transformer complet

On assemble plusieurs têtes d'attention, un petit réseau MLP, des connexions résiduelles et LayerNorm, puis on empile quelques blocs. **Réussite** : le modèle passe sous le seuil de perte du bigramme.

### Étape 5 · Entraînement

Boucle classique : tirer un batch, calculer la perte, rétropropager, mettre à jour avec AdamW. On mesure aussi la perte de validation à intervalles réguliers. **Réussite** : perte d'entraînement et de validation qui baissent ensemble.

### Étape 6 · Génération et expériences

On génère du texte caractère par caractère par échantillonnage, puis on fait varier la température, la taille du contexte et le nombre de blocs pour observer l'effet. **Réussite** : le texte généré ressemble à du texte du corpus (mots plausibles, ponctuation correcte).

### Étape 7 · Optionnel

Passer à une tokenisation BPE, ajouter du dropout, puis comparer ton code avec nanoGPT pour voir ce qui change à l'échelle réelle.

## Suivi de progression

Coche une étape une fois son critère de réussite atteint.

- [x] Étape 0 · Mise en place
- [ ] Étape 1 · Données et tokenisation
- [ ] Étape 2 · Modèle bigramme
- [ ] Étape 3 · Self-attention
- [ ] Étape 4 · Bloc Transformer complet
- [ ] Étape 5 · Entraînement
- [ ] Étape 6 · Génération et expériences
- [ ] Étape 7 · Optionnel

**Pour reprendre une séance** : ouvre une nouvelle conversation, joins ce document ou son lien, et indique la dernière étape cochée plus le code que tu as déjà. On repart de là.