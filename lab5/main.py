from enum import Enum


class WeatherType(Enum):
    SUNNY = 'Sunny'
    CLOUDY = 'Cloudy'
    RAINY = 'Rainy'
    FOGGY = 'Foggy'
    SNOWY = 'Snowy'


class Weather:
    def __init__(self, day, city, region, country, temp, humidity, wind_speed, pressure, weather_type):
        self.__day = day
        self.__city = city
        self.__region = region 
        self.__country = country
        self.__temp = temp
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__pressure = pressure
        self.__weather_type = weather_type

    def get_day(self):
        return self.__day

    def get_city(self):
        return self.__city
    
    def get_region(self):
        return self.__region

    def get_country(self):
        return self.__country

    def get_temp(self):
        return self.__temp

    def get_humidity(self):
        return self.__humidity
   
    def get_wind_speed(self):
        return self.__wind_speed
    
    def get_pressure(self):
        return self.__pressure

    def get_weather_type(self):
        return self.__weather_type

    def is_lviv_weather(self):
        if self.__humidity > 80 and self.__weather_type == WeatherType.RAINY:
            return 'Typical Lviv weather...'
        else:
            return 'You\'re lucky, man...'

    def __str__(self):
        return (f'Day: {self.__day}\nCity: {self.__city}\n'
                f'Region: {self.__region}\nCountry: {self.__country}\n'
                f'Temperature: {self.__temp}°C\nHumidity: {self.__humidity}%\n'
                f'Wind speed: {self.__wind_speed} km/h\nPressure: {self.__pressure} mmHg\n'
                f'Type of weather: {self.__weather_type.value}\n'
                f'{self.is_lviv_weather()}')


class WeatherCalendar():
    def __init__(self):
        self.__records = []

    def add_weather(self, weather):
        self.__records.append(weather)

    def get_records(self):
        return self.__records

    def find_max_temperature(self, day):
        max_temp = None
        city = None

        for record in self.__records:
            if record.get_day() == day:
                temp = record.get_temp()

                if max_temp is None or temp > max_temp:
                    max_temp = temp
                    city = record.get_city()
        
        if max_temp is None:
            print('Not enough data.')
        else:
            print(f'\nThe maximum temperature on {day} is {max_temp}°C in {city}')
            
    def find_av_press_and_wind_dir(self, day):
        region_pressures = {}

        for record in self.__records:
            if record.get_day() == day:
                region = record.get_region()

                if region not in region_pressures:
                    region_pressures[region] = []

                region_pressures[region].append(record.get_pressure())

        avg_pressures = {}

        for region, pressures in region_pressures.items():
            sum_of_pressures = 0
            for pressure in pressures:
                sum_of_pressures += pressure
            avg_pressures[region] = sum_of_pressures / len(pressures)

        max_pressure = float('-inf')
        max_pressure_region = None
        min_pressure = float('inf')
        min_pressure_region = None

        for region, pressure in avg_pressures.items():
            if pressure > max_pressure:
                max_pressure = pressure
                max_pressure_region = region
            if pressure < min_pressure:
                min_pressure = pressure
                min_pressure_region = region
        
        if len(avg_pressures) < 2:
            print('Records for this day are from one region, wind direction can\'t be known')
        else:
            print(f'On {day} wind blows from {max_pressure_region} region to '
                  f'{min_pressure_region} region with wind coef: {max_pressure - min_pressure}')

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
    weather1 = Weather('Monday', 'Lwiw', 'Lwiw', 'Ukraine', 13, 85, 24, 738, WeatherType.RAINY)
    weather2 = Weather('Monday', 'Terebowla', 'Ternopil', 'Ukraine', 15, 60, 10, 743, WeatherType.SUNNY)
    weather3 = Weather('Tuesday', 'Stryj', 'Lwiw', 'Ukraine', 10, 50, 15, 729, WeatherType.CLOUDY)
    weather4 = Weather('Saturday', 'Basiwka', 'Lwiw', 'Ukraine', 10, 89, 27, 717, WeatherType.RAINY)
    weather5 = Weather('Sunday', 'Ternopil', 'Ternopil', 'Ukraine', 12, 64, 10, 770, WeatherType.FOGGY)
    weather6 = Weather('Saturday', 'Strusiw', 'Ternopil', 'Ukraine', 9, 79, 23, 736, WeatherType.SNOWY)
    weather7 = Weather('Tuesday', 'Ternopil', 'Ternopil', 'Ukraine', 11, 80, 18, 705, WeatherType.RAINY)
    weather8 = Weather('Wednesday', 'Czortkiw', 'Ternopil', 'Ukraine', 8, 100, 15, 777, WeatherType.RAINY)
    weather9 = Weather('Thursday', 'Stanisławiw', 'Stanisławiw', 'Ukraine', 9, 45, 15, 758, WeatherType.SUNNY)
    weather10 = Weather('Thursday', 'Basiwka', 'Lwiw', 'Ukraine', 14, 80, 15, 729, WeatherType.RAINY)
    weather11 = Weather('Sunday', 'Łućk', 'Wołyń', 'Ukraine', 13, 85, 24, 738, WeatherType.RAINY)
    weather12 = Weather('Friday', 'Kalusz', 'Stanisławiw', 'Ukraine', 10, 58, 15, 756, WeatherType.CLOUDY)
    weather13 = Weather('Friday', 'Jaremcze', 'Stanisławiw', 'Ukraine', 10, 58, 15, 718, WeatherType.CLOUDY)
    weather14 = Weather('Wednesday', 'Drohobycz', 'Lwiw', 'Ukraine', 13, 85, 24, 738, WeatherType.RAINY)

    weathers = [weather1, weather2, weather3, weather4, weather5,
                weather6, weather7, weather8, weather9, weather10, 
                weather11, weather12, weather13, weather14]
    
    ordered_weathers = sort_by_day(weathers)
    weather_calendar1 = WeatherCalendar()

    for weather in ordered_weathers:
        weather_calendar1.add_weather(weather)

    print_weather_calendar(weather_calendar1)

    weather_calendar1.find_max_temperature('Monday')
    weather_calendar1.find_av_press_and_wind_dir('Monday')

main()