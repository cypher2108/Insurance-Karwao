# Generated by Django 3.2.1 on 2021-05-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_smartphone_img_automobile_automobile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimlaptop',
            name='is_repairable',
            field=models.BooleanField(default=False),
        ),
    ]
