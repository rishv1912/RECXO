from django.shortcuts import render
from .models import Blog,Comment,Topic
# Create your views here.


def home(request):
    topics = Topic.objects.all()[0:4]
    context = {'topics':topics}
    return render(request,'blog/home.html',context)

