from selenium import webdriver #Importo selenium
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe') #Variable levanta el chrome
driver.get('http://automationpractice.com/index.php') #Abre la pagina que se le pasa entre comillas
driver.find_element_by_id('search_query_top').send_keys('Hola') #Envio en el campo search la palabra Hola
driver.find_element_by_name('submit_search').click() #Hago clic en la lupa
time.sleep(1)
tc.assertEqual('No results were found for your search "Hola"', driver.find_element_by_xpath('//*[@id="center_column"]/p').text) #Compara el texto que se encuentra en el xpath con lo primero
driver.close()
driver.quit()