"""Définition de la classe Personne."""


class Personne:
    """Représente une personne."""

    def __init__(
        self,
        nom: str,
        prenom: str,
        age: int,
        sexe: str,
        adresse: str,
        telephone: str
    ) -> None:
        """Initialise une personne."""
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.adresse = adresse
        self.telephone = telephone

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
    def prenom(self) -> str:
        """Retourne le prénom."""
        return self.__prenom

    @prenom.setter
    def prenom(self, valeur: str) -> None:
        """Modifie le prénom."""
        if not valeur.strip():
            raise ValueError("Le prénom est obligatoire.")
        self.__prenom = valeur.strip()

    @property
    def age(self) -> int:
        """Retourne l'âge."""
        return self.__age

    @age.setter
    def age(self, valeur: int) -> None:
        """Modifie l'âge."""
        valeur = int(valeur)

        if valeur <= 0 or valeur > 120:
            raise ValueError("L'âge doit être compris entre 1 et 120.")

        self.__age = valeur

    @property
    def sexe(self) -> str:
        """Retourne le sexe."""
        return self.__sexe

    @sexe.setter
    def sexe(self, valeur: str) -> None:
        """Modifie le sexe."""
        self.__sexe = valeur.strip()

    @property
    def adresse(self) -> str:
        """Retourne l'adresse."""
        return self.__adresse

    @adresse.setter
    def adresse(self, valeur: str) -> None:
        """Modifie l'adresse."""
        self.__adresse = valeur.strip()

    @property
    def telephone(self) -> str:
        """Retourne le téléphone."""
        return self.__telephone

    @telephone.setter
    def telephone(self, valeur: str) -> None:
        """Modifie le téléphone."""
        self.__telephone = valeur.strip()

    def afficher(self) -> str:
        """Affiche les informations de la personne."""
        return f"{self.prenom} {self.nom}, {self.age} ans"

    def to_dict(self) -> dict:
        """Transforme la personne en dictionnaire."""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "sexe": self.sexe,
            "adresse": self.adresse,
            "telephone": self.telephone
        }
