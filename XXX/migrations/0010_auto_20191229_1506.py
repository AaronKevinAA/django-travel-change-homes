# Generated by Django 2.1.15 on 2019-12-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XXX', '0009_auto_20191229_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpublish',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='home_image/'),
        ),
    ]