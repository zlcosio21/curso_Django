# Generated by Django 4.2.3 on 2023-07-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]