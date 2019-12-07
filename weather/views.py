import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bbcf8d6b286458ad4ea994cb2a9af5f6'

    if request.method == 'POST':

        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []




    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {

            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],

        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data , 'form' : form}




    return render(request, 'weather/index.html' , context)


