from pages.navigation import NavigationPage
from pages.product import ProductPage
from pages.cart import CartPage
from pages.login import LoginPage
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

def test_product_search(page):
    navigation = NavigationPage(page)

    navigation.login_page.navigate_past_banner()
    navigation.click_search("Rivendell")
   
    expect(page.locator('[data-test="search-input-field"]')).to_have_value("Rivendell")

def test_product_search_navigates_to_product(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)

    navigation.login_page.navigate_past_banner()
    navigation.click_search("Rivendell")

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    expect(page).to_have_url("https://www.lego.com/en-us/product/the-lord-of-the-rings-rivendell-10316")


def test_add_product_to_cart(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)    

    navigation.login_page.navigate_past_banner()
    navigation.click_search("Rivendell")

    navigation.login_page.close_survey()

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    product_page.click_add_to_bag()
    product_page.click_view_my_bag()

    expect(cart_page.get_product_quantity("THE LORD OF THE RINGS: RIVENDELL™")).to_have_value("1")

def test_correct_product_added_to_cart(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    navigation.login_page.navigate_past_banner()
    navigation.click_search("Rivendell")

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    navigation.login_page.close_survey()

    product_page.click_add_to_bag()
    product_page.click_view_my_bag()

    expect(cart_page.get_product_name()).to_have_text("THE LORD OF THE RINGS: RIVENDELL™")

def test_remove_product_from_cart(page):
    navigation = NavigationPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    navigation.login_page.navigate_past_banner()
    navigation.click_search("Rivendell")

    product_page.find_product("THE LORD OF THE RINGS: RIVENDELL™")
    product_page.click_product("THE LORD OF THE RINGS: RIVENDELL™")

    product_page.click_add_to_bag()
    product_page.click_view_my_bag()

    cart_page.remove_product()

    expect(page.locator("h1").filter(has_text="You don't have anything in your bag")).to_be_visible()