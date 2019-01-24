import os
from selenium import webdriver

Instance = None


def initialize():
    global Instance
    if Instance is None:
        Instance = webdriver.Chrome(os.path.abspath(os.path.join(__file__, "../../.."))+"\\resource\\chromedriver.exe")
        Instance.implicitly_wait(5)
    return Instance


def close_driver():
    global Instance
    Instance.quit()
    Instance = None
