# Generated by Django 2.0.13 on 2019-04-28 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='autor',
        ),
    ]
