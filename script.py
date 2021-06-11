# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:34:24 2021

@author: gtent
"""

import requests
from bs4 import BeautifulSoup
import urllib.request

#Chemisier en coton-Tunique- T shirts- Cardigan-
objets = "Pull d'hiver- Sous pull- Pantalons de tous les jours- Jean- Pantalon en toile- Ensemble tailleur habillé-imperméable-pardessus-veste duvet-veste laine-écharpe pashmina-tenue d'intérieur-tenues de nuit- 1 maillot de bain- 1 pochette de sous-vêtements- 1 foulard- 1 set chapeau, gant, écharpe- 1 parapluie- 1 paire de chaussures de marche- 1 paire de bottes- 1 paire de chaussures de ville- 1 paire de ballerines tongues- 1 paire de mules sandales- 1 paire de chaussons d'intérieur- 1 bijou- 1 paire de lunettes de soleil- 1 nécessaire à couture- 1 nécessaire à cirer les chaussures- 1 vanity- 1 pèse-personne- 1 peigne - 1 sèche-cheveux- 1 brosse corps- 1 brosse ongles et rape- 1 brosse à dents- 2 sets linge de toilette- 1 trousse de soin- 1 trousse à pharmacie- 1 bouillotte- 1 panier à provision- 1 poêle- 1 faitout cuit vapeur- 1 économe- 1 cuvette- éponge- brosse- set vaisselle occidentale- "#set vaisselle asiatique- bento- casserole- plat à gratin- plat de service- robot de cuisine- toasteur poubelle à couvercle- cul de poule et passoire- tasse graduée- planche à découper, couteau, pierre à aiguiser- rape- bol et pilon- spatule et baguette de cuisine- ouvre-bouteille- ouvre-boite- paire de ciseaux de cuisine- quelques torchons- plateau- gros bol- plateau à thé chinois- bouteille thermos- rideaux- lampe de travail- lit - draps- table et chaises- fauteuil- réfrigérateur- gazinière - Cuisson  (Minuteur à oeufs, four encastrable NEFF ,..)- machine à laver le linge- baquet à lessive. lave- vaisselle- tapis de bain (IKEA)- fer et table à repasser- douze cintres (IKEA)- vase- calendrier mural. paillasson- réveil cafetière- radio- sac à ménage-aspirateur- balai à lingette- boite à outils- Télévision - vidéoprojecteur- ordinateur portable- téléphone portable - IPHONE - ANDROID-sac fourre-tout- sac de jour-valise- agenda à anneaux- coffret de correspondance (le crayon,...)- classeur accordeon- bac de classement en bois-"

liste=[]
debut =0
fin=0
compteur=0
for c in objets:
    if c=='-':
        fin = compteur
        liste.append(objets[debut:fin])
        debut=compteur+1
    compteur+=1


url_base="https://www.amazon.fr/s?k="
url_list =[]

for item in liste:
    for i in range(7):
        url_list.append(url_base+item+"#pa="+str(i+1))

#SCRAPING

compteur_objets=0
page_courante=1


for url in url_list:
    response = requests.get(url)

    soup=BeautifulSoup(response.content, "html.parser")

    #print(soup.prettify())

    images = soup.find_all("img")
    # , {"class" : "s-image"}
    number = 1
    
    for image in images :
        filename=liste[compteur_objets]+"_page"+str(page_courante)+"_"+str(number)
        image_src=image["src"]
        urllib.request.urlretrieve(image_src, filename)
        print(filename)
        number+=1
        
    page_courante+=1
    
    if page_courante==8:
        page_courante=1
        compteur_objets+=1