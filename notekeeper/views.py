from django.shortcuts import render,HttpResponseRedirect
from .forms import NotekeeperForm
from .models import Notekeeper
from django.contrib import messages


def home(request): 
    note=Notekeeper.objects.all()
    return render(request,"notekeeper/home.html",{'note':note})

def create(request):
    if request.method=='POST':
      fm=NotekeeperForm(request.POST)
      if fm.is_valid():
          fm.save()
          fm=NotekeeperForm()  
          messages.success(request,"Task has been added!!") 
          
    else:
        fm=NotekeeperForm()  
    return render(request,"notekeeper/create.html",{'form':fm})

def delete(request,id):
    pi=Notekeeper.objects.get(pk=id)
    pi.delete()
    messages.success(request,"Notes has been deleted!!")
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method=='POST':
        pi=Notekeeper.objects.get(pk=id)
        fm=NotekeeperForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Notes has been updated!!")
    else:
        pi=Notekeeper.objects.get(pk=id)
        fm=NotekeeperForm(instance=pi)
    return render(request,"notekeeper/update.html",{'form':fm})              

def sidebar(request): 
    note=Notekeeper.objects.all()
    return render(request,"notekeeper/sidebar.html",{'note':note})        
