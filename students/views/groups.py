# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import UpdateView, DeleteView

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import StrictButton

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages import get_messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models.deletion import ProtectedError
from django.db import IntegrityError

from ..models import Group, Student
from ..util import paginate, get_current_group

#Groups
def groups_list(request):
    groups = Group.objects.all()

    #try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by == '':
        groups = groups.order_by('title')

    if order_by in ('title', 'leader', 'id'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
                groups = groups.reverse()
    # paginate students
    paginator = Paginator(groups, 4)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:

            # data for group object
            data = {'notes': request.POST.get('notes')}

            # validate user input
            title = request.POST.get('title', '').strip()
            if not title:
                messages.add_message(request, messages.WARNING, "Назва групи є обов'язковою")
            else:
                data['title'] = title

            leader = request.POST.get('leader', '').strip()
            if leader:
                students = Student.objects.filter(pk=leader)
                if hasattr(students[0], 'group'):
                    messages.add_message(request, messages.WARNING, "Обраний студент вже є старостою")
                if len(students) != 1:
                    #errors['student_group'] = u"Оберіть коректну групу"
                    messages.add_message(request, messages.WARNING, "Оберіть коректну групу")
                else:
                    data['leader'] = students[0]

            # save student
            storage = get_messages(request)
            if not storage:
                # create student object
                group = Group(**data)
                group.save()
                # redirect user to students list
                messages.add_message(request, messages.SUCCESS, 'Групу %s успішно додано!'% group)
                return HttpResponseRedirect(reverse('groups'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/groups_add.html',
                    {'students': Student.objects.filter(group=None).order_by('last_name')})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.add_message(request, messages.INFO, 'Додавання групи скасовано!')
            return HttpResponseRedirect(reverse('groups'))
    else:
        # initial form render
        return render(request, 'students/groups_add.html',
        {'students': Student.objects.filter(group=None).order_by('last_name')})


    return render(request, 'students/groups_add.html',
        {'students': Group.objects.all().order_by('last_name')})


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('groups_edit',kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-4'

        # add buttons
        self.helper.layout = Layout(
            'title',
            'leader',
            'notes',
        Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
        Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        
        )

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
            u'%s?status_message=Редагування групи відмінено!' %
        reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        try:
            return super(GroupDeleteView, self).dispatch(*args, **kwargs)
        # can we use ProtectedError without import ?
        except ProtectedError:
            #TODO: use massages
            #messages.add_message(request,messages.INFO, 'Неможливо видалити групу: вона містить студентів!')
            url = self.get_success_url()
            return HttpResponseRedirect(url+u'?status_message=Неможливо видалити групу: вона містить студентів!')


    def get_success_url(self):
        #TODO: message about success deletion 
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        if "cancel_button" in request.POST:
            messages.add_message(request,messages.INFO, 'Видалення групи скасовано!')
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(GroupDeleteView, self).post(request, *args, **kwargs)
