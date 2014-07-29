from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

def homepage(request):
    return HttpResponseRedirect('http://about.me/ankushthapa/')
    #return render_to_response('homepage/homepage.html', {} , context_instance=RequestContext(request))
