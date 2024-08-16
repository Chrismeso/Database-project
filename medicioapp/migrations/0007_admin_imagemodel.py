# Generated by Django 5.0.6 on 2024-07-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicioapp', '0006_member_alter_appointment_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]