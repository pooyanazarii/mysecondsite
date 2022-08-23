from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Post
# Create your views here.

contex_index = {"titel":"This is dictionary from view.py"}
def view_index(request):
    return render(request,"index.html",contex_index)


contex_about = {"titel":"This about view"}
def view_about(request):
    
    return render(request,"about.html",contex_about)


def view_test(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request,'test.html',context)
