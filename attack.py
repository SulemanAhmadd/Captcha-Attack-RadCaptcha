from CAPTCHA_object_detection import *
from selenium import webdriver
import urllib

driver = webdriver.Firefox(executable_path="./driver/geckodriver")
driver.get("https://demos.telerik.com/aspnet-ajax/captcha/examples/overview/defaultcs.aspx")
#print()


while (1):

	try:

		raw_input("Press any key to continue...")

		# clear previous entry
		inputElement = driver.find_element_by_id("ctl00_ContentPlaceholder1_RadCaptcha1_CaptchaTextBox")
		inputElement.send_keys("")

		# get the image source
		img = driver.find_element_by_xpath('//img[@id="ctl00_ContentPlaceholder1_RadCaptcha1_CaptchaImage"]')
		src = img.get_attribute('src')

		# download the image
		urllib.urlretrieve(src, "captcha.jpeg")

		# run model
		captcha_text = Captcha_detection("captcha.jpeg")

		# clear box, and upload outcome
		inputElement = driver.find_element_by_id("ctl00_ContentPlaceholder1_RadCaptcha1_CaptchaTextBox")
		print(captcha_text)
		inputElement.send_keys(captcha_text)

	except Exception:

		driver.close()
		break;