# Changelog

[English changelog](CHANGELOG.md) **·** [Français changelog](doc/changelog/CHANGELOG.fr.md)

<!-- markdownlint-disable-file MD024 -->

Toutes les modifications notables apportées à ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au principe de la [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Non publié]

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
