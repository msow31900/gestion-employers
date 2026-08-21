"""Fonctions de lecture et d'écriture JSON."""

import json
from pathlib import Path
from typing import Any


def charger_json(chemin: str, valeur_defaut: Any) -> Any:
    """Charge un fichier JSON."""
    fichier = Path(chemin)

    try:
        if not fichier.exists():
            return valeur_defaut

        with fichier.open("r", encoding="utf-8") as contenu:
            return json.load(contenu)

    except json.JSONDecodeError as erreur:
        raise ValueError(
            f"Le fichier {chemin} contient un JSON invalide."
        ) from erreur

    except OSError as erreur:
        raise OSError(
            f"Impossible de lire le fichier {chemin}."
        ) from erreur

    finally:
        pass


def sauvegarder_json(chemin: str, donnees: Any) -> None:
    """Enregistre des données dans un fichier JSON."""
    fichier = Path(chemin)
    fichier.parent.mkdir(parents=True, exist_ok=True)

    try:
        with fichier.open("w", encoding="utf-8") as contenu:
            json.dump(
                donnees,
                contenu,
                ensure_ascii=False,
                indent=4
            )

    except OSError as erreur:
        raise OSError(
            f"Impossible d'écrire dans le fichier {chemin}."
        ) from erreur

    finally:
        pass