# Laboratory work №5 (Variant 21)
---
### I. 
1. Create a class Weather (day, city, country, temp, humidity, wind speed).  
2. Add enum type: SUNNY, CLOUDY, RAINY, FOGGY, …. 
3. Add a WeatherCalendar class that contains Weather objects. 
4. Define the function findMaxTemprature( Weather*, day) - find the maximum temperature from the list of weather records for a certain day, if such a day does not exist, then output: "Not enough data". 
5. Add a method for predicting whether the weather record belongs to Lviv isLvivWeather(humidity, type): if humidity > 80% and type = “RAINY”, then output: “The typical day in Lviv”, otherwise: “You're lucky, man". 
6. Sort weather records by day.