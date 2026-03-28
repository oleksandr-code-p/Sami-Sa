from django.db import migrations, models
from exercises.sentence_completion_seed_data import lookup_seed_sentence


def populate_sentence_completion_fields(apps, schema_editor):
    SentenceCompletion = apps.get_model("exercises", "Sentence_Completion")

    for completion in SentenceCompletion.objects.select_related("exercise"):
        answer_text = completion.correct_answer or completion.sentence
        sentence_text = completion.display_sentence or lookup_seed_sentence(
            completion.exercise.lesson_type,
            answer_text,
            completion.hint,
        )

        updates = []
        if not completion.correct_answer and answer_text:
            completion.correct_answer = answer_text
            updates.append("correct_answer")
        if not completion.display_sentence and sentence_text:
            completion.display_sentence = sentence_text
            updates.append("display_sentence")

        if updates:
            completion.save(update_fields=updates)


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0004_remove_sentence_completion_correct_answer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sentence_completion",
            name="correct_answer",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sentence_completion",
            name="display_sentence",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RunPython(populate_sentence_completion_fields, migrations.RunPython.noop),
    ]