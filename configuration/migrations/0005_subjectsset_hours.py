# Generated by Django 2.1.3 on 2019-05-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0004_classes_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectsset',
            name='hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
