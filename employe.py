"""Définition de la classe Employe."""

from personne import Personne
from exceptions import SalaireNegatifError


class Employe(Personne):
    """Représente un employé."""

    def __init__(
        self,
        matricule: str,
        nom: str,
        prenom: str,
        age: int,
        sexe: str,
        adresse: str,
        telephone: str,
        poste: str,
        salaire: float,
        departement: str | None = None
    ) -> None:
        """Initialise un employé."""
        super().__init__(
            nom,
            prenom,
            age,
            sexe,
            adresse,
            telephone
        )

        self.matricule = matricule
        self.poste = poste
        self.salaire = salaire
        self.departement = departement

    @property
    def matricule(self) -> str:
        """Retourne le matricule."""
        return self.__matricule

    @matricule.setter
    def matricule(self, valeur: str) -> None:
        """Modifie le matricule."""
        if not valeur.strip():
            raise ValueError("Le matricule est obligatoire.")
        self.__matricule = valeur.strip()

    @property
    def poste(self) -> str:
        """Retourne le poste."""
        return self.__poste

    @poste.setter
    def poste(self, valeur: str) -> None:
        """Modifie le poste."""
        self.__poste = valeur.strip()

    @property
    def salaire(self) -> float:
        """Retourne le salaire."""
        return self.__salaire

    @salaire.setter
    def salaire(self, valeur: float) -> None:
        """Modifie le salaire."""
        valeur = float(valeur)

        if valeur < 0:
            raise SalaireNegatifError(
                "Le salaire ne peut pas être négatif."
            )

        self.__salaire = valeur

    @property
    def departement(self) -> str | None:
        """Retourne le département."""
        return self.__departement

    @departement.setter
    def departement(self, valeur: str | None) -> None:
        """Modifie le département."""
        self.__departement = valeur

    def afficher(self) -> str:
        """Affiche les informations de l'employé."""
        return (
            f"[{self.matricule}] {self.prenom} {self.nom} | "
            f"Poste : {self.poste} | "
            f"Salaire : {self.salaire:.2f} | "
            f"Département : {self.departement or 'Non affecté'}"
        )

    def to_dict(self) -> dict:
        """Transforme l'employé en dictionnaire."""
        donnees = super().to_dict()

        donnees.update({
            "matricule": self.matricule,
            "poste": self.poste,
            "salaire": self.salaire,
            "departement": self.departement
        })

        return donnees

    @classmethod
    def from_dict(cls, donnees: dict) -> "Employe":
        """Crée un employé depuis un dictionnaire."""
        return cls(
            matricule=donnees["matricule"],
            nom=donnees["nom"],
            prenom=donnees["prenom"],
            age=donnees["age"],
            sexe=donnees["sexe"],
            adresse=donnees["adresse"],
            telephone=donnees["telephone"],
            poste=donnees["poste"],
            salaire=donnees["salaire"],
            departement=donnees.get("departement")
        )
