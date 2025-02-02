from django.contrib import admin
from django.db import models
from .models import*

# Register your models here.

admin.site.register(StudentRegistration)
admin.site.register(Department)
admin.site.register(CollegeCourse)


admin.site.register(Lecturer)
admin.site.register(FirstSemisterResult)
admin.site.register(SecondSemisterResult)
admin.site.register(UploadResult)
admin.site.register(IctStaff)





