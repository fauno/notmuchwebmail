from django.http import HttpResponse
from django.shortcuts import render_to_response
import notmuch
import time

database = notmuch.Database('/home/fauno/Mail/solar.general')

def index(request):
    unread = notmuch.Query(database, 'tag:inbox and tag:unread')
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
