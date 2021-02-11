from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())

    return render(request,'myblog/post_list.html',{'posts':posts})
    
