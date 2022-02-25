import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones
from Funciones.Funciones import Funciones_Globales

tie = .02

def setup_function(function):
    print("\nInicia Test")
    global driver, func
    driver = webdriver.Chrome(executable_path="C:/driverchrome/chromedriver.exe")

    func = Funciones_Globales(driver)
    func.navegar("https://www.bbva.mx/", tie)
    driver.maximize_window()

def teardown_function(function):
    print("Finaliza Test")
    driver.close()

def test_personas():

    func.click_xpath_val("(//span[contains(.,'Acceso')])[1]",tie)
    func.text_xpath_val("//input[contains(@type,'text')]","2222444455556666",tie)
    func.click_xpath_val("//a[@itemprop='url'][contains(.,'Personas')]",tie)
    func.click_xpath_val("//li[contains(@class,'linkwithicon swiper-slide swiper-slide-active')]",.2)
    func.click_xpath_val("//li[contains(@class,'linkwithicon swiper-slide swiper-slide-next')]",tie)
