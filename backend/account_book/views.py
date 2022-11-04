from rest_framework import viewsets

from user.permissions import IsOwner
from .models import AccountBook
from .serializers import AccountBookSerializer


class AccountBookViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBookSerializer
    permission_classes = [IsOwner]
    queryset = AccountBook.objects.all()
