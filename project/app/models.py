from django.db import models
from datetime import datetime 
from datetime import date,time


# Create your models here.


quali = [(1,'B.Tech'),(1,'M.Tech'),(1,'B.B.A'),(1,'M.B.A')]
class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=True,unique=True, db_index=True, blank=False,help_text="Enter a unique username")
    email = models.CharField(max_length=255, unique=True, blank=False, db_index=True)
    bio = models.CharField(max_length=50, null=True, blank=True,help_text="Enter a unique username")
    is_active = models.BooleanField(default=False,db_index=True)
    Qualification = models.CharField(max_length= 100,choices=quali,null=True,db_index=True)
    
class Appointment(models.Model): 
 name = models.CharField(max_length=100) 
 appointment_time = models.DateTimeField(help_text="Enter the appointment date and time.") 
 created_at = models.DateTimeField(auto_now_add=True) 
 updated_at = models.DateTimeField(auto_now=True) 
 default_time = models.DateTimeField(default=datetime.now)

class Shift(models.Model): 
 name = models.CharField(max_length=100) 
 start_time = models.TimeField(default=time(9, 0), help_text="Shift start time.") 
 end_time = models.TimeField(null=True, blank=True, verbose_name="Shift End Time") 
 created_at = models.TimeField(auto_now_add=True) 
 last_updated = models.TimeField(auto_now=True)

class Event(models.Model): 
 name = models.CharField(max_length=100) 
 event_date = models.DateField(help_text="Enter the event date.") 
 created_at = models.DateField(auto_now_add=True) 
 updated_at = models.DateField(auto_now=True) 
 deadline = models.DateField(default=date.today, verbose_name="Submission Deadline")