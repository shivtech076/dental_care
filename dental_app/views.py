from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, UpdateView, DeleteView
# from .forms import Userform

def base_html(request):
    return render(request,'base.html')

def index_html(request):
    return render(request,'index.html')
    
def replacing_html(request):
    return render(request,'replacing_missing_teeth.html')

def root_canal_html(request):
    return render(request,'root_canal_treatment.html')

def wisdom_teeth_html(request):
    return render(request,'wisdom_teeth.html')

def dental_implants_html(request):
    return render(request,'dental_implants.html')

def correction_crooked_html(request):
    return render(request,'correction_crooked.html')

def cavities_html(request):
    return render(request,'cavities.html')

def toothache_html(request):
    return render(request,'toothache.html')

def bad_breath_html(request):
    return render(request,'bad_breath.html')

def sensitivity_html(request):
    return render(request,'sensitivity.html')

def broken_teeth_html(request):
    return render(request,'broken_teeth.html')

def loose_teeth_html(request):
    return render(request,'loose_teeth.html')

def short_teeth_html(request):
    return render(request,'short_teeth.html')

def bleeding_gums_html(request):
    return render(request,'bleeding_gums.html')

def crooked_teeth_html(request):
    return render(request,'crooked_teeth.html')

def about_doctor_html(request):
    return render(request,'about_the_doctor.html')

def about_clinic_html(request):
    return render(request,'about_the_clinic.html')
