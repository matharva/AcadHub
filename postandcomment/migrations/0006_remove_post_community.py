# Generated by Django 3.1.4 on 2020-12-06 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postandcomment', '0005_auto_20201206_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='community',
        ),
    ]
