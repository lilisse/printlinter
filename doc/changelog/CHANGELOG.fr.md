# Changelog

[English changelog](CHANGELOG.md) **·** [Français changelog](doc/changelog/CHANGELOG.fr.md)

<!-- markdownlint-disable-file MD024 -->

Toutes les modifications notables apportées à ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au principe de la [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Non publié]

### Ajouté

- Maintenant on peut ignorer un bloque de code sans réactiver le linteur.
- Ajout d'une méthode pour ignorer un bloque de code avec: `<py-printlinter disable PPLXXX>`
  pour désactiver le linter et `<py-printlinter enable PPLXXX>` pour le réactiver. On peut
  aussi désactiver toutes les rêgles avec `All`.
- Ajout d'une option de configuration pour actver ou désactiver la couleur sur la sortie:
`color`. [Issue](https://github.com/lilisse/printlinter/issues/6).
- Ajout d'une méthode pour ignorer la ligne suivante avec:
`<py-printlinter disable-next PPLXXX>`. [Issue](https://github.com/lilisse/printlinter/issues/1).
- Ajout d'une valeur par défaut pour la configuration `ignored_rep`. Tout ces dossier ne
  seront pas visités par le linter
  - `node_modules`
  - `.vscode/`
  - `__pycache__/`
  - `build/`
  - `develop-eggs/`
  - `dist/`
  - `downloads/`
  - `eggs/`
  - `.eggs/`
  - `lib/`
  - `lib64/`
  - `parts/`
  - `sdist/`
  - `var/`
  - `wheels/`
  - `pip-wheel-metadata/`
  - `share/python-wheels/`
  - `htmlcov/`
  - `.tox/`
  - `.nox/`
  - `.hypothesis/`
  - `.pytest_cache/`
  - `docs/_build/`
  - `__pypackages__/`
  - `.mypy_cache/`
  - `.ruff_cache`
  - `.pyre/`
  - `env/`
  - `venv/`
  - `ENV/`
  - `env.bak/`
  - `venv.bak/`
  - `.venv/`
  - `.env/`
- Ajout d'une barre de progression au cli.

## [0.1.0] - 21-03-2024

### Ajouté

- Ajout de la gestion des fichiers de configuration avec 3 options:
  - `target_version`
  - `ignored_files`
  - `disabled_rules`
- Ajout de la prise en charge des commentaires pour ignorer une ligne ou un fichier entier.
- Ajout de vérificateurs et de formateurs.
- Ajout des tests
- Ajout du verbe `lint` au lanceur pour vérifier un dossier et detecter les fonctions
  d'affichage sur du code python. Voir le [README.md](doc/readme/README.fr.md) pour
  comprendre comment fonctionne le vérificateur.
