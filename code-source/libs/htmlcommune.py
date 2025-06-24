# libs/htmlcommune.py

import random
import json # On importe le module json pour une conversion propre vers JavaScript

def fabrication_str_map(liste_antennes):
    liste_marqueurs = []
    for antenne in liste_antennes:
        # CORRECTION : Remplacer la virgule par un point avant la conversion en float
        try:
            lat_str = antenne["latitude"].replace(',', '.')
            lon_str = antenne["longitude"].replace(',', '.')
            
            # Ajout d'un petit décalage aléatoire pour éviter que les points se superposent parfaitement
            lat = float(lat_str) + random.uniform(-0.0005, 0.0005)
            lon = float(lon_str) + random.uniform(-0.0005, 0.0005)

        except (ValueError, TypeError):
            # Si les coordonnées sont invalides, on ignore cette antenne pour la carte
            continue 

        # Ce dictionnaire sera converti en objet JavaScript
        marqueur = {
            "lat": lat,
            "lon": lon,
            "operator": antenne["opérateur"],
            "popup": (
                f"<b>Opérateur:</b> {antenne['opérateur']}<br>"
                f"<b>ID Antenne:</b> {antenne['id_station']}<br>"
                f"<b>2G:</b> {'Oui' if antenne['f_2g'] else 'Non'}<br>"
                f"<b>3G:</b> {'Oui' if antenne['f_3g'] else 'Non'}<br>"
                f"<b>4G:</b> {'Oui' if antenne['f_4g'] else 'Non'}<br>"
                f"<b>5G:</b> {'Oui' if antenne['f_5g'] else 'Non'}"
            )
        }
        liste_marqueurs.append(marqueur)
        
    if not liste_marqueurs:
        return "<!-- Aucune antenne avec des coordonnées valides à afficher sur la carte. -->"
    
    # CORRECTION : On s'assure aussi de remplacer la virgule pour le centrage de la carte
    first_lat = liste_marqueurs[0]["lat"]
    first_long = liste_marqueurs[0]["lon"]

    # OPTIMISATION : On utilise json.dumps pour créer une chaîne JSON valide, beaucoup plus sûr que str()
    str_liste_marqueurs_json = json.dumps(liste_marqueurs, indent=4) # indent pour la lisibilité
    
    # Le code JavaScript pour générer la carte et les marqueurs
    str_html=f"""    <script>
        var antennes = {str_liste_marqueurs_json};

        var map = L.map('map').setView([{first_lat}, {first_long}], 13);

        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '© OpenStreetMap contributors'
        }}).addTo(map);

        antennes.forEach(function (antenne) {{
            let icon;
            if (antenne.operator === "Free Mobile") {{
                icon = redIcon;
            }} else if (antenne.operator === "Orange") {{
                icon = orangeIcon;
            }} else if (antenne.operator === "SFR") {{
                icon = greenIcon;
            }} else if (antenne.operator === "Bouygues Telecom") {{
                icon = blueIcon;
            }} else {{
                icon = L.Icon.Default(); // Une icône par défaut si l'opérateur n'est pas reconnu
            }}
            L.marker([antenne.lat, antenne.lon], {{icon: icon}}).addTo(map).bindPopup(antenne.popup);
        }});
    </script>"""
    return str_html

def composition_str_antennes(liste_antennes):
    str_html=""
    for antenne in liste_antennes:
        str_temp=f"""
            <tr>
                <td>{antenne["id_station"]}</td>
                <td>{antenne["opérateur"]}</td>
                <td>{antenne["latitude"]}</td>
                <td>{antenne["longitude"]}</td>
                <td class="{"frequence-green" if antenne["f_2g"]==True else "frequence-red"}"></td>
                <td class="{"frequence-green" if antenne["f_3g"]==True else "frequence-red"}"></td>
                <td class="{"frequence-green" if antenne["f_4g"]==True else "frequence-red"}"></td>
                <td class="{"frequence-green" if antenne["f_5g"]==True else "frequence-red"}"></td>
            </tr>
        """
        str_html+=str_temp
    return str_html

def generate_commune_html(liste_antennes):
    if not liste_antennes:
        return "<html><body>Erreur: Aucune antenne trouvée pour cette commune.</body></html>"
        
    random.shuffle(liste_antennes)
    commune=liste_antennes[0]["commune"]
    région=liste_antennes[0]["région"]
    département=liste_antennes[0]["département"]
    liste_antennes_html=composition_str_antennes(liste_antennes)
    script_map=fabrication_str_map(liste_antennes)
    code_html=f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Antennes à {commune}</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css">
</head>
<body>
    <header>
        <h1>Antennes à {commune}</h1>
        <a href="../index.html">Retour à l'accueil</a>
    </header>
    <h2>{commune}</h2>
    <p>{département}, {région}</p>
    <main>
        <table>
            <thead>
                <tr>
                    <th>ID Antenne</th>
                    <th>Opérateur</th>
                    <th>Latitude</th>
                    <th>Longitude</th>
                    <th>2G</th>
                    <th>3G</th>
                    <th>4G</th>
                    <th>5G</th>
                </tr>
            </thead>
            <tbody>
                {liste_antennes_html}
            </tbody>
        </table>
        <div id="map"></div>
    </main>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="../js/colors.js"></script>
    {script_map}
    <footer>
        Réalisé par Tristan BRINGUIER dans le cadre de la SAE15 (BUT R&T) à l'IUT de Villetaneuse.
    </footer>
</body>
</html>
    """
    return code_html
