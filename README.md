# LEGO Playwright Test Automation Project

This project is a Playwright test automation framework built with Python and pytest to automate and validate LEGO website workflows.

The goal of this project was to practice UI automation, Page Object Model design, test case development, and validating different user scenarios across authentication, account creation, navigation, product search, product pages, and shopping cart functionality.

## Tech Stack

* Python
* Playwright
* pytest
* python-dotenv

## Test Coverage

The test suite covers:

### Authentication

* Welcome page loads successfully
* User can continue past the welcome banner
* Login page loads successfully
* Successful login with valid credentials
* Invalid credentials validation
* Empty password validation
* Forgot username navigation
* Forgot password navigation
* Apple authentication redirect

### Account Creation

* Create account page loads successfully
* Country selection
* State selection
* Birthday field entry
* Create account flow navigation

### Navigation

* Shop menu navigation
* Sets by theme navigation
* Sets by age navigation
* New products navigation
* Retiring soon navigation
* Search functionality

### Product

* Product search
* Product selection
* Load more products
* Product page navigation
* Add product to shopping cart

### Shopping Cart

* Verify the correct product is added to the cart
* Remove product from cart

## Project Structure

```text
lego_playwright_python_project/
├── pages/
│   ├── login.py
│   ├── navigation.py
│   ├── product.py
│   └── cart.py
├── tests/
│   ├── test_login.py
│   ├── test_navigation.py
│   └── test_product.py
├── utils/
│   └── config.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/BrooklenBlack/lego_playwright_python_project.git
cd lego_playwright_python_project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```bash
python -m playwright install
```

## Environment Variables

Create a `.env` file in the root of the project using `.env.example` as a guide.

Example:

```env
LEGO_EMAIL=
LEGO_PASSWORD=
LEGO_BASE_URL=https://www.lego.com/en-us
LEGO_LOGIN_URL=https://identity.lego.com/en-US/login
```

Credentials are stored using environment variables and should not be committed to GitHub.

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run tests with the browser visible:

```bash
python -m pytest --headed --slowmo 500
```

## Running in Visual Studio Code (Optional)

1. Open the project folder in Visual Studio Code.
2. Install the Python extension.
3. Select the project virtual environment:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

4. Choose the `.venv` interpreter.
5. Run tests from the terminal:

```bash
python -m pytest
```

## Notes

* This project uses the Page Object Model (POM) to separate page interactions from test logic.
* Credentials are handled through environment variables and excluded from version control.
* The framework uses Playwright locators based on roles, test IDs, and other stable page attributes.
* The tests cover workflows across LEGO's live website, so website changes may require locator or test updates.
* Successful login testing validates navigation to the LEGO identity service because the authentication flow includes MFA.

## Future Work

Planned additions to expand test coverage and improve the framework:

* Improve test stability and reduce flaky test behavior
* Improve test isolation and state management for repeated test executions
* Add additional account creation validation scenarios
* Add more negative test cases for user inputs
* Expand shopping cart coverage
* Add checkout flow testing up to the payment step
* Add CI/CD integration using GitHub Actions
* Add additional reporting and test artifacts
* Survey pop up closure 

