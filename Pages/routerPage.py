from selenium import webdriver
from .BasePage import BasePage 
from selenium.webdriver.common.by import By

# 定位元素
class routerPage(BasePage):

	#写各个定位位置
	#路由管理tab菜单
	router_url = (By.CSS_SELECTOR,'#__layout > div > section > div > ul > li:nth-child(2)')
	#新建路由按钮
	add_router_button = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > form:nth-child(2) > div > div > button')

	#表单元素定位
	#路由名称
	router_name = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(1) > div > div > input')
	#匹配条件--匹配域名
	match_domain = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(2) > div > div > label:nth-child(2) > span.el-radio__label')
	#匹配条件--匹配域名
	match_url = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(2) > div > div > label:nth-child(2) > span.el-radio__input')
	#匹配路径输入框
	match_path = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(3) > div > div > input')
	#添加目标服务按钮
	add_target_button = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(4) > div > div > div > button')
	#目标地址
	target_url = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(4) > div > div > div > div > div > div > div:nth-child(1) > input')
	#目标权重
	target_weight = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(4) > div > div > div > div > div > div > div:nth-child(2) > input')
	#按钮--前缀生效
	prefix_effective = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(5) > div > div > label:nth-child(1) > span.el-radio__input')
	#按钮--前缀不生效
	prefix_uneffective = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(5) > div > div > label:nth-child(1) > span.el-radio__label')
	#状态按钮--启用
	status_effective = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(7) > div > div > label.el-radio.is-checked > span.el-radio__input.is-checked')
	#状态按钮--不启用
	status_uneffective = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(7) > div > div > label.el-radio.is-checked > span.el-radio__label')
	#优先级
	priority = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.top > div > form > div:nth-child(6) > div > div > div > input')
	#按钮-确定/取消
	submit_button = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.footer > span > button:nth-child(2)')
	cancel_button = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-drawer__wrapper > div > div > section > div > div.footer > span > button:nth-child(1)')


	#查询相关
	#路由名称
	select_router_name = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > form.el-form.el-form-renderer.el-form--inline > div:nth-child(1) > div > div > input')
	#路由id
	select_router_id = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > form.el-form.el-form-renderer.el-form--inline > div:nth-child(2) > div > div > input')
	#匹配路径/域名
	select_router_path = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > form.el-form.el-form-renderer.el-form--inline > div:nth-child(3) > div > div > input')
	#查询按钮
	select_submit_button =  (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > form.el-form.el-form-renderer.el-form--inline > div:nth-child(4) > div > button:nth-child(1)')


	def __init__(self,driver):
		self.driver = driver

	def enter_router_page(self):
		self.click(self.router_url)


	def add_router(self,name):
		self.click(self.add_router_button)
		self.send_keys(self.router_name,name)
		self.click(self.match_domain)
		self.send_keys(self.match_path,"www.demo.com")
		self.click(self.add_target_button)
		self.send_keys(self.target_url,"www.baidu.com")
		self.send_keys(self.target_weight,"44")
		self.click(self.prefix_uneffective)
		self.send_keys(self.priority,"4")
		self.click(self.status_effective)
		self.screenshot("添加路由截图")
		self.click(self.submit_button)


	def select_router(self,name):
		self.send_keys(self.select_router_name,name)
		self.send_keys(self.select_router_id,"")
		self.send_keys(self.select_router_path,"")
		self.click(self.select_submit_button)


	def get_router_name_for_table(self):
		path = (By.CSS_SELECTOR,'#__layout > div > section > main > div > div.preview-content > div > div.el-data-table > div.el-table.el-table--fit.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td:nth-child(2)')
		
		return(self.get_text(path))

	def search_content(self,content):
		BaiduContent = self.find_element(*self.search_loc)
		BaiduContent.send_keys(content)

	def btn_click(self):
		BaiduBtn = self.find_element(*self.btn_loc)
		BaiduBtn.click()
