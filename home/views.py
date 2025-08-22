from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
      return render(request,"index.html")


def success_mantra(request):
         print('*'*10)
         return HttpResponse("<h2>hard work always pays</h2>")
         
      