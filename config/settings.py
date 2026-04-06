import os


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1440"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "900"))