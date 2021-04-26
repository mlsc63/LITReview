#                                                                          LITReview



LITReview a comme objectif est de commercialiser un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.
IL est possible de suivre des utilisateurs, d'ajouter une critique sur une demande d'ami. 
La base de données est gérée par sqlite, un superuser est déjà crée :
-user Openclassrooms
-pwd openclassrooms

# Points de teminaison

- `follow/add/<int:follow_id_add>` Ajout d'un ami avec son ID
- `follow/del/<int:follow_id_del>` Supprime un ami avec son ID
- `follow/` Liste des follows
- `ticket/` Ajout d'un ticket
- `ticket/edit/<int:ticket_id_edit>` Modifie un ticket avec son ID
- `ticket/del/<int:ticket_id_del>` Supprime un ticket avec son ID
- `review/` Ajout d'une review
- `review/edit/<int:review_id_edit>` Modifie une review avec son ID
- `review/add/<int:review_id_add>` Ajout d'une review en réponse d'un ticket
- `review/del/<int:review_id_del>`Supprime une review
- `account/login/` 
- `account/signup/`
- `account/logout/`



# Installation

1) Avec CMD, placez-vous dans votre dossier
2) Créez un environnement avec la commande : python -m venv env
3) Activez votre environnement avec la commande : env\Scripts\activate
4) Installez les paquets avec la commande : pip install -r requirements.txt
5) Démarrage du serveur: manage.py runserver.


 
    


# English 

LITReview's objective is to market a product allowing a community of users to consult or request a book review on demand.
It is possible to follow users, to assign a review on a friend request.
The database is managed by sqlite, a superuser is already created:

# Endpoint

- `follow/add/<int:follow_id_add>`Add a friend with ID
- `follow/del/<int:follow_id_del>` Del a friend with ID
- `follow/` List of follows
- `ticket/` Add a ticket
- `ticket/edit/<int:ticket_id_edit>` Edit a ticket with ID
- `ticket/del/<int:ticket_id_del>` Del a ticket with ID
- `review/` Add a review
- `review/edit/<int:review_id_edit>` Edit a rieview with ID
- `review/add/<int:review_id_add>` Adding a review in response to a ticket
- `review/del/<int:review_id_del>`Del a review with ID
- `account/login/` 
- `account/signup/`
- `account/logout/`

# Installation

1) With CMD, go to your file
2) Create an environment with the command: python -m venv env
3) Activate your environment with the command: env\Scripts\activate
4) Install the packages with the command: pip install -r requirements.txt
5) Server startup: manage.py runserver.
