from django.urls import path
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    AnnouncementCreateView,
                    AnnouncementListView,
                    AnnouncementDetailView,
                    AnnouncementUpdateView,
                    AnnouncementDeleteView
                    )
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('', AnnouncementListView.as_view(), name='Announcement'),
    path('Announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='Announcement_detail'),
    path('Announcement/create/', AnnouncementCreateView.as_view(), name='Announcement_create'),
    path('Announcement/<int:pk>/edit/', AnnouncementUpdateView.as_view(), name='Announcement_update'),
    path('Announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='Announcement_delete'),

]
