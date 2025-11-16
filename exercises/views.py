from django.shortcuts import render, get_object_or_404
from .models import Exercise

def exercise_list(request):
    exercises = Exercise.objects.filter(lesson_type=lesson_type)
    context = {
        'exercises': exercises
        'lesson_type': lesson_type
    }
    return render(request, 'templates/exercise_list.html', context)

def exercise_detail(request,exercise_id):
    exercise = get_object_or_404(Exercise, exercise_id)

    if request.method == "POST":
        user_answer = request.POST.get('answer')
        correct = user_answer.strip().lower() == exercise.answer.strip().lower()

        context = {
            'exercise': exercise,
            'correct': correct,
            'user_answer': user_answer
        }
        return render(request, 'templates/exercise_result.html', context)


    return render(request, 'templates/exercise_detail.html', {'exercise'; exercise})