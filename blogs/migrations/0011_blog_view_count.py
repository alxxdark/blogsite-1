# Generated by Django 5.1.7 on 2025-05-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
