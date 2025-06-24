from libs.clearchar import nettoyer_chaine
def composition_str_communes(liste_communes,nb_antennes_communes):
    str_html=""
    for commune in liste_communes:
        nom_commune=nettoyer_chaine(commune)
        nb_antennes=str(nb_antennes_communes[commune])
        str_html_temp=f"""
                <tr>
                    <td><a href="./communes/{nom_commune}.html">{commune}</a></td>
                    <td>{nb_antennes}</td>
                </tr>
        """
        str_html+=str_html_temp
    return str_html
def generate_index_html(liste_communes,nb_antennes_communes,Nb_antenne_free,Nb_antennes_bouygues,Nb_antennes_orange,Nb_antennes_sfr):
    html_communes_table=composition_str_communes(liste_communes,nb_antennes_communes)
    L_nombre_antennes_operateurs=[]
    L_nombre_antennes_operateurs.append(Nb_antennes_orange)
    L_nombre_antennes_operateurs.append(Nb_antennes_bouygues)
    L_nombre_antennes_operateurs.append(Nb_antennes_sfr)
    L_nombre_antennes_operateurs.append(Nb_antenne_free)
    str_L_nombre_antennes_operateurs=str(L_nombre_antennes_operateurs)
    code_html=f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Antennes réseau par commune</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div id="container">
        <h1>Antennes réseau par commune</h1>
        <p>
        J'ai choisi de traiter les données de l'ARCEP concernant les antennes de téléphonie mobile en France.
        <br>
        Le csv de base contiens toutes les données liées à chaque antenne, leur compatibilité en fonction des fréquences, leur localisation...
        <br>
        Ce site permet de naviguer entre les communes et voir où se situent précisément les antennes ainsi qu'à quel opérateur elles appartiennent.
        <br>
        Le dataset est disponible au lieu suivant (extrait de data.gouv.fr) : https://data.arcep.fr/mobile/sites/last/
        </p>
        <input type="text" id="searchInput" placeholder="Filtrer les communes..." onkeyup="filterCommunes()">
        
        <table id="communeTable">
            <thead>
                <tr>
                    <th>Nom de la commune</th>
                    <th>Nombre d'antennes</th>
                </tr>
            </thead>
            <tbody>
            {html_communes_table}
            </tbody>
        </table>
        <h1>Statistiques globales au jeu de données :</h1>
        <div>
            <canvas id="tauxoperateurs"></canvas>
        </div>
    </div>
    <script src="js/main.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    const ctx = document.getElementById('tauxoperateurs');
    new Chart(ctx, {{
        type: 'bar',
        data: {{
            labels: ['Orange', 'Bouygues Telecom', 'SFR', 'Free Mobile'],
            datasets: [{{
                label: "Nombre d'antennes par opérateur",
                data: {str_L_nombre_antennes_operateurs},
                borderWidth: 1
            }}]
        }},
        options: {{
            scales: {{
                y: {{
                beginAtZero: true
            }}
        }}
    }}
    }});
</script>
    <footer>
        Réalisé par Tristan BRINGUIER dans le cadre de la SAE15 (BUT R&T) à l'IUT de Villetaneuse.
    </footer>
    </body>
</html>
    """
    return code_html