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

from django.conf import settings
from django.shortcuts import render_to_response
import notmuch
import time

database = notmuch.Database(settings.NOTMUCH_DIR)

def index(request):
    return search(request, 'tag:inbox and tag:unread')

def search(request, search_string):
    unread = notmuch.Query(database, str(search_string))
    result = unread.search_threads()

    result_threads = []
    threads = []
    count = 0

    for thread in result:
        count += 1
        if count > 50: break

        result_threads.append(thread)

    for thread in result_threads:
        threads.append({
            'id': thread.get_thread_id(),
            'subject': thread.get_subject(),
            'message_count': thread.get_total_messages(),
            'newest_date': time.asctime(time.localtime(thread.get_newest_date())),
            'oldest_date': time.asctime(time.localtime(thread.get_oldest_date())),
            'duration': thread.get_newest_date() - thread.get_oldest_date(),
            'tag_list': str(thread.get_tags()).split()
        })


    return render_to_response('threads.html', { 'threads': threads })
