# Generated by Django 5.0.6 on 2024-07-26 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitlogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitlog',
            old_name='fields',
            new_name='QR_fields',
        ),
    ]
