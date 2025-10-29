from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('admin_index/',views.admin_index,name='admin_index'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_userdata/',views.admin_userdata,name='admin_userdata'),
    path('admin_notesdata/',views.admin_notesdata,name='admin_notesdata'),
    path('Approve/<int:id>',views.Approve,name='Approve'),
    path('Reject/<int:id>',views.Reject,name='Reject'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),    
]
