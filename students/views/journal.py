# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def journal_list(request):
	student = (
		{'id': 1,
		'first_name': u'Тарас',
		'last_name': u'Зак',
		'ticket': 8,
		'image': 'img/yeah.jpg'},
		{'id': 2,
		'first_name': u'Сергей',
		'last_name': u'Гичкос',
		'ticket': 1,
		'image': 'img/hood.jpg'},
		)
	return render(request, 'students/journal.html', 
		{'student': student})
