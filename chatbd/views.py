from django.shortcuts import render
from .forms import ChatForm
from django.http import HttpResponseRedirect,HttpResponse

def index(request):
    message="vu"
    form=ChatForm()
    if request.is_ajax() and request.POST:
        message=request.POST.get('message','')
    return render(request,'chatbd/index.html',{'form':form,'message':message})


