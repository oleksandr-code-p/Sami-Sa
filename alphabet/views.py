from .models import Letter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

letters = letters.object.all()
vowels = letters.filter(category = 'vowel')
consonants = letters.filter(category = 'consonants')

context = {
    'vowels': vowels,
    'consonants': consonants,
    'letters': letters,
}

return render(request, "alphabet.html", context)