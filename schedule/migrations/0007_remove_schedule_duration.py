# Generated by Django 2.2.1 on 2019-06-12 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_schedule_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='duration',
        ),
    ]
