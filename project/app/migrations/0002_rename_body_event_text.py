# Generated by Django 4.2.1 on 2023-05-25 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(model_name="event", old_name="body", new_name="text",),
    ]
