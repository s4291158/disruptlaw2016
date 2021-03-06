# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160806_1641'),
        ('disputes', '0005_auto_20160806_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='disputematerial',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dispute',
            name='customer1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer1_dispute', to='users.Customer'),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='customer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer2_dispute', to='users.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='disputematerial',
            unique_together=set([('dispute', 'customer')]),
        ),
    ]
