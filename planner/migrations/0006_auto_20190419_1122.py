# Generated by Django 2.1.4 on 2019-04-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20190419_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
