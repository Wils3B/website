# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-13 23:24
from __future__ import unicode_literals

from django.db import migrations
import datetime

def update_intern_selections(apps, schema_editor):
    InternSelection = apps.get_model('home.InternSelection')
    interns = InternSelection.objects.all()
    for i in interns:
        i.initial_feedback_due = i.project.project_round.participating_round.initialfeedback
        i.initial_feedback_opens = i.initial_feedback_due - datetime.timedelta(days=7)
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0118_auto_20181213_2324'),
    ]

    operations = [
        migrations.RunPython(update_intern_selections, reverse_code=migrations.RunPython.noop),
    ]