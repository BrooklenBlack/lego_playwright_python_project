from pages.product import ProductPage
from playwright.sync_api import expect


def test_shop_menu_opens(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    expect(page.get_by_text("Sets by theme")).to_be_visible()

def test_shop_menu_navigates_to_set_themes(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_sets_by_theme()

    expect(page.get_by_text("SEE ALL THEMES")).to_be_visible()

def test_shop_menu_navigates_to_botanicals(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_sets_by_theme()
    product_page.click_botanicals()

    expect(page.get_by_role("Heading", name="LEGO® Flower and Plant Gifts")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/botanicals")

def test_shop_menu_navigates_to_harry_potter(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_sets_by_theme()
    product_page.click_harry_potter()

    expect(page.get_by_role("Heading", name="Harry Potter™ Toys and Gifts")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/harry-potter")

def test_shop_menu_navigates_to_technic(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_sets_by_theme()
    product_page.click_technic()

    expect(page.get_by_role("Heading", name="LEGO® Technic Toys and Sets")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/technic")

def test_shop_menu_navigates_to_set_ages(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_sets_by_age()

    expect(page.get_by_text("SEE ALL AGES")).to_be_visible()

def test_shop_menu_navigates_to_new(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_new()

    expect(page.get_by_role("Heading", name="New LEGO® sets and toys")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/categories/new-sets-and-products")

def test_new_page_loads_more_products(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()
    product_page.click_new()

    product_page.scroll_to_load_more()
    product_page.click_load_more()

    expect(page).to_have_url("https://www.lego.com/en-us/categories/new-sets-and-products?page=2")

def test_shop_menu_navigates_to_product(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()
    product_page.click_new()

    product_page.scroll_to_load_more()
    product_page.click_load_more()

    product_page.find_product("Kakamora")
    product_page.click_product("Kakamora")

    expect(page).to_have_url("https://www.lego.com/en-us/product/kakamora-43293")

def test_shop_menu_navigates_to_retiring_soon(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_retiring_soon()

    expect(page.get_by_role("Heading", name="LEGO Sets Retiring Soon")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/categories/last-chance-to-buy")

def test_shop_menu_navigates_to_retiring_soon_product(page):
    product_page = ProductPage(page)
    product_page.navigate_to_product_lists()

    product_page.click_retiring_soon()
    product_page.find_product("Fawkes™: Dumbledore's Phoenix")
    product_page.click_product("Fawkes™: Dumbledore's Phoenix")

    expect(page).to_have_url("https://www.lego.com/en-us/product/fawkes-dumbledores-phoenix-76448")