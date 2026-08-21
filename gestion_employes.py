"""Gestion des employés."""

from statistics import mean

from employe import Employe
from exceptions import MatriculeInexistantError
from utils import charger_json, sauvegarder_json


class GestionEmployes:
    """Gère les employés de l'entreprise."""

    def __init__(self, chemin: str = "data/employes.json") -> None:
        """Initialise le gestionnaire."""
        self.__chemin = chemin
        self.__employes = {}
        self.charger()

    def ajouter(self, employe: Employe) -> None:
        """Ajoute un employé."""
        if employe.matricule in self.__employes:
            raise ValueError("Ce matricule existe déjà.")

        self.__employes[employe.matricule] = employe

    def rechercher(self, matricule: str) -> Employe:
        """Recherche un employé."""
        if matricule not in self.__employes:
            raise MatriculeInexistantError(
                f"Matricule inexistant : {matricule}"
            )

        return self.__employes[matricule]

    def supprimer(self, matricule: str) -> None:
        """Supprime un employé."""
        self.rechercher(matricule)
        del self.__employes[matricule]

    def modifier(self, matricule: str, **modifications) -> None:
        """Modifie un employé."""
        employe = self.rechercher(matricule)

        for attribut, valeur in modifications.items():
            if valeur is not None:
                setattr(employe, attribut, valeur)

    def afficher_tous(self) -> None:
        """Affiche tous les employés."""
        if not self.__employes:
            print("Aucun employé enregistré.")
            return

        for employe in self.__employes.values():
            print(employe.afficher())

    def affecter_departement(
        self,
        matricule: str,
        code_departement: str
    ) -> None:
        """Affecte un département à un employé."""
        employe = self.rechercher(matricule)
        employe.departement = code_departement.upper()

    def statistiques(self) -> dict:
        """Calcule les statistiques salariales."""
        salaires = [
            employe.salaire
            for employe in self.__employes.values()
        ]

        if not salaires:
            return {
                "total": 0,
                "minimum": 0,
                "maximum": 0,
                "moyenne": 0,
                "masse_salariale": 0
            }

        return {
            "total": len(salaires),
            "minimum": min(salaires),
            "maximum": max(salaires),
            "moyenne": mean(salaires),
            "masse_salariale": sum(salaires)
        }

    def nombre_par_departement(self) -> dict:
        """Compte les employés par département."""
        resultat = {}

        for employe in self.__employes.values():
            code = employe.departement or "Non affecté"
            resultat[code] = resultat.get(code, 0) + 1

        return resultat

    def sauvegarder(self) -> None:
        """Sauvegarde les employés."""
        donnees = [
            employe.to_dict()
            for employe in self.__employes.values()
        ]
        sauvegarder_json(self.__chemin, donnees)

    def charger(self) -> None:
        """Charge les employés depuis le fichier JSON."""
        donnees = charger_json(self.__chemin, [])

        self.__employes = {
            donnees_employe["matricule"]:
                Employe.from_dict(donnees_employe)
            for donnees_employe in donnees
        }
