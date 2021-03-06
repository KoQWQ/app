# Generated by Django 2.1.7 on 2019-02-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_competition_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='users',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='competition',
        ),
        migrations.AddField(
            model_name='competition',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Participant', verbose_name='Участники конкурса'),
        ),
    ]
