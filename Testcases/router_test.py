#coding:utf-8 
#uinttest
import unittest
import sys
import time
sys.path.append("..")
from Pages import BasePage
from Pages import routerPage
from Pages import LoginPage
from selenium import webdriver

class Test(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		#设置隐式等待15s
		#self.driver.implicitly_wait(15)
		t = LoginPage.LoginPage(self.driver)
		t.login_page()


	def test_login(self):
		s = routerPage.routerPage(self.driver)
		s.enter_router_page()
		s.add_router("chenxing")
		self.assertEqual(s.get_router_name_for_table(),"chenxing","判断是否添加成功");

	def tearDown(self):
		self.driver.quit();


if __name__ == '__main__':
	unittest.main(verbosity=2);
