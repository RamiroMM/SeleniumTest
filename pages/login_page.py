from utils.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:

	def __init__(self, driver):
		self.driver = driver

	def login(self, user, password):
		user_field = WebDriverWait(self.driver, 10).until(
			ec.presence_of_element_located((By.ID, Locators.user_field_id)))
		password_field = WebDriverWait(self.driver, 10).until(
			ec.presence_of_element_located((By.ID, Locators.password_field_id)))
		login_button = WebDriverWait(self.driver, 10).until(
			ec.presence_of_element_located((By.ID, Locators.login_button_id)))

		if user_field.is_enabled:
			user_field.send_keys(user)
			if password_field.is_enabled:
				password_field.send_keys(password)
				if login_button.is_enabled:
					login_button.click()
				else:
					print("Login button is not enabled")
			else:
				print("Password field is not enabled")	
		else:
			print("User field is not enabled")

