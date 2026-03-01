from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Exercise, Exercise_Choice, Matching_Pair, Word_Scramble, Sentence_Completion, Translation, UserProgress, LESSON_TYPES, EXERCISE_TYPES
from lessons.models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson
from django.contrib.auth.decorators import login_required


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
def Exercise_Dashboard(request):

    context = {
        'lesson_types': LESSON_TYPES,
        'exercise_types': EXERCISE_TYPES,
        'page_title': 'Panel učenia jazykov',
        'welcome_message': 'Vitajte v cvičeniach zo angličtiny',
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
# ...existing code...

def Exercise_Choice_list(request):
    queryset = Exercise.objects.filter(exercise_type='multiple_choice').prefetch_related('choices')

    lesson_type = request.GET.get("lesson_type")
    if lesson_type:
        queryset = queryset.filter(lesson_type=lesson_type)

    context = {
        'exercises': queryset,
        'lesson_type': LESSON_TYPES,
        'page_title': 'Cvičenia - výber správnej odpovede',
        'overview': 'Precvič si zručnosti výberom odpovede.',
    }

    return render(request, 'exercises/exercise_choice_list.html', context)

from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

# ...existing code...

@login_required
@require_POST
def submit_answer(request):
    """Handle answer submission for all exercise types"""
    try:
        # Handle both POST form data and JSON data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            exercise_id = data.get("exercise_id")
            is_correct = data.get("is_correct")
        else:
            exercise_id = request.POST.get("exercise_id")
            is_correct = request.POST.get("is_correct") == 'true'
        
        exercise = Exercise.objects.get(id=exercise_id)
        
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            exercise=exercise
        )

        progress.attempts += 1

        if is_correct:
            progress.correct_attempts += 1
            progress.is_completed = True

        progress.save()

        return JsonResponse({
            "success": True,
            "correct": is_correct,
            "attempts": progress.attempts,
            "correct_attempts": progress.correct_attempts,
            "accuracy": round((progress.correct_attempts / progress.attempts) * 100, 1)
        })
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)

def filter_exercises(request, queryset):
    lesson_type = request.GET.get("lesson_type")
    if lesson_type:
        queryset = queryset.filter(exercise__lesson_type=lesson_type)
    
    exercise_type = request.GET.get("exercise_type")
    if exercise_type:
        queryset = queryset.filter(exercise__exercise_type=exercise_type)

    return queryset
    
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
# ...existing code...

# ...existing code...

def Sentence_Completion_list(request):
    completions = Sentence_Completion.objects.select_related("exercise")
    
    lesson_type = request.GET.get("lesson_type")
    if lesson_type:
        completions = completions.filter(exercise__lesson_type=lesson_type)

    context = {
        'completions': completions,
        'lesson_types': LESSON_TYPES,
        'page_title': 'Cvičenia - dopĺňanie do viet',
        'overview': 'Precvič si zručnosti dopĺňaním do viet.',
    }

    return render(request, 'exercises/sentence_completion_list.html', context)


def filter_exercises(request, queryset):
    lesson_type = request.GET.get("lesson_type")
    if lesson_type:
        # For Sentence_Completion, filter by exercise's lesson_type
        if hasattr(queryset.model, 'exercise'):
            queryset = queryset.filter(exercise__lesson_type=lesson_type)
        else:
            queryset = queryset.filter(lesson_type=lesson_type)
    
    return queryset


# --------------------------------------------------
# LIST OF TRANSLATION
# --------------------------------------------------
def Translation_list(request):
    queryset = Translation.objects.select_related("exercise").order_by("id")
    translations = filter_exercises(request, queryset)

    context = {
        "translations": translations,
        "lesson_types": LESSON_TYPES,
        "page_title": "Cvičenia - preklad",
        "overview": "Precvič si zručnosti prekladom viet.",
    }
    return render(request, "exercises/translation_list.html", context)


@login_required
def user_progress(request):
    progress_list = UserProgress.objects.filter(user=request.user).select_related('exercise').order_by('-correct_attempts')
    attempts = 0
    correct_attempts = 0
    for p in progress_list:
        attempts += p.attempts
        correct_attempts += p.correct_attempts
    if attempts > 0:
        overall_accuracy = correct_attempts / attempts * 100
    else: 
        overall_accuracy = 0


    context = {
        'progress_list': progress_list,
        'attempts': attempts,
        'correct_attempts': correct_attempts,
        'overall_accuracy': round(overall_accuracy, 1),
        'page_title': 'Môj pokrok',
    }

    return render(request, 'exercises/user_progress.html', context)