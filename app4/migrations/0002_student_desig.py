# Generated by Django 4.2.13 on 2024-06-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='desig',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]