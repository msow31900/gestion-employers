"""Exceptions personnalisées de l'application."""


class GestionEmployesError(Exception):
    """Exception générale de l'application."""


class SalaireNegatifError(GestionEmployesError):
    """Exception levée lorsqu'un salaire est négatif."""


class AgeInvalideError(GestionEmployesError):
    """Exception levée lorsqu'un âge est invalide."""


class MatriculeInexistantError(GestionEmployesError):
    """Exception levée lorsqu'un matricule n'existe pas."""


class DepartementIntrouvableError(GestionEmployesError):
    """Exception levée lorsqu'un département est introuvable."""


class DonneesInvalidesError(GestionEmployesError):
    """Exception levée lorsque des données sont invalides."""
