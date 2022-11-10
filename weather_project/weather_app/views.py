from django.shortcuts import render
from django.http import HttpResponse
from src import CityNotFound, WttrClass

# Create your views here.
def index(request):
    return render(request, 'html/plz.html')

def weather_api(request):
    if request.method == 'POST':
        output = ""
        m_plz = request.POST.get('plz', None)

        try:
            _wttr = WttrClass(m_plz)
            _wttr.getWeather()
        except CityNotFound as e:
            output += e.message
        else:
            for i in _wttr.calls:
                output += f'{i["plz"]} {i["city_name"]}<br>'
                output += f'{i["date"]}<br>'
                output += f'tmp: {i["temp"]}<br>'
                output += '<br>'

        return HttpResponse(output)
    return HttpResponse("no")
