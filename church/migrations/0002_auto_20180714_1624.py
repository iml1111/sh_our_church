# Generated by Django 2.0.6 on 2018-07-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
    ]
