# -*- coding: utf-8 -*-
# notmuch webmail
# Aiming to be a libre replacement for GMail
# Copyright (C) 2010 Nicolás Reynolds <fauno@kiwwwi.com.ar>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# Django settings for notmuchwebmail project.

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^notmuchwebmail/', include('notmuchwebmail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^inbox/$', 'inbox.views.index'),
    (r'^inbox/unread$', 'inbox.views.index'),
    url(r'^pager/(?P<thread_id>[a-z0-9]+)$', 'pager.views.index', name='pager'),
    (r'^download/', include('django_agpl.urls'))
)
