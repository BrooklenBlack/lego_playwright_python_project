from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_product_quantity(self, product_name: str):
        return self.page.get_by_label(f"Quantity, {product_name}").last

    def get_product_name(self):
        return self.page.locator('[data-test="product-title"]').last

    def remove_product(self):
        return self.page.locator('[data-test="remove-from-cart"]').last.click()

