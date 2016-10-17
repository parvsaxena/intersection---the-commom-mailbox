from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=14)
    rec_email=models.CharField(max_length=100)
    def __str__(self):
        return self.username
class User_id(models.Model):

    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    email_id=models.CharField(max_length=100)
    #password=models.CharField(max_length=20)
    #modified=models.DateField(auto_now=True)
    internaldate=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.email_id


class Mail(models.Model):
    user_n=models.ForeignKey(User_id,on_delete=models.CASCADE)
    sender=models.CharField(max_length=256,default="")
    msg_id=models.CharField(max_length=256)
    html_body=models.TextField(default="")
    plain_body=models.TextField(default="")
    date=models.CharField(max_length=30)
    snippet=models.CharField(max_length=500)
    subject=models.CharField(max_length=500)
    intern=models.CharField(max_length=100,default="")
