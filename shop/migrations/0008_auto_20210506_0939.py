# Generated by Django 3.2.1 on 2021-05-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210506_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='claimautomobile',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='claimlaptop',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
