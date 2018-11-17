from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def allblogs(request):
    blogposts = Blogpost.objects
    return render(request, 'blog/allblogs.html', {'blogposts': blogposts})

def detail(request, blog_id):
    details = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'details': details})
