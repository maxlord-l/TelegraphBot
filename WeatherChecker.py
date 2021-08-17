import requests
from datetime import datetime
current_datetime = datetime.now()
s_city = "Saint Petersburg,RU"
city_id = 498817
appid = '5dcefac1583b994bdf51528966b802e4'
def get_weather(city_id,):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print(current_datetime)
        print("Погода:", data['weather'][0]['description'])
        print("Температура:", data['main']['temp'])
        print("Минимальная:", data['main']['temp_min'])
        print("Максимальная:", data['main']['temp_max'])
    except Exception as e:
        print("Exception (weather):", e)
        pass
get_weather(498817)