# coding=utf-8
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def configure_env(driver_bin):
    """
    Allow configure environment to run this test. Create output folders and set driver
    :param driver_bin: Name of the driver file to run selenium. Must be in drivers folder inside this project. By the moment, only Chrome is supported
    :return: Return a pointer to browser driver
    """
    project_folder = os.path.abspath(os.path.dirname(__file__))
    driver_bin = os.path.join(project_folder, "drivers", driver_bin)
    chromedriver = webdriver.Chrome(executable_path=driver_bin)
    if not os.path.exists("output"):
        os.mkdir("output/")
        os.mkdir("output/error")
        os.mkdir("output/screenshot")
    return chromedriver


if __name__ == '__main__':
    driver = configure_env("chromedriver92")
    try:
        driver.get("https://app.sysdigcloud.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        # Assert page correctly loaded
        tbx__username = driver.find_element_by_name("username")
        assert tbx__username.is_displayed()
        tbx__password = driver.find_element_by_name("password")
        assert tbx__password.is_displayed()
        btn__login = driver.find_element_by_xpath("//button[@data-id='submit-login']")
        assert btn__login.is_displayed()
        lnk__forgotPwd = driver.find_element_by_xpath("//a[@data-test='link-forgot-password']")
        assert lnk__forgotPwd.is_displayed()
        lnk__googleLogin = driver.find_element_by_xpath("//a[img[@alt='Google']]")
        assert lnk__googleLogin.is_displayed()
        lnk__samlLogin = driver.find_element_by_xpath("//a[img[@alt='SAML']]")
        assert lnk__samlLogin.is_displayed()
        lnk__openidLogin = driver.find_element_by_xpath("//a[img[@alt='OpenID']]")
        assert lnk__openidLogin.is_displayed()
        lnk__signup = driver.find_element_by_xpath("//a[@class='login__link']")
        assert lnk__signup.is_displayed()
        # Take screenshot as evidence
        driver.save_screenshot("output/screenshot/Page correctly displayed.png")
        # Try login
        tbx__username.send_keys("sergio")
        tbx__password.send_keys("is my name")
        btn__login.click()
        # Improvement -> Capture JS alert message "Username must contains @...". Workaround to test, check username input is displayed (Still on login page)
        assert tbx__username.is_displayed()
        driver.save_screenshot("output/screenshot/Login error if write invalid username.png")
        tbx__username.clear()
        tbx__password.clear()
        tbx__username.send_keys("sergio.lozanot@1234.com")
        tbx__password.send_keys("sysdig1234")
        btn__login.click()
        # Check login with credentials invalid returns an error. Take screenshot
        txt__crendentialsInvalid = driver.find_element_by_xpath("//p[@class='login__error-display']")
        assert txt__crendentialsInvalid.is_displayed()
        assert "Credentials are not valid" == txt__crendentialsInvalid.text
        driver.save_screenshot("output/screenshot/Login error if write invalid credentials.png")
        # Assert that links to external apps are correctly linked.
        assert lnk__signup.get_attribute("href") == "https://sysdig.com/sign-up/"
        assert lnk__forgotPwd.get_attribute("href") == "https://app.sysdigcloud.com/#/forgotPassword"
        assert lnk__googleLogin.get_attribute("href") == "https://app.sysdigcloud.com/api/oauth/google?redirectRoute=/"
        assert lnk__samlLogin.get_attribute("href") == "https://app.sysdigcloud.com/#/samlAuthentication"
        assert lnk__openidLogin.get_attribute("href") == "https://app.sysdigcloud.com/#/openIdAuthentication"
        driver.close()
    # In case that any exception with element not found, print on console, take an screenshot and close driver
    except NoSuchElementException as Exception:
        print(Exception)
        # Errors screenshot are saved in output/error folder.
        driver.save_screenshot("output/error/" + time.ctime() + "_" + Exception.msg + ".png")
        driver.close()
