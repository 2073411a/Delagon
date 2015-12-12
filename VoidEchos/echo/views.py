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

def to_ascii(st):
  ret = ""
  for i in st:
    if not ord(i) > 128:
      ret += i
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
      st = ""
      print request.POST['data']
      for i in Laia5.response(to_ascii(request.POST['data']), 5):
        st += i.word + " "
      context = RequestContext( request, {
        'message' : st
      })
    else:
      message = pop_end().data
      data.lis.append_new(message)
      st = ""
      print request.POST['data']
      for i in Laia5.response(to_ascii(message), 5):
        st += i.word + " "
      data.lis.append_new(st)
      context = RequestContext( request, {
        'message' : st
      })
  else:
    message = pop_end().data
    data.lis.append_new(message)
    st = ""
    print message
    for i in Laia5.response(to_ascii(message), 5):
      st += i.word + " "
    data.lis.append_new(st)
  Laia5.Save()
  return HttpResponse(template.render(context))

