from enum import Enum

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
        return (f'Day: {self.__day}\nCity: {self.__city}\nCountry: {self.__country}\n'
                f'Temperature: {self.__temp}°C\nHumidity: {self.__humidity}%\n'
                f'Wind speed: {self.__wind_speed} km/h\nType of weather: {self.__weather_type.value}')

class WeatherCalendar():
    def __init__(self):
        self.__records = []

    def add_weather(self, weather):
        self.__records.append(weather)

    def get_records(self):
        return self.__records

def print_broadcast(broadcast):
    print('Weather broadcast is:')
    for weather in broadcast.get_records():
        print(f'\n{weather}')

def main():
    weather1 = Weather("Monday", "Lviv", "Ukraine", 13, 85, 24, WeatherType.RAINY)
    weather2 = Weather("Monday", "Stanislaviv", "Ukraine", 15, 60, 10, WeatherType.SUNNY)
    weather3 = Weather("Tuesday", "Ternopil", "Ukraine", 10, 70, 15, WeatherType.CLOUDY)

    broadcast1 = WeatherCalendar()

    broadcast1.add_weather(weather1)
    broadcast1.add_weather(weather2)
    broadcast1.add_weather(weather3)

    print_broadcast(broadcast1)

main()