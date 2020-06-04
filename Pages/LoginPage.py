from selenium import webdriver
from selenium import webdriver
from .BasePage import BasePage 
from selenium.webdriver.common.by import By

# 定位元素
class LoginPage(BasePage):

	#登录地址
	url = "http://10.50.48.5:9999/#/login"
	
	username = (By.CSS_SELECTOR,'#__layout > main > div.login-form > div > div > form > div.el-form-item.input-item.first.el-form-item--feedback.is-required > div > div > input')
	password = (By.CSS_SELECTOR,'#__layout > main > div.login-form > div > div > form > div:nth-child(2) > div > div > input')
	submit = (By.CSS_SELECTOR,'#__layout > main > div.login-form > div > div > form > button')

	def __init__(self,driver):
		self.driver = driver

	def login_page(self):
		self.open(self.url)
		self.send_keys(self.username,"admin")
		self.send_keys(self.password,"admin")
		self.click(self.submit)
		self.screenshot("登录截图")

	def search_content(self,content):
		BaiduContent = self.find_element(self.search_loc)
		BaiduContent.send_keys(content)

	def btn_click(self):
		BaiduBtn = self.find_element(self.btn_loc)
		BaiduBtn.click()
