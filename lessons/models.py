from django.db import models


class Lesson(models.Model):
    name_in_english = models.CharField(max_length=100)
    pronunciation_in_slovak = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        abstract = True
        ordering = ['order']


class NumberLesson(models.Model):
    number = models.CharField(max_length=5)
    name_in_english = models.CharField(max_length=50)
    pronunciation_in_slovak = models.CharField(max_length=50)
    order = models.IntegerField()

    def str(self):
        return f"{self.number} - {self.name_in_english}"

    class Meta:
        ordering = ['order']
        verbose_name = "Number Lesson"
        verbose_name_plural = "Number Lessons"


class ColourLesson(models.Model):
    colour_name = models.CharField(max_length=50)
    colour_hex = models.CharField(max_length=7, blank=True, null=True, help_text="e.g., #FF0000")
    name_in_english = models.CharField(max_length=50)
    pronunciation_in_slovak = models.CharField(max_length=50)
    order = models.IntegerField()

    def str(self):
        return f"{self.colour_name} - {self.name_in_english}"

    class Meta:
        ordering = ['order']
        verbose_name = "Colour Lesson"
        verbose_name_plural = "Colour Lessons"



class FamilyLesson(models.Model):
    family_term = models.CharField(max_length=100)
    overview = models.TextField()
    vocabulary = models.TextField()
    pronunciation_in_slovak = models.TextField()
    order = models.IntegerField()

    def str(self):
        return self.family_term

    class Meta:
        ordering = ['order']
        verbose_name = "Family Lesson"
        verbose_name_plural = "Family Lessons"


class FoodLesson(models.Model):
    name = models.CharField(max_length=10)
    name_in_english=models.CharField(max_length=20)
    overview = models.TextField()
    vocabulary = models.TextField()
    pronunciation_in_slovak = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f"{name}"

    class Meta:
        ordering = ['order']

