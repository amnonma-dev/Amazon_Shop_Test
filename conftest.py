import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


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


@pytest.fixture
def web_driver():
    print("setup")
    web_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield web_driver
    print("teardown")
    web_driver.quit()