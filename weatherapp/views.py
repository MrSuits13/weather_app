# weatherapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from django.views import View  
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Weather
from .forms import WeatherForm

class IndexView(View):
    def get(self, request):
        weathers = Weather.objects.all()
        return render(request, 'index.html', {'weathers': weathers})

class AddWeatherView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')  

    def get(self, request):
        form = WeatherForm()
        return render(request, 'add_weather.html', {'form': form})

    def post(self, request):
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'add_weather.html', {'form': form})

class CustomLoginView(DjangoLoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
