import os


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"