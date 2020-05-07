from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactus(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

class newentry(models.Model):
    sno = models.AutoField(primary_key=True)
    entryname = models.CharField(max_length=150)
    url = models.CharField(max_length=280)
    username = models.CharField(max_length=280, default='username')
    password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.entryname