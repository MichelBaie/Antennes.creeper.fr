#!/usr/bin/python3
import csv # On importe la librarie permettant de traiter du CSV

# Import du code sous la forme de différents modules
from libs.htmlcommune import generate_commune_html
from libs.htmlindex import generate_index_html
from libs.clearchar import nettoyer_chaine
from libs.generatebasefiles import generate_css_js

data_operateurs_brut=open("dataset/2023_T3_sites_Metropole.csv",'r',encoding='utf-8') # Ouverture du dataset
dico_data_operateurs=csv.DictReader(data_operateurs_brut) # Traitement du dataset avec DictReader

Liste_Antennes = [] # Création d'une liste qui contiendras chaque antenne

# Imports des antennes dans la liste (on garde uniquement les données de notre choix)
print("Lecture des antennes....")
for ligne in dico_data_operateurs:
    antenne={} # On crée un dictionnaire vide auquel on ajoute chacune des clés ci-dessous
    antenne["opérateur"]=ligne["nom_op"]
    antenne["id_station"]=ligne["id_station_anfr"]
    antenne["latitude"]=ligne["latitude"]
    antenne["longitude"]=ligne["longitude"]
    antenne["région"]=ligne["nom_reg"]
    antenne["département"]=ligne["nom_dep"]
    antenne["commune"]=ligne["nom_com"]
    antenne["f_2g"]=bool(int(ligne["site_2g"]))
    antenne["f_3g"]=bool(int(ligne["site_3g"]))
    antenne["f_4g"]=bool(int(ligne["site_4g"]))
    antenne["f_5g"]=bool(int(ligne["site_5g"]))
    Liste_Antennes.append(antenne) # On ajoute le dictionnaire créé à la liste

# Différentes données utiles au script
Liste_Communes = [] # Liste contenant toutes les communes
Nb_antennes_communes = {} # Dictionnaire contenant pour clé le nom d'une commune et pour valeur le nombre d'antennes dans celle-ci
Antennes_par_communes = {} # Dictionnaire contenant pour clé le nom d'une commune et pour valeur une liste d'antennes
Nb_antenne_free = 0 # Compteur du nombre d'antennes appartenant à l'opérateur Free Mobile
Nb_antennes_orange = 0 # Compteur du nombre d'antennes appartenant à l'opérateur Orange
Nb_antennes_sfr = 0 # Compteur du nombre d'antennes appartenant à l'opérateur SFR
Nb_antennes_bouygues = 0 # Compteur du nombre d'antennes appartenant à l'opérateur Bouygues Telecom

# Extraction de métadonnées à partir de chaque antennes
print("Rangement des antennes....")
for antenne in Liste_Antennes:
    # Création de la liste de Communes
    if antenne["commune"] not in Liste_Communes:
        Liste_Communes.append(antenne["commune"])
    
    # Création du dictionnaire du Nombre d'Antennes par Commune
    if antenne["commune"] not in Nb_antennes_communes:
        Nb_antennes_communes[antenne["commune"]]=1
    else:
        Nb_antennes_communes[antenne["commune"]]+=1
    
    # Création du dictionnaire contenant la liste d'antenne par Commune
    if antenne["commune"] not in Antennes_par_communes:
        Antennes_par_communes[antenne["commune"]]=[]
        Antennes_par_communes[antenne["commune"]].append(antenne)
    else:
        Antennes_par_communes[antenne["commune"]].append(antenne)
    
    # Comptage du nombre d'antennes pour chaque opérateur (stats en pied de page)
    if antenne["opérateur"]=="Orange":
        Nb_antennes_orange+=1
    if antenne["opérateur"]=="SFR":
        Nb_antennes_sfr+=1
    if antenne["opérateur"]=="Bouygues Telecom":
        Nb_antennes_bouygues+=1
    if antenne["opérateur"]=="Free Mobile":
        Nb_antenne_free+=1

# Tri de la liste de communes dans l'ordre croissant par soucis d'esthétique
Liste_Communes.sort()
print("Antennes rangées !")

# Génération des fichiers de manière dynamique
print("Génération des fichiers HTML...")
generate_css_js() # Génération des dossiers et fichiers javascript/css de base dans le dossier html
for commune in Liste_Communes: # Génération de chaque fichier html par commune
    html_commune = generate_commune_html(Antennes_par_communes[commune])
    filename = "html/communes/" + nettoyer_chaine(commune) + ".html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_commune)
html_index = generate_index_html(Liste_Communes,Nb_antennes_communes,Nb_antenne_free,Nb_antennes_bouygues,Nb_antennes_orange,Nb_antennes_sfr) # Génération du fichier index.html
with open("html/index.html", 'w', encoding='utf-8') as file:
        file.write(html_index)
print("Le traitement des données est terminé ! Vous pouvez retrouver le site depuis le fichier index.html dans le dossier html.")