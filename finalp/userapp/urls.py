from django.contrib import admin
from django.urls import path,include
from userapp import views


urlpatterns = [
    path('',views.index),    
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('signup/', views.usersignup, name='signup'),  # <--- add this line
    path('userlogout/', views.userlogout, name='userlogout'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('Addnotes/',views.Addnotes,name='Addnotes'),

]
