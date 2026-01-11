from django.shortcuts import render, get_object_or_404
from .models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson



def lesson_dashboard(request):
    context = {
        'page_title': 'Panel učenia jazykov',
        'welcome_message': 'Vitajte v lekciách slovenčiny',
    }
    return render(request, 'lessons/dashboard.html', context)


def number_lesson_list(request):
    numbers = NumberLesson.objects.all()

    context = {
        'numbers': numbers,
        'page_title': 'čísla v angličtine',
        'overview': 'Nauč sa základné čísla v angličtine, precvičuj výslovnosť a počítaj od 1 do 1000.',
    }

    return render(request, 'lessons/number_list.html', context)
    

def colour_lesson_list(request):
    colours = ColourLesson.objects.all()

    context = {
        'colours': colours,
        'page_title': 'farby v angličtine',
        'overview': 'Objav bežné farby v angličtine a precvičuj ich správnu výslovnosť.',
    }

    return render(request, 'lessons/colour_list.html', context)


def family_lesson_list(request):
    family_terms = FamilyLesson.objects.all()

    context = {
        'family_terms': family_terms,
        'page_title': 'rodina v angličtine',
        'overview': 'Nauč sa slová súvisiace s rodinou, precvičuj výslovnosť a používaj ich v jednoduchých vetách.',
    }

    return render(request, 'lessons/family_list.html', context)


def food_lesson_list(request):
    food_terms = FoodLesson.objects.all()

    context = {
        'food_terms': food_terms,
        'page_title': 'jedlo v angličtine',
        'overview': 'Preskúmaj každodenné potraviny, nauč sa ich názvy a precvičuj výslovnosť.',
    }

    return render(request, 'lessons/food_list.html', context)


def school_lesson_list(request):
    school_terms = SchoolLesson.objects.all()

    context = {
        'school_terms': school_terms,
        'page_title': 'škola v angličtine',
        'overview': 'Zoznaj sa so školskou slovnou zásobou, predmetmi v triede a jednoduchými vetami.',
    }

    return render(request, 'lessons/school_list.html', context)


def animal_lesson_list(request):
    animals = AnimalLesson.objects.all()

    context = {
        'animals': animals,
        'page_title': 'zvierata v angličtine',
        'overview': 'Nauč sa názvy zvierat v angličtine a precvičuj ich výslovnosť.',
    }

    return render(request, 'lessons/animal_list.html', context)


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


