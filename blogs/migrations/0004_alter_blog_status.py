# Generated by Django 5.1.7 on 2025-03-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_auhor_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default='Draft', max_length=20),
        ),
    ]
