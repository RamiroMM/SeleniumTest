import pytest
from pages.login_page import LoginPage
from pages.sauce_home_page import HomePage
import time

@pytest.mark.usefixtures("test_setup")
class TestCase:

	def test_login(self):
		driver = self.driver
		login_page = LoginPage(driver)
		home_page = HomePage(driver)

		driver.get("https://www.saucedemo.com/")
		login_page.login("standard_user", "secret_sauce")
		assert home_page.verify_home_page_is_displayed()

		time.sleep(5)

	def test_login_locked_out(self):
		driver = self.driver
		login_page = LoginPage(driver)
		home_page = HomePage(driver)

		driver.get("https://www.saucedemo.com/")
		login_page.login("locked_out_user", "secret_sauce")
		assert not home_page.verify_home_page_is_displayed()

		time.sleep(5)
