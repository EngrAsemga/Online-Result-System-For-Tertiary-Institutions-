# Generated by Django 5.0.1 on 2024-02-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0014_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstsemisterresult',
            name='gpa',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
