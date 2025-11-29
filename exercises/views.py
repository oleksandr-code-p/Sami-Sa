from django.shortcuts import render, get_object_or_404
from .models import Exercise, Exercise_Choice, Matching_Pair, Word_Scramble, Sentence_Completion, Translation, UserProgress
from lessons.models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
def Exercise_Dashboard(request):
    exercise_lt = Exercise.objects.values_list("lesson_type", flat=True).distinct()
    exercise_et = Exercise.objects.values_list("exercise_type", flat=True).distinct()

    context = {
        'exercise_lt': exercise_lt,
        'exercise_et': exercise_et,
        'page_title': 'Language Learning Dashboard',
        'welcome_message': 'Welcome to Slovak Language Exercises',
    }

    return render(request, 'exercises/exercise_dashboard.html', context)


# --------------------------------------------------
# CHECK ANSWER (placeholder)
# --------------------------------------------------
def Check_Answer(request):
    answer = request.POST.get("answer")
    correct_answer = request.POST.get("correct_answer")

    context = {
        'answer': answer,
        'correct_answer': correct_answer,
    }

    return render(request, 'exercises/check_answer.html', context)


# --------------------------------------------------
# LIST OF MULTIPLE CHOICE EXERCISES
# --------------------------------------------------
def Exercise_Choice_list(request):
    Choice_Exercises = Exercise_Choice.objects.all()

    context = {
        'Choice_Exercises': Choice_Exercises,
        'page_title': 'Cvičenia - výber správnej odpovede',
        'overview': 'Precvič si zručnosti výberom odpovede.',
    }

    return render(request, 'exercises/exercise_choice_list.html', context)


# --------------------------------------------------
# LIST OF MATCHING PAIRS
# --------------------------------------------------
def Matching_Pair_list(request):
    Matching_Pairs = Matching_Pair.objects.all()

    context = {
        'Matching_Pairs': Matching_Pairs,
        'page_title': 'Cvičenia - spárovanie dvojíc',
        'overview': 'Precvič si spárovanie slov alebo fráz.',
    }

    return render(request, 'exercises/matching_pair_list.html', context)


# --------------------------------------------------
# LIST OF WORD SCRAMBLES
# --------------------------------------------------
def Word_Scramble_list(request):
    Word_Scrambles = Word_Scramble.objects.all()

    context = {
        'Word_Scrambles': Word_Scrambles,
        'page_title': 'Cvičenia - rozhádzané slová',
        'overview': 'Precvič si skladanie slov v správnom poradí.',
    }

    return render(request, 'exercises/word_scramble_list.html', context)


# --------------------------------------------------
# LIST OF SENTENCE COMPLETION
# --------------------------------------------------
def Sentence_Completion_list(request):
    Sentence_Completions = Sentence_Completion.objects.all()

    context = {
        'Sentence_Completions': Sentence_Completions,
        'page_title': 'Cvičenia - dopĺňanie do viet',
        'overview': 'Precvič si zručnosti dopĺňaním do viet.',
    }

    return render(request, 'exercises/sentence_compleion_list.html', context)


# --------------------------------------------------
# LIST OF TRANSLATION
# --------------------------------------------------
def Translation_list(request):
    Translations = Translation.objects.all()

    context = {
        'Translations': Translations,
        'page_title': 'Cvičenia - preklad',
        'overview': 'Precvič si zručnosti prekladom viet.',
    }

    return render(request, 'exercises/translation_list.html', context)














