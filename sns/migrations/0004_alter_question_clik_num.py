# Generated by Django 4.1 on 2022-11-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_question_clik_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='clik_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
