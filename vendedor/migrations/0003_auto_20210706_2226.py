# Generated by Django 3.2.5 on 2021-07-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0002_auto_20210706_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]