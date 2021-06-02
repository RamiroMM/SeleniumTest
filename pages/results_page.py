from utils.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ResultsPage:

	def __init__(self, driver):
		self.driver = driver

	def verify_results(self, word):
		result_list = WebDriverWait(self.driver, 10).until(
			ec.presence_of_all_elements_located((By.XPATH, Locators.search_results)))

		for item in result_list:
			if word in item.text.lower() or "pruebas" in item.text.lower() or "programar" in item.text.lower():
				pass
			else:
				print("Expected: pruebas, testing\n")
				print(f"Found: {item.text}")
				return False
		return True