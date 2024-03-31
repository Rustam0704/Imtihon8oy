# Generated by Django 5.0.3 on 2024-03-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("profession", models.CharField(max_length=128)),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=128)),
                ("phone", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
