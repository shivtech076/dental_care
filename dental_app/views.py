from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, UpdateView, DeleteView
# from .forms import Userform

def base_html(request):
    return render(request,'base.html')