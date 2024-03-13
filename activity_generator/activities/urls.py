
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoriesView.as_view()),
    path('categories/<int:category_id>/activities', ActivitiesView.as_view()),
    path('activities/random/', RandomActivityView.as_view()),
    path("users/", UsersView.as_view()),
    path("create/prefrences/", PreferenceCreateView.as_view()),
    path("prefrences/", PrefrenceView.as_view()),

]
