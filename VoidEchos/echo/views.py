from django.shortcuts import render
from django.http import HttpResponse
import data

def pop_end():
  ret = data.lis
  data.lis = data.lis.nxt
  if data.lis == 0:
    data.lis = ret
  return ret

# Create your views here.

def index(request):
  return HttpResponse(pop_end().data)
