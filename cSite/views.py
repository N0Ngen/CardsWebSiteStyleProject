from django.shortcuts import render
from .models import Tutorial

# Create your views here.

def index(request):
  return render(request, 'cSite/index.html', {'tutorials': Tutorial.objects.all()})