# Generated by Django 3.0.8 on 2020-07-31 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourLeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200)),
                ('venue_address', models.CharField(max_length=200)),
                ('venue_city', models.CharField(max_length=50)),
                ('venue_state', models.CharField(max_length=20)),
                ('venue_lat', models.FloatField(blank=True, null=True)),
                ('venue_lng', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('gig_date', models.DateField()),
                ('gig_start', models.TimeField()),
                ('gig_length', models.IntegerField(default=0)),
                ('pay', models.IntegerField()),
            ],
        ),
    ]
