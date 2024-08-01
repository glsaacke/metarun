from rest_framework import serializers
from .models import BlogPost
from .models import User
from .models import Activity

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "fName", "lName", "age", "weight"]

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "title", "type", "distance", "durationHr", "durationMin", "durationSec", "paceMin", "paceSec", "heartrate"]