#automation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def auto_book(restaurant_name, date, time_slot):
    driver = webdriver.Chrome()
    driver.get("https://your-restaurant-booking-form.com")  # Replace with actual form URL

    try:
        driver.find_element(By.ID, "name").send_keys("Krish Team")
        driver.find_element(By.ID, "restaurant").send_keys(restaurant_name)
        driver.find_element(By.ID, "date").send_keys(date)
        driver.find_element(By.ID, "time").send_keys(time_slot)
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)
    except Exception as e:
        print("Booking failed:", e)
    finally:
        driver.quit()
