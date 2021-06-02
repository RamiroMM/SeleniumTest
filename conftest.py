import pytest

@pytest.fixture(scope="class")
def test_setup(request):
	from selenium import webdriver
	from webdriver_manager.chrome import ChromeDriverManager
	from selenium.webdriver.chrome.options import Options

	options = Options()
	options.add_argument("--start-maximized")

	driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
	driver.implicitly_wait(15)
	request.cls.driver = driver
	yield
	driver.close()
	driver.quit()
