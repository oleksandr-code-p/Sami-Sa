from django.db import migrations

def load_initial_data(apps, schema_editor):
    
    NumberLesson = apps.get_model('lessons', 'NumberLesson')
    
    numbers_data = [
        ('0', 'zero', 'zero'),
        ('1', 'one', 'uan'),
        ('2', 'two', 'tu'),
        ('3', 'three', 'tri'),
        ('4', 'four', 'for'),
        ('5', 'five', 'fajv'),
        ('6', 'six', 'siks'),
        ('7', 'seven', 'seven'),
        ('8', 'eight', 'eit'),
        ('9', 'nine', 'najn'),
        ('10', 'ten', 'ten'),
        ('11', 'eleven', 'ilevn'),
        ('12', 'twelve', 'twelv'),
        ('13', 'thirteen', 'törtin'),
        ('14', 'fourteen', 'fortin'),
        ('15', 'fifteen', 'fiftin'),
        ('16', 'sixteen', 'sikstin'),
        ('17', 'seventeen', 'sevntin'),
        ('18', 'eighteen', 'eitin'),
        ('19', 'nineteen', 'najntin'),
        ('20', 'twenty', 'twenti'),
        ('21', 'twenty-one', 'twenti-uan'),
        ('22', 'twenty-two', 'twenti-tu'),
        ('23', 'twenty-three', 'twenti-tri'),
        ('24', 'twenty-four', 'twenti-for'),
        ('25', 'twenty-five', 'twenti-fajv'),
        ('30', 'thirty', 'törti'),
        ('40', 'forty', 'forti'),
        ('50', 'fifty', 'fifti'),
        ('60', 'sixty', 'siksti'),
        ('70', 'seventy', 'sevnti'),
        ('80', 'eighty', 'eiti'),
        ('90', 'ninety', 'najnti'),
        ('100', 'one hundred', 'uan handred'),
        ('1000', 'one thousand', 'uan tauznd'),
    ]
    
    for i, (number, english, pronunciation) in enumerate(numbers_data, start=1):
        NumberLesson.objects.create(
            number=number,
            name_in_english=english,
            pronunciation_in_slovak=pronunciation,
            order=i
        )
    
    # Load Colours
    ColourLesson = apps.get_model('lessons', 'ColourLesson')
    
    colours_data = [
        ('červená', '#FF0000', 'red', 'red'),
        ('zelená', '#00FF00', 'green', 'grín'),
        ('modrá', '#0000FF', 'blue', 'blú'),
        ('žltá', '#FFFF00', 'yellow', 'jelou'),
        ('oranžová', '#FFA500', 'orange', 'orindž'),
        ('fialová', '#800080', 'purple', 'pörpl'),
        ('ružová', '#FFC0CB', 'pink', 'pink'),
        ('hnedá', '#8B4513', 'brown', 'braun'),
        ('čierna', '#000000', 'black', 'blek'),
        ('biela', '#FFFFFF', 'white', 'vajt'),
        ('sivá', '#808080', 'gray', 'grej'),
        ('tyrkysová', '#40E0D0', 'turquoise', 'törkvojs'),
        ('zlatá', '#FFD700', 'gold', 'gould'),
        ('strieborná', '#C0C0C0', 'silver', 'silvr'),
        ('béžová', '#F5F5DC', 'beige', 'bejž'),
    ]
    
    for i, (slovak_name, hex_code, english, pronunciation) in enumerate(colours_data, start=1):
        ColourLesson.objects.create(
            colour_name=slovak_name,
            colour_hex=hex_code,
            name_in_english=english,
            pronunciation_in_slovak=pronunciation,
            order=i
        )

    FamilyLesson = apps.get_model('lessons', 'FamilyLesson')
    
    family_data = [
        ('rodina', 'family', 'fémily', '👨‍👩‍👧'),
        ('otec', 'father', 'fádr', '👨'),
        ('mama', 'mother', 'madr', '👩'),
        ('brat', 'brother', 'brádr', '👦'),
        ('sestra', 'sister', 'sistr', '👧'),

        ('rodičia', 'parents', 'pérents', '👪'),
        ('syn', 'son', 'san', '🧒'),
        ('dcéra', 'daughter', 'dótr', '👧'),
        ('manžel', 'husband', 'hazbend', '👨‍🦱'),
        ('manželka', 'wife', 'vajf', '👩‍🦰'),

        ('dedo', 'grandfather', 'grándfádr', '👴'),
        ('babka', 'grandmother', 'gránmadr', '👵'),
        ('ujo', 'uncle', 'ankl', '👨‍🦳'),
        ('teta', 'aunt', 'ant', '👩‍🦳'),
        ('bratranec/sesternica', 'cousin', 'kazin', '🧑'),

        ('deti', 'children', 'čildren', '👧🧒'),
        ('bábätko', 'baby', 'béjbi', '👶'),
        ('chlapec', 'boy', 'boj', '👦'),
        ('dievča', 'girl', 'görl', '👧'),
        ('batoľa', 'toddler', 'todlr', '👶'),
    ]
    
    for i, (term, vocab, pronun, emoji) in enumerate(family_data, start=1):
        FamilyLesson.objects.create(
            family_term=term,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
            emoji=emoji,
            order=i
        )
    
    # Load Food Terms
    FoodLesson = apps.get_model('lessons', 'FoodLesson')
    
    food_data = [
    ('chlieb', 'bread', 'bred', '🍞'),
    ('maslo', 'butter', 'batr', '🧈'),
    ('džem', 'jam', 'džem', '🍯'),
    ('mlieko', 'milk', 'milk', '🥛'),
    ('syr', 'cheese', 'číz', '🧀'),
    ('jogurt', 'yogurt', 'jogrt', '🥣'),
    ('voda', 'water', 'wótr', '💧'),
    ('káva', 'coffee', 'kofi', '☕'),
    ('čaj', 'tea', 'tí', '🫖'),
    ('jablko', 'apple', 'epl', '🍎'),
    ('banán', 'banana', 'banána', '🍌'),
    ('hruška', 'pear', 'pér', '🍐'),
    ('pomaranč', 'orange', 'orindž', '🍊'),
    ('jahoda', 'strawberry', 'strobery', '🍓'),
    ('mäso', 'meat', 'mít', '🍖'),
    ('kura', 'chicken', 'čikn', '🍗'),
    ('ryba', 'fish', 'fiš', '🐟'),
    ('zelenina', 'vegetables', 'vedžtebls', '🥒'),
    ('zemiak', 'potato', 'potejto', '🥔'),
    ('mrkva', 'carrot', 'kerot', '🥕'),
    ('cibuľa', 'onion', 'anjn', '🧅'),
    ('paradajka', 'tomato', 'tomejto', '🍅'),
    ('raňajky', 'breakfast', 'brekfast', '🥞'),
    ('obed', 'lunch', 'lanč', '🍽️'),
    ('večera', 'dinner', 'dinr', '🍝'),
    ('polievka', 'soup', 'súp', '🍲'),
    ('šalát', 'salad', 'seled', '🥗'),
    ('pizza', 'pizza', 'pica', '🍕'),
]

    
    for i, (term, english, pronun, emoji) in enumerate(food_data, start=1):
        FoodLesson.objects.create(
            name=term,
            vocabulary=english,
            pronunciation_in_slovak=pronun,
            emoji=emoji,
            order=i
        )
    
    SchoolLesson = apps.get_model('lessons', 'SchoolLesson')
    
    school_data = [
        ('škola', 'school', 'skúl', '🏫'),
        ('trieda', 'classroom', 'klásrum', '🏫'),
        ('učiteľ', 'teacher', 'tíčr', '👨‍🏫'),
        ('učiteľka', 'teacher', 'tíčr', '👩‍🏫'),
        ('žiak', 'pupil', 'pjúpl', '🧒'),
        ('študent', 'student', 'stjúdnt', '🧑‍🎓'),
        ('kniha', 'book', 'buk', '📘'),
        ('zošit', 'notebook', 'noutbuk', '📒'),
        ('pero', 'pen', 'pen', '🖊️'),
        ('ceruzka', 'pencil', 'pensl', '✏️'),
        ('guma', 'eraser', 'irejzr', '🩹'),
        ('pravítko', 'ruler', 'rúlr', '📏'),
        ('lepka', 'glue', 'glú', '🧴'),
        ('nožnice', 'scissors', 'sizrz', '✂️'),
        ('batoh', 'backpack', 'bekpek', '🎒'),
        ('tabuľa', 'board', 'bórd', '🖥️'),
        ('stôl', 'desk', 'desk', '🪑'),
        ('stolička', 'chair', 'čér', '🪑'),
        ('okno', 'window', 'windou', '🪟'),
        ('dvere', 'door', 'dór', '🚪'),
        ('matematika', 'math', 'mahth', '➕'),
        ('slovenčina', 'Slovak language', 'slovek lengvidž', '📘'),
        ('angličtina', 'English', 'ingliš', '🇬🇧'),
        ('dejepis', 'history', 'histri', '📜'),
        ('geografia', 'geography', 'džiógrafi', '🌍'),
        ('chémia', 'chemistry', 'kemistri', '⚗️'),
        ('biológia', 'biology', 'bajolodži', '🧬'),
        ('fyzika', 'physics', 'fyziks', '🔬'),
        ('úloha', 'homework', 'houmwörk', '📝'),
        ('test', 'test', 'test', '🧪'),
        ('projekt', 'project', 'prodžekt', '📁'),
        ('prestávka', 'break', 'brejk', '⏰'),
        ('obed', 'lunch', 'lanč', '🍽️'),
    ]

    
    for i, (name, vocab, pronun, emoji) in enumerate(school_data, start=1):
        SchoolLesson.objects.create(
            name=name,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
            emoji=emoji,
            order=i
        )
    
    # Load Animal Terms
    AnimalLesson = apps.get_model('lessons', 'AnimalLesson')
    
    animal_data = [
        ('pes', 'dog', 'dog', '🐶'),
        ('mačka', 'cat', 'ket', '🐱'),
        ('králik', 'rabbit', 'rebit', '🐰'),
        ('škrečok', 'hamster', 'hemstr', '🐹'),
        ('krava', 'cow', 'kau', '🐮'),
        ('prasa', 'pig', 'pig', '🐷'),
        ('ovca', 'sheep', 'šíp', '🐑'),
        ('koza', 'goat', 'gout', '🐐'),
        ('kôň', 'horse', 'hors', '🐴'),
        ('lev', 'lion', 'lajn', '🦁'),
        ('tiger', 'tiger', 'tajgr', '🐯'),
        ('slon', 'elephant', 'elifnt', '🐘'),
        ('opica', 'monkey', 'manki', '🐒'),
        ('vlk', 'wolf', 'wulf', '🐺'),
        ('ryba', 'fish', 'fiš', '🐟'),
        ('žralok', 'shark', 'šark', '🦈'),
        ('delfín', 'dolphin', 'dolfyn', '🐬'),
        ('veľryba', 'whale', 'wejl', '🐳'),
        ('vták', 'bird', 'börd', '🐦'),
        ('orol', 'eagle', 'ígl', '🦅'),
        ('sova', 'owl', 'aul', '🦉'),
        ('včela', 'bee', 'bí', '🐝'),
        ('motýľ', 'butterfly', 'batrflaj', '🦋'),
        ('mravec', 'ant', 'ent', '🐜'),
        ('had', 'snake', 'snejk', '🐍'),
        ('pavúk', 'spider', 'spajdr', '🕷️'),
    ]

    
    for i, (term, english, pronun, emoji) in enumerate(animal_data, start=1):
        AnimalLesson.objects.create(
            name=term,
            name_in_english=english,
            pronunciation_in_slovak=pronun,
            emoji=emoji,
            order=i
        )

def reverse_load_initial_data(apps, schema_editor):
    """Remove all seeded data"""
    NumberLesson = apps.get_model('lessons', 'NumberLesson')
    ColourLesson = apps.get_model('lessons', 'ColourLesson')
    FamilyLesson = apps.get_model('lessons', 'FamilyLesson')
    FoodLesson = apps.get_model('lessons', 'FoodLesson')
    SchoolLesson = apps.get_model('lessons', 'SchoolLesson')
    AnimalLesson = apps.get_model('lessons', 'AnimalLesson')
    
    NumberLesson.objects.all().delete()
    ColourLesson.objects.all().delete()
    FamilyLesson.objects.all().delete()
    FoodLesson.objects.all().delete()
    SchoolLesson.objects.all().delete()
    AnimalLesson.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_code=reverse_load_initial_data),
    ]