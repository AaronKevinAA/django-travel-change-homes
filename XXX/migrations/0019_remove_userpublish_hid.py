# Generated by Django 2.1.15 on 2019-12-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('XXX', '0018_userpublish_hid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpublish',
            name='hid',
        ),
    ]
