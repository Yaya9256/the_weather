import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=aef6346f7fefc83d28a3eacbf3af68e4'
    city = 'Prague'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    return render(request, 'weather.html', context)