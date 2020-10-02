# Generated by Django 3.0.5 on 2020-10-01 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_remove_titles_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="titles",
            name="rating",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
            preserve_default=False,
        ),
    ]