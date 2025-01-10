from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import student_registration
from .models import user
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=student_registration(request.POST) 
        if fm.is_valid():
            '''nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()'''
            fm.save()
        fm=student_registration()
        data=user.objects.all() 
    else:
        
        fm=student_registration()
        data=user.objects.all() 
    return render(request,'addandshow.html',{'form':fm,'data':data})
def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return redirect('/')
    return render(request,'addandshow.html')
