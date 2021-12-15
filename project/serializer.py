from django.db.models import fields
from rest_framework import serializers
from .models import Category, Projects, UserProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'technologies']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['category', 'user', 'image', 'user_name', 'bio']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['image', 'description', 'name', 'link', 'technologies', 'user', 'posted_at']        