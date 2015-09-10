# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import DeleteView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models.deletion import ProtectedError

from ..models import Group

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
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        try:
            return super(GroupDeleteView, self).dispatch(*args, **kwargs)
        except ProtectedError:
            #TODO: use massages
            #messages.add_message(request,messages.INFO, 'Неможливо видалити группу: вона містить студентів!')
            url = self.get_success_url()
            return HttpResponseRedirect(url+u'?status_message=Неможливо видалити группу: вона містить студентів!')


    def get_success_url(self):
        #TODO: message about success deletion 
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if "cancel_button" in request.POST:
            messages.add_message(request,messages.INFO, 'Видалення групи скасовано!')
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(GroupDeleteView, self).post(request, *args, **kwargs)
