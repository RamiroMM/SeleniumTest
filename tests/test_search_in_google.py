from selenium import webdriver
from pages.google_home import GoogleHome
from pages.results_page import ResultsPage
import time

class TestCase:

	def test_search(self):
		driver = webdriver.Chrome(executable_path='C:\\Users\\Developer\\Desktop\\SeleniumTest\\driver\\chromedriver.exe')
		driver.implicitly_wait(15)

		home = GoogleHome(driver)
		result_page = ResultsPage(driver)
		driver.get("https://google.com/")

		home.send_text_to_search("testing")
		home.click_search_button()

		assert result_page.verify_results("testing")

		time.sleep(2)
		driver.close()
		driver.quit()

	def test_search2(self):
		driver = webdriver.Chrome(executable_path='C:\\Users\\Developer\\Desktop\\SeleniumTest\\driver\\chromedriver.exe')
		driver.implicitly_wait(15)

		home = GoogleHome(driver)
		result_page = ResultsPage(driver)
		driver.get("https://google.com/")

		home.send_text_to_search("programming")
		home.click_search_button()

		assert result_page.verify_results("programming")

		time.sleep(2)
		driver.close()
		driver.quit()
