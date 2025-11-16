from django.db import models
from lessons.model import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson

EXERCISE_TYPES = [
    ('translate', 'preloz_text'),
    ('match', 'spoj_slova'),
    ('multiple_choice', 'vyber_spravne'),
]

class Exercises(models.Model):
    lesson_type = models.charfield(max_lenght=10,
        choices = [
            ('number', 'NumberLesson'),
            ('colour', 'ColourLesson'),
            ('family', 'FamilyLesson'),
            ('food', 'FoodLesson'),
            ('school', 'SchoolLesson'),
            ('animal', 'AnimalLesson'),
        ]
    )

    lesson_id = models.IntegerField()
    exercise_type = models.CharField(max_lenght=15, choices=EXERCISE_TYPES)
    question = models.TextField()
    answer = models.TextField()
    options = models.TextField(blank=True, null=True,)

    def __str__(self):
        return(f'{self.lesson_id}, {self.exercise_type}')






















