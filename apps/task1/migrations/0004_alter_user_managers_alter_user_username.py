# Generated by Django 5.0.3 on 2024-03-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task1", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
