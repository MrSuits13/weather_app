from django.urls import path
from weatherapp.views import IndexView, AddWeatherView, CustomLoginView, RegisterView  

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddWeatherView.as_view(), name='add_weather'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  
]
