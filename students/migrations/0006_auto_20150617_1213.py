# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_student_journal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='student_journal',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_journal',
        ),
    ]
