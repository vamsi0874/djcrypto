from django.urls import path
from . import views
from .views import Login
urlpatterns = [
    path('llogin',Login.as_view(),name='llogin'),
    path('register' , views.register , name = 'register'),
    path('login' , views.login , name = 'login'),
    path('' , views.index , name = 'index'),
    
]

