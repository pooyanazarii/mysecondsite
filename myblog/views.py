from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

contex_index = {"titel":"This is dictionary from view.py"}
def view_index(request):
    return render(request,"index.html",contex_index)

def view_about(request):
    return render(request,"about.html")
