# Generated by Django 5.0 on 2023-12-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='logo',
            field=models.FileField(null=True, upload_to='logo'),
        ),
    ]
