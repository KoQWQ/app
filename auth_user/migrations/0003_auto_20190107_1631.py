# Generated by Django 2.1.4 on 2019-01-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_userabstract_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userabstract',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Статус персонала'),
        ),
    ]
