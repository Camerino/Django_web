from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse, Http404
from .models import Tag
from django.template import Context, loader

def homepage(request):
    tag_list = Tag.objects.all()
    return render_to_response('organizer/tag_list.html',
                              {'tag_list': tag_list})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render_to_response('organizer/tag_detail.html',
                              {'tag': tag})


