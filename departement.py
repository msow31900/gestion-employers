"""Définition de la classe Departement."""


class Departement:
    """Représente un département."""

    def __init__(
        self,
        code: str,
        nom: str,
        description: str
    ) -> None:
        """Initialise un département."""
        self.code = code
        self.nom = nom
        self.description = description

    @property
    def code(self) -> str:
        """Retourne le code."""
        return self.__code

    @code.setter
    def code(self, valeur: str) -> None:
        """Modifie le code."""
        if not valeur.strip():
            raise ValueError("Le code est obligatoire.")
        self.__code = valeur.strip().upper()

    @property
    def nom(self) -> str:
        """Retourne le nom."""
        return self.__nom

    @nom.setter
    def nom(self, valeur: str) -> None:
        """Modifie le nom."""
        if not valeur.strip():
            raise ValueError("Le nom est obligatoire.")
        self.__nom = valeur.strip()

    @property
    def description(self) -> str:
        """Retourne la description."""
        return self.__description

    @description.setter
    def description(self, valeur: str) -> None:
        """Modifie la description."""
        self.__description = valeur.strip()

    def afficher(self) -> str:
        """Affiche les informations du département."""
        return f"[{self.code}] {self.nom} : {self.description}"

    def to_dict(self) -> dict:
        """Transforme le département en dictionnaire."""
        return {
            "code": self.code,
            "nom": self.nom,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, donnees: dict) -> "Departement":
        """Crée un département depuis un dictionnaire."""
        return cls(
            donnees["code"],
            donnees["nom"],
            donnees["description"]
        )