from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

MESSAGE_IDENTIFIANTS_INCORRECTS = (
    "Username and password do not match any user in this service"
)

def test_connexion_normale(page: Page):
    login = LoginPage(page) # créer un objet LoginPage en lui donnant l'onglet du navig
    login.connexion() # appeller la méthode connexion dessus
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()

# rempli mais mauvais saisis
def test_connexion_mauvais_utilisateur(page: Page):
    login = LoginPage(page)
    login.connexion(identifiant="standard", mot_de_passe = "secret_sauce")
    expect(page.locator('[data-test="error"]')).to_contain_text(MESSAGE_IDENTIFIANTS_INCORRECTS)

def test_connexion_mdp_faux(page: Page):
    login = LoginPage(page)
    login.connexion(identifiant="standard_user", mot_de_passe = "secret")
    expect(page.locator('[data-test="error"]')).to_contain_text(MESSAGE_IDENTIFIANTS_INCORRECTS)
    # message erreur mot de passe

# saisis vides

def test_saisi_vide(page: Page):
    login = LoginPage(page)
    login.connexion(identifiant="", mot_de_passe = "")
    expect(page.locator('[data-test="error"]')).to_contain_text("Username is required")

def test_utilisateur_vide(page: Page):
    login = LoginPage(page)
    login.connexion(identifiant="", mot_de_passe = "secret")
    expect(page.locator('[data-test="error"]')).to_contain_text("Username is required")

def test_utilisateur_vide(page: Page):
    login = LoginPage(page)
    login.connexion(identifiant="standard_user", mot_de_passe = "")
    expect(page.locator('[data-test="error"]')).to_contain_text("Password is required")
