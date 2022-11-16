# Generated by Django 4.1.3 on 2022-11-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_propertyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('hold', 'Hold'), ('open', 'Open'), ('closed', 'Closed')], default='buy', max_length=10),
        ),
    ]
