# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from ..models import Exam


def exams_list(request):
	exams = Exam.objects.all()

	return render(request, 'students/exams_list.html', 
		{'exams': exams})

def exam_add(request):
	return HttpResponse('<h1> Exam Form</h1>')

def exam_edit(request, eid):
	return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

def exam_delete(request, eid):
	return HttpResponse('<h1>Delete Exam %s</h1>' % eid)
