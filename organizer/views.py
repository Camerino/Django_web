from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy


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

class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = ('organizer/newslink_form_update.html')

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        context = {'form': self.form_class(instance=newslink),
                   'newslink': newslink,
                   }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(request, self.template_name, context)

class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = ('organizer/tag_form_update.html')

class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    model = Startup
    template_name = ('organizer/startup_form_update.html')

class NewsLinkDelete(View):
    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        return render(request, 'organizer/newslink_confirm_delete.html',
                      {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        startup=newslink.startup
        newslink.delete()
        return redirect(startup)

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    template_name = ('organizer/tag_confirm_delete.html')

class StartupDelete(ObjectDeleteMixin, View):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    template_name = ('organizer/startup_confirm_delete.html')






