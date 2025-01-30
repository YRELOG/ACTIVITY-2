from django.urls import path
from .views import (HouseHoldListView,
                    HouseHoldResidentsListView,
                    ResidentCreateView,
                    ResidentUpdateView,
                    ResidentDeleteView,
                    ComplaintsListView,
                    ComplaintsCreateView,
                    ComplaintsDetailView,
                    ComplaintsUpdateView,
                    ComplaintDeleteView,
                    AnnouncementCreateView,
                    AnnouncementListView,
                    AnnouncementDetailView,
                    AnnouncementUpdateView,
                    AnnouncementDeleteView
                    )
urlpatterns = [
    path('', HouseHoldListView.as_view(), name='Household'),
    path('households/<int:household_id>/residents/', HouseHoldResidentsListView.as_view(), name='household-residents'),
    path('households/<int:household_id>/create-resident/', ResidentCreateView.as_view(), name='resident-create'),
    path('households/<int:household_id>/residents/<int:pk>/update/', ResidentUpdateView.as_view(), name='resident_update'),
    path('households/<int:household_id>/residents/<int:pk>/delete/',ResidentDeleteView.as_view(), name='resident_delete'),

    path('Complaint', ComplaintsListView.as_view(), name='Complaints'),
    path('Complaint/<int:pk>/', ComplaintsDetailView.as_view(), name='Complaints_detail'),
    path('Complaint/create/', ComplaintsCreateView.as_view(), name='Complaints_create'),
    path('Complaint/<int:pk>/edit/', ComplaintsUpdateView.as_view(), name='Complaints_update'),
    path('Complaint/<int:pk>/delete/', ComplaintDeleteView.as_view(), name='Complaints_delete'),

    path('Announcement', AnnouncementListView.as_view(), name='Announcement'),
    path('Announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='Announcement_detail'),
    path('Announcement/create/', AnnouncementCreateView.as_view(), name='Announcement_create'),
    path('Announcement/<int:pk>/edit/', AnnouncementUpdateView.as_view(), name='Announcement_update'),
    path('Announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='Announcement_delete'),

]
