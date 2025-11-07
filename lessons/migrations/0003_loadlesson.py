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
        ('rodina', 'Family members in Slovak', 
         'family - rodina\nfather - otec\nmother - mama\nbrother - brat\nsister - sestra', 
         'fémi - rodina\nfádr - otec\nmadr - mama\nbrádr - brat\nsistr - sestra'),
        
        ('rodičia', 'Parents and immediate family', 
         'parents - rodičia\nson - syn\ndaughter - dcéra\nhusband - manžel\nwife - manželka', 
         'pérents - rodičia\nsan - syn\ndótr - dcéra\nhazbend - manžel\nvajf - manželka'),
        
        ('starí rodičia', 'Grandparents and extended family', 
         'grandfather - dedko\ngrandmother - babka\nuncle - ujo\naunt - teta\ncousin - bratranec/sesternica', 
         'grándfádr - dedko\ngránmadr - babka\nankl - ujo\nant - teta\nkazin - bratranec/sesternica'),
        
        ('deti', 'Children and young family members', 
         'children - deti\nbaby - bábätko\nboy - chlapec\ngirl - dievča\ntoddler - batoľa', 
         'čildren - deti\nbéjbi - bábätko\nboj - chlapec\ngörl - dievča\ntodlr - batoľa'),
    ]
    
    for i, (term, overview, vocab, pronun) in enumerate(family_data, start=1):
        FamilyLesson.objects.create(
            family_term=term,
            overview=overview,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
            order=i
        )
    
    # Load Food Terms
    FoodLesson = apps.get_model('lessons', 'FoodLesson')
    
    food_data = [
        ('chlieb', 'bread', 'Basic Slovak food vocabulary', 'chlieb - bread\nmaslo - butter\ndžem - jam', 'bred - chlieb\nbatr - maslo\ndžem - džem'),
        ('mlieko', 'milk', 'Dairy products in Slovak', 'mlieko - milk\nsyr - cheese\njogurt - yogurt', 'milk - mlieko\nčíz - syr\njogrt - jogurt'),
        ('voda', 'water', 'Beverages in Slovak', 'voda - water\nkáva - coffee\nčaj - tea', 'wótr - voda\nkofi - káva\ntí - čaj'),
        ('jablko', 'apple', 'Fruits in Slovak', 'jablko - apple\nbanán - banana\nhruška - pear', 'epl - jablko\nbanána - banán\npér - hruška'),
        ('mäso', 'meat', 'Meat products in Slovak', 'mäso - meat\nkura - chicken\nryba - fish', 'mít - mäso\nčikn - kura\nfiš - ryba'),
        ('zelenina', 'vegetables', 'Vegetables in Slovak', 'zelenina - vegetables\nzemiak - potato\nmrkva - carrot', 'vedžtebls - zelenina\npotejto - zemiak\nkerot - mrkva'),
        ('raňajky', 'breakfast', 'Meals in Slovak', 'raňajky - breakfast\nobed - lunch\nvečera - dinner', 'brekfast - raňajky\nlanč - obed\ndinr - večera'),
        ('polievka', 'soup', 'Dishes in Slovak', 'polievka - soup\nšalát - salad\npizza - pizza', 'súp - polievka\nseled - šalát\npica - pizza'),
    ]
    
    for i, (name, english, overview, vocab, pronun) in enumerate(food_data, start=1):
        FoodLesson.objects.create(
            name=name,
            name_in_english=english,
            overview=overview,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
            order=i
        )
    
    SchoolLesson = apps.get_model('lessons', 'SchoolLesson')
    
    school_data = [
        ('škola', 'school', 'Basic school vocabulary', 'škola - school\ntrieda - class\nučiteľ - teacher', 'skúl - škola\nklas - trieda\ntíčr - učiteľ'),
        ('kniha', 'book', 'School supplies', 'kniha - book\npero - pen\nceruzka - pencil', 'buk - kniha\npen - pero\npensl - ceruzka'),
        ('tabuľa', 'board', 'Classroom items', 'tabuľa - board\nstôl - desk\nstoličky - chair', 'bórd - tabuľa\ndesk - stôl\nčér - stoličky'),
        ('študent', 'student', 'People at school', 'študent - student\nžiak - pupil\nriaditeľ - principal', 'stjúdnt - študent\npjúpl - žiak\nprinsipl - riaditeľ'),
        ('predmet', 'subject', 'School subjects', 'matematika - math\nslovenčina - Slovak\nangličtina - English', 'meth - matematika\nslouvek - slovenčina\ningliš - angličtina'),
        ('úloha', 'homework', 'School activities', 'úloha - homework\ntest - test\nprojekt - project', 'houmwörk - úloha\ntest - test\nprodžekt - projekt'),
    ]
    
    for i, (name, english, overview, vocab, pronun) in enumerate(school_data, start=1):
        SchoolLesson.objects.create(
            name=name,
            name_in_english=english,
            overview=overview,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
            order=i
        )
    
    # Load Animal Terms
    AnimalLesson = apps.get_model('lessons', 'AnimalLesson')
    
    animal_data = [
        ('pes', 'dog', 'Common pets', 'pes - dog\nmačka - cat\nvták - bird', 'dog - pes\nket - mačka\nbőrd - vták'),
        ('krava', 'cow', 'Farm animals', 'krava - cow\nprasa - pig\nkôň - horse', 'kau - krava\npig - prasa\nhors - kôň'),
        ('lev', 'lion', 'Wild animals', 'lev - lion\ntiger - tiger\nslon - elephant', 'lajn - lev\ntajgr - tiger\nelifnt - slon'),
        ('ryba', 'fish', 'Water animals', 'ryba - fish\nžralok - shark\nveľryba - whale', 'fiš - ryba\nšárk - žralok\nwejl - veľryba'),
        ('vták', 'bird', 'Birds', 'vták - bird\norol - eagle\nsova - owl', 'bőrd - vták\nígl - orol\naul - sova'),
        ('hmyz', 'insect', 'Insects', 'včela - bee\nmotýľ - butterfly\nmravec - ant', 'bí - včela\nbatrflaj - motýľ\nent - mravec'),
    ]
    
    for i, (name, english, overview, vocab, pronun) in enumerate(animal_data, start=1):
        AnimalLesson.objects.create(
            name=name,
            name_in_english=english,
            overview=overview,
            vocabulary=vocab,
            pronunciation_in_slovak=pronun,
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
        ('lessons', '0002_animallesson_schoollesson'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_code=reverse_load_initial_data),
    ]