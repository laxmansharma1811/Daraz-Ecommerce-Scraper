from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.daraz.com.np/")
time.sleep(5)

search_box = driver.find_element(By.ID, "q")
search_query = "laptop"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

products = []
def scrape_product_details():
    product_details = driver.find_elements(By.CLASS_NAME, "gridItem--Yd0sa")
    for i in product_details:
        try:
            product_name = i.find_element(By.CLASS_NAME, "description--H8JN9").text
            products.append(product_name)
            
        except:
            continue


def handle_pagination():
    page_number = 1
    while True:
        scrape_product_details()
        
        try:
            next_page_class = f"ant-pagination-item-{page_number + 1}"
            next_button = driver.find_element(By.CLASS_NAME, next_page_class)
            next_button.click()
            time.sleep(5)  
            page_number += 1
        except:
            break

handle_pagination()

with open('products.txt', 'w') as file:
    for product in products:
        file.write(f"{product}\n")

driver.quit()
