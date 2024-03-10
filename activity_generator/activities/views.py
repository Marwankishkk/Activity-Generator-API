from unicodedata import category
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
import random
from django.http import Http404

# Create your views here.


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
