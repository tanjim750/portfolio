# Generated by Django 5.0 on 2023-12-15 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_contact_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.TextField(null=True),
        ),
    ]
