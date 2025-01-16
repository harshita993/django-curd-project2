from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import student_registration
from .models import user
from django.contrib import messages
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
            new_stu= fm.save()
            messages.success(request,f"{new_stu.name} was successfully added")
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
        messages.success(request,f"{pi.name} was successfully deleted")
        return redirect('/')
    return render(request,'addandshow.html')
def update_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=student_registration(request.POST,instance=pi)
        if fm.is_valid():
           fm.save()
           messages.success(request,f"{pi.name} was successfully updated")
        fm=student_registration()
        return redirect('addshow')
         
    else:
        pi=user.objects.get(pk=id)
        fm=student_registration(instance=pi)
            
    return render(request,'update.html',{'form':fm})