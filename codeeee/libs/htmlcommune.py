import random

def fabrication_str_map(liste_antennes):
    liste_html = []
    for antenne in liste_antennes:
        dico={}
        dico["lat"]=str(float(antenne["latitude"])+random.uniform(0.0005, 0.001))
        dico["lon"]=str(float(antenne["longitude"])+random.uniform(0.0005, 0.001))
        dico["operator"]=antenne["opérateur"]
        dico["id_antenne"]=antenne["id_station"]
        dico["deuxg"]=str(antenne["f_2g"])
        dico["troisg"]=str(antenne["f_3g"])
        dico["quatreg"]=str(antenne["f_4g"])
        dico["cinqg"]=str(antenne["f_5g"])
        liste_html.append(dico)
    str_liste_html=str(liste_html)
    first_lat=liste_antennes[0]["latitude"]
    first_long=liste_antennes[0]["longitude"]
    tag=f"""'Opérateur: ' + antenne.operator + '<br>ID Antenne: ' + antenne.id_antenne + '<br>2G: ' + antenne.deuxg + '<br>3G: ' + antenne.troisg + '<br>4G: ' + antenne.quatreg + '<br>5G: ' + antenne.cinqg"""
    str_html=f"""    <script>
        var antennes = {str_liste_html};

        var map = L.map('map').setView([{first_lat}, {first_long}], 12);

        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '© OpenStreetMap contributors'
        }}).addTo(map);

        antennes.forEach(function (antenne) {{
            if (antenne.operator === "Free Mobile") {{
                L.marker([antenne.lat, antenne.lon],{{icon: redIcon}}).addTo(map).bindPopup({tag});
            }} else if (antenne.operator === "Orange") {{
                L.marker([antenne.lat, antenne.lon],{{icon: orangeIcon}}).addTo(map).bindPopup({tag});
            }} else if (antenne.operator === "SFR") {{
                L.marker([antenne.lat, antenne.lon],{{icon: greenIcon}}).addTo(map).bindPopup({tag});
            }} else if (antenne.operator === "Bouygues Telecom") {{
                L.marker([antenne.lat, antenne.lon],{{icon: blueIcon}}).addTo(map).bindPopup({tag});
            }}
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
    random.shuffle(liste_antennes)
    commune=liste_antennes[0]["commune"]
    code_postal=liste_antennes[0]["code_postal"]
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
    <p>{code_postal}, {département}, {région}</p>
    <main>
        <table>
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
            {liste_antennes_html}
        </table>
        <div id="map"></div>
    </main>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="../js/colors.js"></script>
    {script_map}
    <footer>
        Réalisé par Tristan BRINGUIER dans le cadre de la SAE15 à l'IUT de Villetaneuse
    </footer>
</body>
</html>
    """
    return code_html