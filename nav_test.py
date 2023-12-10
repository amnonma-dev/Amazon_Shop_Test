import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestNavigation:
    def test_back_button(self, web_driver):
        utils.login(web_driver, 'amnonma@gmail.com', 'amnonma123')
        utils.navigate_tabs(web_driver, "home")
        try:
            WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
        except:
            pytest.fail("home text not found")
        search_view = (WebDriverWait(web_driver, 5).until
                       (expected_conditions.presence_of_element_located((By.XPATH,
                                                                         '(//android.widget.TextView[@resource-id='
                                                                         '\"com.amazon.mShop.android.shopping:id/chrome_search_hint_view\"])'))))
        search_view.click()
        try:
            WebDriverWait(web_driver, 5).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
            pytest.fail("home text not expected after nav")
        except:
            pass
        back_button = web_driver.find_element(by=AppiumBy.ID,
                                              value="com.amazon.mShop.android.shopping:id"
                                                    "/chrome_action_bar_back_icon_image")
        back_button.click()
        try:
            WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
        except:
            pytest.fail("home text not found after nav back")

    def test_android_back_button(self, web_driver):
        utils.login(web_driver, 'amnonma@gmail.com', 'amnonma123')
        home_tab_button = WebDriverWait(web_driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                               '(//android.widget.ImageView[@resource-id=\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])[1]')))
        home_tab_button.click()
        try:
            WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
        except:
            pytest.fail("home text not found")
        search_view = WebDriverWait(web_driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                          '(//android.widget.TextView[@resource-id=\"com.amazon.mShop.android.shopping:id/chrome_search_hint_view\"])')))
        search_view.click()
        try:
            WebDriverWait(web_driver, 5).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
            pytest.fail("home text not expected")
        except:
            pass
        web_driver.back()
        try:
            WebDriverWait(web_driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@text=\"Discover Amazon International Shopping\"]')))
        except:
            pytest.fail("home text not found after nav back")
