# Generated by Django 2.2.4 on 2019-08-10 14:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identif', models.CharField(choices=[('TR08000920', 'TR 8:00 - 9:20'), ('TR09301050', 'TR 9:30 - 10:50'), ('TR11001220', 'TR 11:00 - 12:20'), ('TR12301350', 'TR 12:30 - 13:50'), ('TR14001520', 'TR 14:00 - 15:20'), ('TR15301650', 'TR 15:30 - 16:50'), ('TR17001820', 'TR 17:00 - 18:20'), ('TR18301950', 'TR 18:30 - 19:50'), ('MWF08000850', 'MWF 8:00 - 8:50'), ('MWF09000950', 'MWF 9:00 - 9:50'), ('MWF10001050', 'MWF 10:00 - 10:50'), ('MWF11001150', 'MWF 11:00 - 11:50'), ('MWF13401430', 'MWF 13:40 - 14:30'), ('MW12001320', 'MW 12:00 - 13:20'), ('MW15401700', 'MW 15:40 - 17:00'), ('MW17101830', 'MW 17:10 - 18:30')], max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='nbr_sections_offered',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Timeslot_Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateField()),
                ('preference', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('comment', models.TextField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.Faculty')),
                ('ts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.Timeslot')),
            ],
        ),
    ]
