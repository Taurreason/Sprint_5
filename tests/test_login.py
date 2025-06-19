from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestLogin:

 
    def test_login_successful(self, driver):
        driver.find_element(*Buttons.LOGIN_REGISTER).click()
        # Добавим явное ожидание загрузки страницы
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Buttons.LOGIN))

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.EMAIL)).send_keys("kudakaeva_22@yyandex.ru")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.PASSWORD)).send_keys('asdfghjkl')

        # Нажимаем на кнопку "Войти"
        driver.find_element(*Buttons.LOGIN).click()

        # Добавим явное ожидание загрузки страницы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(User.AVATAR))

        # Проверка наличия имени пользователя
        user_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(User.NAME))
        avatar = driver.find_element(*User.AVATAR)
        place_ad_button = driver.find_element(*Buttons.ADD_CREATION)

        assert user_element.is_displayed() and user_element.text.strip() == "User." \
               and avatar.is_displayed() and place_ad_button.is_displayed()

    def test_logout_successful(self, login_user):
        driver = login_user
        # Ожидаем, пока появится имя пользователя
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(User.NAME))
        # Нажимаем кнопку "Выйти"
        driver.find_element(*Buttons.LOGOUT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Buttons.LOGIN_REGISTER))

        # Проверка наличия кнопки логина и регистрации
        register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Buttons.LOGIN_REGISTER))
        place_ad_button = driver.find_element(*Buttons.ADD_CREATION)

        assert register_button.is_displayed() and place_ad_button.is_displayed() \
               and not driver.find_elements(*User.AVATAR) and not driver.find_elements(*User.NAME)
