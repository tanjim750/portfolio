# Generated by Django 5.0 on 2023-12-12 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=1000)),
                ('logo', models.ImageField(upload_to='logos')),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('copyright_text', models.CharField(max_length=50000)),
                ('profile', models.ImageField(upload_to='profile')),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menus')),
                ('social_links', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sociallinks')),
            ],
        ),
    ]