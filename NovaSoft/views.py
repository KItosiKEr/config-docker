from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import filters

from .models import Developer, Contact
from .seriallizers import ContactSerializer, DeveloperSerializer


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #for search into developers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'mail']

class ContactVeiwSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

