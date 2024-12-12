from urllib import response
import requests
from plyer import notification

# константы 
API_KEY = "23496c2a58b99648af590ee8a29c5348"
CITY = "Москва"

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
    return weather_dict # Получили объект Python из JSON

def format_weather_message(weather_dict: dict):
    """
    Функция форматирует данные о погоде в удобочитаемое сообщение.
    Аргументы weather_dict: Словарь с данными о погоде.
    Возвращает str форматированное сообщение о погоде.
    """
    global temp, feels_like, description
    temp = round(weather_dict['main']['temp']) # температура
    feels_like = round(weather_dict['main']['feels_like']) # Ощущается как
    description = weather_dict['weather'][0]['description'] # Описание погоды
    message = 'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}' # форматируем сообщение
    return message # возвращаем сообщение

def notify_weather(message: str):
    """ 
    Функция отправляет уведомление пользователю с информацией о погоде.
    - Аргументы: `message`: Сообщение о погоде для уведомления.
    Возвращает: `None`
    """
    notification.notify(
    title='Погода в Москве',
    message=f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}',
    app_name='Weather',
    app_icon=None)  
    '''
    Это метод notify из библиотеки plyer, который создает системное уведомление на вашем компьютере. Параметры:
    title - заголовок уведомления
    message - текст уведомления с данными о погоде (температура, ощущаемая температура и описание)
    app_name - имя приложения, от которого приходит уведомление
    app_icon - иконка уведомления (сейчас не задана)
    '''
    return None

def main():
    """
    Фукция запускает программу, выполняет вызовы вышеуказанных функций и обрабатывает вывод.
    """
    notify_weather(format_weather_message(get_weather(CITY, API_KEY)))
    
if __name__ == '__main__':
    main()