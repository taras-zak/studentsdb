# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Exam
from ..util import paginate, get_current_group


def exams_list(request):
    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(forgroup_id=current_group)
    else:
        # otherwise show all students
        exams = Exam.objects.all()
    Exam.objects.filter(forgroup_id=2)
    #context = {}
    context = paginate(exams, 5, request, {}, var_name='exams')

    return render(request, 'students/exams_list.html',
        context)

def exam_add(request):
    return HttpResponse('<h1> Exam Form</h1>')

def exam_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

def exam_delete(request, eid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % eid)
