
from django.contrib.auth import views
from.views import*
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   
    path('', views.ResultHome,name='resultHome'), #start
    path('resultlogin',views.Resultlogin,name='resultlogin'),
    path('uploadresult',views.FirstSemister,name='uploadresult'),
    path('resultsignin',views.ResultSignin,name='resultsignin'),
    path('ictStaffregistration',views.ICTStaff,name='ictStaffregistration'),
    path('logout',views.Resultlogout,name='logout'),
    path('Computeresult',views.ComputeResult,name='Computeresult'),
    path('secondresult',views.Secondsemister,name='secondresult'), 
    path('staffpage',views.StaffPage,name='staffpage'),#departmental reg
    path('courseregistration',views.CourseResgistration,name='courseregistration'),
    path('lecturerregistration',views.LecturerRegistration,name='lecturerregistration'),
    path('studentregistration',views.StudentsRegistration,name='studentregistration'), 
    path('changepassword',views.Change_password,name='changepassword'),
    
    
    
    
]

urlpatterns+=staticfiles_urlpatterns()