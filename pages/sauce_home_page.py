from utils.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class HomePage:

	def __init__(self, driver):
		self.driver = driver

	def verify_home_page_is_displayed(self):
		try:
			app_logo = WebDriverWait(self.driver, 10).until(
				ec.presence_of_element_located((By.XPATH, Locators.app_logo)))

			if app_logo.is_displayed:
				print("Home Page is loaded")
				return True
			else:
				print("Home Page is not loaded")
				return False
		except TimeoutException as e:
			print("Home Page not found")
			return False
