# -*- coding: utf-8 -*-

from django.db import models

class MonthJournal(models.Model):
	"""Student Monthly Journal"""

	class Meta:
		verbose_name = u"Група"
		verbose_name_plural = u"Журнал"
	
	date = models.DateField(
		verbose_name=u'Дата',
		blank=False
    )

	student = models.ForeignKey('Student',
		verbose_name=u'Cтудент',
		blank=True,
 		null=True,
		unique_for_month='date'
	)

	# list of days, each says whether student was presenе or not
	present_day1 = models.BooleanField(default=False)	
	present_day2 = models.BooleanField(default=False)
	present_day3 = models.BooleanField(default=False)
	present_day4 = models.BooleanField(default=False)
	present_day5 = models.BooleanField(default=False)
	present_day6 = models.BooleanField(default=False)
	present_day7 = models.BooleanField(default=False)
	present_day8 = models.BooleanField(default=False)
	present_day9 = models.BooleanField(default=False)
	present_day10 = models.BooleanField(default=False)
	present_day11 = models.BooleanField(default=False)
	present_day12 = models.BooleanField(default=False)
	present_day13 = models.BooleanField(default=False)
	present_day14 = models.BooleanField(default=False)
	present_day15 = models.BooleanField(default=False)
	present_day16 = models.BooleanField(default=False)
	present_day17 = models.BooleanField(default=False)
	present_day18 = models.BooleanField(default=False)
	present_day19 = models.BooleanField(default=False)
	present_day20 = models.BooleanField(default=False)
	present_day21 = models.BooleanField(default=False)
	present_day22 = models.BooleanField(default=False)
	present_day23 = models.BooleanField(default=False)
	present_day24 = models.BooleanField(default=False)
	present_day25 = models.BooleanField(default=False)
	present_day26 = models.BooleanField(default=False)
	present_day27 = models.BooleanField(default=False)
	present_day28 = models.BooleanField(default=False)
	present_day29 = models.BooleanField(default=False)
	present_day30 = models.BooleanField(default=False)
	present_day31 = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u"Журнал відвідувань студента %s %s за %s місяць %s року" % (self.student.first_name, self.student.last_name, self.date.month, self.date.year)

"""for i in range(1, 32):
    MonthJournal.add_to_class('day %d' % i, models.BooleanField(
        verbose_name=u'День %d' % i,
        default=None
    ))""" 
