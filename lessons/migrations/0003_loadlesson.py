from django.db import migrations

def load_initial_data(apps, schema_editor):
    
    NumberLesson = apps.get_model('lessons', 'NumberLesson')
    
    numbers_data = [
        ('0', 'zero', '/ˈzɪərəʊ/'),
        ('1', 'one', '/wʌn/'),
        ('2', 'two', '/tuː/'),
        ('3', 'three', '/θriː/'),
        ('4', 'four', '/fɔːr/'),
        ('5', 'five', '/faɪv/'),
        ('6', 'six', '/sɪks/'),
        ('7', 'seven', '/ˈsevən/'),
        ('8', 'eight', '/eɪt/'),
        ('9', 'nine', '/naɪn/'),
        ('10', 'ten', '/ten/'),
        ('11', 'eleven', '/ɪˈlevən/'),
        ('12', 'twelve', '/twelv/'),
        ('13', 'thirteen', '/ˌθɜːˈtiːn/'),
        ('14', 'fourteen', '/ˌfɔːˈtiːn/'),
        ('15', 'fifteen', '/ˌfɪfˈtiːn/'),
        ('16', 'sixteen', '/ˌsɪksˈtiːn/'),
        ('17', 'seventeen', '/ˌsevənˈtiːn/'),
        ('18', 'eighteen', '/ˌeɪˈtiːn/'),
        ('19', 'nineteen', '/ˌnaɪnˈtiːn/'),
        ('20', 'twenty', '/ˈtwenti/'),
        ('21', 'twenty-one', '/ˌtwenti ˈwʌn/'),
        ('22', 'twenty-two', '/ˌtwenti ˈtuː/'),
        ('23', 'twenty-three', '/ˌtwenti ˈθriː/'),
        ('24', 'twenty-four', '/ˌtwenti ˈfɔːr/'),
        ('25', 'twenty-five', '/ˌtwenti ˈfaɪv/'),
        ('30', 'thirty', '/ˈθɜːti/'),
        ('40', 'forty', '/ˈfɔːti/'),
        ('50', 'fifty', '/ˈfɪfti/'),
        ('60', 'sixty', '/ˈsɪksti/'),
        ('70', 'seventy', '/ˈsevənti/'),
        ('80', 'eighty', '/ˈeɪti/'),
        ('90', 'ninety', '/ˈnaɪnti/'),
        ('100', 'one hundred', '/wʌn ˈhʌndrəd/'),
        ('1000', 'one thousand', '/wʌn ˈθaʊzənd/'),
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
        ('červená', '#FF0000', 'red', '/red/'),
        ('zelená', '#00FF00', 'green', '/ɡriːn/'),
        ('modrá', '#0000FF', 'blue', '/bluː/'),
        ('žltá', '#FFFF00', 'yellow', '/ˈjeləʊ/'),
        ('oranžová', '#FFA500', 'orange', '/ˈɒrɪndʒ/'),
        ('fialová', '#800080', 'purple', '/ˈpɜːpl/'),
        ('ružová', '#FFC0CB', 'pink', '/pɪŋk/'),
        ('hnedá', '#8B4513', 'brown', '/braʊn/'),
        ('čierna', '#000000', 'black', '/blæk/'),
        ('biela', '#FFFFFF', 'white', '/waɪt/'),
        ('sivá', '#808080', 'gray', '/ɡreɪ/'),
        ('tyrkysová', '#40E0D0', 'turquoise', '/ˈtɜːrkɔɪz/'),
        ('zlatá', '#FFD700', 'gold', '/ɡəʊld/'),
        ('strieborná', '#C0C0C0', 'silver', '/ˈsɪlvər/'),
        ('béžová', '#F5F5DC', 'beige', '/beɪʒ/'),
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
        ('rodina', 'family', '/ˈfæmɪli/', '👨‍👩‍👧'),
        ('otec', 'father', '/ˈfɑːðər/', '👨'),
        ('mama', 'mother', '/ˈmʌðər/', '👩'),
        ('brat', 'brother', '/ˈbrʌðər/', '👦'),
        ('sestra', 'sister', '/ˈsɪstər/', '👧'),

        ('rodičia', 'parents', '/ˈpeərənts/', '👪'),
        ('syn', 'son', '/sʌn/', '🧒'),
        ('dcéra', 'daughter', '/ˈdɔːtər/', '👧'),
        ('manžel', 'husband', '/ˈhʌzbənd/', '👨‍🦱'),
        ('manželka', 'wife', '/waɪf/', '👩‍🦰'),

        ('dedo', 'grandfather', '/ˈɡrændˌfɑːðər/', '👴'),
        ('babka', 'grandmother', '/ˈɡrændˌmʌðər/', '👵'),
        ('ujo', 'uncle', '/ˈʌŋkəl/', '👨‍🦳'),
        ('teta', 'aunt', '/ɑːnt/', '👩‍🦳'),
        ('bratranec/sesternica', 'cousin', '/ˈkʌzən/', '🧑'),

        ('deti', 'children', '/ˈtʃɪldrən/', '👧🧒'),
        ('bábätko', 'baby', '/ˈbeɪbi/', '👶'),
        ('chlapec', 'boy', '/bɔɪ/', '👦'),
        ('dievča', 'girl', '/ɡɜːl/', '👧'),
        ('batoľa', 'toddler', '/ˈtɒdlər/', '👶'),
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
        ('chlieb', 'bread', '/bred/', '🍞'),
        ('maslo', 'butter', '/ˈbʌtər/', '🧈'),
        ('džem', 'jam', '/dʒæm/', '🍯'),
        ('mlieko', 'milk', '/mɪlk/', '🥛'),
        ('syr', 'cheese', '/tʃiːz/', '🧀'),
        ('jogurt', 'yogurt', '/ˈjoʊɡərt/', '🥣'),
        ('voda', 'water', '/ˈwɔːtər/', '💧'),
        ('káva', 'coffee', '/ˈkɒfi/', '☕'),
        ('čaj', 'tea', '/tiː/', '🫖'),
        ('jablko', 'apple', '/ˈæpəl/', '🍎'),
        ('banán', 'banana', '/bəˈnænə/', '🍌'),
        ('hruška', 'pear', '/peər/', '🍐'),
        ('pomaranč', 'orange', '/ˈɒrɪndʒ/', '🍊'),
        ('jahoda', 'strawberry', '/ˈstrɔːbəri/', '🍓'),
        ('mäso', 'meat', '/miːt/', '🍖'),
        ('kura', 'chicken', '/ˈtʃɪkɪn/', '🍗'),
        ('ryba', 'fish', '/fɪʃ/', '🐟'),
        ('zelenina', 'vegetables', '/ˈvedʒtəbəlz/', '🥒'),
        ('zemiak', 'potato', '/pəˈteɪtoʊ/', '🥔'),
        ('mrkva', 'carrot', '/ˈkærət/', '🥕'),
        ('cibuľa', 'onion', '/ˈʌnjən/', '🧅'),
        ('paradajka', 'tomato', '/təˈmeɪtoʊ/', '🍅'),
        ('raňajky', 'breakfast', '/ˈbrekfəst/', '🥞'),
        ('obed', 'lunch', '/lʌntʃ/', '🍽️'),
        ('večera', 'dinner', '/ˈdɪnər/', '🍝'),
        ('polievka', 'soup', '/suːp/', '🍲'),
        ('šalát', 'salad', '/ˈsæləd/', '🥗'),
        ('pizza', 'pizza', '/ˈpiːtsə/', '🍕'),
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
        ('škola', 'school', '/skuːl/', '🏫'),
        ('trieda', 'classroom', '/ˈklɑːsruːm/', '🏫'),
        ('učiteľ', 'teacher', '/ˈtiːtʃər/', '👨‍🏫'),
        ('učiteľka', 'teacher', '/ˈtiːtʃər/', '👩‍🏫'),
        ('žiak', 'pupil', '/ˈpjuːpəl/', '🧒'),
        ('študent', 'student', '/ˈstjuːdənt/', '🧑‍🎓'),
        ('kniha', 'book', '/bʊk/', '📘'),
        ('zošit', 'notebook', '/ˈnoʊtbʊk/', '📒'),
        ('pero', 'pen', '/pen/', '🖊️'),
        ('ceruzka', 'pencil', '/ˈpensəl/', '✏️'),
        ('guma', 'eraser', '/ɪˈreɪsər/', '🩹'),
        ('pravítko', 'ruler', '/ˈruːlər/', '📏'),
        ('lepka', 'glue', '/ɡluː/', '🧴'),
        ('nožnice', 'scissors', '/ˈsɪzərz/', '✂️'),
        ('batoh', 'backpack', '/ˈbækpæk/', '🎒'),
        ('tabuľa', 'board', '/bɔːrd/', '🖥️'),
        ('stôl', 'desk', '/desk/', '🍽️'),
        ('stolička', 'chair', '/tʃeər/', '🪑'),
        ('okno', 'window', '/ˈwɪndoʊ/', '🪟'),
        ('dvere', 'door', '/dɔːr/', '🚪'),
        ('matematika', 'math', '/mæθ/', '➕'),
        ('slovenčina', 'Slovak language', '/ˈsloʊvæk ˈlæŋɡwɪdʒ/', '📘'),
        ('angličtina', 'English', '/ˈɪŋɡlɪʃ/', '🇬🇧'),
        ('dejepis', 'history', '/ˈhɪstəri/', '📜'),
        ('geografia', 'geography', '/dʒiˈɒɡrəfi/', '🌍'),
        ('chémia', 'chemistry', '/ˈkemɪstri/', '⚗️'),
        ('biológia', 'biology', '/baɪˈɒlədʒi/', '🧬'),
        ('fyzika', 'physics', '/ˈfɪzɪks/', '🔬'),
        ('úloha', 'homework', '/ˈhoʊmwɜːrk/', '📝'),
        ('test', 'test', '/test/', '🧪'),
        ('projekt', 'project', '/ˈprɒdʒekt/', '📁'),
        ('prestávka', 'break', '/breɪk/', '⏰'),
        ('obed', 'lunch', '/lʌntʃ/', '🍽️'),
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
        ('pes', 'dog', '/dɔːɡ/', '🐶'),
        ('mačka', 'cat', '/kæt/', '🐱'),
        ('králik', 'rabbit', '/ˈræbɪt/', '🐰'),
        ('škrečok', 'hamster', '/ˈhæmstər/', '🐹'),
        ('krava', 'cow', '/kaʊ/', '🐮'),
        ('prasa', 'pig', '/pɪɡ/', '🐷'),
        ('ovca', 'sheep', '/ʃiːp/', '🐑'),
        ('koza', 'goat', '/ɡoʊt/', '🐐'),
        ('kôň', 'horse', '/hɔːrs/', '🐴'),
        ('lev', 'lion', '/ˈlaɪən/', '🦁'),
        ('tiger', 'tiger', '/ˈtaɪɡər/', '🐯'),
        ('slon', 'elephant', '/ˈɛlɪfənt/', '🐘'),
        ('opica', 'monkey', '/ˈmʌŋki/', '🐒'),
        ('vlk', 'wolf', '/wʊlf/', '🐺'),
        ('ryba', 'fish', '/fɪʃ/', '🐟'),
        ('žralok', 'shark', '/ʃɑːrk/', '🦈'),
        ('delfín', 'dolphin', '/ˈdɒlfɪn/', '🐬'),
        ('veľryba', 'whale', '/weɪl/', '🐳'),
        ('vták', 'bird', '/bɜːrd/', '🐦'),
        ('orol', 'eagle', '/ˈiːɡəl/', '🦅'),
        ('sova', 'owl', '/aʊl/', '🦉'),
        ('včela', 'bee', '/biː/', '🐝'),
        ('motýľ', 'butterfly', '/ˈbʌtərflaɪ/', '🦋'),
        ('mravec', 'ant', '/ænt/', '🐜'),
        ('had', 'snake', '/sneɪk/', '🐍'),
        ('pavúk', 'spider', '/ˈspaɪdər/', '🕷️'),
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