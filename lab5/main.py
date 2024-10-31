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

    def is_lviv_weather(self):
        if self.__humidity > 80 and self.__weather_type == WeatherType.RAINY:
            return 'Typical Lviv weather...'
        else:
            return 'You\'re lucky, man...'

    def __str__(self):
        return (f'Day: {self.__day}\nCity: {self.__city}\nCountry: {self.__country}\n'
                f'Temperature: {self.__temp}°C\nHumidity: {self.__humidity}%\n'
                f'Wind speed: {self.__wind_speed} km/h\nType of weather: {self.__weather_type.value}\n'
                f'{self.is_lviv_weather()}')

class WeatherCalendar():
    def __init__(self):
        self.__records = []

    def add_weather(self, weather):
        self.__records.append(weather)

    def get_records(self):
        return self.__records

def find_max_temperature(weather_calendar, day):
    temps_for_specific_day = []

    for record in weather_calendar.get_records():
        if record.get_day() == day:
            temps_for_specific_day.append(record.get_temp())

    if not temps_for_specific_day:
        print('Not enough data.')
    else:
        max_temp = 0

        for temp in temps_for_specific_day:
            if temp > max_temp:
                max_temp = temp
        
        print(f'\nThe maximum temperature on {day} is {max_temp}°C')

def sort_by_day(weathers):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ordered_weathers = []

    for day in days_of_week:
        for weather in weathers:
            if weather.get_day() == day:
                ordered_weathers.append(weather)

    return ordered_weathers

def print_weather_calendar(weather_calendar):
    print('Weather calendar:')
    for weather in weather_calendar.get_records():
        print(f'\n{weather}')

def main():
    weather1 = Weather('Monday', 'Lviv', 'Ukraine', 13, 85, 24, WeatherType.RAINY)
    weather2 = Weather('Monday', 'Stanislaviv', 'Ukraine', 15, 60, 10, WeatherType.SUNNY)
    weather3 = Weather('Tuesday', 'Ternopil', 'Ukraine', 10, 50, 15, WeatherType.CLOUDY)
    weather4 = Weather('Saturday', 'Lviv', 'Ukraine', 10, 89, 27, WeatherType.RAINY)
    weather5 = Weather('Sunday', 'Kyiv', 'Ukraine', 12, 64, 10, WeatherType.FOGGY)
    weather6 = Weather('Saturday', 'Luhansk', 'Ukraine', 9, 79, 23, WeatherType.SNOWY)
    weather7 = Weather('Tuesday', 'Ternopil', 'Ukraine', 11, 80, 18, WeatherType.RAINY)
    weather8 = Weather('Wednesday', 'Sudzha', 'Ukraine', 8, 100, 15, WeatherType.RAINY)
    weather9 = Weather('Thursday', 'Xarkiv', 'Ukraine', 9, 45, 15, WeatherType.SUNNY)
    weather10 = Weather('Thursday', 'Peremyszl', 'Poland', 14, 80, 15, WeatherType.RAINY)
    weather11 = Weather('Friday', 'Zhytomyr', 'Ukraine', 10, 58, 15, WeatherType.CLOUDY)

    weathers = [weather1, weather2, weather3, weather4, weather5,
                weather6, weather7, weather8, weather9, weather10, weather11]
    
    ordered_weathers = sort_by_day(weathers)
    
    weather_calendar1 = WeatherCalendar()

    for weather in ordered_weathers:
        weather_calendar1.add_weather(weather)

    print_weather_calendar(weather_calendar1)
    find_max_temperature(weather_calendar1, 'Monday')
    
main()