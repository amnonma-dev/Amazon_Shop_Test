import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    autoGrantPermissions='true',
    appPackage='com.amazon.mShop.android.shopping',
    appActivity='com.amazon.mShop.home.HomeActivity',
    noReset='true',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class CartTest:

    def test_empty_cart_items(web_driver):
        bottom_buttons = web_driver.find_elements(by=AppiumBy.XPATH,
                                                  value='//android.widget.ImageView[@resource-id='
                                                        '\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"]')
        buttons_count = len(bottom_buttons)
        if buttons_count not in (4, 5):
            pytest.fail("tab buttons count mismatch")
        if buttons_count == 4:
            cart_index = 3
        else:
            cart_index = 4
        cart_tab_button = WebDriverWait(web_driver, 20).until(expected_conditions.
                                                              presence_of_element_located((By.XPATH,
                                                                                           '(//android.widget.ImageView[@resource-id='
                                                                                           '\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])['
                                                                                           + str(cart_index) + ']')))
        cart_tab_button.click()
        cart_empty_text = None
        try:
            cart_empty_text = WebDriverWait(web_driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//android.widget.TextView[@text=\"Your Amazon Cart is empty\"]')))
            print('cart empty')
        except:
            print('cart not empty')
        while not cart_empty_text:
            print('deleting item')
            time.sleep(2)
            delete_item = WebDriverWait(web_driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '(//android.widget.Button[@text=\"Delete\"])[1]')))
            delete_item.click()
            cart_tab_button.click()
            try:
                cart_empty_text = WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, '//android.widget.TextView[@text=\"Your Amazon Cart is empty\"]')))
                print('cart empty')
            except:
                print('cart not empty')


def test_search_and_add_to_cart(web_driver) -> None:
    search_view = WebDriverWait(web_driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                       '(//android.widget.TextView[@resource-id=\"com.amazon.mShop.android.shopping:id/chrome_search_hint_view\"])')))
    search_view.click()
    search_text = WebDriverWait(web_driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                       '(//android.widget.EditText[@resource-id=\"com.amazon.mShop.android.shopping:id/rs_search_src_text\"])')))
    search_text.click()
    search_text.clear()
    search_text.send_keys('ner mitzva\n')
    # sleeps added to due to very slow virtual machine in dev environment, might be ommitted on normal env
    time.sleep(10)
    search_suggest = WebDriverWait(web_driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                          '(//android.widget.FrameLayout[@resource-id=\"com.amazon.mShop.android.shopping:id/search_suggestions_frame_layout\"])')))
    search_suggest.click()
    time.sleep(10)
    # web_driver.press_keycode(66)           
    first_item = WebDriverWait(web_driver, 20).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '(//android.widget.TextView[@text=\"Ner Mitzvah\"])[1]')))
    # first_item=result_items
    first_item.click()
    time.sleep(10)
    web_driver.swipe(start_x=75, start_y=1900, end_x=75, end_y=0, duration=800)
    time.sleep(2)
    add_to_cart_button = WebDriverWait(web_driver, 20).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '//android.widget.Button[@resource-id=\"add-to-cart-button\"]')))
    add_to_cart_button.click()
    time.sleep(5)
    confirm_text = WebDriverWait(web_driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Added to Cart"]')))
