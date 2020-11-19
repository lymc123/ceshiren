from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from xueqiu.base_page import BasePage
from xueqiu.market_page import MarketPage


class Main_page(BasePage):
    def goto_market(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        print("进入行情")

        return MarketPage(self.driver) #把driver 传递给下一个










