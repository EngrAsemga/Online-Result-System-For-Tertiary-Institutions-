# Generated by Django 5.0.1 on 2024-02-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
