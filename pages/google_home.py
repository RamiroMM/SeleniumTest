from utils.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class GoogleHome:

	def __init__(self, driver):
		self.driver = driver

	def send_text_to_search(self, word):
		search_bar = WebDriverWait(self.driver, 10).until(
			ec.presence_of_element_located((By.NAME, Locators.search_bar_name)))
		
		search_bar.send_keys(word)

	def click_search_button(self):
		search_button = self.driver.find_element_by_name(Locators.search_button_name)
		search_button.click()