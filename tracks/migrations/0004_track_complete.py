# Generated by Django 2.1.2 on 2018-10-08 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_remove_track_r_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
