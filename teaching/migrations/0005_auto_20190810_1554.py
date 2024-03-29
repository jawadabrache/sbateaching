# Generated by Django 2.2.4 on 2019-08-10 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0004_auto_20190810_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='max_nbr_sections_to_allocate',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='min_nbr_sections_to_allocate',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
            preserve_default=False,
        ),
    ]
