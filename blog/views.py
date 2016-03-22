from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse, Http404
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render_to_response('blog/post_list.html',
                              {'post_list': post_list})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render_to_response('blog/post_detail.html',
                              {'post': post})
