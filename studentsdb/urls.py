from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import groups_add, GroupList, GroupCreateView, GroupUpdateView, GroupDeleteView
from students.views.journal import JournalView
from students.views.users import ProfilesView, ProfileView
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import password_change

urlpatterns = patterns('',
    # Students urls

    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls

    url(r'^groups/$', GroupList.as_view(), name='groups'),
    url(r'^groups/add/$', GroupCreateView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    # Journal urls

    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

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
        template_name='users/profile.html')), name='profile'),
    url(r'^users/profile/change_password/$', password_change, {'template_name': 'users/password_change.html'}, name='change_password'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^users/profiles/$', login_required(ProfilesView), name='profiles'),
    url(r'^users/profiles/(?P<uid>\d+)$', login_required(ProfileView), name='user_profile'),
    #url(r'^users/password/reset/$','django.contrib.auth.views.password_reset',
    #    {'password_reset_form': PasswordResetForm,'post_reset_redirect': '/user/password/reset/done/'},
    #    name='password_reset'),
    #url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
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
