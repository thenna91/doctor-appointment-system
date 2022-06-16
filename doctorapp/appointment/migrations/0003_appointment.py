# Generated by Django 4.0.5 on 2022-06-12 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_doctor_age_remove_doctor_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_firstname', models.CharField(max_length=20)),
                ('patient_lastname', models.CharField(max_length=20)),
                ('appointment_time', models.DateTimeField()),
                ('kind', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.doctor')),
            ],
        ),
    ]
