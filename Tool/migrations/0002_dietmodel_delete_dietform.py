# Generated by Django 4.1 on 2023-03-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tool", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DietModel",
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
                (
                    "Gender",
                    models.CharField(
                        choices=[("Female", "Female"), ("Male", "Male")],
                        default=1,
                        max_length=20,
                    ),
                ),
                ("Mobile_number", models.CharField(max_length=255)),
                ("E_mail", models.EmailField(max_length=254)),
                ("Fecal_sample", models.FileField(upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="DietForm",
        ),
    ]
