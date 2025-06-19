from datetime import datetime
import random
import string

def generate_valid_unique_email(domain='yandexpr.ru'):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"testuser_{timestamp}@{domain}"

def generate_invalid_unique_email(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
