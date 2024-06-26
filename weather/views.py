
from bible_verse import main
from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer

class WeatherView(View):
    def get(self, request):
        verse = main.get_bible_verse()
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        serializer = WeatherSerializer(data=weathers, many=True)
        print(serializer.data)
        return render(request, "home.html", {"weathers":weathers, "verse":verse})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now()
        )
        serializer = WeatherSerializer(data=weather.__dict__)
        if (serializer.is_valid()):
            repository.insert(serializer.data)
        else:
            print(serializer.errors)

        return redirect('Weather View')
    
class WeatherReset(View):
    def get(self, request): 
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()

        return redirect('Weather View')
        

