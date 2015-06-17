# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_journal',
            field=models.ForeignKey(verbose_name='\u0412\u0456\u0434\u0432\u0456\u0434\u0443\u0432\u0430\u043d\u043d\u044f', to='students.Journal', null=True),
            preserve_default=True,
        ),
    ]
