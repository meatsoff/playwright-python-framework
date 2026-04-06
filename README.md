# Playwright Python Framework

A production-style UI automation testing framework built with **Python + Playwright + Pytest** using **Page Object Model (POM)** and CI integration via **GitHub Actions**.

---

## Tech Stack

- Python 3.11+
- Playwright
- Pytest
- Pytest HTML Report
- GitHub Actions
- Page Object Model (POM)

---

## CI/CD

This project includes GitHub Actions workflow that:

- Installs Python dependencies
- Installs Playwright browsers
- Runs test suite in headless mode
- Uploads HTML report as artifact
- Uploads failure screenshots as artifact

---

# Local Setup

## 1. Clone repo

git clone [https://github.com/meatsoff/playwright-python-framework.git](https://github.com/YOUR_USERNAME/playwright-python-framework.git)  
cd playwright-python-framework

## 2. Create virtual environment

python -m venv .venv

## 3. Activate virtual environment

Windows PowerShell -> .venv\Scripts\Activate.ps1
Windows CMD -> .venv\Scripts\activate.bat

## 4. Install dependencies

pip install -r requirements.txt
python -m playwright install

## 5. Run Tests

Default -> pytest
Headless mode -> $env:HEADLESS="true"; pytest
Run on Firefox -> $env:BROWSER="firefox"; pytest
Run on WebKit -> $env:BROWSER="webkit"; pytest

---

## Project Structure

```bash
playwright-python-framework/
├── .github/workflows/         # CI/CD workflows
├── config/                    # Environment settings
├── core/                      # Reserved for future shared core modules
├── data/                      # Test data
├── pages/                     # Page Objects
├── tests/                     # Test cases
├── utils/                     # Logger and helpers
├── reports/                   # HTML reports
├── screenshots/               # Failure screenshots
├── conftest.py                # Fixtures and hooks
├── pytest.ini                 # Pytest config
├── requirements.txt           # Dependencies
└── README.md
```

