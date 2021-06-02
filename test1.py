from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time



# search_bar = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

# driver.find_element_by_name()
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector()
# driver.find_element_by_tag_name()
# link_tag = driver.find_element_by_link_text('English') # <a>
# driver.find_element_by_partial_link_text('Eng')


article_title = driver.find_element_by_id('firstHeading')

try:
	external_links_section = driver.find_element_by_id('External_links')
except NoSuchElementException:
	external_links_section = driver.find_element_by_id('Enlaces_externos')
