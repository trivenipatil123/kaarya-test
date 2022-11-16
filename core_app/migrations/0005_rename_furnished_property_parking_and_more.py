# Generated by Django 4.1.3 on 2022-11-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_property_property_type_alter_property_property_for_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='furnished',
            new_name='parking',
        ),
        migrations.RemoveField(
            model_name='property',
            name='transaction_type',
        ),
        migrations.AddField(
            model_name='property',
            name='allowed_for',
            field=models.CharField(blank=True, choices=[('new', 'Bachelor'), ('family', 'Family')], max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='builtup_area',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='property',
            name='furniture_type',
            field=models.CharField(choices=[('furnished', 'Furnished'), ('semifurnished', 'Semi-furnished'), ('unfurnished', 'Unfurnished')], default='unfurnished', max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='lifts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='rera_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='property',
            name='super_builtup_area',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='property',
            name='age_of_construction',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='builder',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='carper_area',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='facing',
            field=models.CharField(blank=True, choices=[('east', 'east'), ('west', 'west'), ('south', 'south'), ('north', 'north'), ('north-east', 'north-east'), ('north-west', 'north-west'), ('south-east', 'south-east'), ('south-west', 'south-west')], max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='landmark',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='long_desc',
            field=models.CharField(blank=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='no_of_balcony',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='no_of_bath',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='no_of_bed',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_contact',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='type_of_ownership',
            field=models.CharField(blank=True, choices=[('freehold', 'Freehold'), ('leasehold', 'Leasehold'), ('power of attorney', 'Power of attorney'), ('cooperative society', 'Cooperative society')], max_length=20),
        ),
    ]