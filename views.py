from django.shortcuts import render,redirect,get_object_or_404
from .import views
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.http import HttpResponse
from django.contrib import messages
from .models import*
from .forms import* 
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
#from  xhtml2pdf.pisa import  pisa

from django.core import serializers
import json
from django.template.loader import get_template
from io import BytesIO
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView, View
from django.http import Http404
from django.db.models import Q
import csv
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
#from django.db.models.JSONField 

# Create your views here.



# new ends
def ResultHome(request):
    depart=Department.objects.all()
    college=CollegeCourse.objects.all()
    
    return render(request,'Result-Home.html',{'depart':depart,'college':college})


@login_required
def Change_password(request):
    change_user_password=PasswordChangeForm(request.user)
    if request.method=='POST':        
        change_user_password=PasswordChangeForm(request.user, request.POST)
        if change_user_password.is_valid():
            user=change_user_password.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password has been changed')
            return redirect('changepassword')
        else:
            messages.error(request,'Correct the error below')
    return render (request,'changepassword.html',{'change_user_password':change_user_password})



@login_required
def ICTStaff(request):
    Ictform=UploadResultModelForm() #departmental registration
    if request.method == 'POST':
        Ictform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if Ictform.is_valid:
            Ictform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        ict=IctStaff.objects.create(
                            staffname=row[1].upper(),
                            staffNo=row[2].upper(),
                            staffemail=row[3],
                            staffphoneNo=row[4],
                            department=row[5].upper(),
                            rank=row[6].upper(),  
                           # dateEmployed=row[7],                         
                        ) 
                        ict.save() 
                obj.activated=True
                obj.save()    
                messages.info(request," Registered Successfully")
                return redirect('staffpage')   
    return render(request,'Ictstaff.html', {'Ictform':Ictform,})


@login_required
def StaffPage(request):
    departmentform=UploadResultModelForm() #departmental registration
    if request.method == 'POST':
        departmentform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if departmentform.is_valid:
            departmentform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        dept=Department.objects.create(
                            name=row[1].upper(),                            
                        ) 
                        dept.save() 
                obj.activated=True
                obj.save()    
                messages.info(request,"Departments Registered Successfully")
                return redirect('staffpage')            
                
    return render(request, 'staff.html',{'departmentform':departmentform,})

@login_required
def CourseResgistration(request):
    courseform=UploadResultModelForm() #course registration
    if request.method == 'POST':
        courseform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if courseform.is_valid:
            courseform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        cors=CollegeCourse.objects.create(
                            courseTitle=row[1].upper(),
                            courseCode=row[2].upper(),
                            department=row[3].upper(),
                            level=row[4].upper(),
                            Courseunit=row[5],                           
                        ) 
                        cors.save() 
                obj.activated=True
                obj.save()    
                messages.info(request,"Courses Registered Successfully") 
    return render(request, 'courses.html',{'courseform':courseform,})

@login_required
def LecturerRegistration(request):
    lecturerform=UploadResultModelForm() #course registration
    if request.method == 'POST':
        lecturerform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if lecturerform.is_valid:
            lecturerform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        lect=Lecturer.objects.create(
                            name=row[1].upper(),
                            staffNo=row[2].upper(),
                            email=row[3],
                            phoneNo=row[4],
                            department=row[5].upper(),
                            rank=row[6].upper(),
                            #dateEmployed=row[7],                           
                        ) 
                        lect.save() 
                obj.activated=True
                obj.save()    
                messages.info(request,"Lecturers Registered Successfully") 
    return render (request,'lecturer.html',{'lecturerform':lecturerform,})

@login_required
def StudentsRegistration(request):
    studentform=UploadResultModelForm() #course registration
    if request.method == 'POST':
        studentform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if studentform.is_valid:
            studentform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        student=StudentRegistration.objects.create(
                            name=row[1].upper(),
                            regNo=row[2].upper(),
                            department=row[3].upper(),
                            sex=row[4].upper(),
                            phoneNo=row[5],
                            #dob=row[6], 
                            #DateAdmitted=row[7],                          
                        ) 
                        student.save() 
                obj.activated=True
                obj.save()    
                messages.info(request,"Students Registered Successfully")
    return render(request,'student.html',{'studentform':studentform,})

def ResultSignin(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist!")
                return redirect('resultHome')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist!")
                return redirect('resultHome')
            
            else:
                user=User.objects.create_user(username=username,password=password,email=email,)
                user.save();
                messages.info(request,"account created successfully")
                return redirect('resultlogin')
        else:
            
            messages.info(request,"Wrong credentials")
            return redirect('resultHome')
        
                 
    return render(request,'Result-signin.html')

def Resultlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            if Lecturer.objects.filter(staffNo=request.user.username).exists(): #check if is a staff or student
               
                
                return redirect('uploadresult')
                #messages.info(request,"login successfully")
            elif StudentRegistration.objects.filter(regNo=request.user.username).exists():
                return redirect('Computeresult')
                #messages.info(request,"login successfully")
            elif IctStaff.objects.filter(staffNo=request.user.username).exists():
                #messages.info(request,"login successfully")
                return redirect('staffpage')    
                
            else:
                messages.info(request," You Are NOT Registered Contact ICT")
                return redirect('/')    
                
           
        else:
            messages.info(request,"Invalid account!, username or password is Not correct")
            return redirect('resultlogin')
    else:
            
        return render (request, 'ResultManagement.html')
    
    
def Resultlogout(request):
    auth.logout(request)
    return redirect('/')
    
    # Nce 1 first semister result upload
@login_required
def FirstSemister(request):
   
    uploadform=UploadResultModelForm()
    if request.method == 'POST':
        uploadform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if uploadform.is_valid:
            uploadform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        form=FirstSemisterResult.objects.create(
                            regNo=row[1].upper(),
                            level=row[2].upper(),
                            courseCode=row[3].upper(),
                            test=int(row[4]),
                            exams=int(row[5]),
                            scores=int(row[6]),                           
                        ) 
                        form.save()                        
                obj.activated=True
                obj.save()
                messages.info(request,"Result Uploaded Successfully")                             
    return render(request,'uploadResult.html',{'uploadform':uploadform,})
        
    


 # Nce1 second semister result upload 
def Secondsemister (request):
    uploadsecform=UploadResultModelForm()
    if request.method == 'POST':
        uploadsecform=UploadResultModelForm(request.POST or None, request.FILES or None)
        if uploadsecform.is_valid:
            uploadsecform.save()
            obj=UploadResult.objects.get(activated=False)
            with open (obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):
                    if i ==0:
                        pass
                    else:
                        secform=SecondSemisterResult.objects.create(
                            secregNo=row[1].upper(),
                            seclevel=row[2].upper(),
                            seccourseCode=row[3].upper(),
                            sectest=int(row[4]), 
                            secexams=int(row[5]),
                            secscores=int(row[6]),                           
                        ) 
                        secform.save() 
                obj.activated=True
                obj.save()    
                messages.info(request,"Result Uploaded Successfully") 
    return render(request,'secResult.html',{'uploadsecform':uploadsecform})



@login_required
def ComputeResult(request):
    
    fsrt=FirstSemisterResult.objects.filter(regNo=request.user).filter(Q(level='NCE 1')) # filtering for user and level one first semister
    secrt=SecondSemisterResult.objects.filter(secregNo=request.user).filter(Q(seclevel='NCE 1')) # filtering for user and level one second semister
    fsrtNceTwo=FirstSemisterResult.objects.filter(regNo=request.user).filter(Q(level='NCE 2')) # filtering for user and level two first semister
    secrtNceTwo=SecondSemisterResult.objects.filter(secregNo=request.user).filter(Q(seclevel='NCE 2'))#filtering for user and level two scond semister
    fsrtNceThree=FirstSemisterResult.objects.filter(regNo=request.user).filter(Q(level='NCE 3')) #filtering for user and level three first semister
    secrtNceThree=SecondSemisterResult.objects.filter(secregNo=request.user).filter(Q(seclevel='NCE 3'))#filtering for user and level three second semister
    
    
    display_name=''
    sum_gradepoint=0
    sec_sum_gradepoint=0
    total_courseunit=0
    sec_total_courseunit=0
    studentno=''
    studentlevel=''
    Gradepoint=0
    Gpa=0
    studentlevel2=''
    studentnoNce2=''
    studentlevelNce2=''
    NcetfGradepoint=0
    Ncetfsum_gradepoint=0
    Ncetftotal_courseunit=0
    NcetfGpa=0
    Ncetsecstudentno2=''
    Ncetsecstudentlevel2=''
    Ncetsecsec_Gradepoint=0
    Ncetsec_sum_gradepoint=0
    Ncetsec_total_courseunit=0
    Ncetcgpa =0
    Ncetsec_gpa=0
    sec_gpa=0
    cgpa=0
    studentno2=''
    Ncetrfstudentno=''
    Ncetrfstudentlevel=''
    NcetrfGradepoint=0
    Ncetrfsum_gradepoint=0
    Ncetrftotal_courseunit=0
    NcetrfGpa =0
    Ncetrsecstudentno2=''
    Ncetrsecstudentlevel2=''
    Ncetrsec_Gradepoint=0
    Ncetrsec_sum_gradepoint=0
    Ncetrsec_total_courseunit=0
    Ncetrsec_gpa=0
    Ncetrcgpa=0
    FinalCgpa=0
    sec_gpa =0
    TotalUnits=0
    display_name2=''
    studentnameNce2=''
    sec_studentnameNce2=''
    Ncetrfstudentname=''
    Ncetrsecstudentname=''
    
    
    
    
    
    for  result in fsrt:#fsrt
        display_name=result.studentname()
        studentno=result.regNo
        studentlevel=result.level  
        if result.scores >= 70 and int(result.Units()) == 3:
            Gradepoint=15
        
        elif result.scores >= 60 and int(result.Units()) == 3:
            Gradepoint=12
        elif result.scores >= 50 and int(result.Units()) == 3:
            Gradepoint=9
        elif result.scores >= 45 and int(result.Units()) == 3:
            Gradepoint=6
        elif result.scores >= 40 and int(result.Units()) == 3:
            Gradepoint=3
        elif result.scores < 40 and int(result.Units()) == 3:
            Gradepoint=0
            # check for three course units
        elif result.scores >= 70 and  int(result.Units()) == 2:
            Gradepoint=10
        
        elif result.scores >= 60 and int(result.Units()) == 2:
            Gradepoint=8
        elif result.scores >= 50 and  int(result.Units()) == 2:
            Gradepoint=6
        elif result.scores >= 45 and int(result.Units()) == 2:
            Gradepoint=4
        elif result.scores >= 40 and int(result.Units()) ==2:
            Gradepoint=2
        elif result.scores < 40 and int(result.Units()) == 2:
            Gradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 4:
            Gradepoint=20
        
        elif result.scores >= 60 and int(result.Units()) == 4:
            Gradepoint=16
        elif result.scores >= 50 and  int(result.Units()) == 4:
            Gradepoint=12
        elif result.scores >= 45 and int(result.Units())  == 4:
            Gradepoint=8
        elif result.scores >= 40 and int(result.Units()) == 4:
            Gradepoint=4
        elif result.scores < 40 and int(result.Units()) == 4:
            Gradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 1:
            Gradepoint=5
        
        elif result.scores >= 60 and int(result.Units()) == 1:
            Gradepoint=4
        elif result.scores >= 50 and int(result.Units()) == 1:
            Gradepoint=3
        elif result.scores >= 45 and int(result.Units()) == 1:
            Gradepoint=2
        elif result.scores >= 40 and int(result.Units()) == 1:
            Gradepoint=1
        elif result.scores < 40 and int(result.Units()) == 1:
            Gradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 5:
            Gradepoint=25
        
        elif result.scores >= 60 and int(result.Units()) == 5:
            Gradepoint=20
        elif result.scores >= 50 and  int(result.Units()) == 5:
            Gradepoint=15
        elif result.scores >= 45 and int(result.Units()) == 5:
            Gradepoint=10
        elif result.scores >= 40 and int(result.Units()) == 5:
            Gradepoint=5
        elif result.scores < 40 and int(result.Units()) == 5:
            Gradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 6:
            Gradepoint=30
        
        elif result.scores >= 60 and int(result.Units()) == 6:
            Gradepoint=24
        elif result.scores >= 50 and int(result.Units()) == 6:
            Gradepoint=18
        elif result.scores >= 45 and int(result.Units()) == 6:
            Gradepoint=12
        elif result.scores >= 40 and int(result.Units()) == 6:
            Gradepoint=6
        elif result.scores < 40 and int(result.Units()) == 6:
            Gradepoint=0
        
        elif result.scores >= 70 and int(result.Units()) == 7:
            Gradepoint=35
        
        elif result.scores >= 60 and int(result.Units()) == 7:
            Gradepoint=28
        elif result.scores >= 50 and int(result.Units()) == 7:
            Gradepoint=21
        elif result.scores >= 45 and int(result.Units()) == 7:
            Gradepoint=14
        elif result.scores >= 40 and int(result.Units()) == 7:
            Gradepoint=7
        elif result.scores < 40 and int(result.Units()) == 7:
            Gradepoint=0
        else:
            Gradepoint=0
        sum_gradepoint += Gradepoint
        total_courseunit += int(result.Units())  # take total of courseunits
        if sum_gradepoint !=0:
            Gpa = sum_gradepoint / total_courseunit
            
        else:
            Gpa=0
       
        
            
        
    
    #check for second semester nce1 results
    for secondresult in secrt:
        display_name2=secondresult.secstudentname()
        studentno2=secondresult.secregNo
        studentlevel2=secondresult.seclevel
        #sec_total_gradepoint += secondresult.gradePoints
        if secondresult.secscores >= 70 and int(secondresult.secUnits()) == 3:
            sec_Gradepoint=15
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 3:
            sec_Gradepoint=12
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 3:
            sec_Gradepoint=9
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 3:
            sec_Gradepoint=6
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 3:
            sec_Gradepoint=3
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 3:
            sec_Gradepoint=0
            # check for three course units
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=10
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=8
        elif secondresult.secscores >= 50 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=6
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=4
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=2
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 2:
            sec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 4:
            sec_Gradepoint=20
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 4:
            sec_Gradepoint=16
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 4:
            sec_Gradepoint=12
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 4:
            sec_Gradepoint=8
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 4:
            sec_Gradepoint=4
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 4:
            sec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 1:
            sec_Gradepoint=5
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 1:
            sec_Gradepoint=4
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 1:
            sec_Gradepoint=3
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 1:
            sec_Gradepoint=2
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 1:
            sec_Gradepoint=1
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 1:
            sec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 5:
            sec_Gradepoint=25
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) ==5 :
            sec_Gradepoint=20
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 5:
            sec_Gradepoint=15
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 5:
            sec_Gradepoint=10
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 5:
            sec_Gradepoint=5
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 5:
            sec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 6:
            sec_Gradepoint=30
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 6:
            sec_Gradepoint=24
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 6:
            sec_Gradepoint=18
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 6:
            sec_Gradepoint=12
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 6:
            sec_Gradepoint=6
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 6:
            sec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 7:
            sec_Gradepoint=35
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 7:
            sec_Gradepoint=28
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 7:
            sec_Gradepoint=21
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 7:
            sec_Gradepoint=14
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 7:
            sec_Gradepoint=7
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 7:
            sec_Gradepoint=0
        else:
            sec_Gradepoint=0
            
        sec_sum_gradepoint += sec_Gradepoint
        sec_total_courseunit += int(secondresult.secUnits())
        if sec_sum_gradepoint !=0:
            sec_gpa =  sec_sum_gradepoint / sec_total_courseunit
        else:
            sec_gpa=0
            
        cgpa=(sum_gradepoint + sec_sum_gradepoint ) / ( sec_total_courseunit + total_courseunit)           #(Gpa + sec_gpa ) / 2
       
            
    # First semister NCE 2 computations
    for  result in fsrtNceTwo:
        
        studentnameNce2=result.studentname()
        studentnoNce2=result.regNo
        studentlevelNce2=result.level  
        if result.scores >= 70 and int(result.Units()) == 3:
            NcetfGradepoint=15
        
        elif result.scores >= 60 and int(result.Units()) == 3:
            NcetfGradepoint=12
        elif result.scores >= 50 and  int(result.Units()) == 3:
            NcetfGradepoint=9
        elif result.scores >= 45 and int(result.Units()) == 3:
            NcetfGradepoint=6
        elif result.scores >= 40 and int(result.Units()) == 3:
            NcetfGradepoint=3
        elif result.scores < 40 and int(result.Units()) == 3:
            NcetfGradepoint=0
            # check for three course units
        elif result.scores >= 70 and int(result.Units()) == 2:
            NcetfGradepoint=10
        
        elif result.scores >= 60 and int(result.Units()) == 2:
            NcetfGradepoint=8
        elif result.scores >= 50 and  int(result.Units()) == 2:
            NcetfGradepoint=6
        elif result.scores >= 45 and int(result.Units()) == 2:
            NcetfGradepoint=4
        elif result.scores >= 40 and int(result.Units()) == 2:
            NcetfGradepoint=2
        elif result.scores < 40 and int(result.Units()) == 2:
            NcetfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 4:
            NcetfGradepoint=20
        
        elif result.scores >= 60 and int(result.Units()) == 4:
            NcetfGradepoint=16
        elif result.scores >= 50 and  int(result.Units()) == 4:
            NcetfGradepoint=12
        elif result.scores >= 45 and int(result.Units()) == 4:
            NcetfGradepoint=8
        elif result.scores >= 40 and int(result.Units()) == 4:
            NcetfGradepoint=4
        elif result.scores < 40 and int(result.Units()) == 4:
            NcetfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 1:
            NcetfGradepoint=5
        
        elif result.scores >= 60 and int(result.Units()) == 1:
            NcetfGradepoint=4
        elif result.scores >= 50 and  int(result.Units()) == 1:
            NcetfGradepoint=3
        elif result.scores >= 45 and int(result.Units()) == 1:
            NcetfGradepoint=2
        elif result.scores >= 40 and int(result.Units()) == 1:
            NcetfGradepoint=1
        elif result.scores < 40 and int(result.Units()) == 1:
            NcetfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 5:
            NcetfGradepoint=25
        
        elif result.scores >= 60 and int(result.Units()) == 5:
            NcetfGradepoint=20
        elif result.scores >= 50 and  int(result.Units()) == 5:
            NcetfGradepoint=15
        elif result.scores >= 45 and int(result.Units()) == 5:
            NcetfGradepoint=10
        elif result.scores >= 40 and int(result.Units()) == 5:
            NcetfGradepoint=5
        elif result.scores < 40 and int(result.Units()) == 5:
            NcetfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 6:
            NcetfGradepoint=30
        
        elif result.scores >= 60 and int(result.Units()) == 6:
            NcetfGradepoint=24
        elif result.scores >= 50 and  int(result.Units()) == 6:
            NcetfGradepoint=18
        elif result.scores >= 45 and int(result.Units()) == 6:
            NcetfGradepoint=12
        elif result.scores >= 40 and int(result.Units()) == 6:
            NcetfGradepoint=6
        elif result.scores < 40 and int(result.Units()) == 6:
            NcetfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 7:
            NcetfGradepoint=35
        
        elif result.scores >= 60 and int(result.Units()) == 7:
            NcetfGradepoint=28
        elif result.scores >= 50 and  int(result.Units()) == 7:
            NcetfGradepoint=21
        elif result.scores >= 45 and int(result.Units()) == 7:
            NcetfGradepoint=14
        elif result.scores >= 40 and int(result.Units()) == 7:
            NcetfGradepoint=7
        elif result.scores < 40 and int(result.Units()) == 7:
            NcetfGradepoint=0
        else:
            NcetfGradepoint=0
        Ncetfsum_gradepoint += NcetfGradepoint # take sum of gradepoints
        Ncetftotal_courseunit  +=int(result.Units())  # take total of courseunits
        if Ncetfsum_gradepoint !=0:
            NcetfGpa = Ncetfsum_gradepoint / Ncetftotal_courseunit # compute gp
            
        else:
            NcetfGpa=0
       
        
        # second semister NCE2 
    
    
    #second semister NCE2
    
    for secondresult in secrtNceTwo:
        sec_studentnameNce2=secondresult.secstudentname()
        Ncetsecstudentno2=secondresult.secregNo
        Ncetsecstudentlevel2=secondresult.seclevel
        
        if secondresult.secscores >= 70 and int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=15
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=12
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=9
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=6
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=3
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 3:
            Ncetsecsec_Gradepoint=0
            # check for three course units
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=10
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=8
        elif secondresult.secscores >= 50 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=6
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=4
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=2
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 2:
            Ncetsecsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepoint=20
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepoint=16
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepoint=12
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepointt=8
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepoint=4
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 4:
            Ncetsecsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 1:
            Ncetsecsec_Gradepoint=5
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 1:
            Ncetsecsec_Gradepoint=4
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 1:
            Ncetsecsec_Gradepoint=3
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 1:
            Ncetsecsec_Gradepoint=2
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 1:
           Ncetsecsec_Gradepoint=1
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 1:
            Ncetsecsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=25
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=20
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=15
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=10
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=5
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 5:
            Ncetsecsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=30
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=24
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=18
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=12
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=6
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 6:
            Ncetsecsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=35
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=28
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=21
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=14
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=7
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 7:
            Ncetsecsec_Gradepoint=0
        else:
            Ncetsecsec_Gradepoint=0
        Ncetsec_sum_gradepoint += Ncetsecsec_Gradepoint
        Ncetsec_total_courseunit += int(secondresult.secUnits()) 
        if Ncetsec_sum_gradepoint !=0:
            Ncetsec_gpa =  Ncetsec_sum_gradepoint / Ncetsec_total_courseunit
        else:
            Ncetsec_gpa=0
            
        Ncetcgpa = (Ncetfsum_gradepoint + Ncetsec_sum_gradepoint ) / ( Ncetsec_total_courseunit +  Ncetftotal_courseunit) #cgpa for nce2
        
                    
    #first semister result NCE3
    for  result in fsrtNceThree:
        Ncetrfstudentname=result.studentname()
        Ncetrfstudentno=result.regNo
        Ncetrfstudentlevel=result.level  
        if result.scores >= 70 and int(result.Units()) == 3:
            NcetrfGradepoint=15
        
        elif result.scores >= 60 and int(result.Units()) == 3:
            NcetrfGradepoint=12
        elif result.scores >= 50 and  int(result.Units()) == 3:
            NcetrfGradepoint=9
        elif result.scores >= 45 and int(result.Units()) == 3:
            NcetrfGradepoint=6
        elif result.scores >= 40 and int(result.Units()) == 3:
            NcetrfGradepoint=3
        elif result.scores < 40 and int(result.Units()) == 3:
            NcetrfGradepoint=0
            # check for three course units
        elif result.scores >= 70 and int(result.Units()) == 2:
            NcetrfGradepoint=10
        
        elif result.scores >= 60 and int(result.Units()) == 2:
            NcetrfGradepoint=8
        elif result.scores >= 50 and  int(result.Units()) == 2:
           NcetrfGradepoint=6
        elif result.scores >= 45 and int(result.Units()) == 2:
           NcetrfGradepoint=4
        elif result.scores >= 40 and int(result.Units()) == 2:
            NcetrfGradepoint=2
        elif result.scores < 40 and int(result.Units()) == 2:
           NcetrfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 4:
            NcetrfGradepoint=20
        
        elif result.scores >= 60 and int(result.Units()) == 4:
            NcetrfGradepoint=16
        elif result.scores >= 50 and  int(result.Units()) == 4:
            NcetrfGradepoint=12
        elif result.scores >= 45 and int(result.Units()) == 4:
            NcetrfGradepoint=8
        elif result.scores >= 40 and int(result.Units()) == 4:
            NcetrfGradepoint=4
        elif result.scores < 40 and int(result.Units()) == 4:
            NcetrfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 1:
            NcetrfGradepoint=5
        
        elif result.scores >= 60 and int(result.Units()) == 1:
            NcetrfGradepoint=4
        elif result.scores >= 50 and  int(result.Units()) == 1:
            NcetrfGradepoint=3
        elif result.scores >= 45 and int(result.Units()) == 1:
            NcetrfGradepoint=2
        elif result.scores >= 40 and int(result.Units()) == 1:
            NcetrfGradepoint=1
        elif result.scores < 40 and int(result.Units()) == 1:
            NcetrfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 5:
            NcetrfGradepoint=25
        
        elif result.scores >= 60 and int(result.Units()) == 5:
           NcetrfGradepoint=20
        elif result.scores >= 50 and  int(result.Units()) == 5:
            NcetrfGradepoint=15
        elif result.scores >= 45 and int(result.Units()) == 5:
            NcetrfGradepoint=10
        elif result.scores >= 40 and int(result.Units()) == 5:
            NcetrfGradepoint=5
        elif result.scores < 40 and int(result.Units()) == 5:
            NcetrfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 6:
            NcetrfGradepoint=30
        
        elif result.scores >= 60 and int(result.Units()) == 6:
            NcetrfGradepoint=24
        elif result.scores >= 50 and  int(result.Units()) == 6:
            NcetrfGradepoint=18
        elif result.scores >= 45 and int(result.Units()) == 6:
            NcetrfGradepoint=12
        elif result.scores >= 40 and int(result.Units()) == 6:
            NcetrfGradepoint=6
        elif result.scores < 40 and int(result.Units()) == 6:
            NcetrfGradepoint=0
        elif result.scores >= 70 and int(result.Units()) == 7:
            NcetrfGradepoint=35
        
        elif result.scores >= 60 and int(result.Units()) == 7:
            NcetrfGradepoint=28
        elif result.scores >= 50 and  int(result.Units()) == 7:
            NcetrfGradepoint=21
        elif result.scores >= 45 and int(result.Units()) == 7:
            NcetrfGradepoint=14
        elif result.scores >= 40 and int(result.Units()) == 7:
            NcetrfGradepoint=7
        elif result.scores < 40 and int(result.Units()) == 7:
            NcetrfGradepoint=0
        else:
            NcetrfGradepoint=0
        Ncetrfsum_gradepoint += NcetrfGradepoint
        Ncetrftotal_courseunit  +=int(result.Units())  # take total of courseunits
        if Ncetrfsum_gradepoint !=0:
            NcetrfGpa = Ncetrfsum_gradepoint / Ncetrftotal_courseunit
            
        else:
            NcetrfGpa=0
    
    # second semister result NCE3
    for secondresult in secrtNceThree:
        Ncetrsecstudentname=secondresult.secstudentname()
        Ncetrsecstudentno2=secondresult.secregNo
        Ncetrsecstudentlevel2=secondresult.seclevel
        
        if secondresult.secscores >= 70 and int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=15
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=12
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=9
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=6
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=3
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 3:
            Ncetrsec_Gradepoint=0
            # check for three course units
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=10
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=8
        elif secondresult.secscores >= 50 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=6
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=4
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=2
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 2:
            Ncetrsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=20
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=16
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=12
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=8
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=4
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 4:
            Ncetrsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=5
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=4
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=3
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=2
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=1
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 1:
            Ncetrsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=25
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=20
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=15
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=10
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=5
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 5:
            Ncetrsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=30
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=24
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=18
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=12
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=6
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 6:
            Ncetrsec_Gradepoint=0
        elif secondresult.secscores >= 70 and int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=35
        
        elif secondresult.secscores >= 60 and int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=28
        elif secondresult.secscores >= 50 and  int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=21
        elif secondresult.secscores >= 45 and int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=14
        elif secondresult.secscores >= 40 and int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=7
        elif secondresult.secscores < 40 and int(secondresult.secUnits()) == 7:
            Ncetrsec_Gradepoint=0
        else:
            Ncetrsec_Gradepoint=0
        Ncetrsec_sum_gradepoint += Ncetrsec_Gradepoint
        Ncetrsec_total_courseunit += int(secondresult.secUnits())
        if Ncetrsec_sum_gradepoint !=0:
            Ncetrsec_gpa =  Ncetrsec_sum_gradepoint / Ncetrsec_total_courseunit
        else:
            Ncetrsec_gpa=0
            
        Ncetrcgpa = (Ncetrfsum_gradepoint + Ncetrsec_sum_gradepoint ) / ( Ncetrsec_total_courseunit +  Ncetrftotal_courseunit) #cgpa for nce2
        #computer final cgpa
     
    FinalCgpa = (sum_gradepoint + sec_sum_gradepoint +  Ncetfsum_gradepoint + Ncetsec_sum_gradepoint + Ncetrfsum_gradepoint + Ncetrsec_sum_gradepoint) / (total_courseunit + sec_total_courseunit + Ncetftotal_courseunit + Ncetsec_total_courseunit + Ncetrftotal_courseunit + Ncetrsec_total_courseunit)
    TotalUnits=total_courseunit + sec_total_courseunit + Ncetftotal_courseunit + Ncetsec_total_courseunit + Ncetrftotal_courseunit + Ncetrsec_total_courseunit
    context={
            'Ncetrsecstudentname':Ncetrsecstudentname,
            'Ncetrfstudentname':Ncetrfstudentname,
            'sec_studentnameNce2':sec_studentnameNce2,
            'studentnameNce2':studentnameNce2,
            'display_name2':display_name2,
            'display_name':display_name,
            'TotalUnits':TotalUnits,
            'sec_total_courseunit':sec_total_courseunit,
            'sec_sum_gradepoint':sec_sum_gradepoint,
            'Ncetcgpa':Ncetcgpa,
            'FinalCgpa':FinalCgpa,
            'Ncetrcgpa':Ncetrcgpa,
            'Ncetrsec_gpa':Ncetrsec_gpa,
            'Ncetrsec_total_courseunit':Ncetrsec_total_courseunit,
            'Ncetrsec_sum_gradepoint':Ncetrsec_sum_gradepoint,
            'Ncetrsec_Gradepoint':Ncetrsec_Gradepoint,
            'Ncetrsecstudentlevel2':Ncetrsecstudentlevel2,
            'Ncetrsecstudentno2':Ncetrsecstudentno2,
            'NcetrfGpa':NcetrfGpa ,
            'Ncetrftotal_courseunit':Ncetrftotal_courseunit,
            'Ncetrfsum_gradepoint':Ncetrfsum_gradepoint,
            'NcetrfGradepoint':NcetrfGradepoint,
            'Ncetrfstudentlevel':Ncetrfstudentlevel,
            'Ncetrfstudentno':Ncetrfstudentno,          
            'Ncetcgpa':Ncetcgpa,
            'Ncetsec_gpa':Ncetsec_gpa,
            'Ncetsec_total_courseunit':Ncetsec_total_courseunit,
            'Ncetsec_sum_gradepoint':Ncetsec_sum_gradepoint,
            'Ncetsecsec_Gradepoint':Ncetsecsec_Gradepoint,
            'Ncetsecstudentlevel2':Ncetsecstudentlevel2,
            'Ncetsecstudentno2':Ncetsecstudentno2,
            'NcetfGpa':NcetfGpa,
            'Ncetfsum_gradepoint': Ncetfsum_gradepoint,
            'Ncetftotal_courseunit': Ncetftotal_courseunit,
            'studentnoNce2':studentnoNce2,
            'studentlevelNce2':studentlevelNce2,
             'studentlevel2':studentlevel2,
             'studentno2':studentno2,
             'studentno':studentno,
             'studentlevel':studentlevel,
             'Gradepoint':Gradepoint,
             'total_courseunit':total_courseunit,
             'sec_total_courseunit':sec_total_courseunit,
             'sec_sum_gradepoint':sec_sum_gradepoint,
             'sum_gradepoint':sum_gradepoint,
             'studentno2':studentno2,
             'fsrt':fsrt,
             'secrt':secrt,
             'Gpa':Gpa,
             'sec_gpa':sec_gpa,
             'cgpa':cgpa,
             'fsrtNceTwo':fsrtNceTwo,
             'secrtNceTwo':secrtNceTwo,
             'fsrtNceThree':fsrtNceThree,
             'secrtNceThree':secrtNceThree,
             'NcetfGradepoint':NcetfGradepoint,
             }
        
    return render (request,'computeresult.html',context )

