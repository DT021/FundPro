# Generated by Django 3.0.7 on 2020-06-24 03:55

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0003_trader_aum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='positions',
            field=jsonfield.fields.JSONField(),
        ),
    ]