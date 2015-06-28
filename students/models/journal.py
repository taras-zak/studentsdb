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

	def __unicode__(self):
		return u"Журнал відвідувань студента %s %s за %s місяць %s року" % (self.student.first_name, self.student.last_name, self.date.month, self.date.year)

for i in range(1, 32):
    MonthJournal.add_to_class('day %d' % i, models.BooleanField(
        verbose_name=u'День %d' % i,
        default=None
    ))
