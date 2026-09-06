from pages.navigation import NavigationPage
from playwright.sync_api import expect


def test_sets_by_theme_menu_opens(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    expect(page.get_by_text("Sets by theme")).to_be_visible()

def test_shop_menu_displays_sets_by_theme(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()

    expect(page.get_by_text("SEE ALL THEMES")).to_be_visible()

def test_navigates_to_botanicals_theme(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()
    navigation.click_botanicals()

    expect(page.get_by_role("heading", name="LEGO® Flower and Plant Gifts")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/botanicals")

def test_navigates_to_harry_potter_theme(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()
    navigation.click_harry_potter()

    expect(page.get_by_role("heading", name="Harry Potter™ Toys and Gifts")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/harry-potter")

def test_navigates_to_technic_theme(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_theme()
    navigation.click_technic()

    expect(page.get_by_role("heading", name="LEGO® Technic Toys and Sets")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/themes/technic")

def test_shop_menu_navigates_to_age_ranges(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_age()

    expect(page.get_by_text("SEE ALL AGES")).to_be_visible()

def test_shop_menu_navigates_to_ages_six_plus(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_age()
    navigation.click_ages("6+")
    
    expect(page.get_by_role("heading", name="Gifts and Toys for 6, 7 and 8 Year Olds")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/age/6-plus-years")

def test_shop_menu_navigates_to_ages_eighteen_plus(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_age()
    navigation.click_ages("18+")

    expect(page.get_by_role("heading", name="LEGO® Gifts and Collectibles for Adults")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/age/18-plus-years")

def test_shop_menu_navigates_to_all_ages(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_sets_by_age()   
    navigation.click_ages("All Ages")

    expect(page.get_by_role("heading", name="Age")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/age")

def test_shop_menu_navigates_to_new_products(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_new()

    expect(page.get_by_role("heading", name="New LEGO® sets and toys")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/categories/new-sets-and-products")

def test_shop_menu_navigates_to_retiring_soon(page):
    navigation = NavigationPage(page)
    navigation.navigate_to_product_lists()

    navigation.click_retiring_soon()

    expect(page.get_by_role("heading", name="LEGO Sets Retiring Soon")).to_be_visible()
    expect(page).to_have_url("https://www.lego.com/en-us/categories/last-chance-to-buy")