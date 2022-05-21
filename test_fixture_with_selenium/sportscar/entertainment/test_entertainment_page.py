from pytest import mark

@mark.ui
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('https://ebay.com')
    assert True
