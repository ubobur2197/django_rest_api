from rest_framework import viewsets
from .models import Ustoz, Guruh, Talaba
from .serializers import (
    UstozSerializer,
    GuruhSerializer,
    TalabaSerializer
)


class UstozViewSet(viewsets.ModelViewSet):
    queryset = Ustoz.objects.all()
    serializer_class = UstozSerializer


class GuruhViewSet(viewsets.ModelViewSet):
    queryset = Guruh.objects.all()
    serializer_class = GuruhSerializer


class TalabaViewSet(viewsets.ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer

    