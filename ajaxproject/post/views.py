from django.shortcuts import render
from .models import Post , Like 
from django.http import HttpResponse 
# Create your views here.


def index(response) : 
    posts = Post.objects.all()
    
    return render(response, 'index.html', {'posts' : posts})




def like(response):
    if response.method == "GET":
        post_id = response.GET['post_id']
        likedpost = Post.objects.get(id = post_id)
        m = Like(post = likedpost)
        m.save()
        return HttpResponse('<h1>success!!!!!!</h1>')
    else:
        return HttpResponse('<h1>unsuccesful :(</h1>')


