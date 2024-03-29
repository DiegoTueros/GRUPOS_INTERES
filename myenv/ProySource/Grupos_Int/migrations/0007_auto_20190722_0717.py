# Generated by Django 2.2.2 on 2019-07-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos_Int', '0006_convenio_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='hora_entrada',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_salida',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='maximo_horas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='minimo_horas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
