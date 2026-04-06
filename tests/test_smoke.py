def test_homepage(page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()