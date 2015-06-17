# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='room',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u044f', blank=True),
            preserve_default=True,
        ),
    ]
