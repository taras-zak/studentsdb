# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.messages import get_messages

from django.forms import ModelForm
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group
from ..util import paginate, get_current_group

from endless_pagination.decorators import page_template

# Students
@page_template('students/students_list_page.html')
def students_list(request, template='students/students_list.html', extra_context=None):
    # check if we need to show only one group of students
    current_group = get_current_group(request)

    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        #otherwise show all students
        students = Student.objects.all()

    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by == '':
        students = students.order_by('last_name')

    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
                students = students.reverse()

    return render(request, template, {'students': students})

@login_required
def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            #errors = {}
            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                messages.add_message(request, messages.WARNING, "Ім'я є обов'язковим")
                #errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                messages.add_message(request, messages.WARNING, "Прізвище є обов'язковим")
                #errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                messages.add_message(request, messages.WARNING, "Дата народження є обов'язковою")
                #errors['birthday'] = u"Дата народження є обов'язковою"

            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    messages.add_message(request, messages.WARNING, "Введіть коректний формат дати (напр. 1984-12-30)")
                    #errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            #TODO: validate
            if not ticket:
                messages.add_message(request, messages.WARNING, "Номер білета є обов'язковим")
                #errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                messages.add_message(request, messages.WARNING, "Оберіть групу для студента")
                #errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    #errors['student_group'] = u"Оберіть коректну групу"
                    messages.add_message(request, messages.WARNING, "Оберіть коректну групу")
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo and ('image' in photo.content_type):
                data['photo'] = photo
            elif 'image' not in photo.content_type:
                messages.add_message(request, messages.WARNING, "Завантажте корректне зображення")

            # save student
            storage = get_messages(request)
            if not storage:
                # create student object
                student = Student(**data)
                student.save()

                # redirect user to students list
                messages.add_message(request, messages.SUCCESS, 'Студента %s успішно додано!'% student)
                return HttpResponseRedirect(reverse('home'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title')})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.add_message(request, messages.INFO, 'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})


    return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit',kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-4'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return u'%s?status_message=Студента успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
            u'%s?status_message=Редагування студента відмінено!' %
        reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return u'%s?status_message=Студента успішно видалено!' % reverse('home')
