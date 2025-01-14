# Generated by Django 4.2.1 on 2023-05-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_event_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Upcoming Event", "Upcoming Event"),
                    ("Past Event", "Past Event"),
                ],
                default="Upcoming Event",
                max_length=50,
                null=True,
            ),
        ),
    ]
