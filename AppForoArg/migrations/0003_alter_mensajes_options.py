# Generated by Django 4.2.2 on 2023-07-10 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppForoArg', '0002_rename_mensaje_mensajes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ('enviado',), 'verbose_name_plural': 'Mensajes'},
        ),
    ]