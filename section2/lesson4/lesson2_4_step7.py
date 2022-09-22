import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_form():
    try:
        browser = webdriver.Chrome()
        # говорим WebDriver ждать все элементы в течение 5 секунд
        browser.implicitly_wait(5)

        browser.get("http://suninjuly.github.io/wait2.html")

        # button = browser.find_element(By.ID, "verify")
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
        button.click()
        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    fill_form()