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

    # Number - Translation (Slovak to English)
    translation_exercise = Exercise.objects.create(
        title='Čísla - Preklad',
        lesson_type='number',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si použitie čísiel v anglických vetách.',
        order=3,
    )

    number_sentences = [
        ('Mám jeden dom.', 'I have one house.', 'dom = house'),
        ('Vidím dve autá.', 'I see two cars.', 'autá = cars'),
        ('Mám tri jablká.', 'I have three apples.', 'jablká = apples'),
        ('Je tu päť detí.', 'There are five children here.', 'deti = children'),
        ('Mám desať rokov.', 'I am ten years old.', 'rokov = years old'),
    ]

    for i, (slovak, english, hint) in enumerate(number_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
        )

    # Number - Sentence Completion (complete English sentences)
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
        ('She has ___ cats. (dve)', 'two', 'dva'),
        ('There are ___ days in a week. (sedem)', 'seven', 'sedem'),
        ('A decade is ___ years. (desať)', 'ten', 'desať'),
        ('I see ___ birds. (päť)', 'five', 'päť'),
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

    # Colour - Translation
    translation_exercise = Exercise.objects.create(
        title='Farby - Preklad',
        lesson_type='colour',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si použitie farieb v anglických vetách.',
        order=3,
    )

    colour_sentences = [
        ('Mám červené auto.', 'I have a red car.', 'auto = car'),
        ('Obloha je modrá.', 'The sky is blue.', 'obloha = sky'),
        ('Tráva je zelená.', 'The grass is green.', 'tráva = grass'),
        ('Slnko je žlté.', 'The sun is yellow.', 'slnko = sun'),
        ('Moja mačka je čierna.', 'My cat is black.', 'mačka = cat'),
        ('Sneh je biely.', 'Snow is white.', 'sneh = snow'),
    ]

    for i, (slovak, english, hint) in enumerate(colour_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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

    # Family - Translation
    translation_exercise = Exercise.objects.create(
        title='Rodina - Preklad',
        lesson_type='family',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si slovíčka o rodine v anglických vetách.',
        order=3,
    )

    family_sentences = [
        ('Moja mama je učiteľka.', 'My mother is a teacher.', 'učiteľka = teacher'),
        ('Môj otec pracuje v banke.', 'My father works in a bank.', 'pracuje = works'),
        ('Mám jedného brata.', 'I have one brother.', 'jedného = one'),
        ('Moja sestra je mladšia.', 'My sister is younger.', 'mladšia = younger'),
        ('Babka varí obed.', 'Grandmother is cooking lunch.', 'varí = is cooking'),
        ('Dedko číta noviny.', 'Grandfather is reading the newspaper.', 'noviny = newspaper'),
        ('Moji rodičia sú doma.', 'My parents are at home.', 'doma = at home'),
    ]

    for i, (slovak, english, hint) in enumerate(family_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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
        ('My ___ is my male parent. (otec)', 'father', 'otec'),
        ('My ___ is my parent\'s daughter. (sestra)', 'sister', 'sestra'),
        ('My ___ is my parent\'s son. (brat)', 'brother', 'brat'),
        ('My ___ is my mother\'s mother. (babka)', 'grandmother', 'babka'),
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

    # Food - Translation
    translation_exercise = Exercise.objects.create(
        title='Jedlo - Preklad',
        lesson_type='food',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si slovíčka o jedle v anglických vetách.',
        order=3,
    )

    food_sentences = [
        ('Chcem chlieb s maslom.', 'I want bread with butter.', 'chcem = I want'),
        ('Pijem mlieko.', 'I drink milk.', 'pijem = I drink'),
        ('Mám rád syr.', 'I like cheese.', 'mám rád = I like'),
        ('Jablko je červené.', 'The apple is red.', 'červené = red'),
        ('Polievka je horúca.', 'The soup is hot.', 'horúca = hot'),
        ('Dáte si kávu alebo čaj?', 'Would you like coffee or tea?', 'dáte si = would you like'),
        ('Potrebujem zeleninu.', 'I need vegetables.', 'potrebujem = I need'),
    ]

    for i, (slovak, english, hint) in enumerate(food_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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

    # School - Translation
    translation_exercise = Exercise.objects.create(
        title='Škola - Preklad',
        lesson_type='school',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si školské slovíčka v anglických vetách.',
        order=3,
    )

    school_sentences = [
        ('Idem do školy.', 'I am going to school.', 'idem = I am going'),
        ('Učiteľka píše na tabuľu.', 'The teacher is writing on the blackboard.', 'píše = is writing'),
        ('Moja kniha je na stole.', 'My book is on the desk.', 'na stole = on the desk'),
        ('Potrebujem ceruzku.', 'I need a pencil.', 'potrebujem = I need'),
        ('Máme prestávku.', 'We have a break.', 'máme = we have'),
        ('Zabudol som domácu úlohu.', 'I forgot my homework.', 'zabudol som = I forgot'),
        ('Skúška je zajtra.', 'The exam is tomorrow.', 'zajtra = tomorrow'),
    ]

    for i, (slovak, english, hint) in enumerate(school_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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

    # Animal - Translation
    translation_exercise = Exercise.objects.create(
        title='Zvieratá - Preklad',
        lesson_type='animal',
        exercise_type='translation',
        question_text='Preložte vety do angličtiny.',
        correct_answer='',
        explanation='Precvičte si názvy zvierat v anglických vetách.',
        order=3,
    )

    animal_sentences = [
        ('Môj pes je veľký.', 'My dog is big.', 'veľký = big'),
        ('Mačka spí na posteli.', 'The cat is sleeping on the bed.', 'spí = is sleeping'),
        ('Kôň beží rýchlo.', 'The horse runs fast.', 'beží = runs'),
        ('Vidím vtáka na strome.', 'I see a bird in the tree.', 'na strome = in the tree'),
        ('Slon je veľké zviera.', 'An elephant is a big animal.', 'zviera = animal'),
        ('Líška je chytrá.', 'The fox is clever.', 'chytrá = clever'),
        ('Králik má dlhé uši.', 'The rabbit has long ears.', 'dlhé uši = long ears'),
    ]

    for i, (slovak, english, hint) in enumerate(animal_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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
        ('A ___ says "woof". (pes)', 'dog', 'pes'),
        ('A ___ says "meow". (mačka)', 'cat', 'mačka'),
        ('A ___ gives us milk. (krava)', 'cow', 'krava'),
        ('A ___ has a long trunk. (slon)', 'elephant', 'slon'),
        ('A ___ is the king of the jungle. (lev)', 'lion', 'lev'),
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

    # Alphabet - Translation with tricky English sounds
    translation_exercise = Exercise.objects.create(
        title='Anglická abeceda - Slová',
        lesson_type='alphabet',
        exercise_type='translation',
        question_text='Preložte slová s ťažkými anglickými hláskami.',
        correct_answer='',
        explanation='Precvičte si slová s ťažkými anglickými hláskami.',
        order=3,
    )

    alphabet_sentences = [
        ('Ďakujem.', 'Thank you.', 'th = jazyk medzi zuby'),
        ('Myslím, že áno.', 'I think so.', 'th = jazyk medzi zuby'),
        ('Toto je moja loď.', 'This is my ship.', 'sh = š'),
        ('Telefonujem mame.', 'I am phoning my mom.', 'ph = f'),
        ('Dosť!', 'Enough!', 'gh = f na konci'),
        ('Prečo?', 'Why?', 'wh = hw alebo w'),
    ]

    for i, (slovak, english, hint) in enumerate(alphabet_sentences):
        Translation.objects.create(
            exercise=translation_exercise,
            slovak_sentence=slovak,
            english_sentence=english,
            hint=hint,
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
    ]

    for i, (sentence, missing, hint) in enumerate(alphabet_completions):
        Sentence_Completion.objects.create(
            exercise=completion_exercise,
            sentence=sentence,          # ✅ CORRECT
            correct_answer=missing,     # ✅ CORRECT
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