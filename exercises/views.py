from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Exercise, Exercise_Choice, Matching_Pair, Word_Scramble, Sentence_Completion, Translation, UserProgress
from lessons.models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson
from django.contrib.auth.decorators import login_required


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
@require_POST
def Check_Answer(request):
    answer = request.POST.get("answer")
    correct_answer = request.POST.get("correct_answer")
    is_correct = answer.lower() == correct_answer.lower()

    context = {
        'answer': answer,
        'correct_answer': correct_answer,
        'is_correct': is_correct,
    }

    return render(request, 'exercises/check_answer.html', context)


# --------------------------------------------------
# LIST OF MULTIPLE CHOICE EXERCISES
# --------------------------------------------------
def Exercise_Choice_list(request):
    queryset = Exercise_Choice.objects.select_related("exercise")
    choices = filter_exercises(request, queryset)

    context = {
        'choices': choices,
        'lesson_type': LESSON_TYPES,
        'page_title': 'Cvičenia - výber správnej odpovede',
        'overview': 'Precvič si zručnosti výberom odpovede.',
    }

    return render(request, 'exercises/exercise_choice_list.html', context)


def filter_exercises(request, queryset):
    lesson_type = request.GET.get("lesson_type")
    if lesson_type:
        queryset = queryset.filter(exercise_lesson_type=lesson_type)
    
    exercise_type = request.GET.get("exercise_type")
    if exercise_type:
        queryset = queryset.filter(exercise_exercise_type=exercise_type)

    
# --------------------------------------------------
# LIST OF MATCHING PAIRS
# --------------------------------------------------
def Matching_Pair_list(request):
    queryset = Matching_Pair.objects.select_related("exercise")
    pairs = filter_exercises(request, queryset)


    context = {
        'pairs': pairs,
        'lesson_type': LESSON_TYPES,
        'page_title': 'Cvičenia - spárovanie dvojíc',
        'overview': 'Precvič si spárovanie slov alebo fráz.',
    }

    return render(request, 'exercises/matching_pair_list.html', context)


# --------------------------------------------------
# LIST OF WORD SCRAMBLES
# --------------------------------------------------
def Word_Scramble_list(request):
    queryset = Word_Scramble.objects.select_related("exercise")
    word = filter_exercises(request, queryset)

    context = {
        'word': word,
        'lesson_type': LESSON_TYPES,
        'page_title': 'Cvičenia - rozhádzané slová',
        'overview': 'Precvič si skladanie slov v správnom poradí.',
    }

    return render(request, 'exercises/word_scramble_list.html', context)


# --------------------------------------------------
# LIST OF SENTENCE COMPLETION
# --------------------------------------------------
def Sentence_Completion_list(request):
    queryset = Sentence_Completion.objects.select_related("exercises")
    sentence = filter_exercises(request, queryset)

    context = {
        'sentence': sentence,
        'lesson_type': LESSON_TYPES,
        'page_title': 'Cvičenia - dopĺňanie do viet',
        'overview': 'Precvič si zručnosti dopĺňaním do viet.',
    }

    return render(request, 'exercises/sentence_completion_list.html', context)


# --------------------------------------------------
# LIST OF TRANSLATION
# --------------------------------------------------
def Translation_list(request):
    queryset = Translation.objects.select_related("exercises")
    translate = filter_exercises(request, queryset)

    context = {
        'translate': translate,
        'lesson_type': LESSON_TYPES,         
        'page_title': 'Cvičenia - preklad',
        'overview': 'Precvič si zručnosti prekladom viet.',
    }

    return render(request, 'exercises/translation_list.html', context)


@login_required
def user_progress(request):
    """Display user's progress across all exercises."""
    progress_list = UserProgress.objects.filter(user=request.user).select_related('exercise').order_by('-correct_attempts')

    # Calculate overall stats
    total_attempts = sum(p.attempts for p in progress_list)
    total_correct = sum(p.correct_attempts for p in progress_list)
    overall_accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0

    context = {
        'progress_list': progress_list,
        'total_attempts': total_attempts,
        'total_correct': total_correct,
        'overall_accuracy': round(overall_accuracy, 1),
        'page_title': 'Môj pokrok',
    }

    return render(request, 'exercises/user_progress.html', context)