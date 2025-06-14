# Generated by Django 5.2.1 on 2025-05-31 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.CharField(max_length=100)),
                ('pickup_location', models.CharField(max_length=100)),
                ('dropoff_location', models.CharField(max_length=100)),
                ('cycle_hours_used', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
