# Generated by Django 4.0.5 on 2022-06-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
    ]
