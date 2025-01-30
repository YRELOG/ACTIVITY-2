from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Announcement, Household, Resident, Complaint
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HouseHoldListView(ListView):
    model = Household
    context_object_name = 'households'
    template_name = 'app/Household.html'

class HouseHoldResidentsListView(ListView):
    model = Resident
    context_object_name = 'residents'
    template_name = 'app/HouseholdResidents.html'

    def get_queryset(self):
        household_id = self.kwargs.get('household_id')
        return Resident.objects.filter(household_id=household_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['household'] = Household.objects.get(pk=self.kwargs.get('household_id'))
        return context

class ResidentCreateView(CreateView):
    model = Resident
    fields = ['first_name', 'last_name', 'age', 'gender']
    template_name = 'app/Residents_create.html'

    def form_valid(self, form):
        household_id = self.kwargs.get('household_id')  # Get household_id from URL
        household = get_object_or_404(Household, pk=household_id)  # Get Household object
        form.instance.household = household  # Assign household to resident
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['household'] = Household.objects.get(pk=self.kwargs.get('household_id'))
        return context

    def get_success_url(self):
        return reverse('household-residents', kwargs={'household_id': self.kwargs.get('household_id')})

class ResidentUpdateView(UpdateView):
    model = Resident
    fields = ['first_name', 'last_name', 'age', 'gender']
    template_name = 'app/Residents_update.html'

    def form_valid(self, form):
        household_id = self.kwargs.get('household_id')  # Get household_id from URL
        household = get_object_or_404(Household, pk=household_id)  # Get Household object
        form.instance.household = household  # Assign household to resident
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['household'] = Household.objects.get(pk=self.kwargs.get('household_id'))
        return context

    def get_success_url(self):
        return reverse('household-residents', kwargs={'household_id': self.kwargs.get('household_id')})

class ResidentDeleteView(DeleteView):
    model = Resident
    template_name = 'app/Residents_delete.html'

    def get_success_url(self):
        """Redirect to the household's residents list after deletion"""
        household_id = self.kwargs.get('household_id')  # Get household ID from URL
        return reverse_lazy('household-residents', kwargs={'household_id': household_id})

    def get_context_data(self, **kwargs):
        """Pass household data to the template"""
        context = super().get_context_data(**kwargs)
        context['household'] = get_object_or_404(Household, pk=self.kwargs.get('household_id'))
        return context

class ComplaintsListView(ListView):
    model = Complaint
    context_object_name = 'complaints'
    template_name = 'app/Complaints_list.html'

class ComplaintsCreateView(CreateView):
    model = Complaint
    fields = ['resident', 'description', 'status']
    template_name = 'app/Complaints_create.html'


class ComplaintsDetailView(DetailView):
    model = Complaint
    template_name = 'app/Complaints_detail.html'
    context_object_name = 'complaint'

class ComplaintsUpdateView(UpdateView):
    model = Complaint
    fields = ['resident', 'description', 'status']
    template_name = 'app/Complaints_update.html'

class ComplaintDeleteView(DeleteView):
    model = Complaint
    template_name = 'app/Complaints_delete.html'
    success_url = reverse_lazy('Complaints')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['complaint'] = self.object
        return context

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