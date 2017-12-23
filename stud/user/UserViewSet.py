# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework import viewsets

from stud.user.UserSerializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
