# Generated by Django 5.0.3 on 2024-03-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task1", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RenameField(
            model_name="user",
            old_name="deleted",
            new_name="is_deleted",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
