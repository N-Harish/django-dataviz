# Generated by Django 3.1.3 on 2020-12-20 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0002_auto_20201220_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='Customer_ID',
        ),
    ]
