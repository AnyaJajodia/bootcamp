from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from contacts.models import Contact
from .serializers import ContactSerializer


# @csrf_exempt
# @api_view(['GET', 'POST'])
def contact_list(request):
    """List or Create Contact models
    """
    queryset = Contact.objects.all()
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(instance=contacts, many=True)
        # return JsonResponse(data=serializer.data, safe=False)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # data = JSONParser().parse(request.data)
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(data=serializer.data, status=201)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticated])
def contact_details(request, contact_id):
    """Retrieve, update or delete Contact model
    """
    try:
        contact = Contact.objects.get(id=contact_id)

        if request.method == 'GET':
            serializer = ContactSerializer(instance=contact)
            # return JsonResponse(data=serializer.data)
            return Response(data=serializer.data)
        
        elif request.method == 'PUT':
            # data = JSONParser().parse(request)
            # data = JSONParser().parse(request.data)
            serializer = ContactSerializer(instance=contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                # return JsonResponse(data=serializer.data, status=201)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(data=serializer.errors, status=400)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            contact.delete()
            # return HttpResponse(status=204)
            return Response(status=status.HTTP_204_NO_CONTENT)


    except Contact.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_400_BAD_REQUEST)
