# Generated by Django 5.1.3 on 2024-12-02 05:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armani', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
