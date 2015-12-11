from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import data
import Laia5

def pop_end():
  ret = data.lis
  data.lis = data.lis.prev
  if data.lis == 0:
    data.lis = ret
  return ret

# Create your views here.

def index(request):
  template = loader.get_template('echo/index.html')
  context = RequestContext( request, {
    'message' : pop_end().data
  })
  if request.method == 'POST':
    if request.POST['data'] != "":
      data.lis.append_new(request.POST['data'])
  else:
    message = pop_end().data
    data.lis.append_new(message)
    st = ""
    for i in Laia5.response(message, 5):
      st += i.word + " "
    data.lis.append_new(st)
  return HttpResponse(template.render(context))

