# Generated by Django 5.0.1 on 2024-02-17 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0018_remove_firstsemisterresult_gpa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckResult',
        ),
        migrations.RemoveField(
            model_name='firstsemisterresult',
            name='level',
        ),
        migrations.RemoveField(
            model_name='secondsemisterresult',
            name='level',
        ),
        migrations.RemoveField(
            model_name='collegecourse',
            name='department',
        ),
        migrations.RemoveField(
            model_name='secondsemisterresult',
            name='courseCode',
        ),
        migrations.RemoveField(
            model_name='firstsemisterresult',
            name='courseCode',
        ),
        migrations.RemoveField(
            model_name='firstsemisterresult',
            name='regNo',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.RemoveField(
            model_name='secondsemisterresult',
            name='regNo',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='CollegeCourse',
        ),
        migrations.DeleteModel(
            name='FirstSemisterResult',
        ),
        migrations.DeleteModel(
            name='SecondSemisterResult',
        ),
        migrations.DeleteModel(
            name='StudentRegistration',
        ),
    ]
