# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Students

def students_list(request):
	students = (
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
		{'id': 3,
		'first_name': u'Брат',
		'last_name': u'Махмуда',
		'ticket': 777,
		'image': 'img/snglss.jpg'},
		)
	return render(request, 'students/students_list.html', 
		{'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Groups
def groups_list(request):
	groups = (
		{'id': 1,
		'title': u'ФЕ-11',
		'leader': u'Піздюк а не староста'},
		{'id': 2,
		'title': u'ФБ-11',
		'leader': u'Староста халявщиков'},
		)
	return render(request, 'students/groups_list.html', 
		{'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
