from appium import webdriver

from appium import webdriver

des={
    'platformName' :'Android',
    'platformVersion' : '6.0.1',
    'deviceName' : '309b589a',
    'appPackage' : 'com.ktakilat.loan',
    'appActivity' : 'com.pendanaan.kta.ui.activity.home.Home2018Activity'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',des)