# Generated by Django 2.1.4 on 2019-01-05 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190104_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_off', models.BooleanField(default=False, verbose_name='Участник проходит')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('competition', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='api.Competition', verbose_name='Конкурс')),
                ('participants', models.ManyToManyField(blank=True, related_name='_participants', to='api.Round', verbose_name='Участники')),
                ('round', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='round', to='api.Round', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Заход',
                'verbose_name_plural': 'Заходы',
            },
        ),
    ]
