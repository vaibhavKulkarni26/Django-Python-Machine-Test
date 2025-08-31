# core/urls.py

from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView, landing_page

urlpatterns = [
    path('', landing_page, name='landing-page'),  # Add landing page URL
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),  # Updated URL
    path('projects/', ProjectListCreateView.as_view(), name='user-projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]