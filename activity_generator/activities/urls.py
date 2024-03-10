
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoriesView.as_view()),
    path('categories/<int:category_id>/activities', ActivitiesView.as_view()),
    path('activities/random/', RandomActivityView.as_view()),
]
