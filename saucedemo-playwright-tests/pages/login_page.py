import pytest
from playwright.sync_api import Page

URL_SITE = "https://www.saucedemo.com/"

class LoginPage: # on définit l'emplacement des éléments qui nous intéressent
    def __init__(self, page:Page) -> None:
        self.page = page
        self.champ_identifiant = page.locator('[data-test="username"]')
        self.champ_mot_de_passe = page.locator('[data-test="password"]')
        self.bouton_connexion = page.locator('[data-test="login-button"]')
        self.message_erreur = page.locator('[data-test="error"]')

    
    def ouvrir(self)-> None:
        self.page.goto(URL_SITE)

    def connexion(self, identifiant: str = "standard_user", mot_de_passe: str= "secret_sauce") -> None:
        self.champ_identifiant.fill(identifiant)
        self.champ_mot_de_passe.fill(mot_de_passe)
        self.bouton_connexion.click()

class Basket:
    def __init__(self, page: Page):

 page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.get_by_text("Sauce Labs Backpackcarry.").click()

    
class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.champ_prenom = page.locator('[data-test="firstName"]')
        self.champ_nomDeFamille = page.locator('[data-test="lastName"]')
        self.champ_codePostale = page.locator('[data-test="postalCode"]')
        self.bouton_continuer = page.locator('[data-test="continue"]')
        self.bouton_finir = page.locator('[data-test="finish"]')

    def paiement(self, prenom: str = "Jeanne", nomDeFamille = "Martin", codePostale = "35000"):
        self.champ_prenom.fill(prenom)
        self.champ_nomDeFamille.fill(nomDeFamille)
        self.champ_codePostale.fill(codePostale)
        self.bouton_continuer.click()