# Generated by Django 3.1.4 on 2020-12-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='field_of_study',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.TextField(blank=True),
        ),
    ]