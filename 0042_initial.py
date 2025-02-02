# Generated by Django 5.0.1 on 2024-03-19 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ResultManagementApp', '0041_remove_collegecourse_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FirstSemisterResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNo', models.CharField(max_length=50)),
                ('courseCode', models.CharField(max_length=50)),
                ('scores', models.IntegerField()),
                ('mylevel', models.CharField(max_length=50)),
                ('dateUploaded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('staffNo', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNo', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
                ('dateEmployed', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondSemisterResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secregNo', models.CharField(max_length=50)),
                ('seclevel', models.CharField(max_length=50)),
                ('seccourseCode', models.CharField(max_length=50)),
                ('secscores', models.IntegerField()),
                ('seccourseUnit', models.IntegerField()),
                ('dateUploaded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('regNo', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('phoneNo', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('DateAdmitted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTitle', models.CharField(max_length=100)),
                ('courseCode', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=10)),
                ('Courseunit', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResultManagementApp.department')),
            ],
        ),
    ]
