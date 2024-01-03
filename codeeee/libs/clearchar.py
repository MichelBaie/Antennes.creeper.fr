# Permet de retirer les caractères spéciaux et espaces d'un nom de commune pour obtenir un nom propre pour les chemins de fichiers.
import re
def nettoyer_chaine(chaine):
    # Convertit la chaîne en minuscules
    chaine_minuscules = chaine.lower()
    # Supprime les caractères spéciaux et les espaces
    chaine_propre = re.sub(r'[^a-z]', '', chaine_minuscules)
    return chaine_propre