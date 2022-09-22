import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import time

def fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/find_xpath_form")

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
        input3.send_keys("Smolensk")

        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")

        button = browser.find_element(By.XPATH, ".//button[text()='Submit']")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    fill_form()