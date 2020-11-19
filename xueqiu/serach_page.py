from selenium.webdriver.common.by import By

from xueqiu.base_page import BasePage



class Serach_Page(BasePage):
    def serach(self):
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("小米")
        print("搜索小米公司")
        return True

