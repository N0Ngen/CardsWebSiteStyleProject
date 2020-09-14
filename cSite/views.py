# render handle views
from django.shortcuts import render
# import Tutorial obj from models
from .models import Tutorial

# Create your views here.

def index(request):
  return render(request, 'cSite/index.html', {'tutorials': Tutorial.objects.all()})