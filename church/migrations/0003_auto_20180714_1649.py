# Generated by Django 2.0.6 on 2018-07-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_auto_20180714_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
