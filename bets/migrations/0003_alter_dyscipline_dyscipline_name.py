# Generated by Django 4.0.6 on 2022-07-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_dyscipline_blogabetbets_dyscipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dyscipline',
            name='dyscipline_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]