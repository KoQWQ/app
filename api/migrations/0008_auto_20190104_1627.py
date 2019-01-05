# Generated by Django 2.1.4 on 2019-01-04 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190104_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='competition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Competition', verbose_name='Конкурс'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number',
            field=models.PositiveIntegerField(default=None, verbose_name='Место в конкурсе'),
        ),
    ]