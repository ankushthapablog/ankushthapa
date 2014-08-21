from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

def homepage(request):
    return render_to_response('homepage/homepage.html', {} , context_instance=RequestContext(request))

def redirecter(request):
    return HttpResponseRedirect('/')
    #return render_to_response('homepage/homepage.html', {} , context_instance=RequestContext(request))

