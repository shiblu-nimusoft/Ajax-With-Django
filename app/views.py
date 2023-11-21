from django.http import JsonResponse
from django.shortcuts import render
from .models import Demo
from .forms import DemoForm
# Create your views here.


def home(request):
    data = Demo.objects.all()
    form = DemoForm()
    return render(request, 'home.html', {'data': data,'form':form})


