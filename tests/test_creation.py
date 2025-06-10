from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from locators import *
import time


class TestCreation:


    def test_add_creation_guest(self, driver):
       # Переход на страницу создания объявления
        driver.find_element(*Buttons.ADD_CREATION).click()
        # Явное ожидание загрузки формы
        header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Headers.REGISTRATION_CREATION))
        assert header.is_displayed() and header.text.strip() == "Чтобы разместить объявление, авторизуйтесь"
       
    def test_add_creation_authorized_user(self, login_user):

        driver = login_user
        driver.find_element(*Buttons.ADD_CREATION).click()
        # Переход на страницу создания объявления
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Inputs.TITLE))

        # Заполнение полей
        driver.find_element(*Inputs.TITLE).send_keys("Test Product")
        driver.find_element(*Inputs.DESCRIPTION).send_keys("Б/у, в хорошем состоянии.")
        driver.find_element(*Inputs.PRICE).send_keys("25000")

        # Открываем дропдаун "Категория" и выбираем опцию
        driver.find_element(*Dropdowns.CATEGORY_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Dropdowns.CATEGORY_OPTION_AUTO))
        driver.find_element(*Dropdowns.CATEGORY_OPTION_AUTO).click()

        # Открываем дропдаун "Город" и выбираем опцию
        driver.find_element(*Dropdowns.CITY_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Dropdowns.CITY_OPTION_SPB))
        driver.find_element(*Dropdowns.CITY_OPTION_SPB).click()

        # выбрать состояние (радиокнопка)
        driver.find_element(*Radio.CONDITION["used"]).click()

        # нажимаем кнопку "опубликовать"
        driver.find_element(*Buttons.PUBLISH).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(User.AVATAR))

        # Переход в профиль
        # Скроллим страницу наверх
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        driver.find_element(*User.AVATAR).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/profile"))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Headers.PROFILE))
        # Проверка заголовка блока
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Headers.CREATION))

        # Скролл до низа страницы        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Небольшая задержка, чтобы все успело отрисоваться

        found = False
        while True:
            listings = driver.find_elements(*Listings.TEST_PRODUCT)
            if any(listing.is_displayed() for listing in listings):
                found = True
                break

            # Переход на следующую страницу, если возможно
            try:
                next_button = driver.find_element(*Buttons.PAGE)
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                next_button.click()
                time.sleep(1)
            except NoSuchElementException:
                break  # Следующей страницы нет

        assert found
