# Generated by Django 3.0.5 on 2020-08-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200811_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='cntlike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
