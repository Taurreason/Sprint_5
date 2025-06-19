from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestRegistration:


    def test_registration_valid_user(self, driver, unique_valid_email):
        # находим кнопку "вход и регистрация"
        driver.find_element(*Buttons.LOGIN_REGISTER).click()
        driver.find_element(*Buttons.NO_ACCOUNT).click()

        # Явное ожидание загрузки страницы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Headers.REGISTRATION))

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.EMAIL)).send_keys(unique_valid_email)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.PASSWORD)).send_keys('some_password')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.REPEAT_PASSWORD)).send_keys('some_password')

        driver.find_element(*Buttons.CREATE_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.url_contains("/regiatration"))

        user_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(User.NAME))
        avatar = driver.find_element(*User.AVATAR)
        place_ad_button = driver.find_element(*Buttons.ADD_CREATION)

        assert user_element.is_displayed() and user_element.text.strip() == "User." \
               and avatar.is_displayed() and place_ad_button.is_displayed()
        
        # регистрация пользователя не по маске (с красными полями)
    def test_registration_invalid_email(self, driver, unique_invalid_email):
        driver.find_element(*Buttons.LOGIN_REGISTER).click()  
        # находим кнопку "Нет аккаунта"
        driver.find_element(*Buttons.NO_ACCOUNT).click()
        # Явное ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Headers.REGISTRATION))

        # Выполняем авторизацию с некорректными данными
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.EMAIL)).send_keys(unique_invalid_email)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.PASSWORD)).send_keys('some_password')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Inputs.REPEAT_PASSWORD)).send_keys('some_password')

        # Нажимаем на кнопку "Создать аккаунт"
        driver.find_element(*Buttons.CREATE_ACCOUNT).click()
        # Явное ожидание появления ошибки
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Errors.TEXT_REGISTRATION))
        
        # Находим элемент с текстом ошибки
        error_message_email_field = driver.find_element(*Errors.TEXT_REGISTRATION)
        # Проверяем, что он отображается и содержит нужный текст
        error_text_correct = error_message_email_field.is_displayed() and error_message_email_field.text.strip() == "Ошибка"
        # Проверяем, что все три поля подсвечены красным (видимы)
        error_fields_visibility_red = all([
                driver.find_element(*Errors.EMAIL_FIELD).is_displayed(),
                driver.find_element(*Errors.PASSWORD_FIELD).is_displayed(),
                driver.find_element(*Errors.REPEAT_PASSWORD_FIELD).is_displayed()
            ])

        assert error_text_correct and error_fields_visibility_red

    def test_registration_with_existing_user(self, driver):
        driver.find_element(*Buttons.LOGIN_REGISTER).click()
        driver.find_element(*Buttons.NO_ACCOUNT).click()

        # Явное ожидание загрузки попапа регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Headers.REGISTRATION))

        # Регистрируемся с именем существующего пользователя: Заполняем поля email/пароль/повтор пароля
        driver.find_element(*Inputs.EMAIL).send_keys('kudakaeva_22@yyandex.ru')
        driver.find_element(*Inputs.PASSWORD).send_keys('asdfghjkl')
        driver.find_element(*Inputs.REPEAT_PASSWORD).send_keys('asdfghjkl')

        # Нажимаем на кнопку "Создать аккаунт"
        driver.find_element(*Buttons.CREATE_ACCOUNT).click()
        # Явное ожидание появления ошибки
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Errors.TEXT_REGISTRATION))

        # Находим элемент с текстом ошибки
        error_message_email_field = driver.find_element(*Errors.TEXT_REGISTRATION)
        # Проверяем, что он отображается и содержит нужный текст
        error_text_correct = error_message_email_field.is_displayed() and error_message_email_field.text.strip() == "Ошибка"
        # Проверяем, что все три поля подсвечены красным (видимы)
        error_fields_visibility_red = all([
            driver.find_element(*Errors.EMAIL_FIELD).is_displayed(),
            driver.find_element(*Errors.PASSWORD_FIELD).is_displayed(),
            driver.find_element(*Errors.REPEAT_PASSWORD_FIELD).is_displayed()
        ])

        assert error_text_correct and error_fields_visibility_red
