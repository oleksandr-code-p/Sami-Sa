from django.urls import path
from . import views
app_name = 'alphabet'


urlpatterns = [
    path('', views.alphabet_list, name='alphabet_list'),
    path('letter/<int:letter_id>/', views.letter_detail, name='letter_detail'),
    path('pronunciation/', views.pronunciation_guide, name='pronunciation_guide'),
    path('vowels/', views.vowels_list, name='vowels'),
    path('consonants/', views.consonants_list, name='consonants'),
]