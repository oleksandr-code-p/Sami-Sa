from .models import Letter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


def alphabet_list(request):
    letters = Letter.objects.all()
    vowels = letters.filter(category='vowel')
    consonants = letters.filter(category='consonant')
    
    context = {
        'letters': letters,
        'vowels': vowels,
        'consonants': consonants,
    }
    return render(request, "alphabet/alphabet.html", context)


def letter_detail(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    context = {
        'letter': letter,
    }
    return render(request, "alphabet/letter_detail.html", context)


def pronunciation_guide(request):
    pronunciation_in_slovak = {
        "A": "ej", "B": "bí", "C": "cí", "D": "dí", 
        "E": "í", "F": "ef", "G": "dží", "H": "ejč", 
        "I": "ai", "J": "džej", "K": "kej", "L": "el", 
        "M": "em", "N": "en", "O": "ou", "P": "pí", 
        "Q": "kju", "R": "ar", "S": "es", "T": "tí", 
        "U": "ju", "V": "ví", "W": "dabl ju", "X": "ex", 
        "Y": "vaj", "Z": "zet/zí"
    }
    
    context = {
        'pronunciation_in_slovak': pronunciation_in_slovak,
    }
    return render(request, "alphabet/alphabet_pronunciation.html", context)


def vowels_list(request):
    vowels = Letter.objects.filter(category='vowel')
    context = {
        'letters': vowels,
        'title': 'Vowels (Samohlásky)',
        'category': 'vowel'
    }
    return render(request, "alphabet/category_list.html", context)


def consonants_list(request):
    consonants = Letter.objects.filter(category='consonant')
    context = {
        'letters': consonants,
        'title': 'Consonants (Spoluhlásky)',
        'category': 'consonant'
    }
    return render(request, "alphabet/category_list.html", context)




