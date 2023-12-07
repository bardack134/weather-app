from django.http import HttpResponse
from django.shortcuts import render

# Importa la biblioteca 'requests' para realizar solicitudes HTTP.
import requests

# Importa la biblioteca 'json' para trabajar con datos en formato JSON.
import json 



# Create your views here.
def index(request):
    try:

        city='london'
        # Define la clave de la API.
        apikey='99468f5d704838bdc037ae66b01460e5'

        # Realiza una solicitud GET a la API de OpenWeatherMap para obtener los datos del clima de la ciudad.
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric')

        # Convierte la respuesta de la API a texto.
        data_texto=response.text
        
        # Convierte el texto a un diccionario de Python.
        data_diccionario=json.loads(data_texto)

                      

        # Crea un nuevo diccionario con los datos relevantes.
        contexto= {
            'latitude':data_diccionario['coord']['lon'],
            'longitude':data_diccionario['coord']['lat'],
            'weather':data_diccionario['weather'][0]['description'],
            'temperature':data_diccionario['main']['temp'],
            'feels_like':data_diccionario['main']['feels_like'],
            'wind':data_diccionario['wind']['speed'],
            'Cloudiness':data_diccionario['clouds']['all'],
            'pressure':data_diccionario['main']['pressure'],
            'humidity':data_diccionario['main']['humidity']
            }
        
        return render(request, 'index.html', contexto)

        # # Extrae los datos relevantes del diccionario.
        # latitude = data['latitude']
        # longitude= data['longitude']
        # weather_2 = data['weather'] 
        # temperature = data['temperature']
        # feels_like = data['feels_like']
        # wind = data['wind']
        # Cloudiness = data['Cloudiness']
        # pressure = data['pressure']
        # humidity = data['humidity']

        

    # Maneja las excepciones en caso de que ocurra un error al realizar la solicitud HTTP.
    except requests.exceptions.RequestException as err:
        return HttpResponse(f'An error occurred: {str(err)}')

    return render(request, 'index.html')