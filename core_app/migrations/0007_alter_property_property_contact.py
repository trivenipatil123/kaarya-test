# Generated by Django 4.1.3 on 2022-11-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0006_alter_property_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
