# Generated by Django 5.0.6 on 2024-06-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0002_student_desig'),
    ]

    operations = [
        migrations.CreateModel(
            name='social',
            fields=[
                ('roll', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('dept', models.CharField(max_length=50)),
                ('fb', models.CharField(default='0', max_length=100)),
                ('twr', models.CharField(default='0', max_length=100)),
                ('lin', models.CharField(default='0', max_length=100)),
                ('git', models.CharField(default='0', max_length=100)),
                ('insta', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='graduation',
            new_name='dept',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='desig',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pincode',
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.CharField(default=None, max_length=10, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
