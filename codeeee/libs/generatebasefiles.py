import os
def generate_css_js():
    try:
        os.mkdir("html")
    except FileExistsError:
        pass
    try:
        os.mkdir("html/css")
    except FileExistsError:
        pass
    try:
        os.mkdir("html/js")
    except FileExistsError:
        pass
    try:
        os.mkdir("html/communes")
    except FileExistsError:
        pass
    with open("html/css/style.css", 'w', encoding='utf-8') as file:
        file.write("""body {
    align-items: center;
    text-align: center;
    margin: 40px;
    background-color: #f0f8ff; /* Bleu clair */
    font-family: Arial, sans-serif;
    color: #000080; /* Bleu marine */
}

#container {
    width: 80%;
    margin: 0 auto;
}

#searchInput {
    padding: 10px;
    margin-top: 20px;
    width: 100%;
    box-sizing: border-box;
}

#communeTable {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

#communeTable th, #communeTable td {
    border: 1px solid #000080; /* Bleu marine */
    padding: 10px;
    text-align: left;
}

a {
    color: #000080; /* Bleu marine */
    text-decoration: underline;
}

header {
    width: 100%;
    background-color: #3498db;
    color: white;
    padding: 10px;
    text-align: left;
    margin-bottom: 20px;
}

main {
    display: flex;
    width: 100%;
    justify-content: space-around;
}

table {
    border-collapse: collapse;
    width: 48%;
    height: 300px; /* Ajustez la hauteur selon vos besoins */
}

th, td {
    border: 1px solid #ddd;
    text-align: left;
    padding: 8px;
    overflow: hidden; /* Masque le contenu dépassant de la cellule */
    white-space: nowrap; /* Empêche le texte de se replier à la ligne */
    text-overflow: ellipsis; /* Ajoute des points de suspension pour le texte dépassant */
}

th {
    background-color: #3498db;
    color: white;
}

td {
    background-color: #ecf0f1;
}

#map {
    height: 400px;
    width: 48%;
}
.frequence-green {
    width: 16px;
    height: 16px;
    background-color: #2ecc71;
}
.frequence-red {
    width: 16px;
    height: 16px;
    background-color: #e74c3c;
}
#map {
    height: 400px;
    margin-top: 20px;
}
footer {
    background-color: #808080; /* Gris */
    color: white;
    text-align: center;
    padding: 10px;
    bottom: 0;
    width: 100%;
}""")
    with open("html/js/colors.js", 'w', encoding='utf-8') as file:
        file.write("""var blueIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png',
	shadowUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});
var redIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
	shadowUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});
var greenIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
	shadowUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});
var orangeIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png',
	shadowUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});""")
    with open("html/js/main.js", 'w', encoding='utf-8') as file:
        file.write("""function filterCommunes() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("communeTable");
    tr = table.getElementsByTagName("tr");

    var count = 0; // Compteur pour limiter le nombre de résultats affichés

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                count++;

                if (count >= 100) {
                    // Limite atteinte, masquer les résultats restants
                    for (var j = i + 1; j < tr.length; j++) {
                        tr[j].style.display = "none";
                    }
                    break;
                }
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
filterCommunes()""")