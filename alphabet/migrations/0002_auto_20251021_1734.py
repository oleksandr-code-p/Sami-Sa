from django.db import migrations

def load_english_alphabet(apps, schema_editor):
    Letter = apps.get_model('alphabet', 'Letter')

    letters = [
        ('A', 'a', 'A', 'vowel'),
        ('B', 'b', 'Bee', 'consonant'),
        ('C', 'c', 'Cee', 'consonant'),
        ('D', 'd', 'Dee', 'consonant'),
        ('E', 'e', 'E', 'vowel'),
        ('F', 'f', 'Ef', 'consonant'),
        ('G', 'g', 'Gee', 'consonant'),
        ('H', 'h', 'Aitch', 'consonant'),
        ('I', 'i', 'I', 'vowel'),
        ('J', 'j', 'Jay', 'consonant'),
        ('K', 'k', 'Kay', 'consonant'),
        ('L', 'l', 'El', 'consonant'),
        ('M', 'm', 'Em', 'consonant'),
        ('N', 'n', 'En', 'consonant'),
        ('O', 'o', 'O', 'vowel'),
        ('P', 'p', 'Pee', 'consonant'),
        ('Q', 'q', 'Queue', 'consonant'),
        ('R', 'r', 'Ar', 'consonant'),
        ('S', 's', 'Es', 'consonant'),
        ('T', 't', 'Tee', 'consonant'),
        ('U', 'u', 'U', 'vowel'),
        ('V', 'v', 'Vee', 'consonant'),
        ('W', 'w', 'Double U', 'consonant'),
        ('X', 'x', 'Ex', 'consonant'),
        ('Y', 'y', 'Wy', 'consonant'),
        ('Z', 'z', 'Zee', 'consonant'),
    ]

    for i, (upper, lower, name, category) in enumerate(letters, start=1):
        Letter.objects.create(
            uppercase=upper,
            lowercase=lower,
            name=name,
            category=category,
            order=i,
            pronunciation_in_slovak='',  # Add later if needed
        )

def unload_english_alphabet(apps, schema_editor):
    Letter = apps.get_model('alphabet', 'Letter')
    Letter.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('alphabet', '0001_initial'),  # update to your latest migration name
    ]

    operations = [
        migrations.RunPython(load_english_alphabet, reverse_code=unload_english_alphabet),
    ]