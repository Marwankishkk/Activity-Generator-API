
from rest_framework import serializers
from .models import *


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
