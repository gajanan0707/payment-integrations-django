# Generated by Django 4.1.4 on 2023-04-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("thumbnail", models.CharField(max_length=500)),
                ("image", models.CharField(max_length=100)),
                ("rating", models.FloatField()),
                ("brand", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
            ],
        ),
    ]
