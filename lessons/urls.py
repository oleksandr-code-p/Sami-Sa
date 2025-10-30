from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lesson_dashboard, name='lesson_dashboard'),

    path('numbers/', views.number_lesson_list, name='number_lesson_list'),
    path('numbers/<int:number_id>/', views.number_lesson_detail, name='number_lesson_detail'),

    path('colours/', views.colour_lesson_list, name='colour_lesson_list'),
    path('colours/<int:colour_id>/', views.colour_lesson_detail, name='colour_lesson_detail'),

    path('family_terms/', views.family_lesson_list, name='family'),
    path('family_terms/<int:family_id>/', views.family_lesson_detail, name='family_detail'),
    
    path('food_terms/', views.food_lesson_list, name='food_terms'),
    path('food_terms/<int:food_id>/', views.food_lesson_detail, name='food_detail'),
    
]