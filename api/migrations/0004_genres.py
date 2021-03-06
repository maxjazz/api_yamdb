# Generated by Django 3.0.5 on 2020-09-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genres",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=12)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]
