# Generated by Django 5.0.1 on 2024-04-14 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0054_remove_firstsemisterresult_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegecourse',
            name='semester',
        ),
    ]
