from playwright.sync_api import Page
from pages.login import LoginPage

class ProductPage:
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

    def click_sets_by_age(self):
        self.page.get_by_role("button", name="Age").click()

    def click_new(self):
        self.page.get_by_role("link", name="New").nth(1).click()

    def scroll_to_load_more(self):
        self.page.get_by_role("link", name="Load More").scroll_into_view_if_needed()

    def click_load_more(self):
        self.page.get_by_role("link", name="Load More").click()

    def find_product(self, product_name: str):
        product = self.page.locator('[data-test="product-leaf-title"]').filter(has_text=product_name)
        product.scroll_into_view_if_needed()
        return product

    def click_product(self, product_name: str):
        self.find_product(product_name).click()

    def click_retiring_soon(self):
        self.page.get_by_role("link", name="Retiring soon").click()


