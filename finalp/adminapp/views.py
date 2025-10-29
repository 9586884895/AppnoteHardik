from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from datetime import datetime
from django.core.mail import send_mail
from finalp import settings
from django.contrib.auth import logout

# Create your views here.
def admin_index(request):  # login page
    if request.method=='POST':
        if request.POST["username"]=="admin" and request.POST["password"]=="Admin@123":
            print("login sucessfully")
            return redirect("admin_dashboard")
        else:
            print("errors, login failed")
    return render(request,'admin_index.html')

def admin_dashboard(request):
    userdata=signup.objects.all()
    u=len(userdata) # length find return int value
    notesdata=note.objects.all()
    n=len(notesdata) # length find return int value
    return render(request,'admin_dashboard.html',{'userdata':u,'notesdata':n,'udata':userdata})

def admin_userdata(request):
    userdata=signup.objects.all()
    return render(request,'admin_userdata.html',{'userdata':userdata})

def admin_notesdata(request):
    notesdata=note.objects.all()      
    return render(request,'admin_notesdata.html',{'notesdata':notesdata})

def Approve(request,id):
    notes=get_object_or_404(note,id=id)
    notes.status="Approved"
    notes.update_at=datetime.now()
    notes.save()
    print("Notes approved Sucessfully")
    sub="Notes Status updates"
    message=f"Dear {notes.email.fullname} \n\nCongratulations!!,\n\nYour notes Approved By admin\n\nThanks & Regards\nAppNotes Teams\n+91 9586884895 | hardik.isavani@gmail.com"
    from_email=settings.EMAIL_HOST_USER
    to_email=[notes.email.email]
    send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
    print("Updates send to User Sucessfully")
    return redirect("admin_notesdata")
    

def Reject(request,id):
    notes=get_object_or_404(note,id=id)
    notes.status="Rejected"
    notes.update_at=datetime.now()
    notes.save()
    print("Notes Reject by Admin")
    sub="Notes Status updates"
    message=f"Dear {notes.email.fullname} \n\n SORRY from our side!!,\n\nYour notes Reject By admin cause of Community Guidelines\n\nThanks & Regards\nAppNotes Teams\n+91 9586884895 | hardik.isavani@gmail.com"
    from_email=settings.EMAIL_HOST_USER
    to_email=[notes.email.email]
    send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
    print("Updates send to User Sucessfully")
    return redirect("admin_notesdata")

def adminlogout(request):
    logout(request)
    return redirect("admin_index")

