# Generated by Django 5.0 on 2023-12-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_visitedurl_total_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='page_title',
            field=models.CharField(default='Tanjim Abubokor', max_length=100000),
        ),
        migrations.AddField(
            model_name='blog',
            name='page_title',
            field=models.CharField(default='Tanjim Abubokor', max_length=100000),
        ),
        migrations.AddField(
            model_name='home',
            name='page_title',
            field=models.CharField(default='Tanjim Abubokor', max_length=100000),
        ),
        migrations.AddField(
            model_name='project',
            name='page_title',
            field=models.CharField(default='Tanjim Abubokor', max_length=100000),
        ),
        migrations.AddField(
            model_name='service',
            name='page_title',
            field=models.CharField(default='Tanjim Abubokor', max_length=100000),
        ),
    ]