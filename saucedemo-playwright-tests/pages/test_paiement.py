from pages.login_page import LoginPage

from pages.login_page import PaymentPage

from playwright.sync_api import Page, expect

def test_paiement_normale(page: Page):
    login = LoginPage(page)
    login.connexion()

    paiement = PaymentPage(page)
    paiement.paiement()

    page.locator('[data-test="finish"]').click()
    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

