# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_exam_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('day 1', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 1')),
                ('day 2', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 2')),
                ('day 3', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 3')),
                ('day 4', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 4')),
                ('day 5', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 5')),
                ('day 6', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 6')),
                ('day 7', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 7')),
                ('day 8', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 8')),
                ('day 9', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 9')),
                ('day 10', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 10')),
                ('day 11', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 11')),
                ('day 12', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 12')),
                ('day 13', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 13')),
                ('day 14', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 14')),
                ('day 15', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 15')),
                ('day 16', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 16')),
                ('day 17', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 17')),
                ('day 18', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 18')),
                ('day 19', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 19')),
                ('day 20', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 20')),
                ('day 21', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 21')),
                ('day 22', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 22')),
                ('day 23', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 23')),
                ('day 24', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 24')),
                ('day 25', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 25')),
                ('day 26', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 26')),
                ('day 27', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 27')),
                ('day 28', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 28')),
                ('day 29', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 29')),
                ('day 30', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 30')),
                ('day 31', models.BooleanField(default=None, verbose_name='\u0414\u0435\u043d\u044c 31')),
                ('student', models.ForeignKey(unique_for_month=b'date', blank=True, to='students.Student', null=True, verbose_name='C\u0442\u0443\u0434\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0416\u0443\u0440\u043d\u0430\u043b',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='journal',
            name='student',
        ),
        migrations.DeleteModel(
            name='Journal',
        ),
    ]
