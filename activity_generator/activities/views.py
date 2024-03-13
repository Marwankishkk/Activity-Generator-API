from unicodedata import category
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
import random
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views herfrom django.contrib.auth.models import User


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class ActivitiesView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitiesSerializer
    lookup_field = 'category_id'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        queryset = Activity.objects.filter(category__id=category_id)
        return queryset


class RandomActivityView(generics.RetrieveAPIView):
    serializer_class = ActivitiesSerializer

    def get_object(self):
        # Get the total number of activities
        total_activities = Activity.objects.count()
        if total_activities == 0:
            raise Http404("No activities found.")
        random_index = random.randint(0, total_activities - 1)
        random_activity = Activity.objects.all()[random_index]
        return random_activity


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PrefrenceView(generics.ListAPIView):
    serializer_class = ActivitiesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the current user's preferences
        user = self.request.user
        try:
            user_preference = UserPreference.objects.get(user=user)
        except UserPreference.DoesNotExist:
            # Handle the case where preferences are not set
            return Activity.objects.none()

        # Filter activities based on user preferences
        queryset = Activity.objects.filter(
            difficulty_level=user_preference.preferred_difficulty_level,
            category=user_preference.category
        )

        return queryset


class PreferenceCreateView(generics.CreateAPIView):
    serializer_class = PreferenceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user field to the currently signed-in user
        serializer.save(user=self.request.user)
