# Generated by Django 5.0.1 on 2024-04-10 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0051_uploadresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegecourse',
            name='department',
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
        migrations.DeleteModel(
            name='StudentRegistration',
        ),
        migrations.DeleteModel(
            name='UploadResult',
        ),
        migrations.DeleteModel(
            name='CollegeCourse',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
