# Generated by Django 4.1.5 on 2023-01-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_auto_20190703_1816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="present",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="time",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
