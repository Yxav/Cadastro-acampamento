# Generated by Django 2.2.5 on 2019-09-04 02:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_remove_register_sleeping'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='sleep',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Alocação'),
            preserve_default=False,
        ),
    ]
