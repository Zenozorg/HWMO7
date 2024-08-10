# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')
# driver.get('https://example.com/currency')
# time.sleep(5)
# currency_element = driver.find_element(By.CLASS_NAME, 'currency-class')
# currency_rate = currency_element.text
# print("Курс валют:", currency_rate)
# driver.quit() #task a



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')
# driver.get('https://example.com/marketplace')
# time.sleep(5)
# price_elements = driver.find_elements(By.CLASS_NAME, 'price-class')
# prices = [element.text for element in price_elements]
# print("Цены на сайте:")
# for price in prices:
#     print(price)
# driver.quit() #task b
