# Generated by Django 2.2.5 on 2019-09-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='primeiro nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='ultimo nome')),
                ('phone', models.CharField(blank=True, default='', max_length=15, verbose_name='telefone')),
                ('age', models.CharField(blank=True, default='', max_length=2, verbose_name='idade')),
                ('church', models.CharField(max_length=100, verbose_name='cidade')),
                ('city', models.CharField(max_length=100, verbose_name='igreja')),
                ('email', models.EmailField(max_length=254)),
                ('obs', models.CharField(max_length=500, verbose_name='observação')),
            ],
        ),
    ]