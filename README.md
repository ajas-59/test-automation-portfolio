
# Portfolio – Automatisation de tests

[![Tests](https://github.com/ajas-59/test-automation-portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/ajas-59/test-automation-portfolio/actions/workflows/main.yml)

Études de cas réalisées dans le cadre de ma préparation au métier d'ingénieure en automatisation de tests. Chaque projet part d'une application de démonstration publique, définit une stratégie de test, l'automatise et documente les anomalies trouvées.

**Outils :** Python · pytest · Playwright · GitHub Actions

---

## Projets

### [Sauce Demo – tests end-to-end](./saucedemo-playwright-tests)

Tests fonctionnels de l'interface d'un site e-commerce de démonstration, sur le parcours d'achat critique.

- **15 cas de test** répartis en trois fonctionnalités : connexion (C1–C7), panier (P1–P4), paiement (K1–K4)
- Cas normaux et cas d'erreur (champs vides, identifiants invalides, panier vide…)
- **1 anomalie détectée et documentée** : une commande peut être passée avec un panier vide
- Architecture modulaire : un fichier de test par fonctionnalité, fonctions d'aide partagées, fixtures pytest

➡️ Détails, tableau des cas de test et rapport d'anomalie dans le [README du projet](./saucedemo-playwright-tests/README.md).

#### Versions du projet

Le dépôt conserve les itérations successives, pour montrer l'évolution de la démarche :

| Dossier | Contenu |
|---------|---------|
| [`brouillon/`](./brouillon) | Première itération de l'étude de cas |
| [`brouillon_2/`](./brouillon_2) | Deuxième itération |
| [`saucedemo-playwright-tests/`](./saucedemo-playwright-tests) | **Version finale, à jour et utilisable** |

Seule la version finale est maintenue et testée par l'intégration continue.

### Tests d'API ParaBank *(en cours)*

Tests d'une API REST bancaire de démonstration : connexion, consultation des comptes, virements, avec un accent sur les cas limites (montant négatif, solde insuffisant, compte inexistant).

---

## Intégration continue

Un workflow GitHub Actions ([`.github/workflows/main.yml`](./.github/workflows/main.yml)) lance automatiquement la suite de tests à chaque push et à chaque pull request sur `main`. Il installe Python, les dépendances et le navigateur sur une machine Ubuntu, puis exécute `pytest`.

## Lancer les tests en local

```bash
cd saucedemo-playwright-tests
pip install -r requirements.txt
playwright install chromium
pytest -v
```

## Prochaines étapes

- Migration du projet Sauce Demo vers le **Page Object Model**
- Paramétrage des cas de connexion (**approche data-driven**)
- Finalisation de l'étude de cas API ParaBank

---

*Amélie Smith – M2 Langue et Informatique, Sorbonne Université*
