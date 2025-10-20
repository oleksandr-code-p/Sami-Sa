from django.shortcuts import render
from .models import Letter
from django.shortcuts import get_object_or_404
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

    return render(request, 'alphabet/alphabet.html', context)

def alphabet_pronunciation(request):
    pronunciation_in_slovak = {
        "A": "ej", "B": "bí", "C": "cí", "D": "dí", "E": "í",
        "F": "ef", "G": "dží", "H": "ejč", "I": "ai", "J": "džej",
        "K": "kej", "L": "el", "M": "em", "N": "en", "O": "ou",
        "P": "pí", "Q": "kju", "R": "ar", "S": "es", "T": "tí",
        "U": "ju", "V": "ví", "W": "dabl ju", "X": "ex", "Y": "vaj",
        "Z": "zet/zí"
    }
    
    context = {
        'pronunciation_in_slovak': pronunciation_in_slovak,
    }

    return render(request, 'alphabet/alphabet_pronunciation.html', context)




