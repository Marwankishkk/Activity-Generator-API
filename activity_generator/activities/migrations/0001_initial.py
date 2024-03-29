# Generated by Django 4.2.11 on 2024-03-10 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Activity",
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
                ("text", models.CharField(max_length=255)),
                ("tags", models.CharField(blank=True, max_length=255)),
                (
                    "difficulty_level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="activities.category",
                    ),
                ),
            ],
        ),
    ]
