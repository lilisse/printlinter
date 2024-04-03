<!-- markdownlint-disable-file MD041 -->

<!-- TODO: Add badge
TODO: logo -->

[English readme](README.md) **·** [Français readme](doc/readme/README.fr.md)

PrintLinter est un linter python pour detecter et signaler les fonctions d'affichage dans
du code python.

## Sommaire

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Codes d'erreur](#codes-derreur)
- [Ignorer des erreurs](#ignorer-des-erreurs)
- [Configuration](#configuration)
- [Pour la suite](#pour-la-suite)

# Installation

Installer avec `pip` ou votre gestionnaire de paquets PyPI préféré.

```sh
pip install printlinter
```

Lancer la commande suivante pour tester l'installation de PrintLinter.

```sh
printlinter --version
```

# Utilisation

## Verbes

Pour avoir de l'aide sur l'usage d'un verbe.

```sh
printlinter <verb> --help
```

### Lint

Pour linter un fichier ou un dossier.

```sh
printlinter lint <file|folder>
```

Le résultat produit resemble à ça.

`file_path:line:column error_code display_function_detected error_name`

Par défaut nous avons désactiver le linter sur certains dossiers.

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

#### Exemple

<!-- markdownlint-disable MD013 -->
```sh
tests/testing_files/mixed/mixed0.py:5:0: PPL001 `print("toto")` print-detected
tests/testing_files/mixed/mixed0.py:6:0: PPL002 `pprint("titi")` prettyprint-detected
tests/testing_files/mixed/mixed1/mixed2.py:5:0: PPL001 `print("toto")` print-detected
tests/testing_files/mixed/mixed1/mixed2.py:6:0: PPL002 `pprint("titi")` prettyprint-detected
tests/testing_files/pprint/pprint1.py:6:0: PPL002 `pprint("Hello, world")` prettyprint-detected
tests/testing_files/pprint/pprint2/pprint3.py:11:4: PPL002 `pprint("tata")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl005.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_nothing.py:6:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_nothing.py:8:0: PPL002 `pprint("toto")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl006.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl002.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl001.py:9:0: PPL002 `pprint("toto")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl004.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl003.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/disable_in_wrong_place.py:8:0: PPL001 `print("toto")` print-detected
tests/testing_files/sys/stderr/write/stderr1.py:7:0: PPL004 `sys.stderr.write("Hello, world")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr1.py:8:0: PPL004 `stderr.write("Hello, world")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr2/stderr3.py:13:4: PPL004 `sys.stderr.write("tata")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr2/stderr3.py:14:4: PPL004 `stderr.write("tata")` sys.stderr.write-detected
tests/testing_files/sys/stderr/writelines/stderr1.py:7:0: PPL006 `sys.stderr.writelines(["Hello", "world"])` sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr1.py:8:0: PPL006 `stderr.writelines(["Hello", "world"])` sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr2/stderr3.py:13:4: PPL006 `sys.stderr.writelines(["tata", "tutu"])`
sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr2/stderr3.py:14:4: PPL006 `stderr.writelines(["tata", "tutu"])`
sys.stderr.writelines-detected
tests/testing_files/sys/stdout/write/stdout1.py:7:0: PPL003 `sys.stdout.write("Hello, world")` sys.stdout.write-detected
tests/testing_files/sys/stdout/write/stdout2/stdout3.py:13:4: PPL003 `sys.stdout.write("tata")` sys.stdout.write-detected
tests/testing_files/sys/stdout/writelines/stdout1.py:7:0: PPL005 `sys.stdout.writelines(["Hello", "world"])` sys.stdout.writelines-detected
tests/testing_files/sys/stdout/writelines/stdout2/stdout3.py:14:4: PPL005 `stdout.writelines(["tata", "tutu"])`
sys.stdout.writelines-detected
tests/testing_files/print/toto_1.py:3:0: PPL001 `print("Hello, world")` print-detected
tests/testing_files/print/toto2/toto3.py:7:4: PPL001 `print("tata")` print-detected
Found 27 errors
```
<!-- markdownlint-enable MD013 -->

# Codes d'erreur

Toutes les erreurs ont un code individuel basé sur `PPLXXX`.
Chaque librairie a son propre "domaine" d'erreurs.

| Librairie | Domaine d'erreur |
|:----------|:-----------------|
| Standard  | PPL0XX           |

## Librairie standard

| Fonction                | Code d'erreur |
|:------------------------|:--------------|
| `print`                 | PPL001        |
| `pprint`                | PPL002        |
| `sys.stdout.write`      | PPL003        |
| `sys.stderr.write`      | PPL004        |
| `sys.stdout.writelines` | PPL005        |
| `sys.stderr.writelines` | PPL006        |

# Ignorer des erreurs

Vous pouvez ignorer les erreurs avec le linter.

## Ignorer une erreur sur une ligne

Pour ignorer une rêgle sur une ligne, ajoutez un commentaire à la fin de la ligne.
`# noqa: <error_code>`.

<!-- markdownlint-disable-next-line MD024 -->
### Exemple

```python
toto = 1
titi = 2
print (toto + titi) # noqa: PPL001
```

## Ignorer sur un fichier entier

Pour ignorer une rêgle, les rêgles d'une librairie ou toutes les rêgles, ajoutez un
commentaire au début du fichier. `# <py-printlinter disable-file <error_code>`.

<!-- markdownlint-disable-next-line MD036 -->
**Le commentaire DOIT être avant tout code dans le fichier.**

### Exemples

#### Une seul erreur

```python
# <py-printlinter disable-file PPL002>
from pprint import pprint
toto = 1
titi = 2
pprint(titi + toto)  # ignored error
...
```

#### Toutes les erreurs d'une librairie

```python
# <py-printlinter disable-file PPL000>
import sys
toto = 1
titi = 2
print(titi + toto)  # ignored error
sys.stdout.write(titi + toto)  # ignored error
...
```

#### Toutes les erreurs

```python
# <py-printlinter disable-file ALL>
from sys import stdout, stderr
from pprint import pprint
toto = 1
titi = 2
print(titi + toto)  # ignored error
pprint(titi + toto)  # ignored error
stdout.write(titi + toto)  # ignored error
stderr.write(titi + toto)  # ignored error
stdout.writelines(titi + toto)  # ignored error
stderr.writelines(titi + toto)  # ignored error
...
```

# Configuration

Vous pouvez configurer le linter avec un fichier de configuration (la configuration en
ligne de commande arrive dans une version future).

PrintLinter support 3 différent type de fichier.

- `.yaml/.yml`
- `.json`
- `.toml`

Par défaut le linter utilise un de ces fichier et chargés dans cet ordre.

- `printlinter.yaml`
- `printlinter.yml`
- `printlinter.json`
- `printlinter.toml`
- `pyproject.toml`

Vous pouvez également utiliser un autre fichier et exécuter le  linter à partir de la
ligne de commande.

```sh
printlinter lint <file|folder> --config-file </path/of/config/file>
```

## Target version

Le fichier de configuration permet de spécifer la version de python utilisé par le parser.
Utilisez un string qui formater comme `3.10` ou `3.7` pour spécifier la version,

<!-- markdownlint-disable-next-line MD036 -->
**La version ciblé de python DOIT être entre 3.7 et 3.10**

Vous pouvez voir des exemples de configuration [ici](#exemples-de-fichier-configuration).

## Ignored files

Le fichier de configuration permet d'ignorer des fichiers, contrairement au commentaire
qui permet aux erreurs d'être ignorées dans un fichier entier cette option de
configuration empêche le linter de lire le fichier.

Vous pouvez voir des exemples de configuration [ici](#exemples-de-fichier-configuration).

## Disabled rules

Le fichier de configuration permet de désactiver des rêgles dans tout les fichiers et dossiers.

Vous pouvez voir des exemples de configuration [ici](#exemples-de-fichier-configuration).

## Exemples de fichier configuration

### Fichier de configuration Yaml/Yml

```yaml
printlinter:
  target_version: "3.10"
  ignored_files: [toto.py]
  disabled_rules: [PPL001]
```

### Fichier de configuration Json

```json
{
  "printlinter": {
    "target_version": "3.10",
    "ignored_files": ["toto.py"],
    "disabled_rules": ["PPL001"]
  }
}

```

### Fichier de configuration Toml

```toml
[printlinter]
target_version = "3.10"
ignored_files = ["toto.py"]
disabled_rules = ["PPL001"]
```

### Fichier de configuration Pyproject

```toml
[tool.printlinter]
target_version = "3.10"
ignored_files = ["toto.py"]
disabled_rules = ["PPL001"]
```

# Pour la suite

Pour voir les prochaines fonctionnalités qui seront développées regarder [TODO](TOTO.md).
Voici une petite, liste non exhaustive de ce qui est prévu dans les versions futures.

- Ignorer un bloque de code.
- Ignorer la ligne suivante
- Linter les fonctions d'affichage de d'autres librairies
- Ajouter d'autre option de configuration.
- Ajouter d'autres traductions.
