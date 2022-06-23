from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    button = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form"))
    assert button > 0, "Кнопка корзины не найдена"
    time.sleep(5)
