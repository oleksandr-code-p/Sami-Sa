from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lesson_dashboard, name='lesson_dashboard'),

    path('numbers/', views.number_lesson_list, name='number_lesson_list'),

    path('colours/', views.colour_lesson_list, name='colour_lesson_list'),

    path('family_terms/', views.family_lesson_list, name='family_lesson_list'),
   
    path('food_terms/', views.food_lesson_list, name='food_lesson_list'),

    path('school_terms', views.school_lesson_list, name='school_lesson_list'),

    path('animals', views.animal_lesson_list, name='animal_lesson_list'),
  
]