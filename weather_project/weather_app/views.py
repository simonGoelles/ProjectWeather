from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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

def login(request):
    return render(request, 'html/login.html')

def login_search(request):
    if request.method == 'POST':
        print("in search == 'POST'")
        username_id = request.POST.get('username', None)
        password_id = request.POST.get('password', None)
        print(username_id)
        user = authenticate(request, username=username_id, password=password_id)
        if user is not None:
            login(request)
            return redirect('/weather_app/')
        else:
            return redirect('/weather_app/login')

def register(request):
    return render(request, 'html/register.html')

def register_add(request):
    # TODO register
    if request.method == 'POST':
        new_username = request.POST.get('username', None)
        new_password = request.POST.get('password', None)
        new_user = User(username=new_username)
        new_user.set_password(new_password)
        new_user.save()
    else:
        print("Fail")
    return redirect('/weather_app/')
