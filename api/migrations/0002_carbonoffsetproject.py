# Generated by Django 5.1.1 on 2024-11-07 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonOffsetProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('offset_potential_tons', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('benefits', models.JSONField()),
                ('activities', models.JSONField()),
                ('link', models.URLField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
