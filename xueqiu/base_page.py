from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    _blacklist = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    _maxcount =9
    _errorcount=0



    def __init__(self,driver:WebDriver=None):
        if driver is None: #判断driver是否存在 不存在初始化
            caps={}
            caps['platformName']='Android'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = 'com.xueqiu.android'
            # caps['automationName'] ='uiautomator2'
            caps['appActivity'] = '.view.WelcomeActivityAlias'
            caps['noReset'] = 'true'
            # caps['dontStopAppOnReset']='true'
            # caps['skipDeviceInitialization']='true'
            # caps['skipServerInstallation']='true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver=driver


    def find(self,by,locator=None):  #封装driver方法
        try:
            if locator is None:
                result= self.driver.find_element(*by)  #解包
            else:
                result= self.driver.find_element(by,locator)

            self._errorcount=0  #找到计数器归零

            return  result

        except Exception as e:
            if self._errorcount>self._maxcount:  #如果黑名单元素的失败次数> 最大次数 直接抛出异常
                raise

            self._errorcount +=1    #计数器+1

            for blackelemnt in self._blacklist:
                elem= self.driver.find_elements(*blackelemnt)
                if len(elem)>0 :  #黑名单大于1 取第一个直接点击
                    elem[0].click()
                    return self.find(by,locator)
            raise e   #黑名单元素为空抛出异常



            print(e)






