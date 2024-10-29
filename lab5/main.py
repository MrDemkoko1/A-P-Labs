from enum import Enum
from typing import List

class WeatherType(Enum):
    SUNNY = 'Sunny'
    CLOUDY = 'Cloudy'
    RAINY = 'Rainy'
    FOGGY = 'Foggy'
    SNOWY = 'Snowy'

class Weather:
    def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type):
        self.__day = day
        self.__city = city
        self.__country = country
        self.__temp = temp
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__weather_type = weather_type

    def get_day(self):
        return self.__day

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_temp(self):
        return self.__temp

    def get_humidity(self):
        return self.__humidity

    def get_wind_speed(self):
        return self.__wind_speed
    
    def get_weather_type(self):
        return self.__weather_type

    def __str__(self):
        return f'Day: {self.__day}\nCity: {self.__city}\nCountry: {self.__country}\nTemperature: {self.__temp}\nHumidity: {self.__humidity}%\nWind speed: {self.__wind_speed} km/h\nType of weather: {self.__weather_type}'

class WeatherCalendar(Weather):
    pass

def main():
    weather_broadcast_1 = Weather('Monday', 'Lviv', 'Ukraine', 13, 60, 24, 'Cloudy')

    print(weather_broadcast_1)

main()