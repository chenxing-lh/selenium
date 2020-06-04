from selenium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
	def __init__(self,driver):
		self.driver = driver
		#self.base_url = base_url

	def find_element(self,*loc):
		try:
			#显示等待
			WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))

			return self.driver.find_element(*loc)
		except Exception as e:
			print("页面没有找到元素",e)

	def send_keys(self,element,value):
		try:
			t = self.find_element(*element)
			t.clear()
			t.send_keys(value)
		except Exception as e:
			print("设置文本内容失败",e)

	#点击
	def click(self,loc):
		self.find_element(*loc).click()

	#获取当前属性文本内容
	def get_text(self,loc):
		try:
			return self.find_element(*loc).text
		except Exception as e:
			print("获取当前属性文本内容出错",e)

	#跳转到url
	def open(self,url):
		self.driver.get(url);
		# 设置全屏
		self.driver.maximize_window()

	#隐式等待
	def hidWait(self,time=15):
		self.driver.implicitly_wait(time)


	#显式等待
	def showWait(self):
		pass;

	#获取当前title
	def get_title(self):
		return self.driver.title

	#后退
	def back(self):
		self.driver.back()

	#前进
	def forward(self):
		self.driver.forward()

	def screenshot(self,filename):
		#获取当前工作路径的父目录，拼接为img的路径
		path = os.path.abspath('..')+"\\Img\\"+str(self.__class__.__name__)+str(filename)+".png"
		print(path)
		self.driver.save_screenshot(path)

# path = os.path.abspath('..')+"\\Img\\BasePage\\"+str(123)+".png"
# print(path)
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.save_screenshot(path)