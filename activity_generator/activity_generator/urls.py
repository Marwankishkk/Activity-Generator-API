
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("activities.urls")),
    path('api/auth/', include('djoser.urls.authtoken')),  # Authentication URLs

]
