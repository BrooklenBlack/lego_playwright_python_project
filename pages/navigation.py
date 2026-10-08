from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page
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

    def click_view_all_themes(self):
        self.page.get_by_role("link", name="View Sets by theme").click()

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
        self.page.get_by_role("link", name="SEE ALL AGES").click()

    def click_ages(self, age: str):
        return self.page.locator('[data-navigation-section-id="blt0ea34b527fb8f037"]').get_by_role("link", name=age)
        
    def click_new(self):
        self.page.get_by_role("toolbar").get_by_role("link", name="New").click()

    def click_retiring_soon(self):
        self.page.get_by_role("link", name="Retiring soon").click()

    def click_search(self, search_term: str):
        search = self.page.get_by_role("combobox", name="Search")
        search.wait_for()
        search.click()
        search.fill(search_term)
        search.press("Enter")

