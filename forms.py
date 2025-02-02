

from django.db import models
from django.forms import ModelForm,TextInput,EmailInput
from django import forms
from .models import*
from django.contrib.auth.models import User



class UploadResultModelForm(forms.ModelForm):
    
    class Meta:
        model = UploadResult
        fields = ('file_name',)
        
class UploadCoursesModelForm(forms.ModelForm):
    
    class Meta:
        model = UploadCourses
        fields = ('file_name',)
        

        




