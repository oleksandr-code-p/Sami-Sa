from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
    path('<str:lesson_type>/', views.exercise_list, name='exercise_list'),
    path('detail/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
]