# Generated by Django 2.0.2 on 2018-03-09 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0007_userprofile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followed_users',
        ),
    ]
