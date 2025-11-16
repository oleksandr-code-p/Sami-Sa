from django.shortcuts import render, get_object_or_404
from .models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson



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
        'overview': 'Learn the basic numbers in English, practice pronunciation, and count from 1 to 1000',
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
        'overview': 'Discover common colours in English and practice saying them correctly.',
    }

    return render(request, 'lessons/colour_list.html', context)

def colour_lesson_detail(request, colour_id):
    colour = get_object_or_404(ColourLesson, id=colour_id)

    context = {
        'colour': colour,
    }

    return render(request, 'lessons/colour_detail.html', context)


def family_lesson_list(request):
    family_terms = FamilyLesson.objects.all()

    context = {
        'family_terms': family_terms,
        'page_title': 'rodina v angličtine',
        'overview': 'Learn family-related words, practice pronunciation, and use them in simple phrases.',
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
        'overview': 'Explore everyday food items, learn their names, and practice pronunciation.',
    }

    return render(request, 'lessons/food_list.html', context)


def food_lesson_detail(request, food_id):
    food = get_object_or_404(FoodLesson, id=food_id)

    context = {
        'food': food,
    }

    return render(request, 'lessons/food_detail.html', context)


def school_lesson_list(request):
    school_terms = SchoolLesson.objects.all()

    context = {
        'school_terms': school_terms,
        'page_title': 'škola v angličtine',
        'overview': 'Get familiar with school vocabulary, classroom objects, and simple phrases.',
    }

    return render(request, 'lessons/school_list.html', context)


def school_lesson_detail(request, school_id):
    school = get_object_or_404(SchoolLesson, id=school_id)

    context = {
        'school': school,
    }

    return render(request, 'lessons/school_detail.html', context)


def animal_lesson_list(request):
    animals = AnimalLesson.objects.all()

    context = {
        'animals': animals,
        'page_title': 'zvierata v angličtine',
        'overview': 'short description',
    }

    return render(request, 'lessons/animal_list.html', context)


def animal_lesson_detail(request, animal_id):
    animal = get_object_or_404(AnimalLesson, id=animal_id)

    context = {
        'animal': animal,
    }

    return render(request, 'lessons/animal_detail.html', context),

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


