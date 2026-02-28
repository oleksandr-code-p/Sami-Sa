from django.db import models
from lessons.models import NumberLesson, ColourLesson, FamilyLesson, FoodLesson, SchoolLesson, AnimalLesson

EXERCISE_TYPES = [
    ('translation', 'Translation'),
    ('matching', 'Matching'),
    ('multiple_choice', 'Multiple Choice'),
    ('sentence_completion', 'Sentence Completion'),
    ('word_scrambles', 'Word Scramble'),
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

class Exercise(models.Model):
    title = models.TextField()
    lesson_type = models.TextField(choices=LESSON_TYPES)
    exercise_type = models.TextField(choices=EXERCISE_TYPES)
    question_text = models.TextField()
    correct_answer = models.TextField()
    explanation = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    number_lesson = models.ForeignKey(NumberLesson, on_delete=models.CASCADE, null=True, blank=True)
    colour_lesson = models.ForeignKey(ColourLesson, on_delete=models.CASCADE, null=True, blank=True)
    family_lesson = models.ForeignKey(FamilyLesson, on_delete=models.CASCADE, null=True, blank=True)
    food_lesson = models.ForeignKey(FoodLesson, on_delete=models.CASCADE, null=True, blank=True)
    school_lesson = models.ForeignKey(SchoolLesson, on_delete=models.CASCADE, null=True, blank=True)
    animal_lesson = models.ForeignKey(AnimalLesson, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['lesson_type', 'order']

    def __str__(self):
        return f"{self.title} ({self.exercise_type})"


class Exercise_Choice(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.choice_text


class Matching_Pair(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='matching_pairs')
    left_text = models.TextField()
    right_text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.left_text} → {self.right_text}"


class Word_Scramble(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='word_scrambles')
    original_word = models.TextField()
    scrambled_word = models.TextField()
    hint = models.TextField(blank=True)

    def __str__(self):
        return f"{self.scrambled_word} → {self.original_word}"


class Translation(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='translations')
    slovak_sentence = models.TextField()
    english_sentence = models.TextField()
    hint = models.TextField(blank=True)

    def __str__(self):
        return f"{self.slovak_sentence}"


class Sentence_Completion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sentence_completion')
    english_sentence = models.TextField()
    missing_word = models.TextField()
    hint = models.TextField(blank=True)

    def __str__(self):
        return f"{self.english_sentence}"

class UserProgress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    correct_attempts = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    best_score = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.user.username} - {self.exercise.title}"


    @property
    def accuracy(self):
        if self.attempts == 0:
            return 0
        else:
            return((self.correct_attempts/self.attempts)*100)

    class Meta:
        unique_together = ['user', 'exercise']




