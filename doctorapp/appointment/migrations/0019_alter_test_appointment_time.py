# Generated by Django 4.0.5 on 2022-06-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0018_alter_test_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='appointment_time',
            field=models.TimeField(),
        ),
    ]
