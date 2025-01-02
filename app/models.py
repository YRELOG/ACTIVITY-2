from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Official(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.position}: {self.first_name} {self.last_name}"


class Complaint(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='complaints')
    official = models.ForeignKey(Official, on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints')
    description = models.TextField()
    date_filed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')

    def __str__(self):
        return f"Complaint by {self.household} - {self.status}"
