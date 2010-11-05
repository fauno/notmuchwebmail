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
from json import loads as json_load
from base64 import b64decode

database = notmuch.Database(settings.NOTMUCH_DIR)

# TODO DRY it a little
# TODO retrieve top level messages and their replies.
def index(request, thread_id):
    # Unicode thread_id fails
    query =''.join(['thread:', str(thread_id)])
    thread = notmuch.Query(database, query)
    result = thread.search_messages()

    result_messages = []
    messages = []

    for message in result:
        result_messages.append(message)

    count = 0
    for message in result_messages:
        messages.append(json_load(message.format_message_as_json()))
        messages[count]['body'][0]['content'] = b64decode(messages[count]['body'][0]['content'])
        count += 1

    return render_to_response('pager.html', { 'messages': messages })
