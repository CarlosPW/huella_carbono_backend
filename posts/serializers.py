from rest_framework import serializers

from accounts.models import CustomUser
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.CharField()
    # users = serializers.SlugRelatedField(queryset=CustomUser.objects.all(), many=True, slug_field="email") 

    class Meta:
        fields = (
            "id",
            "author",
            "address_start_point",
            "address_end_point",
            "transportation",
            "kilometers",
            "users",
            "round_trip",
        )
        model = Post