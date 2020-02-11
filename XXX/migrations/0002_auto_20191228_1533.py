# Generated by Django 2.1.15 on 2019-12-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XXX', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realname',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='account',
            field=models.CharField(blank=True, default='一只小XX', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='credit',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='head_img',
            field=models.ImageField(default='/static/images/1.jpg', upload_to='head_img/'),
        ),
    ]
