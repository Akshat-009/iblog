# Generated by Django 3.0.5 on 2020-08-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200811_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.IntegerField(default=0),
        ),
    ]