# Generated by Django 2.2.10 on 2020-03-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0016_commandexecution_org_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='crontab',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Regularly perform'),
        ),
        migrations.AlterField(
            model_name='task',
            name='interval',
            field=models.IntegerField(blank=True, default=24, null=True, verbose_name='Cycle perform'),
        ),
    ]
