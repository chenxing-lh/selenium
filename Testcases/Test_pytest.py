#pytest
import pytest
import sys
import time

from selenium import webdriver
sys.path.append("..")
from Pages import BasePage,routerPage,LoginPage


class Test:
	
	def setup_class(self):
		self.driver = webdriver.Chrome()
		#设置隐式等待15s
		self.driver.implicitly_wait(15)
		t = LoginPage.LoginPage(self.driver)
		t.login_page()
		

	def test_login(self):
		s = routerPage.routerPage(self.driver)
		s.enter_router_page()
		s.add_router("chenxing")
		assert s.get_router_name_for_table()=="chenxing"

	def teardown_class(self):
		self.driver.quit();


if __name__ == '__main__':
	pytest.main(['-v','-s','Test_pytest.py'])