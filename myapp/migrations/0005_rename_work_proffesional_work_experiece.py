# Generated by Django 4.2 on 2023-05-03 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_proffesional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proffesional',
            old_name='work',
            new_name='work_experiece',
        ),
    ]
