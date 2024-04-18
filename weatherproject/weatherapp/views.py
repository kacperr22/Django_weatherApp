from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amsterdam'

    appid = '' ## put here you API key 
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid' : appid, 'units':'metric'}
    r = requests.get(url, params=params)
    response = r.json()
    description = response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    date = datetime.date.today()
    temperature = response['main']['temp']
    return render(request, 'weatherapp/index.html',
                  {'description':description,
                   'icon':icon,
                   'temperature':temperature, 'date': date, 'city': city})
