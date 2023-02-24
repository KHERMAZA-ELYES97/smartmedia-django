Django Smartmedia Flower (A modifier après)

Le fichier.env ne doit pas etre comitté et on doit le mentionner dans le gitignore 

Fonctionnement:
L'interface permet à l'utilisateur l'ajout de produit (Flower seulement pour le cas d'usage) 

pour avoir accès à l'interface cliquer sur : nom_du_domaine:8000/admin


Les identifiants de l'interface Django

Username: smartmedia
password: citc

Ensuite on clique sur products et après add product

Le formulaire contient les champs suivants:
{
    "Flower id": "",
    "Identité": "",
    "Entretien": "",
    "Floraison": "",
    "Remarques": "",
	"img1": "",
    "img2": "",
}


Pour voir le contenu de la base de données: nom_du_domaine:8000/product_info

Le format des données est le suivant:
{
    "tag": "",
    "text1": "",
    "text2": "",
    "text3": "",
    "text4": "",
	"img1": "",
    "img2": "",
	"img1_checksum": "",
	"img2_checksum": "",
}


A ne pas oublier après avoir choisi le nom de domaine rajouter un truc qui permet de spécifier qu'on donne accès à lui sur l'interface
A voir si çà se fait juste sur le fichier settings.py

"""ALLOWED_HOSTS=127.0.0.1"""

A ne pas oublier d'enlever dans le caddyfile http:// pour que caddy génères les certificats





