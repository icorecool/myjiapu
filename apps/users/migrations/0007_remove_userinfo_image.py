# Generated by Django 2.2 on 2020-05-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_userinfo_add_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='image',
        ),
    ]