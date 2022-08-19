import requests
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        city = data['name']
        current_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        print(f'Температура в городе {city}: {current_weather}\n'
              f'Влажность: {humidity}\n'
              f'Давление:{pressure}\n'
              f'Скорость ветра: {wind_speed}')
    except Exception as ex:
        print(ex)
        print('Проверьте развание города!')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
