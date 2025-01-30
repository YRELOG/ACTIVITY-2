from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Announcement(models.Model):
    official = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='announcements')
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=
    [('ANNOUNCED', 'Announced'),
     ('ONGOING', 'Ongoing'),
     ('COMPLETED', 'Completed')],
     default='PENDING')
    details = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.details

    def get_absolute_url(self):
        return reverse('Announcement_detail', kwargs={'pk': self.pk})
    

class Household(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Resident(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='residents')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=
        [('MALE', 'Male'),
         ('FEMALE', 'Female')],
         default='PENDING')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def get_default_resident():
    """Returns the first Resident or creates a default one if none exists."""
    try:
        return Resident.objects.first().id  # Get the ID of the first resident
    except AttributeError:
        raise ObjectDoesNotExist("No Resident exists. Create one before applying migrations.")

class Complaint(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='complaints', default=get_default_resident)
    description = models.TextField()
    date_filed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')

    def __str__(self):
        return f"Complaint by {self.resident} - {self.status}"

    def get_absolute_url(self):
        return reverse('Complaints_detail', kwargs={'pk': self.pk})
