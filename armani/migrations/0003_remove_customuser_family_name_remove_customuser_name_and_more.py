# Generated by Django 5.1.3 on 2024-12-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armani', '0002_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(blank=True, max_length=11, null=True),
        ),
    ]