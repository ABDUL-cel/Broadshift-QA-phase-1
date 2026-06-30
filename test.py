from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = None

try:
    driver = webdriver.Firefox()
    driver.maximize_window()

    file_path = os.path.abspath("from.html")
    driver.get(f"file:///{file_path}")
    time.sleep(2)

    text_box = driver.find_element(By.NAME, "my-text")
    text_box.send_keys("Abdulazeez Khalid")

    password_box = driver.find_element(By.NAME, "my-password")
    password_box.send_keys("Khalid123")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()

    time.sleep(1)

    success_message = driver.find_element(By.TAG_NAME, "h1").text

    assert success_message == "Received!"
    print("[PASS] TEST PASSED: Form submitted successfully")

except Exception as e:
    print(f"[FAIL] TEST FAILED: {e}")

finally:
    if driver:
        time.sleep(2)
        driver.quit()

