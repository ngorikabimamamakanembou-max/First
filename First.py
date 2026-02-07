# ================================
# Programme d'inscription
# École : CSP GOURE
# ================================

def inscription():
    print("=" * 40)
    print("   BIENVENUE À L'ÉCOLE CSP GOURE")
    print("=" * 40)

    # Saisie des informations
    nom = input("Entrez votre nom : ").strip()
    prenom = input("Entrez votre prénom : ").strip()

    while True:
        try:
            age = int(input("Entrez votre âge : "))
            if age <= 0:
                print("❌ L'âge doit être positif.")
            else:
                break
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")

    classe = input("Entrez votre classe (ex: L2 Info, 3ème, etc.) : ").strip()
    telephone = input("Entrez votre numéro de téléphone : ").strip()

    # Affichage récapitulatif
    print("\n📋 RÉCAPITULATIF DE L'INSCRIPTION")
    print("-" * 40)
    print(f"Nom        : {nom}")
    print(f"Prénom     : {prenom}")
    print(f"Âge        : {age}")
    print(f"Classe     : {classe}")
    print(f"Téléphone  : {telephone}")

    confirmation = input("\nConfirmer l'inscription ? (oui/non) : ").lower()

    if confirmation == "oui":
        enregistrer_inscription(nom, prenom, age, classe, telephone)
        print("\n✅ Inscription réussie ! Bienvenue à CSP GOURE 🎉")
    else:
        print("\n❌ Inscription annulée.")


def enregistrer_inscription(nom, prenom, age, classe, telephone):
    with open("inscriptions_csp_goure.txt", "a", encoding="utf-8") as fichier:
        fichier.write(
            f"Nom: {nom}, Prénom: {prenom}, Âge: {age}, "
            f"Classe: {classe}, Téléphone: {telephone}\n"
        )


# Lancement du programme
inscription()
