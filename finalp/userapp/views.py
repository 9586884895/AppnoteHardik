from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from finalp import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    ##email=signup.objects.get(email=user)
    return render(request,'index.html',{'user':user})
def Addnotes(request):
    user=request.session.get("user")
    email=signup.objects.get(email=user)
    if request.method=='POST':
        form=notesform(request.POST,request.FILES)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.status="pending"
            temp.email=email
            temp.save()
            print("Notes submitted sucessfully")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'Addnotes.html')

def contact(request):
    if request.method=='POST':
        form=cform(request.POST)
        if form.is_valid():
            form.save()
            print("Message sent sucessfully")
            return redirect('contact')
        else:
            print(form.errors)
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def profile(request):
    userid=request.session.get("userid")
    cuser=signup.objects.get(id=userid)
    if request.method=='POST':
        form=signupform(request.POST,instance=cuser)
        if form.is_valid():
            form.save()
            msg="updated sucessfully"
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'profile.html',{'userid':cuser})


def login(request):
    msg=""
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['password']
        user=signup.objects.filter(email=email,password=pas)
        userid=signup.objects.get(email=email)
        print(userid.id) 
        request.session["userid"]=userid.id
        if user: #true
            print("login sucessfully")
            msg="Login Sucessfully!"
            request.session["user"]=email
            return redirect('/')
        else:
            print("Error! login failed..")
            msg="Error! login failed.."
    return render(request,'login.html',{'msg':msg})
otp=0
def usersignup(request):
    msg=""
    global otp
    if request.method=="POST":
        form=signupform(request.POST)
        em=request.POST["email"]
        email=signup.objects.filter(email=em).exists()
        if email:
            print("Email id already Exists")
            msg="Email address already Exists"
        else:    
            if form.is_valid():
                form.save()
                msg="Signup sucessfully!"

                # otp sending code...
                otp=random.randint(111111,999999)
                sub="your one time password"
                message=f"Dear User!\n\nThanks for register our service!\n\For account verification, Your one time password is {otp}.\n\nThanks & Regards\nAppNotes Teams\n+91 9586884895 | hardik.isavani@gmail.com"
                from_email=settings.EMAIL_HOST_USER
                to_email=[request.POST["email"]]
                send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
                print("email send sucessfully")
                return redirect('otpverify')
            else:
                print(form.errors)
                msg="error!Something Went wrong..."
    return render(request,'signup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('login')

def otpverify(request):
    global otp
    print(otp)
    if request.method=='POST':
        myotp=request.POST['otp']
        if otp==int(myotp):
            print("Signup sucessfully")
            return redirect("/")
        else:
            print("Error ! Please try again")            
    return render(request,'otpverify.html')

