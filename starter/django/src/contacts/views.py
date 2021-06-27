from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse

from .models import Contact
from .forms import ContactForm

# List
# CRUD
# Create
# Retreive 
# Update 
# Delete

# ORM - Object Relational Model

def index(request):
    """List Contacts
    """
    # return HttpResponse('Contacts Index Page')
    contacts = Contact.objects.all() # QuerySet
    return render(
        request, 
        template_name='contacts/index.html', 
        context={
            'contacts': contacts,
        }
    )


def details(request, contact_id):
    """Details for Contact
    """
    # return HttpResponse('Contacts Details Page')
    contact = Contact.objects.get(pk=contact_id)
    return render(
        request, 
        template_name='contacts/details.html', 
        context={
            'contact': contact,
        }
    )


def create(request):
    """Create New Contact
    """
    form = ContactForm()

    # Creating Contact
    if request.method == 'POST': # GET, PUT, PATCH, DELETE
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            # Add foreign objects if needed
            contact.save()
            form.save_m2m()

            return HttpResponseRedirect(
                reverse(
                    viewname='contacts:contact_details',
                    kwargs={
                        'contact_id': contact.id,
                    }
                )
            )
        else:
            print(form.errors)
        
    # return HttpResponse('Contacts Create Page')
    return render(
        request, 
        template_name='contacts/create.html', 
        context={
            'form': form,
        }
    )


def edit(request, contact_id):
    """Edit Contact
    """
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid:
            contact = form.save(commit=False)
            # Add foreign objects if needed
            contact.save()
            form.save_m2m()

            return HttpResponseRedirect(
                reverse(
                    viewname='contacts:contact_details',
                    kwargs={
                        'contact_id': contact.id,
                    }
                )
            )

    # return HttpResponse('Contacts Edit Page')
    return render(
        request, 
        template_name='contacts/edit.html', 
        context={
            'form': form,
            'contact_id': contact.id,
        }
    )


def delete(request, contact_id):
    """Delete Contact
    """
    contact = Contact.objects.get(pk=contact_id)

    if request.method == 'POST':        
        contact.delete()

        return HttpResponseRedirect(
            reverse(
                viewname='contacts:contact_index',
            )
        )

    # return HttpResponse('Contacts Delete Page')
    return render(
        request, 
        template_name='contacts/delete.html', 
        context={
            'contact': contact,
        }
    )
