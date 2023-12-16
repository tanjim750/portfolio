# Generated by Django 5.0 on 2023-12-16 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='visited_url',
        ),
        migrations.CreateModel(
            name='VisitedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.visitor')),
            ],
        ),
    ]