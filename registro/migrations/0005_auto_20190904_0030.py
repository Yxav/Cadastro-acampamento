# Generated by Django 2.2.5 on 2019-09-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_register_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]