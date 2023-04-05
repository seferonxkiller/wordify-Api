from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics


class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# class ContactCreateView(generics.CreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
