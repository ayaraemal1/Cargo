# Generated by Django 4.2.1 on 2023-05-25 10:22
import csv

from django.db import migrations

BATCH_SIZE = 10000


def load_locations(apps, schema_editor):
    Location = apps.get_model("location", "Location")
    with open("apps/location/uszips.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        batch = []
        for row in reader:
            batch.append(Location(zip_code=row[0], latitude=row[1], longitude=row[2], city=row[3], state=row[5]))
            if len(batch) >= BATCH_SIZE:
                Location.objects.bulk_create(batch)
                batch = []
        if batch:
            Location.objects.bulk_create(batch)


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_locations),
    ]
