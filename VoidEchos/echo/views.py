from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import data
import Laia5
import threading

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

class threadSave(threading.Thread):
  def run(self):
    Laia5.Save()

# Create your views here.

def index(request):
  threadSave().start()
  template = loader.get_template('echo/index.html')
  context = RequestContext( request, {
    'message' : pop_end().data,
    'last' : " "
  })
  if request.method == 'POST':
    if request.POST['data'] != "":
      data.lis.append_new(request.POST['data'])
      st = ""
      print request.POST['data']
      resp = Laia5.response(to_ascii(request.POST['data']), 5)
      for i in resp:
        st += i.word + " "
      context = RequestContext( request, {
        'message' : st,
        'last' : request.POST['data']
      })
      if request.POST['last'] != " ":
        s1 = Laia5.concept(request.POST['last'], 5 ,5)
        s2 = Laia5.concept(st, 5 , 5)
        Laia5.memories += [Laia5.memory(s1,s2)]
    else:
      message = pop_end().data
      data.lis.append_new(message)
      st = ""
      for i in Laia5.response(to_ascii(message), 5):
        st += i.word + " "
      data.lis.append_new(st)
      context = RequestContext( request, {
        'message' : st,
        'last' : " "
      })
      if request.POST['last'] != " ":
        s1 = Laia5.concept(request.POST['last'], 5 ,5)
        s2 = Laia5.concept(st, 5 , 5)
        Laia5.memories += [memory(s1,s2)]
  else:
    message = pop_end().data
    data.lis.append_new(message)
    st = ""
    print message
    for i in Laia5.response(to_ascii(message), 5):
      st += i.word + " "
    data.lis.append_new(st)
  return HttpResponse(template.render(context))

