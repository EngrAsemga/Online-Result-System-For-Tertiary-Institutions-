# Generated by Django 5.0.1 on 2024-02-10 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0012_alter_firstsemisterresult_coursetitle_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckResult',
        ),
        migrations.RemoveField(
            model_name='collegecourse',
            name='department',
        ),
        migrations.RemoveField(
            model_name='declareresult',
            name='select_class',
        ),
        migrations.RemoveField(
            model_name='declareresult',
            name='select_student',
        ),
        migrations.DeleteModel(
            name='FirstSemisterResult',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='SecondSemisterResult',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.RemoveField(
            model_name='subjectcombination',
            name='select_class',
        ),
        migrations.DeleteModel(
            name='StudentRegistration',
        ),
        migrations.RemoveField(
            model_name='subjectcombination',
            name='select_subject',
        ),
        migrations.DeleteModel(
            name='CollegeCourse',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='DeclareResult',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='SubjectCombination',
        ),
    ]
