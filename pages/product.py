from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

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

    def get_product_image(self):
        return self.page.locator('[data-test="mediagallery-image-0"]')

    def get_product_price(self):
        return self.page.locator('[data-test="product-price-display-price"]').first

    

