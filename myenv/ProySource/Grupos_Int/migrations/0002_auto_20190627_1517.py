# Generated by Django 2.2.2 on 2019-06-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos_Int', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='ruc',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='representante',
            name='dni',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
