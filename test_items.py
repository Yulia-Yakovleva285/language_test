import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def test_find_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    try:   
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        el = True
    except: 
        el = False
    assert el, 'No element!'
    
