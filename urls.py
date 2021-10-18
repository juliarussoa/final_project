from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from mysite.core import views as core_views
from mysite.notes import views as note_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^note/', note_views.home, name='note'),
    url(r'^create_note/', note_views.create_note, name='create_note'),
    url('.*', core_views.home, name='home')
]
