# Generated by Django 5.1.3 on 2024-12-02 06:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armani', '0004_rename_mentors_mentor_alter_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]