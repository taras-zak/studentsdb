# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
	"""Exam Model"""

	class Meta(object):
		verbose_name = u"Іспит"
		verbose_name_plural = u"Іспити"

	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва Іспиту")

	date = models.DateTimeField(
		blank=False,
		verbose_name=u"Час проведення")

	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Викладач")

	forgroup = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Группа")
	
	room = models.CharField(
		max_length=256,
		blank=True,
		null=True,
		verbose_name=u"Аудиторія")

	def __unicode__(self):
		return u"%s (%s)" % (self.title, self.teacher)
	
	
