# Generated by Django 5.1.2 on 2024-10-14 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_proyectos_fecha_inicio_alter_proyectos_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
