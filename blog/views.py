from django.shortcuts import render_to_response, get_object_or_404
from .models import Post
from django.views.generic import View

class PostList(View):
    def get(self, request):
        post_list = Post.objects.all()
        return render_to_response('blog/post_list.html',
                              {'post_list': post_list})

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post,
                             pub_date__year = year,
                             pub_date__month = month,
                             slug = slug)
    return render_to_response('blog/post_detail.html',
                              {'post': post})
