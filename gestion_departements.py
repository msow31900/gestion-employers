"""Gestion des départements."""

from departement import Departement
from exceptions import DepartementIntrouvableError
from utils import charger_json, sauvegarder_json


class GestionDepartements:
    """Gère les départements de l'entreprise."""

    def __init__(
        self,
        chemin: str = "data/departements.json"
    ) -> None:
        """Initialise le gestionnaire."""
        self.__chemin = chemin
        self.__departements = {}
        self.charger()

    def ajouter(self, departement: Departement) -> None:
        """Ajoute un département."""
        if departement.code in self.__departements:
            raise ValueError("Ce code existe déjà.")

        self.__departements[departement.code] = departement

    def rechercher(self, code: str) -> Departement:
        """Recherche un département."""
        code = code.upper()

        if code not in self.__departements:
            raise DepartementIntrouvableError(
                f"Département introuvable : {code}"
            )

        return self.__departements[code]

    def modifier(self, code: str, **modifications) -> None:
        """Modifie un département."""
        departement = self.rechercher(code)

        for attribut, valeur in modifications.items():
            if valeur is not None:
                setattr(departement, attribut, valeur)

    def supprimer(self, code: str) -> None:
        """Supprime un département."""
        self.rechercher(code)
        del self.__departements[code.upper()]

    def afficher_tous(self) -> None:
        """Affiche tous les départements."""
        if not self.__departements:
            print("Aucun département enregistré.")
            return

        for departement in self.__departements.values():
            print(departement.afficher())

    def sauvegarder(self) -> None:
        """Sauvegarde les départements."""
        donnees = [
            departement.to_dict()
            for departement in self.__departements.values()
        ]
        sauvegarder_json(self.__chemin, donnees)

    def charger(self) -> None:
        """Charge les départements depuis le fichier JSON."""
        donnees = charger_json(self.__chemin, [])

        self.__departements = {
            element["code"]: Departement.from_dict(element)
            for element in donnees
        }