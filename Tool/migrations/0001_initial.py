# Generated by Django 4.1 on 2023-03-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DietForm",
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
                ("Full_name", models.CharField(max_length=255)),
                ("Age", models.IntegerField()),
                ("Mobile_number", models.CharField(max_length=255)),
                ("E_mail", models.EmailField(max_length=254)),
            ],
        ),
    ]
