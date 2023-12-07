import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import utils


class TestLogin:

    def test_login_negative(self, web_driver):
        time.sleep(20)
        logged_in = None
        try:
            logged_in = utils.verify_login(web_driver)
        except:
            pass
        if logged_in:
            pytest.fail('already logged in, run test after reset app')
        try:
            sign_in_button = WebDriverWait(web_driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, "com.amazon.mShop.android.shopping:id/sign_in_button")))
        except:
            pytest.fail("couldn't find sign in button")
        # self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/sign_in_button")
        sign_in_button.click()
        # time.sleep(12)
        sign_in_option = WebDriverWait(web_driver, 40).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text="Sign in. Already a customer?"]')))
        # self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Sign in. Already a customer?"]')
        sign_in_option.click()
        time.sleep(10)
        email_edit = WebDriverWait(web_driver, 20).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
        email_edit.click()
        email_edit.send_keys("amnonma1@gmail.com")
        email_edit.click()
        time.sleep(5)
        continue_button = WebDriverWait(web_driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text="Continue"]')))
        continue_button.click()
        try:
            no_account_text = WebDriverWait(web_driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//*[@text="No account found with email address"]')))
        except:
            pytest.fail("expected login message not found")

    def test_login_positive(self, web_driver):
        logged_in = None
        try:
            logged_in = utils.verify_login(web_driver)
        except:
            pass
        if logged_in:
            pytest.fail('already logged in, run test after reset app')
        if not utils.login(web_driver, 'amnonma@gmail.com', 'amnonma123'):
            pytest.fail('login failed')
        if not utils.verify_login(web_driver):
            pytest.fail("log in verification failed")
