"""Point d'entrée de l'application."""

from departement import Departement
from employe import Employe
from exceptions import GestionEmployesError
from gestion_departements import GestionDepartements
from gestion_employes import GestionEmployes


def demander_entier(message: str) -> int:
    """Demande un entier à l'utilisateur."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez saisir un entier valide.")


def demander_float(message: str) -> float:
    """Demande un nombre décimal."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Veuillez saisir un nombre valide.")


def ajouter_employe(gestion: GestionEmployes) -> None:
    """Ajoute un employé avec les données saisies."""
    employe = Employe(
        matricule=input("Matricule : "),
        nom=input("Nom : "),
        prenom=input("Prénom : "),
        age=demander_entier("Âge : "),
        sexe=input("Sexe : "),
        adresse=input("Adresse : "),
        telephone=input("Téléphone : "),
        poste=input("Poste : "),
        salaire=demander_float("Salaire : ")
    )

    gestion.ajouter(employe)
    gestion.sauvegarder()
    print("Employé ajouté avec succès.")


def ajouter_departement(gestion: GestionDepartements) -> None:
    """Ajoute un département."""
    departement = Departement(
        code=input("Code : "),
        nom=input("Nom : "),
        description=input("Description : ")
    )

    gestion.ajouter(departement)
    gestion.sauvegarder()
    print("Département ajouté avec succès.")


def afficher_statistiques(gestion: GestionEmployes) -> None:
    """Affiche les statistiques."""
    statistiques = gestion.statistiques()

    print(f"Total : {statistiques['total']}")
    print(f"Minimum : {statistiques['minimum']:.2f}")
    print(f"Maximum : {statistiques['maximum']:.2f}")
    print(f"Moyenne : {statistiques['moyenne']:.2f}")
    print(f"Masse salariale : {statistiques['masse_salariale']:.2f}")

    print("\nEmployés par département :")
    for code, nombre in gestion.nombre_par_departement().items():
        print(f"{code} : {nombre}")


def menu() -> None:
    """Lance le menu principal."""
    gestion_employes = GestionEmployes()
    gestion_departements = GestionDepartements()

    while True:
        print("\n===== GESTION DES EMPLOYÉS =====")
        print("1. Ajouter un employé")
        print("2. Rechercher un employé")
        print("3. Supprimer un employé")
        print("4. Afficher les employés")
        print("5. Ajouter un département")
        print("6. Afficher les départements")
        print("7. Statistiques")
        print("8. Sauvegarder")
        print("9. Quitter")

        choix = input("Votre choix : ")

        try:
            if choix == "1":
                ajouter_employe(gestion_employes)

            elif choix == "2":
                matricule = input("Matricule : ")
                employe = gestion_employes.rechercher(matricule)
                print(employe.afficher())

            elif choix == "3":
                matricule = input("Matricule : ")
                gestion_employes.supprimer(matricule)
                gestion_employes.sauvegarder()
                print("Employé supprimé.")

            elif choix == "4":
                gestion_employes.afficher_tous()

            elif choix == "5":
                ajouter_departement(gestion_departements)

            elif choix == "6":
                gestion_departements.afficher_tous()

            elif choix == "7":
                afficher_statistiques(gestion_employes)

            elif choix == "8":
                gestion_employes.sauvegarder()
                gestion_departements.sauvegarder()
                print("Données sauvegardées.")

            elif choix == "9":
                gestion_employes.sauvegarder()
                gestion_departements.sauvegarder()
                print("Au revoir.")
                break

            else:
                print("Choix invalide.")

        except GestionEmployesError as erreur:
            print(f"Erreur : {erreur}")
        except ValueError as erreur:
            print(f"Erreur de saisie : {erreur}")
        except OSError as erreur:
            print(f"Erreur de fichier : {erreur}")


if __name__ == "__main__":
    menu()
