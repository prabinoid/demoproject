from django.shortcuts import render
import requests
from .models import Employee
# Create your views here.


from .models import Employee


def employeeData(request):
    a = Employee.objects.all()
    return render(request, 'index.html', {'a': a})
