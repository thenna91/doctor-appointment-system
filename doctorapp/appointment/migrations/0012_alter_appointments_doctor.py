# Generated by Django 4.0.5 on 2022-06-12 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_alter_appointments_doctor_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctorappt', to='appointment.doctor'),
        ),
    ]
