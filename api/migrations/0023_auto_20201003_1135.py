# Generated by Django 3.0.5 on 2020-10-03 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20201001_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['pub_date']},
        ),
    ]
