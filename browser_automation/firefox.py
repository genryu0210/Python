# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:35:44 2022

@author: 406429
"""

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.proxy import Proxy


driver = webdriver.Firefox()

driver.get("https://172.17.5.11:8080/status.jsp")
