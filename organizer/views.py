from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .utils import ObjectCreateMixin
from .models import Tag, Startup
from .forms import TagForm, StartupForm, NewsLinkForm
from django.views.generic import View

def tag_list(request):
    tag_list = Tag.objects.all()
    return render_to_response('organizer/tag_list.html',
                              {'tag_list': tag_list})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render_to_response('organizer/tag_detail.html',
                              {'tag': tag})


def startup_list(request):
    startup_list = Startup.objects.all()
    return render_to_response('organizer/startup_list.html',
                              {'startup_list': startup_list})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render_to_response('organizer/startup_detail.html',
                              {'startup': startup})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
    else:
        form = TagForm()
        return render(request, 'organizer/tag_form.html',
                      {'form': form})

class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'





