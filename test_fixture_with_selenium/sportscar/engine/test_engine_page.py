from pytest import mark

@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get("https://www.amazon.com")
    assert True
