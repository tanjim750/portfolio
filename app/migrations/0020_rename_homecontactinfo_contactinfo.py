# Generated by Django 5.0 on 2023-12-15 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_sidebar_logo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeContactInfo',
            new_name='ContactInfo',
        ),
    ]