from rest_framework import viewsets
from .serializers import NordicSerializer
from .models import Nordic
from rest_framework import permissions

# Create your views here.

class NordicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Nordic.objects.all().order_by('-pk')
    serializer_class = NordicSerializer
    permission_classes = [permissions.IsAuthenticated]
