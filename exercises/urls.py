from django.urls import path
from . import views

app_name = "exercises"

urlpatterns = [
    path("", views.Exercise_Dashboard, name="exercise_dashboard"),

    path("choices/", views.Exercise_Choice_list, name="exercise_choice_list"),

    path("matching/", views.Matching_Pair_list, name="matching_pair_list"),

    path("scrambles/", views.Word_Scramble_list, name="word_scramble_list"),

    path("translations/", views.Translation_list, name="translation_list"),

    path("completion/", views.Sentence_Completion_list, name="sentence_completion_list"),
]
