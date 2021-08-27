import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
from datetime import datetime

options = Options()
options.add_argument('--no-sandbox')
options.headless = False

driver = webdriver.Chrome(options=options, executable_path='C:\geckodriver.exe')

driver.get('https://orteil.dashnet.org/cookieclicker/')