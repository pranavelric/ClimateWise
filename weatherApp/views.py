from django.shortcuts import render
from django.views.generic.base import TemplateView
import urllib.request
import json

# api: 4XS2Ea1S1zP0NbmArsQvVGkBuhBllKh6


class Index(TemplateView):

    template_name = 'weatherapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # form = PostForm()
        # context['form'] = form
        return context    

    def post(self,request, *args, **kwargs):
        city = request.POST['city']
        source =  urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=f4ccf2fc945090572f8743493fa613fb').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "main": str(list_of_data['weather'][0]['main']),
            "temp": str(list_of_data['main']['temp']),
            "pressure":str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon":  str(list_of_data['weather'][0]['icon']),
            "name": str(list_of_data['name']),
            "wind": str(list_of_data['wind']['speed']),
            
        }
        return super(TemplateView, self).render_to_response(data)
    
    def get(self,request, *args, **kwargs):
        data = {}
        return super(TemplateView, self).render_to_response(data)
    

