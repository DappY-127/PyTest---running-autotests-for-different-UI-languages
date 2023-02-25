from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_present(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    # Check if there is an add-to-cart button
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_cart_button.is_displayed()
    # Comment on the "print" below and add the "-s" mark 
    # when running the tests to see and compare the name of the add to cart button in different localizations
    # print(add_to_cart_button.text)