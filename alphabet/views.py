from .models import Letter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

def alphabet(request):
    uppercase = []
    lowercase = []
    i = 65
    while i <= 90:
        uppercase.append(chr(i))
        i += 1
    j = 97
    while j <= 122:
        lowercase.append(chr(j))
        j += 1
    context = {
        'uppercase': uppercase,
        'lowercase': lowercase,
    }
    return(request, context)
        

def letter_list(request):
    letters = Letter.object.all()
    vowels = letters.filter(category = 'vowel')
    consonants = letters.filter(category = 'consonants')
    context = {
        'letters': letters,
        'vowels': vowels,
        'consonants': consonants,
    }
    return render(request, "alphabet/list.html", context)


def pronunciation_alphabet(request):
    pronounciation_in_slovak = {"A": "ej", "B": "bí", "C": "cí", "D": "dí", "E": "í", "F": "ef", "G": "dží", "H": "ejč", "I": "ai", "J": "džej", "K": "kej", "L": "el", "M": "em", "N": "en", "O": "ou", "P": "pí", "Q": "kju", "R": "ar", "S": "es", "T": "tí", "U": "ju", "V": "ví", "W": "dabl ju", "X": "ex", "Y": "vaj", "Z": "zet/zí"}
    context{
        'pronounciation_in_slovak': pronounciation_in_slovak,
    }
    return (request, context)





    