# Generated by Django 3.0.3 on 2020-02-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pzz', '0006_auto_20200220_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='body',
        ),
        migrations.AddField(
            model_name='pizza',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
