from django.shortcuts import render
from django.http import HttpResponse
from .models import Parsing


# Create your views here.



def test(request):
   context=0
   return render(request, template_name="testapp/test.html", context=context)

