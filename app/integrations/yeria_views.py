from yeriasdk import YeriaUI

def home_view():

    view = (
        YeriaUI.create_action_list_view("id-menu", "Menu", "Gérer vos opérations ici")
        .add_action(
            "available-products",
            "Liste des produits",
            "Voir la liste des produits disponibles"
        )
        
        .add_action(
            "available-promotions",
            "Liste des promotions",
            "Voir la liste des promotions actuelles"
        )
        
        .add_action(
            "search",
            "Recherche",
            "Trouver un produit particulier"
        )
        
        .add_action(
            "mapping",
            "Recherche de proximité",
            "Trouver une boutique proche de vous"
        )
        
        .add_action(
            "order-history",
            "Historique de commande",
            "Liste de vos précédentes commandes ou réservations"
        )
        
        .add_action(
            "manage",
            "Gestion de commerce",
            "Gérer votre commerce"
        )
    )

    return view

def available_products_view():

    view = (
        YeriaUI.create_action_grid_view(
            "id-produits",
            "Liste des produits",
            "Voici la liste des produits disponibles"
        )
        .set_columns(1)
        .add_action(
            "produit-1",
            "Pain",
            "Détails sur le produit",
            "https://images.unsplash.com/photo-1598373182133-52452f7691ef?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )

        .add_action(
            "produit-2",
            "Lait",
            "Détails sur le produit",
            ""
        )

        .add_action(
            "produit-3",
            "Jus",
            "Détails sur le produit",
            "https://images.unsplash.com/photo-1598373182133-52452f7691ef?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )
    )
    return view

def available_promotion_view():

    view = (
        YeriaUI.create_carousel_view("promotion-available", "Les promotions disponibles")
        .add_slide(
            slide=[
                
            ]
        )
    )

    return view

def search_view():
    view = (
        YeriaUI.create_form_view(
            "id-search",
            "Recherche",
            "Vous pouvez chercher un produit particulier"
        )

        .add_text_field(
            "product_name",
            "Saisir du nom"
        )
        .secondary_button(
            "Rechercher",
            "/search-results",
            "navigate",
            "GET"
        )
    )

    return view

def search_results_view():

    view = (
        YeriaUI.create_action_grid_view(
            "id-search-results",
            "Résultats de recherche",
            "Produits correspondant à votre recherche"
        )

        .add_action(
            "result-1",
            "Pain",
            "Détails sur le produit",
            "https://example.com/images/pain.jpg"
        )

        .add_action(
            "result-2",
            "Lait",
            "Détails sur le produit",
            "https://example.com/images/lait.jpg"
        )

        .add_action(
            "result-3",
            "Jus",
            "Détails sur le produit",
            "https://example.com/images/jus.jpg"
        )
    )

    return view


def product_details_view():
    view = (
        YeriaUI.create_reader_view('product-info', 'Détails du produit')
            .set_intro("Informations détaillées sur ce produit")
            .add_image(
                'https://images.unsplash.com/photo-1598373182133-52452f7691ef?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'Image du produit',
                'Image du produit'
            )
            .add_paragraph('Pain frais disponible dans notre boutique.')
            .add_subtitle('Informations')
            .add_list_field([
                'Nom : Pain',
                'Unité : 1000FCFA',
                'Boutique : Boutique Chez Koffi',
                'Adresse : Lomé, Tokoin'
            ])
    )

    return view

def promotion_details_view():
    view = (
        YeriaUI.create_reader_view('promotion-info', 'Détails de la promotion')
        .set_intro('Informations détaillées sur cette promotion')
        .add_image(
            'https://example.com/promotion.jpg',
            'Image de la promotion',
            'Image du produit en promotion'
        )
        .add_paragraph('Profitez de cette offre à prix réduit pendant la période indiquée.')
        .add_subtitle('Informations sur la promotion')
        .add_list_field([
            'Produit : Pain',
            'Prix initial : 500 FCFA',
            'Prix réduit : 350 FCFA',
            'Réduction : 30 %',
            'Quantité disponible : 20',
            'Date de début : 05/10/2026',
            'Date de fin : 06/10/2026',
            'Boutique : Boutique Chez Koffi'
        ])
    )

    return view

def store_management_view():
    view = (
        YeriaUI.create_action_list_view(
            "store-management",
            "Gestion de commerce"
        )
        .add_action(
            "add-product",
            "Ajout des produits",
            "Ajouter vos produits disponibles"
        )
        .add_action(
            "my-products",
            "Liste des produits",
            "Consulter la liste de vos produits ajoutés"
        )
        .add_action(
            "create-promotion",
            "Création de promotion",
            "Mettre en ligne les promotions"
        )
        .add_action(
            "my-promotions",
            "Liste des promotions",
            "Consulter la liste de vos promotions ajoutées"
        )
    )

    return view

def create_business_view():
    view = (
        YeriaUI.create_form_view(
            "create-store",
            "Création d'un commerce"
        )
        .set_intro(
            "Renseignez les informations de votre commerce"
        )

        # Informations générales
        .add_text_field(
            "nom",
            "Nom du commerce",
            "Saisissez le nom de votre commerce"
        )

        .add_text_field(
            "description",
            "Description",
            "Décrivez brièvement votre commerce"
        )

        # Catégorie
       
        # Informations de contact
        .add_text_field(
            "telephone",
            "Téléphone",
            "Numéro de téléphone du commerce"
        )

        .add_text_field(
            "adresse",
            "Adresse",
            "Adresse du commerce"
        )

        # Localisation
        .add_text_field(
            "latitude",
            "Latitude",
            "Latitude de votre commerce"
        )

        .add_text_field(
            "longitude",
            "Longitude",
            "Longitude de votre commerce"
        )

        .submit_button(
            "Créer"
            "POST"
        )
    )

    return view