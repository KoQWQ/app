# Generated by Django 2.1.4 on 2019-01-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_judge_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='cost',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость участия'),
        ),
    ]