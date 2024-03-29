# Generated by Django 2.2.4 on 2019-08-09 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identif', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=60)),
                ('level', models.CharField(choices=[('U', 'Undergraduate'), ('G', 'Graduate')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('status', models.CharField(choices=[('Assis.', 'Assistant Professor'), ('Assoc.', 'Associate Professor'), ('Full', 'Full Professor'), ('Lect.', 'Lecturer'), ('Adjun.', 'Adjunct')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateField()),
                ('preference', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('comment', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.Course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.Faculty')),
            ],
        ),
    ]
