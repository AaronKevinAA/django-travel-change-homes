# Generated by Django 2.1.15 on 2019-12-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XXX', '0003_auto_20191228_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='account',
            field=models.CharField(default='一只小XX', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='credit',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='head_img',
            field=models.ImageField(default='/static/images/1.jpg', upload_to='head_img/'),
        ),
    ]
