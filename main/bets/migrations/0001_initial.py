# Generated by Django 4.0.6 on 2022-07-05 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogabetAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_name', models.CharField(max_length=255)),
                ('author_yield', models.FloatField()),
                ('author_odds', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogabetBets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(max_length=255)),
                ('pick', models.CharField(max_length=255)),
                ('odd', models.FloatField()),
                ('start', models.DateTimeField(max_length=100)),
                ('stake', models.IntegerField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.blogabetauthor')),
            ],
            options={
                'ordering': ['-start'],
                'abstract': False,
            },
        ),
    ]
