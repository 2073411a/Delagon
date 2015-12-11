from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import data

def pop_end():
  ret = data.lis
  data.lis = data.lis.nxt
  if data.lis == 0:
    data.lis = ret
  return ret

# Create your views here.

def index(request):
  template = loader.get_template('echo/index.html')
  context = RequestContext( request, {
    'message' : pop_end()
  })
  return HttpResponse(template.render(context))
