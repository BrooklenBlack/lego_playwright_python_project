from playwright.sync_api import Page
from pages.login import LoginPage

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(self.page)

    def click_shop(self):
        self.page.get_by_role("button", name="Shop").first.click()

    def navigate_to_product_lists(self):
        self.login_page.navigate_past_banner()
        self.click_shop()

    def click_sets_by_theme(self):
        self.page.get_by_role("button", name="Sets by theme").click()

    def click_botanicals(self):
        self.page.get_by_role("link", name="Botanicals").click()
    
    def click_harry_potter(self):
        self.page.get_by_role("link", name="Harry Potter™").click()
    
    def click_technic(self):
        self.page.get_by_role("link", name="Technic").click()

    def click_lego_icons(self):
        self.page.get_by_role("link", name="LEGO® Icons").click()

    def click_sets_by_age(self):
        self.page.get_by_role("button", name="Age").click()

    def click_see_all_ages(self):
        self.page.get_by_text("SEE ALL AGES", exact=True).click()

    def click_ages(self, age: str):
        self.page.get_by_role("link", name=age).click()
        
    def click_new(self):
        self.page.locator('[data-test="navigation-submenu-link"]').filter(has_text="New").click()

    def click_retiring_soon(self):
        self.page.get_by_role("link", name="Retiring soon").click()

    """ def click_search(self):
        self.page.locator('[data-test="search-input-button"]').last.click() """