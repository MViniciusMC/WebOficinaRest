# Generated by Django 5.0.2 on 2024-02-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_workshop', '0003_alter_veiculos_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculos',
            name='ano',
            field=models.CharField(max_length=4),
        ),
    ]
