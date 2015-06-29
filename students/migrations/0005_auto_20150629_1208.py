# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_exam_monthjournal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 1',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 10',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 11',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 12',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 13',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 14',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 15',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 16',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 17',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 18',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 19',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 2',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 20',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 21',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 22',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 23',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 24',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 25',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 26',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 27',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 28',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 29',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 3',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 30',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 31',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 4',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 5',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 6',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 7',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 8',
        ),
        migrations.RemoveField(
            model_name='monthjournal',
            name='day 9',
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day1',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day10',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day11',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day12',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day13',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day14',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day15',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day16',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day17',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day18',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day19',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day2',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day20',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day21',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day22',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day23',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day24',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day25',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day26',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day27',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day28',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day29',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day3',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day30',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day31',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day4',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day5',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day6',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day7',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day8',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='present_day9',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
