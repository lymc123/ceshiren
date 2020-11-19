
from selenium.webdriver.common.by import By


from xueqiu.base_page import BasePage
from xueqiu.serach_page import Serach_Page


class MarketPage(BasePage):
    def goto_serach(self):
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        print("进入搜索页面")

        return Serach_Page(self.driver)#把driver 传递给下一个