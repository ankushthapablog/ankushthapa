from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from stats.models import AccessLogs
from django.shortcuts import render
import datetime

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_access_string(request):
    try:
        http_referer = request.META['HTTP_REFERER']
    except:
        http_referer = None
    client_ip = get_client_ip(request)
    user_agent = request.META['HTTP_USER_AGENT']
    dt = datetime.datetime.now()
    return str(dt) + ' - ' + str(user_agent) + ' - ' + str(client_ip) + ' - ' + str(http_referer)

def homepage(request):
    page = 'homepage'
    access_string = get_access_string(request)
    AccessLogs.objects.create(access_string=access_string, page_name=page)
    return render_to_response('homepage/homepage.html', {} , context_instance=RequestContext(request))
