from playwright.sync_api import Page
from utils.config import LEGO_BASE_URL, LEGO_LOGIN_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def load_welcome(self):
        self.page.goto(LEGO_BASE_URL)

    def click_continue(self):
        self.page.get_by_role("button", name="Continue", exact=True).click()

    def accept_cookies(self):
        self.page.get_by_role("button", name="Accept All").click()

    def load_login(self):
        self.page.goto(LEGO_LOGIN_URL)

    def navigate_to_login(self):
        self.load_welcome()
        self.click_continue()
        self.accept_cookies()
        self.click_sign_in()
        self.click_modal_sign_in()

    def enter_email(self, email: str):
        self.page.get_by_role("textbox", name="Email or username").first.fill(email)

    def enter_password(self, password: str):
        self.page.locator('input[type="password"]').fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").first.click()

    def click_modal_sign_in(self):
        self.page.locator("dialog[open]").get_by_text("Sign In", exact=True).click()
    
    def click_forgot_username(self):
        self.page.get_by_role("link", name="Forgot your username?").click()

    def click_forgot_password(self):
        self.page.get_by_role("link", name="Forgot your password?").click()

    def click_modal_create_account(self):
        self.page.locator("dialog[open]").get_by_text("Become a member", exact=True).click()

    def navigate_to_create_account(self):
        self.load_welcome()
        self.click_continue()
        self.accept_cookies()
        self.click_sign_in()
        self.click_modal_create_account()

    def open_country_dropdown(self):
        country = self.page.get_by_test_id("country")
        country.focus()
        country.press("Space")

    def select_country(self, country: str):
        self.page.get_by_role("button", name=country).click()

    def open_state_dropdown(self):
        state = self.page.get_by_test_id("countrySubdivision")
        state.focus()
        state.press("Space")

    def select_state(self, state: str):
        self.page.get_by_role("option", name=state).click()

    def enter_birth_day(self, day: str):
        self.page.get_by_test_id("dob-day").fill(day)

    def enter_birth_month(self, month: str):
        self.page.get_by_test_id("dob-month").fill(month)

    def enter_birth_year(self, year: str):
        self.page.get_by_test_id("dob-year").fill(year)

    
