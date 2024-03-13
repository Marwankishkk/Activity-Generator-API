
from rest_framework import serializers
from .models import *
# Replace with your custom user model if applicable
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"


class ActivitiesSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta():
        model = Activity
        fields = ["category_name", "text", "tags", "difficulty_level"]

    def get_category_name(self, obj):
        return obj.category.title


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserPreference
        fields = ["category", "preferred_difficulty_level"]
