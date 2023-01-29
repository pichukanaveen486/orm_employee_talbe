from django.shortcuts import render
from app.models import *
# Create your views here.
def employee(request):
    QSE=Employee.objects.all()
    d={'employee':QSE}
    return render(request,'employee.html',d)