function filterCommunes() {
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
filterCommunes()