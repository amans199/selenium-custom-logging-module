import logging
import os.path
import time
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# https://docs.python.org/3/library/logging.html

class  Logger (object) :

    def  __init__ (self, logger) : 

        driver = webdriver.Chrome(PATH)

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # define name 
        rq = time.strftime( '%Y%m%d%H%M' , time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/py_selenium/logs/' 
        screenshots_path = os.path.dirname(os.getcwd()) + '/py_selenium/screenshots/' 
        log_name = log_path + rq + '.log'  

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        
        driver.get_screenshot_as_file(screenshots_path + rq + '.png')
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter( '%(asctime)s-%(name)s-%(levelname)s-%(message)s' )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def  getlog (self) : 
        return self.logger