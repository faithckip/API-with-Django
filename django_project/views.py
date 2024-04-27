import requests
from django.shortcuts import render

def home(request):
    # Define your OpenWeatherMap API key
    
    api_key = "c0f12f7a0708d3aa963e006e6dd473cc"
    # Define the city for weather forecast
    city = "Nairobi"
    
    # Fetch data from GitHub API
    response_github = requests.get("https://api.github.com/events")
    data_github = response_github.json()
    result_github = data_github[0]["repo"]

    # Fetch weather data from OpenWeatherMap API
    url_weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response_weather = requests.get(url_weather)
    data_weather = response_weather.json()
    result_weather = data_weather["main"]["temp"]
    
    # Fetch data from free test API
    response_students = requests.get('https://freetestapi.com/api/v1/students')
    data_students = response_students.json()
    students = data_students[0]["name"]

    # Fetch a random dog image from Dog CEO API
    response_dog = requests.get('https://dog.ceo/api/breeds/image/random')
    data_dog = response_dog.json()
    dog = data_dog['message']
  
    # Render the template with fetched data
    return render(request, 'templates/index.html', {'result_github': result_github, 'students': students, 'dog': dog, 'result_weather': data_weather})

