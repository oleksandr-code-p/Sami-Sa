from django.urls import path
from . import views
app_name = 'alphabet'


urlpatterns = [
    path('', views.alphabet_list, name='alphabet_list'),
    path('pronunciation', views.alphabet_pronunciation, name='alphabet_pronunciation')
]