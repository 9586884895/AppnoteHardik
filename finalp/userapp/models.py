from django.db import models

# Create your models here.
class signup(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class note(models.Model):
    submitted_at=models.DateTimeField(auto_now_add=True)
    email=models.ForeignKey(signup,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    notesfile=models.FileField(upload_to='Notesdata')
    Desc=models.TextField()
    statuschoice=[
        ('pending','pending'),
        ('Approve','Approve'),
        ('Reject','Reject'),
    ]
    status=models.CharField(choices=statuschoice,max_length=50)
    update_at=models.DateTimeField(blank=True,null=True)

class cntc(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()    
    msg=models.TextField()






    