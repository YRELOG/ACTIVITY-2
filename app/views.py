from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Announcement
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['type', 'location', 'status', 'details']
    template_name = 'app/Announcement_create.html'

class AnnouncementListView(ListView):
    model = Announcement
    fields = ['type']
    context_object_name = 'posts'
    template_name = 'app/Announcement_list.html'


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['type', 'location', 'status', 'details']
    template_name = 'app/Announcement_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object  # Explicitly add 'post' to the context
        return context

    def get_success_url(self):
        return reverse_lazy('Announcement_detail', kwargs={'pk': self.object.pk})

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'app/Announcement_detail.html'
    context_object_name = 'post'


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'app/Announcement_delete.html'
    success_url = reverse_lazy('Announcement')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context