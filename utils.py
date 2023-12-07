import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import pytest

USERNAME = 'amnon'


def navigate_tabs(driver, tab_name):
    tabs_indexes = {'home': 1, 'inspire': 2, 'account': 3, 'cart': 4, 'settings': 5}
    if tab_name not in tabs_indexes.keys():
        pytest.fail("invalid tab name  provided")
    bottom_buttons = driver.find_elements(by=AppiumBy.XPATH,
                                          value='//android.widget.ImageView[@resource-id=\"'
                                                'com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"]')
    buttons_count = len(bottom_buttons)
    if buttons_count not in (4, 5):
        pytest.fail("tab buttons count mismatch")
    if buttons_count == 4 and tabs_indexes[tab_name] > 2:
        tab_index = tabs_indexes[tab_name] - 1
    else:
        tab_index = tabs_indexes[tab_name]
    tab_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH,
                                                         '(//android.widget.ImageView[@resource-id=\"'
                                                         'com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])'
                                                         '[' + str(tab_index) + ']')))
    tab_button.click()
    time.sleep(5)


def verify_login(driver):
    navigate_tabs(driver, "account")
    try:
        account_name_text = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located
                                                            ((By.XPATH, '//android.widget.TextView[@text=\"' + str(
                                                                USERNAME) + '\"]')))
        return True
    except:
        return False


def login(driver, user, passw):
    try:
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, "com.amazon.mShop.android.shopping:id/sign_in_button")))
            sign_in_button.click()
        except:
            pass
        sign_in_option = WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located
                                                         ((By.XPATH, '//*[@text="Sign in. Already a customer?"]')))
        sign_in_option.click()
        email_edit = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
        email_edit.click()
        email_edit.send_keys(user)
        continue_button = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text="Continue"]')))
        continue_button.click()
        pass_edit = WebDriverWait(driver, 40).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '(//android.widget.EditText[@resource-id=\"ap_password\"])')))
        pass_edit.click()
        pass_edit.send_keys(passw)
        time.sleep(5)
        driver.press_keycode(66)
        # sign_in_final_button = WebDriverWait(driver, 40).until(
        #     expected_conditions.presence_of_element_located((By.CLASS_NAME, "android.widget.Button")))
        # sign_in_final_button.click()
        time.sleep(10)
        return True
    except:
        return False
