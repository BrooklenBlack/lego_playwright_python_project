from tkinter import dialog

from playwright.sync_api import Page
from utils.config import LEGO_BASE_URL

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
    
    def load_welcome(self):
        self.page.goto(f"{LEGO_BASE_URL}")

    def click_continue(self):
        self.page.get_by_role("button", name="Continue", exact=True).click()

    def accept_cookies(self):
        self.page.get_by_role("button", name="Accept All").click()

    def load_login(self):
        self.page.goto(f"{LEGO_BASE_URL}/login")

    def navigate_to_login(self):
        self.load_welcome()
        self.click_continue()
        self.accept_cookies()
        self.click_sign_in()
        self.click_modal_sign_in()

    def enter_email(self, email:str):
        self.page.get_by_role("textbox", name="Email or username").first.fill(email)

    def enter_password(self, password:str):
        self.page.locator('input[type="password"]').fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").first.click()

    def click_modal_sign_in(self):
        self.page.locator("dialog[open]").get_by_text("Sign In", exact=True).click()
    
    def click_forgot_username(self):
        self.page.get_by_role("link", name="Forgot your username?").click()

    def click_forgot_password(self):
        self.page.get_by_role("link", name="Forgot your password?").click()

    def create_account(self):
        self.page.get_by_role("link", name="Become a member").click()

    def open_country_dropdown(self):
        self.page.locator(".country-search-input").click()

    def click_country(self, country:str):
        option = self.page.get_by_role("", has_text=country).first
        option.scroll_into_view_if_needed()
        option.click

    

    
