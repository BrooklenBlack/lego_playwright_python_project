
import re
from pages.login import LoginPage
from playwright.sync_api import Page, expect
from utils.config import LEGO_BASE_URL, LEGO_LOGIN_URL, LEGO_EMAIL, LEGO_PASSWORD

def test_welcome_banner_loads(page):
    login_page = LoginPage(page)
    login_page.load_welcome()

    expect(page.get_by_role("heading", name="THE PLAY ZONE")).to_be_visible()


def test_continuing_after_banner(page):
    login_page = LoginPage(page)
    login_page.load_welcome()
    login_page.click_continue()
    login_page.accept_cookies()

    page.wait_for_load_state("networkidle")
    print(page.url)

    expect(page).to_have_url(LEGO_BASE_URL)

def test_login_page_loads(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    expect(page).to_have_url(re.compile(f"{LEGO_LOGIN_URL}.*"))

def test_login_page_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    login_page.enter_email(LEGO_EMAIL)
    login_page.click_continue()

    login_page.enter_password(LEGO_PASSWORD)
    login_page.click_sign_in()

    expect(page).to_have_url(
        re.compile(r".*identity\.lego\.com.*")
    ) #avoiding the MFA

def test_login_page_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    login_page.enter_email("FakeEmail@gmail.com")
    login_page.click_continue()

    login_page.enter_password("FakePassword")
    login_page.click_sign_in()

    expect(page.get_by_text("Wrong username or password.")).to_be_visible()
    assert "login" in page.url.lower()

def test_login_page_with_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    login_page.enter_email(LEGO_EMAIL)
    login_page.click_continue()

    login_page.enter_password("")
    login_page.click_sign_in()

    expect(page.get_by_text("Required field is not valid")).to_be_visible()
    assert "login" in page.url.lower()


def test_forgot_username_link(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    login_page.click_forgot_username()
    expect(page.get_by_text("Forgot your username?")).to_be_visible()
    assert("forgot-username" in page.url.lower()) 

def test_forgot_password_link(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    login_page.enter_email(LEGO_EMAIL)
    login_page.click_continue()

    login_page.click_forgot_password()
    expect(page.get_by_text("Forgot your password?")).to_be_visible()
    assert("forgot-password" in page.url.lower())

def test_login_page_with_Apple(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    page.get_by_role("button", name="Continue with Apple").click()
    expect(page).to_have_url(re.compile(r".*appleid\.apple\.com.*")) #avoiding the MFA and just testing that it loads the Apple login page