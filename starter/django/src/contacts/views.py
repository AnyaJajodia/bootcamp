from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact


def index(request):
    """List Contacts
    """
    # return HttpResponse('Contacts Index Page')
    contacts = Contact.objects.all()
    return render(request, template_name='contacts/index.html', context={
        'contacts': contacts,
    })


def details(request, contact_id):
    """Details for Contact
    """
    # return HttpResponse('Contacts Details Page')
    contact = Contact.objects.first(pk=contact_id)
    return render(request, template_name='contacts/details.html', context={
        'contact': contact,
    })

def create(request):
    """Create New Contact
    """
    if request.method == 'POST':
        pass
    # return HttpResponse('Contacts Create Page')
    return render(request, template_name='contacts/create.html', context={
        # 'contacts': contacts,
    })

def edit(request, contact_id):
    """Edit Contact
    """
    return HttpResponse('Contacts Edit Page')


def delete(request, contact_id):
    """Delete Contact
    """
    return HttpResponse('Contacts Delete Page')
