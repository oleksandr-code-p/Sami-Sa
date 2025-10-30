from django.shortcuts import render, get_object_or_404
from .models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson



def lesson_dashboard(request):
    context = {
        'number_count': NumberLesson.objects.count(),
        'colour_count': ColourLesson.objects.count(),
        'family_count': FamilyLesson.objects.count(),
        'food_count': FoodLesson.objects.count(),
        'page_title': 'Language Learning Dashboard',
        'welcome_message': 'Welcome to Slovak Language Lessons',
    }
    return render(request, 'lessons/dashboard.html', context)


def number_lesson_list(request):
    numbers = NumberLesson.objects.all()

    context = {
        'numbers': numbers,
        'page_title': 'čísla v angličtine',
        'overview': 'short description',
    }

    return render(request, 'lessons/number_list.html', context)


def number_lesson_detail(request, number_id):
    number = get_object_or_404(NumberLesson, id=number_id)

    context = {
        'number': number,
    }
    
    return render(request, "lessons/number_detail.html", context)
    

def colour_lesson_list(request):
    colours = ColourLesson.objects.all()

    context = {
        'colours': colours,
        'page_title': 'farby v angličtine',
        'overview': 'short description',
    }

    return render(request, 'lessons/colour_list.html', context)

def colour_lesson_detail(request, colour_id):
    colour = get_object_or_404(ColourLesson, id=colour_id)

    context = {
        'colour': colour,
    }

    return render(request, 'lessons/colour_detail.html', context)


def family_lesson_list(request):
    family_terms = FamilyLesson.object.all()

    context = {
        'family_terms': family_terms,
        'page_title': 'rodina v angličtine',
        'overview': 'short description',
    }

    return render(request, 'lessons/family_list.html', context)


def family_lesson_detail(request, family_id):
    family = get_object_or_404(FamilyLesson, id=family_id)

    context = {
        'family': family,
    }

    return render(request, 'lessons/family_detail.html', context)


def food_lesson_list(request):
    food_terms = FoodLesson.objects.all()

    context = {
        'food_terms': food_terms,
        'page_title': 'jedlo v angličtine',
        'overview': 'short description',
    }

    return render(request, 'lessons/food_list.html', context)


def food_lesson_detail(request, food_id):
    food = get_object_or_404(FoodLesson, id=food_id)

    context = {
        'food': food,
    }

    return render(request, 'lessons/food_detail.html', context)







# def family_voc_pronun(request):
#     lessons = FamilyLesson.objects.all()

#     family_vocabulary = {
#     "family": "rodina",
#     "father / dad": "otec",
#     "mother / mom": "mama",
#     "brother": "brat",
#     "sister": "sestra",
#     "grandfather / grandpa": "dedo",
#     "grandmother / grandma": "babka",
#     "uncle": "ujo",
#     "aunt": "teta",
#     "cousin": "bratranec / sesternica",
#     "son": "syn",
#     "daughter": "dcéra",
#     "husband": "manžel",
#     "wife": "manželka",
#     "parents": "rodičia",
#     "children / kids": "deti",
#     "baby": "bábätko",
#     "friend": "kamarát",
#     "people": "ľudia"
#     }

#     family_pronunciation = {
#     "family": "fémi",
#     "father / dad": "fáder / dád",
#     "mother / mom": "máder / mám",
#     "brother": "bráder",
#     "sister": "sistr",
#     "grandfather / grandpa": "grándfáder / grándpa",
#     "grandmother / grandma": "grándmáder / grándma",
#     "uncle": "ankl",
#     "aunt": "ant",
#     "cousin": "kazin",
#     "son": "san",
#     "daughter": "dóter",
#     "husband": "hazbend",
#     "wife": "vajf",
#     "parents": "pérents",
#     "children / kids": "čildren / kids",
#     "baby": "bébi",
#     "friend": "frend",
#     "people": "pípol"
#     }

#     context = {
#         'lessons': lessons,
#         'vocabulary': family_vocabulary,
#         'pronunciation': family_pronunciation,
#     }
        
#     return render(request, 'family_voc_pronun.html', context)


