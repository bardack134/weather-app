from django.shortcuts import render


# Importa la biblioteca 'requests' para realizar solicitudes HTTP.
import requests

# Importa la biblioteca 'json' para trabajar con datos en formato JSON.
import json 

# Importamos el módulo para manejar mensajes
from django.contrib import messages

# Create your views here.
def index(request):
   
    # La solicitud POST no está vacía, procesamosd los datus
    if request.POST:

        city=request.POST["city"]
        # Define la clave de la API.
        apikey='99468f5d704838bdc037ae66b01460e5'#DO NOT PLACE THE API VALUE DIRECTLY IN THE CODE; INSTEAD, USE AN ENVIRONMENT VARIABLE

        # Realiza una solicitud GET a la API de OpenWeatherMap para obtener los datos del clima de la ciudad.
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric')
        
        #voy a comprar primero si la respuesta　de la API fue exitosa
        if response.status_code==200:  # Es decvir si La solicitud a la API fue exitosa
            
            # Convierte la respuesta de la API a texto.
            data_texto=response.text
                
            # Convierte el texto a un diccionario de Python.
            data_diccionario=json.loads(data_texto)

                            

            # Crea un nuevo diccionario con los datos relevantes.
            contexto= {
                # uso de get() con un valor predeterminado 'none' es una forma segura de acceder a claves anidadas, ya que evita errores si alguna de las claves no está presente.
                'latitude':data_diccionario.get('coord', None).get('lon'), #si la clave 'coord' no está presente en el diccionario principal, la variable asociada a 'latitude' será None.
                'longitude':data_diccionario.get('coord', None).get('lat'),
                'weather':data_diccionario.get('weather', None)[0].get('description'),
                'temperature':data_diccionario.get('main', None).get('temp'),
                'feels_like':data_diccionario.get('main', None).get('feels_like'),
                'wind':data_diccionario.get('wind', None).get('speed'),
                'Cloudiness':data_diccionario.get('clouds', None).get('all'),
                'pressure':data_diccionario.get('main').get('pressure'),
                'humidity':data_diccionario.get('main').get('humidity')
                }
                
            return render(request, 'index.html', contexto)
            
    else:
        messages.error(request, 'registered not found')

        return render(request, 'index.html')
            
    return render(request, 'index.html')
   