# Generated by Django 5.0.1 on 2024-01-29 20:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0002_remove_checkresult_level_remove_checkresult_semister_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkresult',
            name='cname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
