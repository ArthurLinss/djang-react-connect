# Generated by Django 4.1.2 on 2023-07-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="quote",
            name="category",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
    ]
