from datetime import time

from selenium import webdriver

driver = webdriver.Chrome(
executable_path="http://127.0.0.1:8000/")

time.sleep(5)

driver.close()