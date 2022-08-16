from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mydif(r):
    return render(r,"index.html")
