# Generated by Django 3.0.11 on 2021-07-24 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20210724_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 24, 19, 38, 14, 749101, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
