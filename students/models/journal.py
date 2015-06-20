# -*- coding: utf-8 -*-

from django.db import models

class Journal(models.Model):

	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Журнал"
	
	month = models.CharField(
		verbose_name=u'Месяц',
		max_length=140,
		null=True,
		blank=True
    )
	student = models.ForeignKey('Student',
		verbose_name=u'Cтудент',
		blank=True,
 		null=True
	)

	def __unicode__(self):
		return u"Журнал відвідувань студента %s %s за %s місяць" % (self.student.first_name, self.student.last_name, self.month)

for i in range(0, 32):
    Journal.add_to_class('day %d' % i, models.BooleanField(
        verbose_name=u'День %d' % i,
        default=None
    ))
