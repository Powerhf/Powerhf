# Generated by Django 5.0 on 2024-03-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_energydieelfilling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energydieelfilling',
            name='Global_ID',
            field=models.CharField(max_length=50, verbose_name='Global ID'),
        ),
    ]
