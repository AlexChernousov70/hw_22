from urllib import response
import requests
from plyer import notification

# константы 
API_KEY = "23496c2a58b99648af590ee8a29c5348"
CITY = "Москва"
weather_dict = {}
message = ''

def get_weather(city: str, api_key: str):
    """
    Функция вполняет запрос к API и возвращает данные о погоде в виде словаря.
    Аргументы:
        city: str название города для получения прогноза погоды.
        api_key: str ключ API для доступа к сервису.
    Возвращаеn dict словарь с данными о погоде.
    """
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru' # Сформировали URL для запроса
    response = requests.get(url) # Сделали запрос и получили объект ответа
    print(response.status_code) # Получили статус ответа
    weather_dict = response.json() # Получили JSON из объекта ответа
    return print(weather_dict)  # Получили объект Python из JSON
    
get_weather(CITY, API_KEY)


def format_weather_message(weather_dict: dict):
    pass
    """
    Функция форматирует данные о погоде в удобочитаемое сообщение.
    Аргументы weather_dict: Словарь с данными о погоде.
    Возвращает str форматированное сообщение о погоде.
    """
    # return str


def notify_weather(message: str):
    pass
    """ 
    Функция отправляет уведомление пользователю с информацией о погоде.
    - Аргументы: `message`: Сообщение о погоде для уведомления.
    Возвращает: `None`
    """
    # return None


def main():
    pass
    """
    Фукция запускает программу, выполняет вызовы вышеуказанных функций и обрабатывает вывод.
    """
    get_weather(CITY, API_KEY)
    format_weather_message(weather_dict)
    notify_weather(message)

# main()