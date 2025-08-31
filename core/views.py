# core/views.py
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.http import HttpResponse

# Landing Page View
def landing_page(request):
    return HttpResponse("<h1>Welcome to the API</h1><p>Visit <a href='/admin/'>Admin</a> or <a href='/api/clients/'>Clients API</a></p>")


# Clients Views

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


# Projects Views

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user)

    def perform_create(self, serializer):
        client_id = self.kwargs['client_id']
        client = Client.objects.get(id=client_id)
        serializer.save(client=client, created_by=self.request.user)


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
