# Generated by Django 2.1.4 on 2019-01-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190104_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='competition',
            field=models.ManyToManyField(blank=True, null=True, to='api.Competition', verbose_name='Конкурсы, в которых он является судьей'),
        ),
    ]
