from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import date
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField 
from django.db.models import Sum
#from .models import StudentClass

# Create your models here.


class StudentRegistration(models.Model):
    name=models.CharField(max_length=50)
    regNo=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    sex=models.CharField(max_length=10)
    phoneNo=models.CharField(max_length=20)
    dob=models.DateTimeField(blank=True,null=True)
    DateAdmitted=models.DateTimeField(blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.regNo} - {self.name}"
    
class Department(models.Model):
     name=models.CharField(max_length=100)
     
     def __str__(self):
         return(self.name)
     
class CollegeCourse(models.Model):
    courseTitle=models.CharField(max_length=100)
    courseCode=models.CharField(max_length=20)
    department=models.CharField(max_length=100)
    level=models.CharField(max_length=10)
    Courseunit=models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.courseCode} - {self.courseTitle}"
    


    
    
class Lecturer(models.Model):
    name=models.CharField(max_length=50)
    staffNo=models.CharField(max_length=20)
    email=models.EmailField()
    phoneNo=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    rank=models.CharField(max_length=50)
   
    dateEmployed=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.staffNo} - {self.name}"


class IctStaff(models.Model):
    staffname=models.CharField(max_length=50)
    staffNo=models.CharField(max_length=20)
    staffemail=models.EmailField()
    staffphoneNo=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    rank=models.CharField(max_length=50)
   
    dateEmployed=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.staffNo} - {self.staffname}"    




class UploadResult(models.Model):
    file_name=models.FileField(upload_to='media') 
    dateUploaded=models.DateField(auto_now_add=True)
    activated=models.BooleanField(default=False) 
    
    def __str__ (self):
        return f"{self.file_name}"
    
class UploadCourses(models.Model):
    file_name=models.FileField(upload_to='media') 
    dateUploaded=models.DateField(auto_now_add=True)
    activated=models.BooleanField(default=False) 
    
    def __str__ (self):
        return f"{self.file_name}"
    

    
    
    
class SecondSemisterResult(models.Model):  
    secregNo=models.CharField(max_length=50)
    seclevel=models.CharField(max_length=50)    
    seccourseCode=models.CharField(max_length=50)
    sectest=models.IntegerField()
    secexams=models.IntegerField()
    secscores=models.IntegerField()

   
    def __str__(self):
        return f"{self.secregNo} - {self.seccourseCode}"
    
    
    def secUnits(self): # grap the course units for college courses
        secunit=CollegeCourse.objects.get(courseCode=self.seccourseCode)
        seccorsunits=secunit.Courseunit         
        return seccorsunits
    
    def SecTitle(self): # grap the course title for college courses
        title=CollegeCourse.objects.get(courseCode=self.seccourseCode)
        coursetitle=title.courseTitle        
        return coursetitle
    
    def secstudentname(self): # grap the course units for college courses
        secnames=StudentRegistration.objects.get(regNo=self.secregNo)
        secmyname=secnames.name     
        return secmyname
    
    
    def sec_grade(self):
        if self.secscores >=70:
            grade="A"
        elif self.secscores >=60 and self.secscores <= 69:
            grade="B"
        elif self.secscores >=50 and self.secscores < 60:
            grade="C"
        elif self.secscores >=45 and self.secscores <50:
            grade="D"
        elif self.secscores >=40 and self.secscores <45:
            grade="E"
        else:
            grade="F"
        return grade
    
    
    
    
    
class FirstSemisterResult(models.Model): 
    regNo=models.CharField(max_length=50) 
    level=models.CharField(max_length=50)
    courseCode=models.CharField(max_length=50)
    test=models.IntegerField()
    exams=models.IntegerField()
    scores=models.IntegerField()
    
    
    def __str__(self):
        
        return f"{self.regNo} - {self.courseCode}"
    

    def Title(self): # grap the course title for college courses
        title=CollegeCourse.objects.get(courseCode=self.courseCode)
        coursetitle=title.courseTitle     
        return coursetitle
    
    
    def Units(self): # grap the course units for college courses
        unit=CollegeCourse.objects.get(courseCode=self.courseCode)
        corsunits=unit.Courseunit     
        return corsunits
    
    def studentname(self): # grap the course units for college courses
        names=StudentRegistration.objects.get(regNo=self.regNo)
        myname=names.name     
        return myname
    
    
       
    def total_courses(self):
        try:
            total = FirstSemisterResult.objects.filter(courseCode = self).count()
        except:
            total = 0
        return total
    
    
    def total_scores(self):
        try:
            Scores = FirstSemisterResult.objects.aggregate(Sum('scores'))
        except:
            Scores = 0
        return Scores
    
    def total_courseunint(self):
        try:
       
            courseunit = FirstSemisterResult.objects.aggregate(Sum('courseUnit'))
        except:
            courseunit=0
        return courseunit
    
    def total_gradepoint(self):
        try:
       
            Gradepoint = FirstSemisterResult.objects.aggregate(Sum('gradePoints'))
        except:
            Gradepoint=0
        return Gradepoint
    
    def grade(self):
        if self.scores >=70:
            grade="A"
        elif self.scores >=60 and self.scores <= 69:
            grade="B"
        elif self.scores >=50 and self.scores < 60:
            grade="C"
        elif self.scores >=45 and self.scores <50:
            grade="D"
        elif self.scores >=40 and self.scores <45:
            grade="E"
        else:
            grade="F"
        return grade 

    



