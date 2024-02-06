from django.contrib import admin
from django.urls import path, include
from weatherapp.views import IndexView, AddWeatherView, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherapp/', include('weatherapp.urls')),
    path('', IndexView.as_view(), name='index'),
    path('add/', AddWeatherView.as_view(), name='add_weather'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
