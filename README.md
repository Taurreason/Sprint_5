# Selenium UI Tests for Registration, Login and Listing Creation

## Структура проекта
.
├── tests/
│ ├── test_registration.py       # Тесты регистрации
│ ├── test_login.py              # Тесты логина и выхода
│ ├── test_creation.py           # Тесты создания объявления
├── locators.py                  # Все локаторы, структурированные по типу элемента
├── conftest.py                  # Pytest фикстуры: WebDriver, логин, email-генерация
├── helpers.py                   # Вспомогательные функции: генерация email
├── README.md                    # Документация проекта


---

## Что покрывают тесты

### Регистрация:
- Успешная регистрация нового пользователя
- Ошибка при вводе некорректного email
- Ошибка при регистрации с уже существующим email

### Авторизация:
- Успешный вход в систему
- Выход из системы и проверка, что элементы авторизации исчезают

### Объявления:
- Переход на форму логина при попытке разместить объявление в неавторизованном состоянии
- Успешное размещение объявления авторизованным пользователем, появление в профиле

---

## Требования

- Python 3.8+
- Google Chrome
- Установленные зависимости:

```bash
pip install selenium pytest
```

## Запуск тестов

```bash
pytest tests/
```

Можно также добавить ключи:

```bash
pytest -v       # подробный вывод
```

## Обзор ключевых файлов

### tests/

Содержит модульные файлы с тестами:

* `test_registration.py` — регистрация
* `test_login.py` — логин и логаут
* `test_creation.py` — размещение объявления

### locators.py

Все локаторы сгруппированы по смыслу в классы:

* `Buttons`
* `Inputs`
* `Headers`
* `User`
* `Errors`
* `Dropdowns`
* `Radio`
* `Listings`

Пример обращения к локаторам:

```python
Buttons.LOGIN
User.AVATAR
```

### conftest.py

Pytest-файл с фикстурами:

* `driver()` — запуск и закрытие `ChromeDriver`
* `login_user()` — вход в систему как зарегистрированный пользователь
* `unique_valid_email()` / `unique_invalid_email()` — генерация email для различных кейсов

### helpers.py

Вспомогательные функции:

* `generate_valid_unique_email()` — email с временной меткой
* `generate_invalid_unique_email()` — email без домена (для проверки валидации)