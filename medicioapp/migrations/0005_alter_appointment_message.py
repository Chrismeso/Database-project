# Generated by Django 5.0.6 on 2024-07-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicioapp', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.CharField(max_length=200),
        ),
    ]
