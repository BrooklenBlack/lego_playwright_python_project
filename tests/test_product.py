from pages.navigation import NavigationPage
from pages.product import ProductPage
from playwright.sync_api import expect


def test_new_page_loads_more_products(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.navigate_to_product_lists()
    navigation.click_new()

    product_page.scroll_to_load_more()
    product_page.click_load_more()

    expect(page).to_have_url("https://www.lego.com/en-us/categories/new-sets-and-products?page=2")

def test_new_product_navigation_after_loading_more(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.navigate_to_product_lists()
    navigation.click_new()

    product_page.scroll_to_load_more()
    product_page.click_load_more()

    product_page.find_product("Jaguar E-Type")
    product_page.click_product("Jaguar E-Type")

    expect(page).to_have_url("https://www.lego.com/en-us/product/jaguar-e-type-11381")
    expect(page.locator('[data-test="product-overview-name"]')).to_have_text("Jaguar E-Type")

def test_shop_menu_navigates_to_retiring_soon_product(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.navigate_to_product_lists()

    navigation.click_retiring_soon()
    product_page.find_product("Fawkes™: Dumbledore's Phoenix")
    product_page.click_product("Fawkes™: Dumbledore's Phoenix")

    expect(page).to_have_url("https://www.lego.com/en-us/product/fawkes-dumbledores-phoenix-76448")

def test_product_image_is_visible(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()
    navigation.click_lego_icons()

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    expect(product_page.get_product_image()).to_be_visible()

def test_product_price_is_visible(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()
    navigation.click_lego_icons()

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    expect(product_page.get_product_price()).to_be_visible()

""" def test_product_search_clicks(page):
    navigation = NavigationPage(page)

    navigation.login_page.navigate_past_banner()
    navigation.click_search()

    expect(page.locator('[data-test="search-input-button"]')).to_be_focused() """



