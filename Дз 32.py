class Pénalité:
    def __init__(self, type_pénalité, ville, montant):
        self.type_pénalité = type_pénalité
        self.ville = ville
        self.montant = montant

class Node:
    def __init__(self, code_identification):
        self.code_identification = code_identification
        self.pénalités = []
        self.left = None
        self.right = None

class BaseDeDonnéesPénalités:
    def __init__(self):
        self.root = None

    def ajouter_personne(self, code_identification):
        if not self.root:
            self.root = Node(code_identification)
        else:
            self._ajouter_personne_récursif(self.root, code_identification)

    def _ajouter_personne_récursif(self, current_node, code_identification):
        if code_identification < current_node.code_identification:
            if current_node.left is None:
                current_node.left = Node(code_identification)
            else:
                self._ajouter_personne_récursif(current_node.left, code_identification)
        elif code_identification > current_node.code_identification:
            if current_node.right is None:
                current_node.right = Node(code_identification)
            else:
                self._ajouter_personne_récursif(current_node.right, code_identification)

    def ajouter_pénalité(self, code_identification, type_pénalité, ville, montant):
        personne = self._trouver_personne(self.root, code_identification)
        if personne:
            personne.pénalités.append(Pénalité(type_pénalité, ville, montant))
        else:
            print("Personne non trouvée dans la base de données.")

    def _trouver_personne(self, nœud_actuel, code_identification):
        if nœud_actuel is None:
            return None
        if nœud_actuel.code_identification == code_identification:
            return nœud_actuel
        elif code_identification < nœud_actuel.code_identification:
            return self._trouver_personne(nœud_actuel.left, code_identification)
        else:
            return self._trouver_personne(nœud_actuel.right, code_identification)

    def afficher_base_de_données(self):
        self._afficher_base_de_données_récursif(self.root)

    def _afficher_base_de_données_récursif(self, nœud_actuel):
        if nœud_actuel:
            self._afficher_base_de_données_récursif(nœud_actuel.left)
            print("Code d'identification:", nœud_actuel.code_identification)
            print("Pénalités:")
            for pénalité in nœud_actuel.pénalités:
                print("- Type:", pénalité.type_pénalité)
                print("  Ville:", pénalité.ville)
                print("  Montant:", pénalité.montant)
            print()
            self._afficher_base_de_données_récursif(nœud_actuel.right)

    def afficher_données_personne(self, code_identification):
        personne = self._trouver_personne(self.root, code_identification)
        if personne:
            print("Code d'identification:", personne.code_identification)
            print("Pénalités:")
            for pénalité in personne.pénalités:
                print("- Type:", pénalité.type_pénalité)
                print("  Ville:", pénalité.ville)
                print("  Montant:", pénalité.montant)
        else:
            print("Personne non trouvée dans la base de données.")

    def afficher_pénalités_par_type(self, type_pénalité):
        self._afficher_pénalités_par_type_récursif(self.root, type_pénalité)

    def _afficher_pénalités_par_type_récursif(self, nœud_actuel, type_pénalité):
        if nœud_actuel:
            self._afficher_pénalités_par_type_récursif(nœud_actuel.left, type_pénalité)
            for pénalité in nœud_actuel.pénalités:
                if pénalité.type_pénalité == type_pénalité:
                    print("Code d'identification:", nœud_actuel.code_identification)
                    print("Type:", pénalité.type_pénalité)
                    print("Ville:", pénalité.ville)
                    print("Montant:", pénalité.montant)
            self._afficher_pénalités_par_type_récursif(nœud_actuel.right, type_pénalité)

    def afficher_pénalités_par_ville(self, ville):
        self._afficher_pénalités_par_ville_récursif(self.root, ville)

    def _afficher_pénalités_par_ville_récursif(self, nœud_actuel, ville):
        if nœud_actuel:
            self._afficher_pénalités_par_ville_récursif(nœud_actuel.left, ville)
            for pénalité in nœud_actuel.pénalités:
                if pénalité.ville == ville:
                    print("Code d'identification:", nœud_actuel.code_identification)
                    print("Type:", pénalité.type_pénalité)
                    print("Ville:", pénalité.ville)
                    print("Montant:", pénalité.montant)
            self._afficher_pénalités_par_ville_récursif(nœud_actuel.right, ville)

    def supprimer_pénalité(self, code_identification, type_pénalité, ville, montant):
        personne = self._trouver_personne(self.root, code_identification)
        if personne:
            for pénalité in personne.pénalités:
                if pénalité.type_pénalité == type_pénalité and pénalité.ville == ville and pénalité.montant == montant:
                    personne.pénalités.remove(pénalité)
                    print("Pénalité supprimée avec succès.")
                    return
            print("Pénalité non trouvée pour les critères spécifiés.")
        else:
            print("Personne non trouvée dans la base de données.")

    def mettre_à_jour_infos_personne(self, code_identification, nouveau_code_identification):
        personne = self._trouver_personne(self.root, code_identification)
        if personne:
            personne.code_identification = nouveau_code_identification
            print("Informations sur la personne mises à jour avec succès.")
        else:
            print("Personne non trouvée dans la base de données.")

base_de_données_pénalités = BaseDeDonnéesPénalités()
base_de_données_pénalités.ajouter_personne(12345)
base_de_données_pénalités.ajouter_pénalité(12345, "Штраф за паркування", "Париж", 200)
base_de_données_pénalités.afficher_base_de_données()
base_de_données_pénalités.afficher_données_personne(12345)
base_de_données_pénalités.afficher_pénalités_par_type("Штраф за паркування")
base_de_données_pénalités.afficher_pénalités_par_ville("Париж")
base_de_données_pénalités.ajouter_personne(67890)
base_de_données_pénalités.ajouter_pénalité(67890, "Штраф за швидкість", "Ліон", 200)

base_de_données_pénalités.ajouter_pénalité(12345, "Штраф за паркування", "Марсель", 150)

base_de_données_pénalités.supprimer_pénalité(12345, "Штраф за паркування", "Марсель", 150)

base_de_données_pénalités.mettre_à_jour_infos_personne(12345, 123456)

base_de_données_pénalités.afficher_base_de_données()

base_de_données_pénalités.afficher_données_personne(12345)

base_de_données_pénalités.afficher_pénalités_par_type("Штраф за паркування")

base_de_données_pénalités.afficher_pénalités_par_ville("Париж")

