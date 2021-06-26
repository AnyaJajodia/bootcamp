from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact


def index(request):
    """List Contacts
    """
    return HttpResponse('Contacts Index Page')


def details(request, contact_id):
    """Details for Contact
    """
    return HttpResponse('Contacts Details Page')


def create(request):
    """Create New Contact
    """
    return HttpResponse('Contacts Create Page')
    

def edit(request, contact_id):
    """Edit Contact
    """
    return HttpResponse('Contacts Edit Page')


def delete(request, contact_id):
    """Delete Contact
    """
    return HttpResponse('Contacts Delete Page')
