import time
import selenium.common.exceptions
import engine
from engine import *

time.sleep(4)   # wait for the page load

def cookie_click():
    big_cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')
    print("start clicking !!")
    while 1 < 10:
        big_cookie.click()

def cookie_upgrade():
    while 1 < 10:
        try:
            up_cookie = driver.find_element_by_xpath('/html/body/div/div[2]/div[19]/div[3]/div[5]/div')
            up_cookie.click()
            print("Time to get better")
        except NoSuchElementException:
            return 0
        time.sleep(0.5)
        return 1

def cookie_workers():
    while 1 < 10:
        try:
            for count in range(18):
                hire_workers = driver.find_element_by_xpath(f'//*[@id="product{count}"]')
                hire_workers.click()
                print("Turn on the heat")
        except NoSuchElementException:
            return 0
        except selenium.common.exceptions.ElementNotInteractableException:
            return 0
        return 1
