# Generated by Django 4.2.6 on 2023-11-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_list', '0002_alter_question_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
