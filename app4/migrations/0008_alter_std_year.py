# Generated by Django 5.0.6 on 2024-06-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0007_alter_std_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]
