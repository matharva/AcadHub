# Generated by Django 3.1.4 on 2020-12-06 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postandcomment', '0006_remove_post_community'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Community',
        ),
    ]
