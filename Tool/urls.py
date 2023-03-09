from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('form.html', views.New_DietForm),
]
