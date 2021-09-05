from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('base_html/',base_html, name="base"),
    path('',index_html, name="index"),
    path('replaceing_html/',replacing_html,name="replace"),
    path('root_canal_html/',root_canal_html,name="canal"),
    path('wisdom_teeth_html/',wisdom_teeth_html,name="wisdom"),
    path('dental_implants_html/',dental_implants_html,name="implants"),
    path('correction_crooked_html/',correction_crooked_html,name="crooked"),
    path('cavities_html/',cavities_html,name="cavities"),
    path('toothache_html/',toothache_html,name="toothache"),
    path('bad_breath_html/',bad_breath_html,name="bad_breath"),
    path('sensitivity_html/',sensitivity_html,name="sensitivity"),
    path('broken_teeth_html/',broken_teeth_html,name="broken_teeth"),
    path('loose_teeth_html/',loose_teeth_html,name="loose_teeth"),
    path('short_teeth_html/',short_teeth_html,name="short_teeth"),
    path('bleeding_gums_html/',bleeding_gums_html,name="bleeding_gums"),
    path('crooked_teeth_html/',crooked_teeth_html,name="crooked_teeth"),
    path('about_doctor_html/',about_doctor_html,name="doctor"),
    path('about_clinic_html/',about_clinic_html,name="clinic"),
    path('contact_html/',contact_html,name="contact"),
    path('orthodontia_html/',orthodontia_html,name="orthodontia"),
    
    ]



    