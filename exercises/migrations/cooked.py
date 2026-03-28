"""
Data migration to seed English language exercises for Slovak speakers.
Place this file in: exercises/migrations/
Run with: python manage.py migrate exercises
"""

import random
from django.db import migrations


def scramble_word(word):
    """Scramble a word ensuring it's different from original."""
    word_list = list(word.lower())
    attempts = 0
    scrambled = word_list.copy()
    while ''.join(scrambled) == word.lower() and attempts < 10:
        random.shuffle(scrambled)
        attempts += 1
    return ''.join(scrambled)


def seed_exercises(apps, schema_editor):
    """Seed all exercise data - Teaching English to Slovak speakers."""
    Exercise = apps.get_model('exercises', 'Exercise')
    Exercise_Choice = apps.get_model('exercises', 'Exercise_Choice')
    Matching_Pair = apps.get_model('exercises', 'Matching_Pair')
    Word_Scramble = apps.get_model('exercises', 'Word_Scramble')
    Translation = apps.get_model('exercises', 'Translation')
    Sentence_Completion = apps.get_model('exercises', 'Sentence_Completion')

    # ==========================================================
    # NUMBER EXERCISES (Čísla)
    # ==========================================================
    numbers_data = [
        ('one', 'jeden', '1'),
        ('two', 'dva', '2'),
        ('three', 'tri', '3'),
        ('four', 'štyri', '4'),
        ('five', 'päť', '5'),
        ('six', 'šesť', '6'),
        ('seven', 'sedem', '7'),
        ('eight', 'osem', '8'),
        ('nine', 'deväť', '9'),
        ('ten', 'desať', '10'),
        ('eleven', 'jedenásť', '11'),
        ('twelve', 'dvanásť', '12'),
        ('twenty', 'dvadsať', '20'),
        ('thirty', 'tridsať', '30'),
        ('hundred', 'sto', '100'),
    ]

    # Number - Multiple Choice
    for i, (english, slovak, num) in enumerate(numbers_data[:10]):
        mc_exercise = Exercise.objects.create(
            title=f'Čo znamená "{slovak}"?',
            lesson_type='number',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}" ({num}).',
            order=10 + i,
        )

        wrong_options = [e for e, s, n in numbers_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # Number - Matching
    matching_exercise = Exercise.objects.create(
        title='Čísla - Spárovanie',
        lesson_type='number',
        exercise_type='matching',
        question_text='Spárujte slovenské čísla s anglickými prekladmi.',
        correct_answer='',
        explanation='Spojte slovenské čísla s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak, _) in enumerate(numbers_data[:10]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # Number - Word Scramble (scramble English words)
    scramble_exercise = Exercise.objects.create(
        title='Čísla - Rozhádzané písmená',
        lesson_type='number',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vzniklo správne anglické číslo.',
        correct_answer='',
        explanation='Poskladajte anglické čísla z rozhádzaných písmen.',
        order=2,
    )

    for i, (english, slovak, num) in enumerate(numbers_data[:10]):
        Word_Scramble.objects.create(
            exercise=scramble_exercise,
            original_word=english,
            scrambled_word=scramble_word(english),
            hint=f'Slovensky: {slovak} ({num})',
        )

    completion_exercise = Exercise.objects.create(
        title='Čísla - Doplň slovo',
        lesson_type='number',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické číslo do vety.',
        correct_answer='',
        explanation='Doplňte správne anglické číslo.',
        order=4,
    )

    number_completions = [
        ('I have ___ apple. (jedno)', 'one', 'jeden'),
        ('She has ___ cats at home. (dve)', 'two', 'dva'),
        ('I see ___ dogs in the park. (tri)', 'three', 'tri'),
        ('He has ___ pens on the table. (päť)', 'five', 'päť'),
        ('I have ___ books to read. (desať)', 'ten', 'desať'),
        ('There are ___ chairs in the room. (dvadsať)', 'twenty', 'dvadsať'),
        ('I see ___ birds on the tree. (tridsať)', 'thirty', 'tridsať'),
        ('She has ___ balls in the garden. (päťdesiat)', 'fifty', 'päťdesiat'),
        ('I have ___ toys for my friends. (sto)', 'one hundred', 'sto'),
        ('He has ___ apples in the basket. (dvesto)', 'two hundred', 'dvesto'),
        ('I see ___ cars on the street. (päťsto)', 'five hundred', 'päťsto'),
        ('She has ___ pencils for school. (tisíc)', 'one thousand', 'tisíc'),
        ('I bought ___ oranges yesterday. (šesť)', 'six', 'šesť'),
        ('They have ___ chairs in the hall. (osem)', 'eight', 'osem'),
        ('I saw ___ flowers in the garden. (deväť)', 'nine', 'deväť'),
        ('He drank ___ glasses of water. (sedem)', 'seven', 'sedem'),
        ('I found ___ coins on the floor. (dvadsaťpäť)', 'twenty-five', 'dvadsaťpäť'),
        ('She has ___ hats in her shop. (tridsaťpäť)', 'thirty-five', 'tridsaťpäť'),
        ('I saw ___ cats on the street. (šesťdesiat)', 'sixty', 'šesťdesiat'),
        ('He bought ___ books yesterday. (osemdesiat)', 'eighty', 'osemdesiat'),
        ('I have ___ chairs in my room. (sto päť)', 'one hundred five', 'sto päť'),
        ('They own ___ bicycles. (dvesto päťdesiat)', 'two hundred fifty', 'dvesto päťdesiat'),
        ('I saw ___ stars in the sky. (tristo)', 'three hundred', 'tristo'),
        ('She found ___ coins in the drawer. (šesťsto)', 'six hundred', 'šesťsto'),
]

    for i, (sentence, missing, hint) in enumerate(number_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # COLOUR EXERCISES (Farby)
    # ==========================================================
    colours_data = [
        ('red', 'červená'),
        ('blue', 'modrá'),
        ('green', 'zelená'),
        ('yellow', 'žltá'),
        ('orange', 'oranžová'),
        ('purple', 'fialová'),
        ('pink', 'ružová'),
        ('black', 'čierna'),
        ('white', 'biela'),
        ('brown', 'hnedá'),
        ('grey', 'sivá'),
        ('gold', 'zlatá'),
        ('silver', 'strieborná'),
    ]

    # Colour - Multiple Choice
    for i, (english, slovak) in enumerate(colours_data[:10]):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa povie "{slovak}"?',
            lesson_type='colour',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}".',
            order=10 + i,
        )

        wrong_options = [e for e, s in colours_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # Colour - Matching
    matching_exercise = Exercise.objects.create(
        title='Farby - Spárovanie',
        lesson_type='colour',
        exercise_type='matching',
        question_text='Spárujte slovenské farby s anglickými prekladmi.',
        correct_answer='',
        explanation='Spojte slovenské farby s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak) in enumerate(colours_data[:10]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # Colour - Word Scramble
    scramble_exercise = Exercise.objects.create(
        title='Farby - Rozhádzané písmená',
        lesson_type='colour',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vznikla správna anglická farba.',
        correct_answer='',
        explanation='Poskladajte anglické farby z rozhádzaných písmen.',
        order=2,
    )

    for i, (english, slovak) in enumerate(colours_data[:10]):
        Word_Scramble.objects.create(
            exercise=scramble_exercise,
            original_word=english,
            scrambled_word=scramble_word(english),
            hint=f'Slovensky: {slovak}',
        )

    # Colour - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Farby - Doplň slovo',
        lesson_type='colour',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúcu anglickú farbu do vety.',
        correct_answer='',
        explanation='Doplňte správnu anglickú farbu.',
        order=4,
    )

    colour_completions = [
        ('The sky is ___. (modrá)', 'blue', 'modrá'),
        ('Grass is ___. (zelená)', 'green', 'zelená'),
        ('The sun is ___. (žltá)', 'yellow', 'žltá'),
        ('Snow is ___. (biela)', 'white', 'biela'),
        ('Coal is ___. (čierna)', 'black', 'čierna'),
        ('My car is ___. (červená)', 'red', 'červená'),
        ('The flower is ___. (oranžová)', 'orange', 'oranžová'),
        ('Her dress is ___. (ružová)', 'pink', 'ružová'),
        ('The table is ___. (sivá)', 'gray', 'sivá'),
        ('My house is ___. (hnedá)', 'brown', 'hnedá'),
        ('The ring is ___. (zlatá)', 'gold', 'zlatá'),
        ('The bracelet is ___. (strieborná)', 'silver', 'strieborná'),
        ('The balloon is ___. (fialová)', 'purple', 'fialová'),
    ]

    for i, (sentence, missing, hint) in enumerate(colour_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # FAMILY EXERCISES (Rodina)
    # ==========================================================
    family_data = [
        ('mother', 'mama', 'mom'),
        ('father', 'otec', 'dad'),
        ('brother', 'brat', ''),
        ('sister', 'sestra', ''),
        ('son', 'syn', ''),
        ('daughter', 'dcéra', ''),
        ('grandmother', 'babka', 'grandma'),
        ('grandfather', 'dedko', 'grandpa'),
        ('aunt', 'teta', ''),
        ('uncle', 'strýko', ''),
        ('cousin', 'bratranec/sesternica', ''),
        ('husband', 'manžel', ''),
        ('wife', 'manželka', ''),
        ('parents', 'rodičia', ''),
        ('children', 'deti', ''),
    ]

    # Family - Multiple Choice
    for i, (english, slovak, alt) in enumerate(family_data[:12]):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa povie "{slovak}"?',
            lesson_type='family',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}".' + (f' (alebo {alt})' if alt else ''),
            order=10 + i,
        )

        wrong_options = [e for e, s, a in family_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # Family - Matching
    matching_exercise = Exercise.objects.create(
        title='Rodina - Spárovanie',
        lesson_type='family',
        exercise_type='matching',
        question_text='Spárujte slovenské slová pre členov rodiny s anglickými.',
        correct_answer='',
        explanation='Spojte slovenské slová s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak, _) in enumerate(family_data[:10]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # Family - Word Scramble
    scramble_exercise = Exercise.objects.create(
        title='Rodina - Rozhádzané písmená',
        lesson_type='family',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vzniklo správne anglické slovo.',
        correct_answer='',
        explanation='Poskladajte anglické slová pre členov rodiny.',
        order=2,
    )

    for i, (english, slovak, _) in enumerate(family_data[:10]):
        Word_Scramble.objects.create(
            exercise=scramble_exercise,
            original_word=english,
            scrambled_word=scramble_word(english),
            hint=f'Slovensky: {slovak}',
        )

    # Family - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Rodina - Doplň slovo',
        lesson_type='family',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické slovo do vety.',
        correct_answer='',
        explanation='Doplňte správneho člena rodiny po anglicky.',
        order=4,
    )

    family_completions = [
        ('My ___ is my female parent. (mama)', 'mother', 'mama'),
        ('I love my ___. (otec)', 'father', 'otec'),
        ('Her ___ is older than me. (sestra)', 'sister', 'sestra'),
        ('His ___ plays football. (brat)', 'brother', 'brat'),
        ('My ___ makes delicious cookies. (babka)', 'grandmother', 'babka'),
        ('His ___ tells funny stories. (dedko)', 'grandfather', 'dedko'),
        ('I visited my ___. (teta)', 'aunt', 'teta'),
        ('We saw our ___. (strýko)', 'uncle', 'strýko'),
        ('My ___ is very clever. (synovec)', 'nephew', 'synovec'),
        ('Her ___ likes drawing. (neter)', 'niece', 'neter'),
        ('My ___ helps me every day. (manžel)', 'husband', 'manžel'),
        ('Her ___ cooks well. (manželka)', 'wife', 'manželka'),
        ('Their ___ goes to school. (syn)', 'son', 'syn'),
        ('Our ___ is very kind. (dcéra)', 'daughter', 'dcéra'),
        ('I met my ___. (švagriná)', 'sister-in-law', 'švagriná'),
        ('He talks to his ___. (švagor)', 'brother-in-law', 'švagor'),
        ('My ___ lives next door. (bratranec / sesternica)', 'cousin', 'bratranec / sesternica'),
        ('Her ___ loves football. (bratranec)', 'cousin', 'bratranec'),
        ('I met my ___. (svokra)', 'mother-in-law', 'svokra'),
        ('His ___ is very friendly. (svokor)', 'father-in-law', 'svokor'),
        ('They like their ___. (švagor)', 'brother-in-law', 'švagor'),
        ('We talked to our ___. (švagriná)', 'sister-in-law', 'švagriná'),
]

    for i, (sentence, missing, hint) in enumerate(family_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # FOOD EXERCISES (Jedlo)
    # ==========================================================
    food_data = [
        ('bread', 'chlieb'),
        ('milk', 'mlieko'),
        ('butter', 'maslo'),
        ('cheese', 'syr'),
        ('egg', 'vajce'),
        ('meat', 'mäso'),
        ('fish', 'ryba'),
        ('vegetables', 'zelenina'),
        ('fruit', 'ovocie'),
        ('apple', 'jablko'),
        ('pear', 'hruška'),
        ('orange', 'pomaranč'),
        ('banana', 'banán'),
        ('strawberry', 'jahoda'),
        ('potatoes', 'zemiaky'),
        ('rice', 'ryža'),
        ('soup', 'polievka'),
        ('salad', 'šalát'),
        ('coffee', 'káva'),
        ('tea', 'čaj'),
        ('water', 'voda'),
    ]

    # Food - Multiple Choice
    for i, (english, slovak) in enumerate(food_data[:15]):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa povie "{slovak}"?',
            lesson_type='food',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}".',
            order=10 + i,
        )

        wrong_options = [e for e, s in food_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # Food - Matching
    matching_exercise = Exercise.objects.create(
        title='Jedlo - Spárovanie',
        lesson_type='food',
        exercise_type='matching',
        question_text='Spárujte slovenské slová pre jedlo s anglickými.',
        correct_answer='',
        explanation='Spojte slovenské slová s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak) in enumerate(food_data[:12]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # Food - Word Scramble
    scramble_exercise = Exercise.objects.create(
        title='Jedlo - Rozhádzané písmená',
        lesson_type='food',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vzniklo správne anglické slovo.',
        correct_answer='',
        explanation='Poskladajte anglické slová pre jedlo.',
        order=2,
    )

    for i, (english, slovak) in enumerate(food_data[:12]):
        Word_Scramble.objects.create(
            exercise=scramble_exercise,
            original_word=english,
            scrambled_word=scramble_word(english),
            hint=f'Slovensky: {slovak}',
        )

    # Food - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Jedlo - Doplň slovo',
        lesson_type='food',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické slovo do vety.',
        correct_answer='',
        explanation='Doplňte správne anglické slovo o jedle.',
        order=4,
    )

    food_completions = [
        ('I drink ___ every morning. (káva)', 'coffee', 'káva'),
        ('I eat ___ for breakfast. (chlieb)', 'bread', 'chlieb'),
        ('An ___ a day keeps the doctor away. (jablko)', 'apple', 'jablko'),
        ('I put ___ on my bread. (maslo)', 'butter', 'maslo'),
        ('___ is white and comes from cows. (mlieko)', 'Milk', 'mlieko'),
        ('I like ___ with my salad. (syr)', 'cheese', 'syr'),
        ('I cook ___ for dinner. (mäso)', 'meat', 'mäso'),
        ('We eat ___ on Fridays. (ryba)', 'fish', 'ryba'),
        ('I eat ___ every day. (zelenina)', 'vegetables', 'zelenina'),
        ('She likes ___ after lunch. (ovocie)', 'fruit', 'ovocie'),
        ('I eat a ___ for snack. (banán)', 'banana', 'banán'),
        ('I love ___ in summer. (jahoda)', 'strawberry', 'jahoda'),
        ('I cook ___ with meat. (zemiaky)', 'potatoes', 'zemiaky'),
        ('I eat ___ with curry. (ryža)', 'rice', 'ryža'),
        ('I eat ___ before dinner. (polievka)', 'soup', 'polievka'),
        ('I eat ___ with my lunch. (šalát)', 'salad', 'šalát'),
        ('I drink ___ in the morning. (čaj)', 'tea', 'čaj'),
        ('I drink ___ when I am thirsty. (voda)', 'water', 'voda'),
        ('I eat a ___ or a pear. (hruška)', 'pear', 'hruška'),
        ('I peel an ___ before eating. (pomaranč)', 'orange', 'pomaranč'),
]

    for i, (sentence, missing, hint) in enumerate(food_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # SCHOOL EXERCISES (Škola)
    # ==========================================================
    school_data = [
        ('school', 'škola'),
        ('classroom', 'trieda'),
        ('teacher', 'učiteľ/učiteľka'),
        ('student', 'žiak/žiačka'),
        ('book', 'kniha'),
        ('notebook', 'zošit'),
        ('pen', 'pero'),
        ('pencil', 'ceruzka'),
        ('blackboard', 'tabuľa'),
        ('chair', 'stolička'),
        ('desk', 'stôl'),
        ('bag', 'taška'),
        ('homework', 'domáca úloha'),
        ('exam', 'skúška'),
        ('break', 'prestávka'),
        ('lesson', 'hodina'),
        ('schedule', 'rozvrh'),
        ('grade', 'známka'),
    ]

    # School - Multiple Choice
    for i, (english, slovak) in enumerate(school_data[:15]):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa povie "{slovak}"?',
            lesson_type='school',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}".',
            order=10 + i,
        )

        wrong_options = [e for e, s in school_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # School - Matching
    matching_exercise = Exercise.objects.create(
        title='Škola - Spárovanie',
        lesson_type='school',
        exercise_type='matching',
        question_text='Spárujte slovenské školské slová s anglickými.',
        correct_answer='',
        explanation='Spojte slovenské slová s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak) in enumerate(school_data[:12]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # School - Word Scramble
    scramble_exercise = Exercise.objects.create(
        title='Škola - Rozhádzané písmená',
        lesson_type='school',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vzniklo správne anglické slovo.',
        correct_answer='',
        explanation='Poskladajte anglické školské slová.',
        order=2,
    )

    for i, (english, slovak) in enumerate(school_data[:10]):
        if ' ' not in english:
            Word_Scramble.objects.create(
                exercise=scramble_exercise,
                original_word=english,
                scrambled_word=scramble_word(english),
                hint=f'Slovensky: {slovak}',
            )

    # School - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Škola - Doplň slovo',
        lesson_type='school',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické slovo do vety.',
        correct_answer='',
        explanation='Doplňte správne anglické školské slovo.',
        order=4,
    )

    school_completions = [
        ('I write with a ___. (pero)', 'pen', 'pero'),
        ('I read a ___. (kniha)', 'book', 'kniha'),
        ('The ___ teaches students. (učiteľ)', 'teacher', 'učiteľ'),
        ('I sit on a ___. (stolička)', 'chair', 'stolička'),
        ('I carry my books in a ___. (taška)', 'bag', 'taška'),
        ('I take notes in a ___. (zošit)', 'notebook', 'zošit'),
        ('We have a ___ every morning. (hodina)', 'lesson', 'hodina'),
        ('The ___ is green and big. (tabuľa)', 'blackboard', 'tabuľa'),
        ('I sit at a ___. (stôl)', 'desk', 'stôl'),
        ('I am a ___. (žiak/žiačka)', 'student', 'žiak/žiačka'),
        ('Our ___ shows our subjects. (rozvrh)', 'schedule', 'rozvrh'),
        ('I do my ___ at home. (domáca úloha)', 'homework', 'domáca úloha'),
        ('I have a ___ tomorrow. (skúška)', 'exam', 'skúška'),
        ('We have a short ___ now. (prestávka)', 'break', 'prestávka'),
        ('I got a good ___ on my test. (známka)', 'grade', 'známka'),
        ('The ___ writes on the blackboard. (učiteľ/učiteľka)', 'teacher', 'učiteľ/učiteľka'),
        ('I read my ___ before class. (kniha)', 'book', 'kniha'),
        ('I write my answers in my ___. (zošit)', 'notebook', 'zošit'),
        ('I put my pen and pencil in my ___. (taška)', 'bag', 'taška'),
    ]
    for i, (sentence, missing, hint) in enumerate(school_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # ANIMAL EXERCISES (Zvieratá)
    # ==========================================================
    animal_data = [
        ('dog', 'pes'),
        ('cat', 'mačka'),
        ('horse', 'kôň'),
        ('cow', 'krava'),
        ('pig', 'prasa'),
        ('sheep', 'ovca'),
        ('goat', 'koza'),
        ('chicken', 'sliepka'),
        ('rooster', 'kohút'),
        ('duck', 'kačica'),
        ('goose', 'hus'),
        ('rabbit', 'králik'),
        ('mouse', 'myš'),
        ('bird', 'vták'),
        ('fish', 'ryba'),
        ('snake', 'had'),
        ('frog', 'žaba'),
        ('bear', 'medveď'),
        ('wolf', 'vlk'),
        ('fox', 'líška'),
        ('deer', 'jeleň'),
        ('elephant', 'slon'),
        ('lion', 'lev'),
        ('tiger', 'tiger'),
        ('monkey', 'opica'),
    ]

    # Animal - Multiple Choice
    for i, (english, slovak) in enumerate(animal_data[:18]):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa povie "{slovak}"?',
            lesson_type='animal',
            exercise_type='multiple_choice',
            question_text=f'Ako sa povie "{slovak}" po anglicky?',
            correct_answer=english,
            explanation=f'"{slovak}" sa po anglicky povie "{english}".',
            order=10 + i,
        )

        wrong_options = [e for e, s in animal_data if e != english]
        random.shuffle(wrong_options)
        all_choices = [english] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == english),
                order=j,
            )

    # Animal - Matching
    matching_exercise = Exercise.objects.create(
        title='Zvieratá - Spárovanie',
        lesson_type='animal',
        exercise_type='matching',
        question_text='Spárujte slovenské názvy zvierat s anglickými.',
        correct_answer='',
        explanation='Spojte slovenské slová s ich anglickými ekvivalentmi.',
        order=1,
    )

    for i, (english, slovak) in enumerate(animal_data[:12]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=slovak,
            right_text=english,
            order=i,
        )

    # Animal - Word Scramble
    scramble_exercise = Exercise.objects.create(
        title='Zvieratá - Rozhádzané písmená',
        lesson_type='animal',
        exercise_type='word_scrambles',
        question_text='Usporiadajte písmená tak, aby vznikol správny anglický názov zvieraťa.',
        correct_answer='',
        explanation='Poskladajte anglické názvy zvierat.',
        order=2,
    )

    for i, (english, slovak) in enumerate(animal_data[:12]):
        Word_Scramble.objects.create(
            exercise=scramble_exercise,
            original_word=english,
            scrambled_word=scramble_word(english),
            hint=f'Slovensky: {slovak}',
        )

    # Animal - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Zvieratá - Doplň slovo',
        lesson_type='animal',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické zviera do vety.',
        correct_answer='',
        explanation='Doplňte správne anglické zviera.',
        order=4,
    )

    animal_completions = [
        ('My ___ barks loudly. (pes)', 'dog', 'pes'),
        ('I walk my __ every morning. (pes)', 'dog', 'pes'),
        ('The ___ sleeps on the sofa. (mačka)', 'cat', 'mačka'),
        ('I feed my ___ milk. (mačka)', 'cat', 'mačka'),
        ('The ___ runs fast in the field. (kôň)', 'horse', 'kôň'),
        ('I ride a ___ on weekends. (kôň)', 'horse', 'kôň'),
        ('We milk the ___ every day. (krava)', 'cow', 'krava'),
        ('The ___ rolls in the mud. (prasa)', 'pig', 'prasa'),
        ('The ___ gives us wool. (ovca)', 'sheep', 'ovca'),
        ('I see a ___ on the hill. (koza)', 'goat', 'koza'),
        ('The ___ lays eggs every morning. (sliepka)', 'chicken', 'sliepka'),
        ('The ___ crows at dawn. (kohút)', 'rooster', 'kohút'),
        ('The ___ swims in the pond. (kačica)', 'duck', 'kačica'),
        ('The ___ honks loudly. (hus)', 'goose', 'hus'),
        ('The ___ hops fast. (králik)', 'rabbit', 'králik'),
        ('The ___ likes cheese. (myš)', 'mouse', 'myš'),
        ('The ___ sings in the morning. (vták)', 'bird', 'vták'),
        ('I see a ___ in the aquarium. (ryba)', 'fish', 'ryba'),
        ('The ___ slithers on the ground. (had)', 'snake', 'had'),
        ('The ___ jumps into the water. (žaba)', 'frog', 'žaba'),
        ('The ___ lives in the forest. (medveď)', 'bear', 'medveď'),
        ('The ___ howls at night. (vlk)', 'wolf', 'vlk'),
        ('The ___ is clever and fast. (líška)', 'fox', 'líška'),
        ('The ___ runs in the forest. (jeleň)', 'deer', 'jeleň'),
        ('The ___ has orange stripes. (tiger)', 'tiger', 'tiger'),
        ('The ___ climbs trees. (opica)', 'monkey', 'opica'),
]

    for i, (sentence, missing, hint) in enumerate(animal_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )

    # ==========================================================
    # ALPHABET EXERCISES (Abeceda) - English alphabet for Slovaks
    # ==========================================================
    # Focus on letters/sounds that are different or tricky for Slovak speakers
    alphabet_data = [
        ('A a', 'ej', 'ako v "day"'),
        ('E e', 'í', 'ako v "see"'),
        ('I i', 'aj', 'ako v "my"'),
        ('O o', 'ou', 'ako v "go"'),
        ('U u', 'jú', 'ako v "you"'),
        ('W w', 'dabljú', 'neexistuje v slovenčine'),
        ('Q q', 'kjú', 'vždy s "u" - "qu"'),
        ('X x', 'eks', 'ako "ks"'),
        ('Y y', 'uaj', 'ako v "why"'),
        ('Th th', 'th', 'jazyk medzi zuby'),
        ('Ch ch', 'č', 'ako v "church"'),
        ('Sh sh', 'š', 'ako v "ship"'),
        ('Ph ph', 'f', 'ako v "phone"'),
        ('Gh gh', 'g/f/-', 'rôzna výslovnosť'),
    ]

    # Alphabet - Matching
    matching_exercise = Exercise.objects.create(
        title='Anglická abeceda - Spárovanie',
        lesson_type='alphabet',
        exercise_type='matching',
        question_text='Spárujte anglické písmená s ich výslovnosťou.',
        correct_answer='',
        explanation='Spojte písmená s ich správnou anglickou výslovnosťou.',
        order=1,
    )

    for i, (letter, sound, description) in enumerate(alphabet_data[:10]):
        Matching_Pair.objects.create(
            exercise=matching_exercise,
            left_text=letter,
            right_text=f'{sound} ({description})',
            order=i,
        )

    # Alphabet - Multiple Choice
    for i, (letter, sound, description) in enumerate(alphabet_data):
        mc_exercise = Exercise.objects.create(
            title=f'Ako sa vyslovuje "{letter}"?',
            lesson_type='alphabet',
            exercise_type='multiple_choice',
            question_text=f'Ako sa správne vyslovuje anglické písmeno/kombinácia "{letter}"?',
            correct_answer=description,
            explanation=f'"{letter}" sa vyslovuje {description}.',
            order=10 + i,
        )

        wrong_options = [d for l, s, d in alphabet_data if d != description]
        random.shuffle(wrong_options)
        all_choices = [description] + wrong_options[:3]
        random.shuffle(all_choices)

        for j, choice in enumerate(all_choices):
            Exercise_Choice.objects.create(
                exercise=mc_exercise,
                choice_text=choice,
                is_correct=(choice == description),
                order=j,
            )

    # Alphabet - Sentence Completion
    completion_exercise = Exercise.objects.create(
        title='Anglická abeceda - Doplň slovo',
        lesson_type='alphabet',
        exercise_type='sentence_completion',
        question_text='Doplňte chýbajúce anglické slovo (pozor na výslovnosť).',
        correct_answer='',
        explanation='Doplňte správne anglické slovo.',
        order=4,
    )

    alphabet_completions = [
        ('___ you very much! (Ďakujem)', 'Thank', 'th = jazyk medzi zuby'),
        ('I ___ so. (Myslím)', 'think', 'th = jazyk medzi zuby'),
        ('The ___ is sailing. (loď)', 'ship', 'sh = š'),
        ('My ___ number is 123. (telefónne)', 'phone', 'ph = f'),
        ('I have ___ money. (dosť)', 'enough', 'gh = f'),
        ('Please ___ the door. (zatvorte)', 'shut', 'sh = š'),
        ('I ___ reading books. (milujem)', 'love', 'v = zvuk v angličtine'),
        ('The baby is ___ loudly. (pláče)', 'crying', 'y = aj/e'),
        ('He ___ the guitar well. (hrá)', 'plays', 'ay = ej'),
        ('I ___ my keys. (stratil)', 'lost', 'o = krátke o'),
        ('They ___ to school every day. (chodia)', 'go', 'o = krátke o'),
        ('I need to ___ a letter. (napísať)', 'write', 'wr = tiché w'),
        ('She ___ her homework quickly. (robí)', 'does', 'o = krátke o'),
        ('The ___ is very bright. (slnko)', 'sun', 'u = krátke u'),
        ('I ___ a lot of water. (pijem)', 'drink', 'i = krátke i'),
        ('He ___ a beautiful song. (spieva)', 'sings', 'ng = nosový zvuk'),
        ('We ___ pizza for lunch. (jem)', 'eat', 'ea = i dlhé'),
        ('The cat ___ on the mat. (sedí)', 'sits', 'i = krátke i'),
        ('___ you like ice cream? (Máš rád)', 'Do', 'D = dlhé d'),
        ('I ___ very happy today. (som)', 'am', 'a = krátke a'),
]

    for i, (sentence, missing, hint) in enumerate(alphabet_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            english_sentence=sentence,
            missing_word=missing,
            hint=hint,
        )


def reverse_seed(apps, schema_editor):
    """Remove all seeded data."""
    Exercise = apps.get_model('exercises', 'Exercise')
    Exercise.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),  # Update this to your latest migration
    ]

    operations = [
        migrations.RunPython(seed_exercises, reverse_seed),
    ]