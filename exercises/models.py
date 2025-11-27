from django.db import models
from lessons.model import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson
from alphabet.models import Letter


EXERCISE_TYPES = [
    ('translation', 'Translation'),
    ('matching', 'Matching'),
    ('multiple_choice', 'Multiple_Choice'),
    ('sentence_completion', 'Sentence_Completion'),
    ('word_scramble', 'Word_Scramble'),   
]

LESSON_TYPES = [
    ('number', 'Numbers'),
    ('colour', 'Colours'),
    ('family', 'Family'),
    ('food', 'Food'),
    ('school', 'School'),
    ('animal', 'Animals'),
    ('alphabet', 'Alphabet'),
]


DIFFICULTY_LEVELS = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]


class Exercise(models.Model):
    title = models.TextField()
    lesson_type = models.TextField(choices=LESSON_TYPES)
    exercise_type = models.TextField(choices=EXERCISE_TYPES)
    difficulty = models.TextField(choices=DIFFICULTY_LEVELS, default='beginner')
    question_text = models.TextField()
    correct_answer = models.TextField()
    explanaion = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    number_lesson = models.ForeignKey(NumberLesson, on_delete=models.CASCADE, null=True, blank=True)
    colour_lesson = models.Foreignkey(ColourLesson, on_delete=models.CASCADE, null=True, blank=True)
    family_lesson = models.ForeignKey(FamilyLesson, on_delete=models.CASCADE, null=True, blank=True)
    food_lesson = models.ForeignKey(FoodLesson, on_delete=models.CASCADE, null=True, blank=True)
    school_lesson = models.ForeignKey(FoodLesson, on_ddelete=models.CASCADE, null=True, blank=True)
    animal_lessom = models.ForeignKey(AnimalLesson, on_delete=models.Cascade, null=True, blank=True)


    def str(self):
        return f"{self.title}({self.exercise_type})"


    class Meta:
        ordering = ['lesson_type', 'order']
    

    def get_related_lesson(self):
        if self.lesson_type == 'number':
            return self.number_lesson 
        elif self.lesson_type == 'colour':
            return self.colour_lesson
        elif self.lesson_type == 'family':
            return self.family_lesson
        elif self.lesson_type == 'food':
            return self.food_lesson
        elif self.lesson_type == 'school':
            return self.school_lesson
        elif self.lesson_type == 'animal':
            return self.animal_lesson














