from django.shortcuts import render
from .forms import ChatForm
from django.http import HttpResponseRedirect,HttpResponse

def index(request):
    form=ChatForm()
    return render(request,'chatbd/index.html',{'form':form})

def envoi(request):
    message = request.GET.get('message', None)
    return HttpResponse(message)
