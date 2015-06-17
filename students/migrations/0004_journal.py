# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=140, null=True, verbose_name='\u041c\u0435\u0441\u044f\u0446', blank=True)),
                ('student_journal', models.ForeignKey(verbose_name='C\u0442\u0443\u0434\u0435\u043d\u0442', blank=True, to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0416\u0443\u0440\u043d\u0430\u043b',
            },
            bases=(models.Model,),
        ),
    ]
