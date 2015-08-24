from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import groups_list, groups_add, groups_edit, groups_delete
from students.views.journal import JournalView
from students.views.users import ProfileView
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Students urls

    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls

    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', login_required(groups_add), name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'),

    # Journal urls

    url(r'^journal/$', JournalView.as_view(), name='journal'),

    # Exams urls

    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^exams/(?P<eid>\d+)/edit/$', 'students.views.exams.exam_edit', name='exam_edit'),
    url(r'^exams/(?P<eid>\d+)/delete/$', 'students.views.exams.exam_delete', name='exam_delete'),

    # Contact urls
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),

    #admin
    url(r'^admin/', include(admin.site.urls)),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),
    url(r'^users/profile/(?P<uid>\d+)$', login_required(ProfileView), name='user_profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':	'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),	name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    # Social Auth Related urls
    url('', include('social.apps.django_app.urls', namespace='social')),

)

if DEBUG:
    # serve files from media folder
        urlpatterns += patterns('',
                                url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                    'document_root': MEDIA_ROOT}))
