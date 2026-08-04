# LEGO Login Test Automation Project

This project is a Playwright test automation framework built with Python and pytest to test the LEGO authentication and account creation flows.

The goal of this project was to practice UI automation, Page Object Model design, and validating different user scenarios including successful login, negative login cases, and account creation navigation.

## Tech Stack

- Python
- Playwright
- pytest
- python-dotenv

## Test Coverage

The test suite covers:

- Welcome page loads successfully
- User can continue past the welcome banner
- Login page loads successfully
- User can log in with valid credentials
- Invalid credentials show an error message
- Empty password validation
- Forgot username navigation
- Forgot password navigation
- Apple authentication redirect
- Create account page loads successfully
- Country selection
- State selection
- Birthday field entry
- Create account flow navigation

## Project Structure

```
lego_playwright_project/
├── pages/
│   └── login.py
├── tests/
│   └── test_login.py
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

```
Ctrl + Shift + P
Python: Select Interpreter
```

4. Choose the `.venv` interpreter.
5. Run tests from the terminal:

```bash
python -m pytest
```

## Notes

- This project uses the Page Object Model (POM) to separate page interactions from test logic.
- Credentials are handled through environment variables and excluded from version control.
- The framework handles dynamic web components including modal dialogs and custom dropdown menus.
- Successful login testing validates navigation to the LEGO identity service because the authentication flow includes MFA.
