# Generated by Django 4.0.6 on 2022-07-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0006_forumbukmacherskieauthor_zawodtyperbets_analise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zawodtyperbets',
            name='bukmacher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
