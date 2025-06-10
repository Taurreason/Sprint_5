# from selenium.webdriver.common.by import By

# # Кнопки
# LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Вход и регистрация']")  # кнопка "Вход и регистрация"
# NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Нет аккаунта']")      # кнопка "Нет аккаунта"
# CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Создать аккаунт']")  # кнопка "Создать аккаунт"
# BUTTON_ADD_CREATION = (By.XPATH, "//button[text()='Разместить объявление']")  # кнопка "Разместить объявление"
# PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Опубликовать']")  #  кнопка "Опубликовать"
# LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Войти']")  # кнопка "Войти"
# LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'btnSmall') and text()='Выйти']")  # кнопка "Выйти"


# # Поля ввода
# EMAIL_INPUT = (By.NAME, "email")  # поле ввода email
# PASSWORD_INPUT = (By.NAME, "password")  # поле ввода пароля
# SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")  # поле ввода повторить пароль

# # Поля ввода при создании объявления
# TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')  # поле ввода "Название"
# DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, 'textarea[name="description"]')  # поле ввода "Описание товара"
# PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')  # поле ввода "Стоимость"


# # Дропдауны
# CITY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="city"] + button')  # выпадающий список городов
# CATEGORY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="category"] + button')  # выпадающий список категорий
# CATEGORY_OPTION_AUTO = (By.XPATH, '//button[.//span[text()="Авто"]]')  # выбор Авто выпадающего списка категорий
# CITY_OPTION_SPB = (By.XPATH, '//button[.//span[text()="Санкт-Петербург"]]')  # выбор города Санкт-Петербург выпадающего списка городов

# # радиокнопки
# RADIO_CONDITION = {
#     "new": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Новый"]]'),  # выбор радиокнопки "Новый"
#     "used": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Б/У"]]'),  # выбор радиокнопки "Б/У"
# }

# # Хедер и пользователь
# POPUP_REGISTRATION = (By.CLASS_NAME, "homePage_homepageStyleMob__iJ9CT")
# USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
# USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
# PROFILE_HEADER = (By.XPATH, '//h1[text()="Мой профиль"]')
# HEADER_CREATION = (By.XPATH, '//h1[text()="Мои объявления"]')
# HEADER_REGISTRATION = (By.XPATH, '//h1[text()="Зарегистрироваться"]')
# HEADER_REGISTRATION_CREATION = (By.XPATH, '//h1[text()="Чтобы разместить объявление, авторизуйтесь"]')


# EMAIL_ERROR_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="email"]')
# PASSWORD_ERROR_INPUT = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="password"]')
# REPEAT_PASSWORD_ERROR_FIELD = (By.CSS_SELECTOR,'div.input_inputError__fLUP9 input[name="submitPassword"]')
# TEXT_ERROR_FIELD_REGISTRATION = (By.CLASS_NAME, "input_span__yWPqB")  # текст ошибки под полем email при регистрации


# MY_LISTING_TITLE = (By.XPATH, '//div[contains(@class, "profilePage_listningBlock__") and .//h1[text()="Мои объявления"]]//h2[text()="Test Product"]')


# locators.py
from selenium.webdriver.common.by import By

class Buttons:
    LOGIN_REGISTER = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Вход и регистрация']")
    NO_ACCOUNT = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Нет аккаунта']")
    CREATE_ACCOUNT = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Создать аккаунт']")
    ADD_CREATION = (By.XPATH, "//button[text()='Разместить объявление']")
    PUBLISH = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Опубликовать']")
    LOGIN = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Войти']")
    LOGOUT = (By.XPATH, "//button[@type='button' and contains(@class, 'btnSmall') and text()='Выйти']")
    PAGE = (By.XPATH, '//button[contains(@class, "arrowButton--right") and not(@disabled)]')

class Inputs:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    REPEAT_PASSWORD = (By.NAME, "submitPassword")
    TITLE = (By.CSS_SELECTOR, 'input[name="name"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea[name="description"]')
    PRICE = (By.CSS_SELECTOR, 'input[name="price"]')

class Dropdowns:
    CITY_BUTTON = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="city"] + button')
    CATEGORY_BUTTON = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="category"] + button')
    CITY_OPTION_SPB = (By.XPATH, '//button[.//span[text()="Санкт-Петербург"]]')
    CATEGORY_OPTION_AUTO = (By.XPATH, '//button[.//span[text()="Авто"]]')

class Radio:
    CONDITION = {
        "new": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Новый"]]'),
        "used": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Б/У"]]'),
    }

class Headers:
    REGISTRATION = (By.XPATH, '//h1[text()="Зарегистрироваться"]')
    CREATION = (By.XPATH, '//h1[text()="Мои объявления"]')
    PROFILE = (By.XPATH, '//h1[text()="Мой профиль"]')
    REGISTRATION_CREATION = (By.XPATH, '//h1[text()="Чтобы разместить объявление, авторизуйтесь"]')

class User:
    NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR = (By.CSS_SELECTOR, "button.circleSmall")

class Errors:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="password"]')
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="submitPassword"]')
    TEXT_REGISTRATION = (By.CLASS_NAME, "input_span__yWPqB")

class Listings:
    TEST_PRODUCT = (By.XPATH, '//div[contains(@class, "profilePage_listningBlock__") and .//h1[text()="Мои объявления"]]//h2[text()="Test Product"]')
