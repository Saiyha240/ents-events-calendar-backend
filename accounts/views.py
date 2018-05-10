from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics

from accounts.models import User
from accounts.serializers import UserSerializer


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
