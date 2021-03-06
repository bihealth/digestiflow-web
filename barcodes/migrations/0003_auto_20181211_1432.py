# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-11 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectroles", "0006_add_remote_projects"),
        ("barcodes", "0002_auto_20181211_1413"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barcodeset",
            name="short_name",
            field=models.CharField(
                db_index=True,
                help_text="Short, unique identifier of barcode adapter set",
                max_length=100,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="barcodeset", unique_together=set([("project", "short_name")])
        ),
    ]
