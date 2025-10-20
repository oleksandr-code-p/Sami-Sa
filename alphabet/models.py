from django.db import models


CATEGORY_CHOICES = [
    ('vowel', 'Vowel'),
    ('consonant', 'Consonant'),
]


class Letter(models.Model):
    name = models.CharField(max_length=1)
    uppercase = models.CharField(max_length=1)
    lowercase = models.CharField(max_length=1)
    pronunciation = models.FileField(upload_to='letters/', blank=True, null=True)
    category = models.CharField(max_length=10, choices = CATEGORY_CHOICES)
    pronunciation_in_slovak = models.CharField(max_length=10)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.uppercase}/{self.lowercase}"

    class Meta:
        ordering = ['order']
