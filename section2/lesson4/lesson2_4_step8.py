import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def fill_form():
    try:
        browser = webdriver.Chrome()
        # говорим WebDriver ждать все элементы в течение 5 секунд
        browser.implicitly_wait(5)

        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        price_element = WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
        )

        book_button = browser.find_element(By.CSS_SELECTOR, "#book")
        book_button.click()

        answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
        answer_field.send_keys("2408")
        answer_button = browser.find_element(By.CSS_SELECTOR, "#solve")
        answer_button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(60)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    fill_form()