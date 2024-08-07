# Generated by Django 5.0.6 on 2024-06-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0003_social_rename_graduation_student_dept_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=10)),
                ('roll', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]
