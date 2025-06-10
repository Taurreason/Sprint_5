import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium import webdriver
from datetime import datetime
from helpers import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver  # возвращаем драйвер тесту
    driver.quit()

@pytest.fixture
def unique_valid_email():
    return generate_valid_unique_email()

@pytest.fixture
def unique_invalid_email():
    return generate_invalid_unique_email()

# фикстура логина авторизованного пользователя
@pytest.fixture
def login_user(driver):   
    # Кликаем "Вход и регистрация"
    driver.find_element(*Buttons.LOGIN_REGISTER).click()

    # Вводим логин и пароль
    driver.find_element(*Inputs.EMAIL).send_keys("kudakaeva_22@yandex.ru")
    driver.find_element(*Inputs.PASSWORD).send_keys("Qawsedrf1@#456&")

    # Нажимаем "Войти"
    driver.find_element(*Buttons.LOGIN).click()

    # Ожидаем, что пользователь авторизовался (например, по появлению аватара или имени)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(User.AVATAR)
    )

    return driver
