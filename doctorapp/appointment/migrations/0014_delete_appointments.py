# Generated by Django 4.0.5 on 2022-06-12 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0013_doctorappointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointments',
        ),
    ]